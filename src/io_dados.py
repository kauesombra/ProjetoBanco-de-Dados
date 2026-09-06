"""
Funções reutilizáveis de carga dos dados brutos (camada raw) do Tema 1 —
Economia e emprego formal.

"""

from pathlib import Path
import pandas as pd
import geopandas as gpd

RAW_DIR = Path(__file__).resolve().parent.parent / "dados" / "raw"

ARQUIVOS = {
    "cempre": RAW_DIR / "dados_originais" / "t9509_cempre_economia_emprego_2022_ce_br.csv",
    "estrutura_2021": RAW_DIR / "dados_originais" / "t5938_pib_estrutura_economica_2021_ce_br.csv",
    "pib_2022": RAW_DIR / "dados_originais" / "t5938_pib_2022_ce_br.csv",
    "censo_2022": RAW_DIR / "dados_originais" / "t4709_populacao_censo_2022_ce_br.csv",
}

MALHA_PATH = RAW_DIR / "dados_comuns" / "malha_municipal_ce_2022.geojson"

SIMBOLOS_ESPECIAIS_SIDRA = {"-", "0", "X", "..", "..."}


def carregar_tabela_sidra(caminho: Path) -> pd.DataFrame:
    """Carrega um CSV, preservando
    símbolos especiais e tratando códigos territoriais como texto."""
    return pd.read_csv(
        caminho,
        sep=";",
        encoding="utf-8-sig",
        dtype={"territorio_codigo": "string", "variavel_codigo": "string"},
        keep_default_na=False,
    )


def carregar_todas_as_bases() -> dict[str, pd.DataFrame]:
    """Carrega as quatro tabelas SIDRA obrigatórias do tema, sem nenhuma
    limpeza ou filtragem. Retorna um dicionário {nome: DataFrame}."""
    return {nome: carregar_tabela_sidra(caminho) for nome, caminho in ARQUIVOS.items()}


def carregar_malha_municipal() -> gpd.GeoDataFrame:
    """Carrega a malha municipal do Ceará (geojson). A propriedade
    `codarea` contém o código IBGE de 7 dígitos, usado na junção."""
    return gpd.read_file(MALHA_PATH)


def filtrar_municipios(df: pd.DataFrame) -> pd.DataFrame:
    """Remove as linhas de Brasil (N1) e Ceará (N3), mantendo apenas os
    184 municípios (N6)."""
    return df[df["nivel_territorial_codigo"] == "N6"].copy()


def pivotar_wide(df: pd.DataFrame) -> pd.DataFrame:
    """Converte uma tabela SIDRA do formato longo para largo, com uma
    coluna por `variavel_nome`, mantendo `territorio_codigo` e
    `territorio_nome` como identificadores. Útil antes de cruzar tabelas."""
    return df.pivot_table(
        index=["territorio_codigo", "territorio_nome"],
        columns="variavel_nome",
        values="valor",
        aggfunc="first",
    ).reset_index()
