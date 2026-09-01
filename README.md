# CENATE — Materiais Suplementares

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22081499.svg)](https://doi.org/10.5281/zenodo.22081499)

## Resumo executivo

O CENATE (Censo Nacional das Administrações Tributárias Estaduais) é um instrumento censitário padronizado desenvolvido para diagnosticar a maturidade institucional das administrações tributárias estaduais brasileiras no contexto da implementação do Imposto sobre Bens e Serviços (IBS). O repositório reúne os materiais metodológicos, os insumos documentais, as bases anonimizadas e os produtos analíticos utilizados no Trabalho Final de Máster (TFM), assegurando rastreabilidade, transparência metodológica e reprodutibilidade.

## Versão de submissão

Este repositório reflete o estado mais recente dos materiais. A versão correspondente aos dados apresentados no TFM está arquivada no Zenodo (ver seção de citação, abaixo).

### Conteúdo consolidado

- Instrumento aplicado completo, com descritores de calibração, acompanhado da nota de errata.
- Documento institucional original do COMSEFAZ (convite utilizado na coleta).
- Dicionário completo de variáveis, base anonimizada, tabelas desagregadas e script de tabulação.
- Recálculo de indicadores a partir de fontes públicas abertas, em versão pseudonimizada.
- Manifesto SHA-256 e Matriz de Aderência ao TFM.

### Materiais que não integram o repositório

Por decisão expressa do protocolo de pseudonimização (Seção 3.9 do TFM), não se depositam: a exportação sem processamento da plataforma de coleta; a chave de correspondência entre unidade federada e código neutro; os informes individualizados remetidos a cada administração participante; nem o texto integral da monografia.

## Estrutura do repositório

### 01_instrumento
Instrumento efetivamente aplicado do CENATE, em PDF e DOCX, com os enunciados completos dos 68 itens do Bloco B, os 13 itens do Bloco D e os descritores conductuais de calibração (níveis 1, 3 e 5). Inclui também a impressão do formulário eletrônico tal como visto pelos respondentes e a nota de errata autônoma (`ERRATA_instrumento_CENATE.md`), que registra as cinco discrepâncias identificadas entre o formulário aplicado e a especificação metodológica.

O arquivo `Apendice_A_Estrutura_Variaveis_reconstruida.*` traz a listagem estruturada de variáveis reconstruída a partir da base de staging; complementa, mas não substitui, o instrumento aplicado.

### 02_manual_glosario
Manual de preenchimento e glossário operacional utilizados para padronização das respostas.

### 03_diccionario_variables
Dicionário completo de variáveis (codebook), contendo códigos, definições, domínios, regras de preenchimento e especificação dos índices.

### 04_modelos_comunicacion
Modelos de comunicação institucional utilizados durante a coleta.

### 05_solicitudes_acceso_info
Pedidos de acesso à informação (LAI) e documentação analítica associada.

### 06_flujo_tratamiento_datos
Especificação detalhada do fluxo de tratamento, validação e anonimização dos dados.

### 07_tablas_desagregadas_cap5
Tabelas completas que sustentam os resultados apresentados no Capítulo 5 do TFM.

### 08_matriz_comparativa_8criterios
Comparação estruturada entre os referenciais utilizados na construção do instrumento.

### 09_cotejo_bloque_c_fuentes_publicas
Documentação do cotejo entre variáveis do Bloco C e fontes públicas externas.

### 10_protocolo_delphi_propuesta
Proposta metodológica de validação Delphi para ciclos futuros.

### 11_base_dados_anonimizada
Base pública anonimizada utilizada para tabulação e análise.

### 12_script_tabulacion
Scripts de processamento e tabulação.

### anexos

#### Anexo II
**Anexo_II_Memorando_COMSEFAZ_839_2026_Original.pdf**

Documento institucional original utilizado para a articulação da coleta junto às administrações tributárias estaduais.

#### Anexo III
**Anexo_III_Monografia_ICDI.pdf**

Monografia integral do ICDI, disponibilizada para fins de rastreabilidade metodológica do desenvolvimento do CENATE.

## Conformidade com o TFM

A versão 2.4 contempla:

- Instrumento aplicado;
- Manual de preenchimento e glossário;
- Dicionário completo de variáveis;
- Modelos de comunicação institucional;
- Documentação LAI;
- Fluxo de tratamento e validação;
- Tabelas completas dos resultados;
- Síntese dos referenciais utilizados;
- Protocolo Delphi;
- Base anonimizada;
- Anexo II (documento original do COMSEFAZ);
- Anexo III (monografia ICDI).

## Controle de versão

Esta numeração (v2.2, v2.3, v2.4) documenta etapas internas de consolidação de arquivos e é independente da numeração de versões do dataset arquivado no Zenodo (v1.0, v2.0, v2.1), que reflete a evolução da base de dados.

| Versão | Alteração principal |
|---------|--------------------|
| v2.2 | Consolidação inicial para publicação |
| v2.3 | Inclusão de instrumento, codebook, fluxo detalhado e tabelas completas |
| v2.4 | Inclusão do documento original do COMSEFAZ (Anexo II) e atualização da matriz de aderência |

## Reprodutibilidade

O script `12_script_tabulacion/tabular_cenate.py` recalcula os três índices a partir da base anonimizada e verifica automaticamente o resultado contra os valores publicados no Capítulo 5 do TFM:

```
cd 12_script_tabulacion
pip install -r requirements.txt
python tabular_cenate.py
```

Saída esperada:

```
IMI_media    esperado    66.7   obtido    66.7   OK
IPR_media    esperado    53.3   obtido    53.3   OK
IEI_media    esperado    69.9   obtido    69.9   OK
pearson      esperado   -0.32   obtido   -0.32   OK
Reproducao confirmada.
```

## Integridade

O arquivo `MANIFESTO_SHA256.md` lista o hash SHA-256 de cada arquivo do repositório.

## Licenças

- Documentos, dados e planilhas: **CC BY 4.0** (`LICENSE`)
- Rotinas informáticas: **MIT** (`LICENSE-CODE`)

## Citação recomendada

Teixeira, C. J. (2026). CENATE: Materiais suplementares [Conjunto de dados e código]. Zenodo.
https://doi.org/10.5281/zenodo.22081499

**DOI:** [10.5281/zenodo.22081499](https://doi.org/10.5281/zenodo.22081499) · **Registro:** https://zenodo.org/records/22081499
