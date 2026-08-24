#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CENATE — Rotina de tabulação e cálculo dos índices sintéticos
=============================================================

Reproduz, a partir da base anonimizada publicada neste repositório, os valores
apresentados no Capítulo 5 do Trabalho Final de Máster.

Uso:
    cd 12_script_tabulacion
    pip install -r requirements.txt
    python tabular_cenate.py

Saídas geradas no diretório corrente:
    indices_por_unidade.csv     IMI, IPR (e componentes) e IEI por administração
    imi_por_dimensao.csv        média e desvio-padrão de cada dimensão do Bloco B
    resumo_indices.csv          estatísticas descritivas dos três índices

Fórmulas (Seção 3.3.1 do TFM):
    IMI = [(média Bloco B − 1) / 4] × 100
    IPR = 100 − (0,70 × IPR_Likert + 0,30 × IPR_bin)      ← orientação inversa
    IEI = [(média Bloco E − 1) / 4] × 100

No IPR, valores mais altos indicam MENOR preparação e, portanto, MAIOR
prioridade relativa de adaptação.

Tratamento de dados ausentes: respostas "ND" são excluídas do denominador dos
indicadores binários e não são tratadas como negativas (Seção 3.3.1). Zeros em
variáveis de nível do Bloco C são tratados como não informados, conforme a
errata do Apêndice A, item A.1.5.
"""

from pathlib import Path
import sys
import pandas as pd

BASE = Path(__file__).resolve().parent.parent / "11_base_dados_anonimizada" / \
       "CENATE_Base_Dados_Anonimizada_Completa.xlsx"

# Valores publicados no Capítulo 5, usados como teste de regressão
ESPERADO = {"IMI_media": 68.6, "IPR_media": 53.3, "IEI_media": 67.7, "pearson": -0.32}

ROTULOS_B = {
    "B01": "Planejamento e governança estratégica",
    "B02": "Gestão de pessoas e capacidade organizacional",
    "B03": "Gestão de riscos institucionais e integridade",
    "B04": "Tecnologia, governança de dados e regras digitais",
    "B05": "Capacidade analítica e ciência de dados",
    "B06": "Inovação digital, automação e inteligência artificial",
    "B07": "Gestão do risco de conformidade",
    "B08": "Gestão do cadastro de contribuintes",
    "B09": "Declarações e obrigações acessórias",
    "B10": "Serviços digitais e relacionamento com o contribuinte",
    "B11": "Apoio à conformidade e autorregularização",
    "B12": "Gestão de grandes contribuintes",
    "B13": "Fiscalização e auditoria tributária",
    "B14": "Resolução de litígios tributários (contencioso)",
    "B15": "Cobrança, recuperação de créditos e dívida ativa",
    "B16": "Gestão de receitas, arrecadação e conciliação",
    "B17": "Transparência e prestação de contas",
}


def normalizar(media_likert):
    """Converte média de escala Likert 1-5 para escala 0-100."""
    return (media_likert - 1) / 4 * 100


def faixa_imi(v):
    """Faixas interpretativas do IMI (Tabela 9 do TFM)."""
    if v < 40:
        return "Inicial"
    if v < 60:
        return "Basico"
    if v < 80:
        return "Intermediario"
    return "Avancado"


def carregar(aba):
    df = pd.read_excel(BASE, sheet_name=aba, engine="openpyxl")
    return df.set_index("codigo_neutro")


def _sem_acento(s):
    tabela = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüç",
                           "aaaaaeeeeiiiiooooouuuuc")
    return str(s).strip().lower().translate(tabela)


def prop_sim(linha):
    """Proporcao de respostas afirmativas, com ND fora do denominador.

    As respostas "ND" (informacao nao disponivel) sao excluidas do
    denominador e nao contam como negativas (Secao 3.3.1 do TFM).
    """
    vals = [_sem_acento(v) for v in linha]
    validos = [v for v in vals if v.startswith("sim") or v.startswith("nao")]
    if not validos:
        return float("nan")
    return sum(v.startswith("sim") for v in validos) / len(validos) * 100


def main():
    if not BASE.exists():
        sys.exit("ERRO: base nao encontrada em %s" % BASE)

    bloco_b = carregar("03_BLOCO_B").apply(pd.to_numeric, errors="coerce")
    bloco_d = carregar("06_BLOCO_D").apply(pd.to_numeric, errors="coerce")
    bloco_e = carregar("07_BLOCO_E").apply(pd.to_numeric, errors="coerce")
    binario = carregar("05_BLOCO_C_BINARIO")

    print("Base carregada: %d administracoes (N = %d)\n" % (len(bloco_b), len(bloco_b)))

    # ---- IMI: media das 17 dimensoes, cada uma media de 4 itens ----
    dims = {}
    for cod in ROTULOS_B:
        itens = [c for c in bloco_b.columns if str(c).startswith(cod + ".")]
        dims[cod] = normalizar(bloco_b[itens].mean(axis=1))
    dims = pd.DataFrame(dims)
    imi = dims.mean(axis=1)

    # ---- IPR: componente perceptivo (Bloco D) e binario (secao C12) ----
    ipr_likert = normalizar(bloco_d.mean(axis=1))
    ipr_bin = binario.apply(prop_sim, axis=1)
    ipr = 100 - (0.70 * ipr_likert + 0.30 * ipr_bin)

    # ---- IEI ----
    iei = normalizar(bloco_e.mean(axis=1))

    # ---- consolidacao ----
    res = pd.DataFrame({
        "IMI": imi.round(2),
        "Faixa_IMI": imi.map(faixa_imi),
        "IPR_Likert": ipr_likert.round(2),
        "IPR_bin": ipr_bin.round(2),
        "IPR": ipr.round(2),
        "IEI": iei.round(2),
    }).sort_index()
    res.to_csv("indices_por_unidade.csv", encoding="utf-8")

    dim_res = pd.DataFrame({
        "dimensao": [ROTULOS_B[c] for c in dims.columns],
        "media": dims.mean().round(1).values,
        "desvio_padrao": dims.std().round(1).values,
    }, index=dims.columns)
    dim_res.index.name = "codigo"
    dim_res.to_csv("imi_por_dimensao.csv", encoding="utf-8")

    res[["IMI", "IPR", "IEI"]].describe().round(2).to_csv(
        "resumo_indices.csv", encoding="utf-8")

    # ---- verificacao contra os valores publicados ----
    pearson = res["IMI"].corr(res["IPR"])
    obtido = {"IMI_media": round(res["IMI"].mean(), 1),
              "IPR_media": round(res["IPR"].mean(), 1),
              "IEI_media": round(res["IEI"].mean(), 1),
              "pearson": round(pearson, 2)}

    print("Indices por unidade:\n")
    print(res.to_string())
    print("\nIMI por dimensao:\n")
    print(dim_res.to_string())

    print("\n" + "=" * 62)
    print("VERIFICACAO CONTRA OS VALORES PUBLICADOS NO CAPITULO 5")
    print("=" * 62)
    ok = True
    for k, esperado in ESPERADO.items():
        got = obtido[k]
        bate = abs(got - esperado) < 0.05
        ok = ok and bate
        print("  %-12s esperado %7s   obtido %7s   %s"
              % (k, esperado, got, "OK" if bate else "DIVERGE"))
    print("=" * 62)
    print("Reproducao confirmada." if ok else
          "ATENCAO: divergencia detectada. Verifique a integridade da base.")
    print("\nArquivos gerados: indices_por_unidade.csv, imi_por_dimensao.csv, "
          "resumo_indices.csv")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
