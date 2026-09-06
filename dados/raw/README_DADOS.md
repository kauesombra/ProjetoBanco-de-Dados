# Dados da Equipe 01 — Economia e emprego

## Conteúdo do pacote

Os arquivos desta pasta são recortes oficiais do SIDRA/IBGE. O CEMPRE, o Censo e o arquivo separado de PIB total usam **2022**. A estrutura econômica (PIB, VAB e participações setoriais) usa **2021**, último ano em que as dez variáveis selecionadas estão simultaneamente disponíveis. Todos contêm três níveis territoriais na mesma base:

- Brasil (`N1`, código `1`);
- Ceará (`N3`, código `23`);
- os 184 municípios do Ceará (`N6`, códigos IBGE de sete dígitos).

| Arquivo | Tabela | Conteúdo | Linhas |
|---|---:|---|---:|
| `dados_originais/t9509_cempre_economia_emprego_2022_ce_br.csv` | 9509 | Empresas, unidades locais, ocupação, salários e remuneração | 1.116 |
| `dados_originais/t5938_pib_estrutura_economica_2021_ce_br.csv` | 5938 | PIB, VAB e composição setorial em 2021 | 1.860 |
| `dados_originais/t5938_pib_2022_ce_br.csv` | 5938 | PIB a preços correntes em 2022 | 186 |
| `dados_originais/t4709_populacao_censo_2022_ce_br.csv` | 4709 | População, variação absoluta e crescimento geométrico | 558 |

Não há dados limpos, indicadores calculados ou bases cruzadas neste pacote. Essa preparação faz parte do projeto dos alunos.

## Seleções realizadas

### Tabela 9509 — Cadastro Central de Empresas

- `706` — Número de unidades locais;
- `367` — Número de empresas e outras organizações atuantes;
- `707` — Pessoal ocupado total;
- `708` — Pessoal ocupado assalariado;
- `662` — Salários e outras remunerações;
- `10143` — Salário médio mensal em reais.

### Tabela 5938 — PIB dos Municípios, 2022

- `37` — Produto Interno Bruto a preços correntes.

Esse arquivo contém somente o PIB total de 2022. Ele foi fornecido separadamente para permitir o cálculo de PIB per capita com a população do Censo 2022, sem combinar numerador e denominador de anos diferentes.

### Tabela 5938 — Estrutura econômica, 2021

- `37` — Produto Interno Bruto a preços correntes;
- `498` — Valor adicionado bruto a preços correntes total;
- `513` e `516` — VAB da agropecuária e participação no VAB total;
- `517` e `520` — VAB da indústria e participação no VAB total;
- `6575` e `6574` — VAB dos serviços, exceto administração pública, e participação no VAB total;
- `525` e `528` — VAB da administração pública e participação no VAB total.

### Tabela 4709 — Censo Demográfico 2022

- `93` — População residente;
- `5936` — Variação absoluta da população residente em relação a 2010 compatibilizada;
- `10605` — Taxa de crescimento geométrico.

## Estrutura dos CSVs

Os arquivos estão em formato longo, separados por ponto e vírgula e codificados em UTF-8 com BOM. A resposta JSON da API oficial foi apenas transposta para CSV: códigos, nomes, unidades, valores e símbolos foram mantidos sem limpeza ou imputação.

| Coluna | Descrição |
|---|---|
| `nivel_territorial_codigo` | `N1`, `N3` ou `N6` |
| `nivel_territorial_nome` | Nome do nível territorial |
| `territorio_codigo` | Código oficial do território; deve ser lido como texto |
| `territorio_nome` | Brasil, Ceará ou nome do município |
| `ano_codigo`, `ano_nome` | Período da observação |
| `variavel_codigo`, `variavel_nome` | Identificação da variável SIDRA |
| `unidade` | Unidade fornecida pela API |
| `valor` | Valor original ou símbolo especial do SIDRA |

Exemplo de leitura:

```python
import pandas as pd

df = pd.read_csv(
    "dados_originais/t9509_cempre_economia_emprego_2022_ce_br.csv",
    sep=";",
    encoding="utf-8-sig",
    dtype={"territorio_codigo": "string", "variavel_codigo": "string"},
    keep_default_na=False,
)
```

## Cuidados obrigatórios

1. **PIB per capita de 2022:** usar `valor` da variável `37` em `t5938_pib_2022_ce_br.csv` e a população residente (`93`) de `t4709_populacao_censo_2022_ce_br.csv`. Como o PIB está em **mil reais** e a população em **pessoas**, o cálculo em reais por habitante requer multiplicar o PIB por 1.000 antes da divisão.
2. **Estrutura econômica de 2021:** usar `t5938_pib_estrutura_economica_2021_ce_br.csv` para VAB setorial e participações. Em 2022, a fonte disponibiliza o PIB total, mas não as variáveis estruturais selecionadas. Não combinar PIB total de 2022 com VAB de 2021 para criar participações de um suposto mesmo período.
3. Cruzamentos entre a estrutura econômica de 2021 e CEMPRE/Censo de 2022 são aproximações temporais e devem declarar a defasagem de um ano. Associações territoriais não demonstram causalidade.
4. O CEMPRE representa organizações formalmente constituídas e registradas no CNPJ; não mede todo o trabalho informal.
5. PIB, VAB, salários e remunerações estão em valores correntes/nominais. A variação do PIB entre 2021 e 2022 é nominal e não deve ser interpretada como crescimento real sem ajuste de preços.
6. Para cruzamentos, usar `territorio_codigo`, preservar `nivel_territorial_codigo` e manter o ano como parte da chave; não parear apenas pelo nome do município.
7. Brasil e Ceará são referências, não municípios. Não incluí-los em somas municipais.

## Validações realizadas

- todas as requisições responderam HTTP 200;
- esquema, UTF-8 com BOM e separador conferidos;
- exatamente 184 códigos municipais distintos em cada arquivo, além de Ceará e Brasil;
- períodos previstos: 2021 no arquivo estrutural da tabela 5938 e 2022 nos arquivos das tabelas 9509, 4709 e no PIB total da tabela 5938;
- zero ocorrências de `...` nas dez variáveis econômicas de 2021;
- zero ocorrências de símbolos especiais no PIB total de 2022;
- os 184 códigos municipais do PIB 2022 correspondem integralmente aos arquivos de PIB 2021 e Censo 2022;
- chaves territoriais/período/variável sem duplicatas;
- símbolos especiais preservados;
- hashes SHA-256 registrados em `fontes.csv`.

As URLs completas, filtros, horários e hashes estão em `fontes.csv`.
