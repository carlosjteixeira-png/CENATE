# Changelog — CENATE

Todas as alterações relevantes deste repositório são registradas aqui.
O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o versionamento é semântico.

## [2.0.0] — 2026-08-31

Primeira atualização substantiva da base desde o depósito inicial. Incorpora a resposta
da décima terceira administração tributária estadual, recebida em 31 de agosto de 2026.

### Adicionado
- Resposta da administração de código neutro `UF-21` (blocos A, B, D e E completos).
- `dados/cenate_dimensoes_v2.csv`: médias e desvios-padrão do IMI por dimensão do Bloco B.
- Coluna `integra_IPR` em `dados/cenate_indices_v2.csv`, que identifica as unidades com os dois
  componentes do índice disponíveis.
- Aba `13_QUALIDADE_UF21` na planilha de staging, com o cotejo do Bloco C da nova unidade contra
  fonte aberta e o registro das ressalvas de escala.
- Aba `14_EXAUSTIVIDADE` na planilha de staging, com o comparativo de exaustividade por bloco
  entre N = 12 e N = 13.
- Aba `05_COTEJO_UF21` na planilha de recálculo de fontes externas.

### Alterado
- Cobertura do censo: de 12/27 (44,4 %) para **13/27 (48,1 %)**.
- IMI médio: de 68,6 para **66,7**; desvio-padrão de 17,4 para **18,2**; mediana de 68,0 para **67,6**.
- IEI médio: de 67,7 para **69,9**; desvio-padrão de 22,5 para **22,9**; mediana de 72,9 para **75,0**.
- Médias do IMI por dimensão: as dezessete recalculadas. Nenhuma dimensão muda de nível.
- Bloco C: campos com informação utilizável passam de 487/732 (66,5 %) para **509/793 (64,2 %)**.
- Consolidação do controle de solicitações de acesso à informação: de 28 para **31 de agosto de 2026**.
  A distribuição das dezessete solicitações permanece em 5 indeferidas, 5 atendidas e 7 em trâmite.
- Contagem de solicitações em trâmite com prorrogação formalmente registrada: de seis para **cinco**
  (reclassificação decorrente da conferência contra o controle privado).

### Não alterado
- **IPR = 53,3**, IPR_Likert = 48,7 e IPR_bin = 42,0 permanecem calculados sobre **12 unidades**.
  A administração `UF-21` não cumprimentou a seção C12 e não dispôs de via documental que permitisse
  completá-la dentro do período de recolha. Sem o componente binário, o índice composto não é
  calculável; a unidade fica fora do IPR e de **ambos** os seus componentes, para que índice e partes
  repousem sobre o mesmo conjunto. Critério idêntico ao aplicado a `UF-08` antes da obtenção de sua
  seção C12 por via documental.
- Correlação de Pearson entre IMI e IPR: **−0,32**, calculada sobre as mesmas 12 unidades.
- Mínimos e máximos do IMI (29,4 e 91,9) e do IEI (16,7 e 100,0).

### Ressalvas de qualidade registradas
- O Bloco C de `UF-21` apresenta duas escalas monetárias distintas dentro da seção C1, componentes que
  não fecham com o total declarado e uma impossibilidade aritmética (valor pago no prazo superior ao
  total exigível). Nenhum valor foi corrigido de ofício. As 22 variáveis preenchidas contam como
  utilizáveis na contagem formal de exaustividade, mas a unidade fica fora das comparações de
  indicadores. Detalhamento na aba `13_QUALIDADE_UF21`.

### Compatibilidade
- A versão 1.x permanece citável e não foi alterada retroativamente. Trabalhos que citem os números
  de N = 12 devem referenciar o DOI da versão anterior.

## [1.0.0] — 2026-08-28

- Depósito inicial: instrumento, base seudonimizada de 12 administrações, índices IMI, IPR e IEI,
  pacote operacional e documentação metodológica.
