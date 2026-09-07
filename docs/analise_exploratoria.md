# Análise exploratória: economia e emprego formal no Ceará

## Visão geral

As tabelas permitem analisar conjuntamente:

- **PIB e população:** PIB municipal de 2022 e população residente do Censo 2022.
- **Mercado formal:** empresas, unidades locais, pessoal ocupado, assalariados e salários do CEMPRE 2022.
- **Estrutura produtiva:** PIB, VAB total e composição setorial de 2021.
- **Dinâmica demográfica:** variação populacional desde 2010 e taxa de crescimento geométrico.

A chave correta para os cruzamentos é `territorio_codigo`, o código IBGE do município. Brasil e Ceará devem ser tratados como referências, não como municípios. As bases estruturais são de 2021, enquanto CEMPRE, PIB total e Censo são de 2022; portanto, os cruzamentos entre elas têm defasagem temporal de um ano.

## 1. Concentração espacial da atividade econômica

### Insight

A atividade econômica do Ceará é fortemente concentrada em poucos municípios, especialmente Fortaleza e sua área de influência metropolitana.

### Variáveis/Tabelas envolvidas

- PIB 2022: variável `37`, arquivo `t5938_pib_2022_ce_br.csv`;
- Pessoal ocupado total e assalariado: variáveis `707` e `708`, CEMPRE 2022;
- Salários e outras remunerações: variável `662`, CEMPRE 2022;
- População residente: variável `93`, Censo 2022.

### Relação identificada

Fortaleza possui aproximadamente:

- `R$ 81,4 bilhões` de PIB;
- `2,43 milhões` de habitantes;
- `951.646` pessoas ocupadas formalmente;
- `R$ 34,25 bilhões` em salários e outras remunerações.

Isso representa uma parcela muito elevada dos totais estaduais. O município concentra aproximadamente metade do pessoal ocupado do CEMPRE e cerca de 60% da massa salarial formal do Ceará, enquanto sua participação na população estadual é menor.

Além de Fortaleza, destacam-se Maracanaú, Eusébio, Caucaia, Sobral, Juazeiro do Norte e São Gonçalo do Amarante.

### Interpretação

Existe concentração econômica, ocupacional e salarial na capital e em municípios metropolitanos ou polos regionais. Esse padrão pode indicar centralização de empregos formais, serviços especializados, indústria e atividades administrativas.

Essa é uma associação descritiva. Ela não demonstra que a concentração de empregos causou maior PIB ou vice-versa.

### Métrica ou análise estatística recomendada

- Participação de cada município no PIB estadual;
- Participação no pessoal ocupado e na massa salarial;
- Razão entre a participação econômica e a participação populacional;
- Índice de concentração CR5 e CR10;
- Índice de Herfindahl-Hirschman;
- Curva de Lorenz e coeficiente de Gini municipal.

### Visualização recomendada

- Gráfico de Pareto;
- Mapa coroplético;
- Gráfico de barras com os 10 municípios líderes;
- Curva de concentração do PIB e dos salários.

### Possível aplicação prática

Apoiar políticas de desconcentração econômica, infraestrutura regional, qualificação profissional e fortalecimento de polos econômicos fora da capital.

## 2. PIB per capita muito desigual entre os municípios

### Insight

O PIB total e o PIB per capita produzem rankings diferentes. Municípios pequenos podem apresentar PIB per capita muito elevado, mesmo sem estarem entre os maiores em PIB absoluto.

### Variáveis/Tabelas envolvidas

- PIB 2022;
- População residente 2022.

### Relação identificada

O PIB per capita deve ser calculado como:

$$
PIBpc_i = \frac{PIB_i \times 1.000}{População_i}
$$

Exemplos aproximados:

- São Gonçalo do Amarante: cerca de `R$ 127 mil por habitante`;
- Eusébio: cerca de `R$ 61 mil`;
- Maracanaú: cerca de `R$ 60 mil`;
- Fortaleza: cerca de `R$ 33,5 mil`.

São Gonçalo do Amarante apresenta PIB total inferior ao de Fortaleza, mas PIB per capita muito superior devido à combinação de atividade econômica elevada e população menor.

### Interpretação

O PIB per capita é um indicador de produção média por habitante, não de renda efetivamente recebida pelas famílias. Municípios com indústria, refinarias, portos, grandes empresas ou empreendimentos específicos podem apresentar PIB per capita alto sem que isso implique distribuição homogênea de renda.

### Métrica ou análise estatística recomendada

- Mediana, média e percentis do PIB per capita;
- Razão entre o percentil 90 e o percentil 10;
- Coeficiente de variação;
- Assimetria e curtose;
- PIB per capita em escala logarítmica;
- Comparação entre PIB per capita, salário médio e salários por habitante.

### Visualização recomendada

- Histograma em escala logarítmica;
- Boxplot;
- Mapa coroplético;
- Ranking horizontal;
- Gráfico de dispersão entre população e PIB total, com tamanho ou cor representando PIB per capita.

### Possível aplicação prática

Identificar municípios com alta produção média, mas que precisam ser analisados separadamente quanto à distribuição de renda, serviços públicos e qualidade de vida.

## 3. Intensidade da ocupação formal não equivale à taxa de emprego

### Insight

Alguns municípios apresentam quantidade de trabalhadores formais muito alta em relação à população residente.

### Variáveis/Tabelas envolvidas

- Pessoal ocupado total, CEMPRE 2022;
- Pessoal ocupado assalariado, CEMPRE 2022;
- População residente, Censo 2022.

### Relação identificada

Pode-se calcular uma razão exploratória:

$$
IntensidadeFormal_i = \frac{PessoalOcupado_i}{População_i} \times 100
$$

Exemplos:

- Eusébio possui aproximadamente `70%` de pessoas ocupadas formais em relação à população residente;
- Fortaleza possui aproximadamente `39%`;
- São Gonçalo do Amarante possui aproximadamente `30%`.

Essa razão não deve ser chamada de taxa de emprego, pois o CEMPRE registra postos e pessoas vinculadas a organizações formais, enquanto a população inclui crianças, idosos, estudantes, desempregados, trabalhadores informais e pessoas que residem em um município mas trabalham em outro.

### Interpretação

Valores elevados podem indicar:

- forte atração de trabalhadores de outros municípios;
- concentração de empresas e postos de trabalho;
- presença de atividades industriais ou logísticas;
- diferenças entre local de residência e local de trabalho.

### Métrica ou análise estatística recomendada

- Pessoal ocupado por 100 habitantes;
- Pessoal assalariado por 100 habitantes;
- Razão assalariado/ocupado total;
- Unidades locais por 1.000 habitantes;
- Correlação entre intensidade formal e PIB per capita;
- Análise de municípios com valores acima do percentil 95.

### Visualização recomendada

- Mapa de intensidade formal;
- Dispersão entre intensidade formal e PIB per capita;
- Gráfico de barras dos municípios com maior razão;
- Boxplot por região ou grupo de tamanho populacional.

### Possível aplicação prática

Detectar polos de emprego, municípios-dormitório e possíveis deslocamentos pendulares. A interpretação deve ser complementada por dados de mobilidade e residência dos trabalhadores.

## 4. Massa salarial e salário médio medem dimensões diferentes

### Insight

Municípios com maior massa salarial não necessariamente apresentam os maiores salários médios.

### Variáveis/Tabelas envolvidas

- Salários e outras remunerações, variável `662`;
- Salário médio mensal, variável `10143`;
- Pessoal ocupado e pessoal assalariado.

### Relação identificada

Fortaleza concentra a maior massa salarial absoluta, mas o salário médio mensal pode ser maior em municípios menores com estruturas produtivas específicas.

O salário médio informado na base não deve ser confundido com renda média da população. Ele representa os vínculos ou pessoas ocupadas nas organizações formais abrangidas pelo CEMPRE.

### Interpretação

A massa salarial depende principalmente do tamanho do mercado formal. Já o salário médio depende da composição ocupacional, escolaridade, setor, cargos e presença de atividades de maior produtividade.

Um município pode ter:

- baixa massa salarial e salário médio alto;
- alta massa salarial e salário médio próximo da média estadual;
- grande número de trabalhadores, mas remunerações relativamente baixas.

### Métrica ou análise estatística recomendada

- Salários totais por pessoa assalariada;
- Salários por unidade local;
- Razão salário médio municipal/salário médio estadual;
- Correlação entre salário médio e PIB per capita;
- Regressão exploratória com controles para população e composição setorial.

### Visualização recomendada

- Dispersão com eixo logarítmico entre massa salarial e salário médio;
- Quadrantes: alto/baixo salário e alta/baixa massa salarial;
- Mapa do salário médio;
- Boxplots por setor dominante.

### Possível aplicação prática

Direcionar políticas de qualificação, atração de empresas de maior produtividade e melhoria da estrutura ocupacional.

## 5. A indústria apresenta forte concentração territorial

### Insight

A estrutura econômica de 2021 mostra que a indústria não está distribuída uniformemente entre os municípios.

### Variáveis/Tabelas envolvidas

- VAB da indústria, variável `517`;
- Participação da indústria no VAB total, variável `520`;
- PIB municipal 2021 e 2022;
- CEMPRE 2022.

### Relação identificada

A indústria tende a ser especialmente relevante em municípios como:

- Maracanaú;
- Fortaleza;
- Caucaia;
- Eusébio;
- Horizonte;
- São Gonçalo do Amarante;
- Aquiraz.

Os dados mostram, por exemplo, VAB industrial elevado em Caucaia, Fortaleza, Maracanaú, Eusébio e Horizonte.

### Interpretação

Municípios industriais podem apresentar:

- PIB per capita elevado;
- maior concentração de trabalhadores assalariados;
- salário médio superior à média estadual;
- maior arrecadação ou massa salarial.

Entretanto, a presença industrial pode elevar o PIB sem necessariamente produzir aumento proporcional da renda domiciliar ou redução das desigualdades.

### Métrica ou análise estatística recomendada

- Participação industrial no VAB;
- VAB industrial por habitante;
- Correlação entre participação industrial e salário médio;
- Comparação entre municípios industriais e não industriais;
- Teste de Mann-Whitney ou teste t, dependendo da distribuição e das premissas;
- Regressão de salário médio sobre participação industrial, controlando por população.

### Visualização recomendada

- Mapa da participação industrial;
- Dispersão entre participação industrial e salário médio;
- Gráfico de barras dos municípios com maior VAB industrial;
- Boxplot comparando grupos industriais e não industriais.

### Possível aplicação prática

Identificar municípios prioritários para políticas industriais, infraestrutura logística, formação técnica e mitigação de impactos ambientais.

## 6. Serviços e administração pública podem explicar perfis econômicos distintos

### Insight

Municípios com forte participação de serviços ou administração pública podem ter padrões de emprego e remuneração diferentes dos municípios industriais.

### Variáveis/Tabelas envolvidas

- VAB dos serviços, variável `6575`;
- Participação dos serviços, variável `6574`;
- VAB da administração pública, variável `525`;
- Participação da administração pública, variável `528`;
- CEMPRE 2022;
- PIB per capita.

### Relação identificada

Municípios-polo regionais, como Sobral, Crato, Juazeiro do Norte, Iguatu e Crateús, tendem a exercer funções de comércio, saúde, educação, administração e serviços para municípios vizinhos.

Em municípios menores, uma participação elevada da administração pública pode indicar menor diversificação da estrutura produtiva.

### Interpretação

Uma alta participação da administração pública não é necessariamente negativa. Ela pode refletir oferta de serviços regionais. Porém, quando combinada com baixa participação industrial e baixo número de unidades locais, pode indicar dependência relativa do setor público.

A relação entre estrutura setorial e emprego de 2022 é uma associação com defasagem temporal de um ano.

### Métrica ou análise estatística recomendada

- Participação do setor público no VAB;
- Índice de diversificação setorial;
- Razão VAB privado/VAB público;
- Correlação entre participação pública e número de unidades locais;
- Classificação dos municípios em perfis: industrial, serviços, agropecuário, público e diversificado.

### Visualização recomendada

- Gráfico ternário ou quadrantes setoriais;
- Barras empilhadas com a composição do VAB;
- Heatmap das participações setoriais;
- Clusterização exploratória, sem usar o agrupamento como prova causal.

### Possível aplicação prática

Apoiar políticas de diversificação econômica e planejamento de serviços regionais.

## 7. A agropecuária é mais relevante em municípios do interior

### Insight

A participação da agropecuária no VAB é muito heterogênea e tende a ser maior em municípios interioranos e menos urbanizados.

### Variáveis/Tabelas envolvidas

- VAB da agropecuária, variável `513`;
- Participação da agropecuária, variável `516`;
- População;
- PIB per capita;
- Crescimento populacional.

### Relação identificada

A participação agropecuária é elevada em municípios como:

- Milhã;
- Guaraciaba do Norte;
- Missão Velha;
- São João do Jaguaribe;
- Varjota;
- Porteiras;
- Tianguá.

Por outro lado, em Fortaleza, Maracanaú, Eusébio, Sobral e Juazeiro do Norte, a participação agropecuária é muito baixa.

### Interpretação

O padrão é compatível com diferenças de urbanização, disponibilidade de terras, atividades agrícolas, fruticultura, pecuária e estrutura industrial.

A agropecuária pode ter participação percentual alta mesmo em municípios cujo VAB absoluto é pequeno. Por isso, é importante observar simultaneamente participação e valor absoluto.

### Métrica ou análise estatística recomendada

- VAB agropecuário por habitante;
- Participação agropecuária;
- Correlação com crescimento populacional;
- Comparação de PIB per capita entre municípios com alta e baixa participação agropecuária;
- Índice de especialização relativa.

### Visualização recomendada

- Mapa da participação agropecuária;
- Dispersão entre participação agropecuária e PIB per capita;
- Ranking dos municípios;
- Gráfico de composição setorial.

### Possível aplicação prática

Planejar assistência técnica, infraestrutura rural, cadeias produtivas, armazenamento e políticas de adaptação climática.

## 8. Existem sinais de associação entre crescimento populacional e dinamismo econômico

### Insight

Municípios com crescimento populacional elevado podem estar associados a expansão urbana, novos empregos, migração ou investimentos, mas a direção da relação não pode ser estabelecida com essas bases.

### Variáveis/Tabelas envolvidas

- Taxa de crescimento geométrico, variável `10605`;
- Variação absoluta da população, variável `5936`;
- PIB per capita 2022;
- Pessoal ocupado;
- Unidades locais.

### Relação identificada

Exemplos de crescimento elevado:

- Itaitinga: aproximadamente `5,47%`;
- Eusébio: aproximadamente `4,06%`;
- Jijoca de Jericoacoara: aproximadamente `3,48%`;
- Horizonte: aproximadamente `2,56%`.

Exemplos de crescimento baixo ou negativo:

- Catarina: aproximadamente `-4,89%`;
- São João do Jaguaribe: aproximadamente `-2,47%`;
- Caridade: aproximadamente `-1,63%`;
- Fortaleza: aproximadamente `-0,11%`.

### Interpretação

O crescimento pode estar relacionado a:

- expansão metropolitana;
- turismo;
- industrialização;
- disponibilidade de empregos;
- mudanças na estrutura rural;
- migração para centros regionais.

Mas também pode resultar de fatores não observados, como fecundidade, mortalidade, migração e mudanças administrativas.

### Métrica ou análise estatística recomendada

- Correlação de Spearman entre crescimento populacional e PIB per capita;
- Correlação entre crescimento e intensidade formal;
- Comparação entre municípios metropolitanos e não metropolitanos;
- Regressão exploratória, com controles para população inicial e composição setorial;
- Análise de outliers demográficos.

### Visualização recomendada

- Dispersão crescimento populacional versus PIB per capita;
- Mapa bivariado;
- Quadrantes de crescimento e dinamismo econômico;
- Gráfico de barras dos maiores crescimentos e quedas.

### Possível aplicação prática

Antecipar demanda por moradia, transporte, escolas, saúde, saneamento e emprego.

## 9. O crescimento do PIB entre 2021 e 2022 é nominal

### Insight

A comparação dos arquivos de PIB de 2021 e 2022 sugere crescimento nominal em vários municípios, mas não permite afirmar crescimento real da economia.

### Variáveis/Tabelas envolvidas

- PIB 2021 da estrutura econômica;
- PIB 2022;
- CEMPRE 2022;
- Inflação ou deflator, que não estão presentes no pacote.

### Relação identificada

Alguns exemplos aproximados de variação nominal:

- Fortaleza: crescimento de cerca de `10,8%`;
- Maracanaú: crescimento de cerca de `13,5%`;
- Eusébio: crescimento de cerca de `27,4%`;
- São Gonçalo do Amarante: redução nominal de aproximadamente `20%`.

Esses valores são variações de preços correntes e podem refletir inflação, preços relativos, mudanças na produção ou composição setorial.

### Interpretação

O resultado não deve ser descrito como crescimento econômico real. Para isso seriam necessários deflatores, séries em preços constantes ou dados de volume.

Além disso, mudanças muito grandes devem ser investigadas quanto a alterações metodológicas, preços de commodities, grandes empreendimentos ou eventos específicos.

### Métrica ou análise estatística recomendada

- Variação nominal do PIB;
- Variação do PIB per capita;
- Deflacionamento por índice apropriado;
- Comparação com IPCA ou deflator implícito;
- Análise de contribuição setorial, quando houver dados compatíveis.

### Visualização recomendada

- Mapa da variação nominal;
- Ranking de crescimento e queda;
- Gráfico de dispersão PIB 2021 versus PIB 2022;
- Gráfico de barras divergentes.

### Possível aplicação prática

Identificar municípios que precisam de investigação econômica específica, mas sem classificar automaticamente os resultados como expansão ou recessão real.

## 10. Outliers econômicos e demográficos merecem investigação individual

### Insight

Há municípios que se destacam por combinações incomuns de PIB, população, emprego formal e estrutura setorial.

### Possíveis outliers

- **São Gonçalo do Amarante:** PIB per capita muito elevado e forte presença industrial/logística.
- **Eusébio:** alta intensidade de ocupação formal, população relativamente pequena e elevado PIB per capita.
- **Fortaleza:** grande escala absoluta de PIB, emprego e salários, mas PIB per capita inferior ao de vários municípios industriais menores.
- **Itaitinga:** elevado crescimento populacional e dinamismo metropolitano.
- **Catarina:** forte queda populacional e baixa dinâmica relativa.
- **Jijoca de Jericoacoara:** crescimento populacional elevado, possivelmente relacionado ao turismo.
- **Municípios com participação agropecuária acima de 40%:** devem ser analisados quanto à especialização produtiva e à volatilidade agrícola.

### Métrica ou análise estatística recomendada

- Distância da mediana em unidades de desvio robusto;
- Intervalo interquartil;
- Pontuação z para PIB per capita, salário médio e intensidade formal;
- Distância de Mahalanobis para identificar combinações multivariadas atípicas;
- Análise espacial local de outliers, como Local Moran’s I.

### Visualização recomendada

- Scatterplots rotulados;
- Boxplots;
- Mapa de outliers;
- Matriz de dispersão;
- Gráfico de bolhas com população, PIB e emprego.

### Possível aplicação prática

Priorizar estudos de caso municipais, auditoria de dados, investigação de grandes empreendimentos e avaliação de políticas públicas.

## Relações que devem ser testadas estatisticamente

As seguintes associações são plausíveis, mas não devem ser apresentadas como estatisticamente relevantes antes do cálculo:

| Relação | Teste recomendado |
|---|---|
| PIB per capita × intensidade formal | Spearman e Pearson após transformação logarítmica |
| PIB per capita × salário médio | Spearman, regressão robusta |
| Participação industrial × salário médio | Correlação parcial e regressão exploratória |
| Participação agropecuária × crescimento populacional | Spearman |
| Participação pública × unidades locais | Correlação parcial controlando por população |
| População × PIB total | Regressão log-log |
| Crescimento populacional × dinamismo formal | Spearman e análise por grupos |
| Estrutura setorial × PIB per capita | Regressão multivariada com defasagem temporal explicitada |

Para classificar uma associação como estatisticamente relevante, seria necessário observar:

- tamanho do efeito;
- intervalo de confiança;
- valor-p;
- estabilidade a transformações e outliers;
- análise de resíduos;
- correção para múltiplos testes;
- possível dependência espacial.

Um valor-p pequeno, isoladamente, não demonstra causalidade nem importância prática.

## Indicadores derivados prioritários

1. PIB per capita 2022.
2. PIB per capita em logaritmo.
3. Pessoal ocupado formal por 100 habitantes.
4. Pessoal assalariado por 100 habitantes.
5. Unidades locais por 1.000 habitantes.
6. Salário médio relativo ao Ceará.
7. Massa salarial por trabalhador assalariado.
8. VAB setorial por habitante.
9. Índice de diversificação setorial.
10. Participação municipal no PIB estadual.
11. Participação municipal na massa salarial estadual.
12. Variação nominal do PIB entre 2021 e 2022.
13. Crescimento populacional geométrico.
14. Índice de especialização setorial.
15. Índice de concentração econômica municipal.

# 10 insights prioritários

1. **Concentração do PIB, emprego e salários em Fortaleza e na área metropolitana.**
2. **Desigualdade espacial do PIB per capita entre os municípios.**
3. **Diferença entre PIB per capita elevado e renda efetiva da população.**
4. **Municípios com forte intensidade de ocupação formal em relação à população.**
5. **Concentração territorial da indústria e sua possível associação com salários.**
6. **Diferença entre massa salarial total e salário médio mensal.**
7. **Especialização agropecuária de municípios interioranos.**
8. **Dependência relativa da administração pública em determinados municípios.**
9. **Associação entre crescimento populacional, expansão metropolitana e dinamismo formal.**
10. **Outliers econômicos e demográficos que exigem estudos de caso específicos.**

## Conclusão metodológica

Os dados são suficientes para uma análise exploratória robusta de desigualdade, concentração, especialização produtiva e associação entre estrutura econômica e emprego. Porém, não permitem conclusões causais sem controles adicionais, séries temporais mais longas, dados de renda domiciliar, deslocamento pendular, informalidade, preços constantes e métodos de análise espacial.
