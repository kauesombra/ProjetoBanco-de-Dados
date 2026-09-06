"""
O dashboard deve ler somente arquivos estáticos de dados/processed ou
dados/analytical — nenhuma chamada à API do SIDRA em tempo de execução.
"""

import streamlit as st

st.set_page_config(page_title="Economia e Emprego Formal — Ceará", layout="wide")

st.title("Economia e emprego formal nos municípios do Ceará")
st.caption("Dados: IBGE/SIDRA — tabelas 9509, 5938 e 4709 | Malha municipal 2022")

st.markdown("""
### Wireframe (rascunho)

**Aba 1 — Visão geral**
- KPIs: PIB per capita médio, intensidade de ocupação formal média
- Mapa coroplético: PIB per capita por município

**Aba 2 — Estrutura setorial**
- Gráfico de participação setorial do VAB (2021) por município selecionado
- Ranking de municípios por especialização setorial

**Aba 3 — Cruzamento estrutura x emprego**
- Dispersão: participação industrial (2021) x intensidade de ocupação
  formal (2022), com nota sobre defasagem temporal

**Aba 4 — Fontes e metodologia**
- Tabelas utilizadas, períodos, limitações e cuidados de interpretação
""")

st.info("Wireframe inicial — conteúdo funcional será implementado após a definição final dos indicadores.")
