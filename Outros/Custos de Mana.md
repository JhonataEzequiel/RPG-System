Este documento calcula o preço, em PMs, de certos efeitos. O principal intuito dele não é providenciar um balanceamento 100% correto, sempre sendo seguido à risca, mas sim uma ideia de como cada efeito contribui para o todo.

## Ordem de Cálculo

1. Some o preço de cada efeito da Magia (seção 2), incluindo Graus e duração.
2. Multiplique pelo fator de Área ou de Múltiplos Alvos, quando houver.
3. Some o custo de Alcance.
4. Aplique os descontos percentuais. Eles se somam entre si, até o máximo de 50%.
5. Subtraia o desconto fixo de Sacrifício de PV.
6. Arredonde (0,5 vira 1). O custo final nunca fica abaixo de 25% do custo bruto (o valor obtido no passo 3) e nunca fica abaixo de 1 PM.

Uma Magia com vários efeitos soma o preço de cada um no passo 1.

## 1. Custo Base

O dano de Grau 3 custa 1 PM, e esse é o parâmetro base da análise. Graus menores que isso são gratuitos. Alguns custos podem ser maiores ou menores que o esperado, sendo arbitrários com alguma lógica por trás. Outros podem ter valores fracionados, mas o custo final será dado como inteiro, arredondando de acordo com a matemática (0,5 vira 1).

### 1.1 Custo de Graus

A tabela a seguir mostra quanto cada Grau de dano, cura e restauração de Mana se converte em PMs. A cura custa 2x o preço do dano. Os preços são diferentes dos presentes nos equipamentos devido ao fato de que o dano aqui calculado é instantâneo, ou seja, uma instância de dano por PMs, ao invés de uma quantidade de dano sempre possível de ser causada através de Ataques. Os preços não são lineares.

|Grau|Média|Custo do Dano|Custo da Cura|Custo de PMs Restaurados|
|---|---|---|---|---|
|1|2,5|0 PM|0 PM|4 PM|
|2|3,5|0 PM|0 PM|5 PM|
|3|4,5|1 PM|2 PM|7 PM|
|4|5,5|1,5 PM|3 PM|8 PM|
|5|6,5|2 PM|4 PM|10 PM|
|6|7,0|2,5 PM|5 PM|11 PM|
|7|9,0|3 PM|6 PM|14 PM|
|8|11,0|3,5 PM|7 PM|17 PM|
|9|13,0|4 PM|8 PM|20 PM|
|10|16,5|5 PM|10 PM|25 PM|

Uma Magia de dano que não soma o BD do conjurador paga metade do custo de dano da tabela.

### 1.2 Estatísticas da Magia

As Estatísticas da Magia contribuem para o custo. O custo mínimo é 1.

Magias que têm um requisito adicional (como um item) não têm o custo diminuído, pois fazem parte da fantasia.

#### Área

O multiplicador de Área vale para o preço de todos os efeitos que afetam as criaturas dentro dela: dano, cura, Dano Contínuo, Regeneração, Condições, bônus, penalidades e demais.

|Raio equivalente|Multiplicador|
|---|---|
|1,5 metros|2x|
|3 metros|2,5x|
|4,5 metros|3x|
|6 metros|3,5x|
|7,5 metros|4x|
|9 metros|4,5x|
|Cada 1,5 metros a mais|+0,5x|

- **Esfera e Cilindro**: o raio equivalente é o próprio raio.
- **Cone e Cubo**: o raio equivalente é metade do comprimento (Cone) ou do lado (Cubo), arredondado para cima ao múltiplo de 1,5 metros mais próximo, com mínimo de 1,5 metros.
- **Linha**: o raio equivalente é 1,5 metros para cada 9 metros de comprimento (arredondando para cima), mais 1,5 metros caso a largura seja de 3 metros ou mais.

#### Múltiplos Alvos

O preço total dos efeitos é multiplicado pela quantidade de alvos escolhidos. Alvo Único multiplica por 1.

#### Alcance

|Alcance|Custo|
|---|---|
|Toque e até 9 metros|Gratuito|
|Cada 1,5 metros além de 9 metros|0,2 PM|

Em Magias de Múltiplos Alvos, o custo de Alcance é multiplicado pela quantidade de alvos. Em Magias de Área, o Alcance é pago uma única vez, até o Ponto de Origem.

### 1.3 Descontos

Os descontos percentuais abaixo se somam, até o máximo de 50%.

|Condição|Desconto|
|---|---|
|Ação Livre|0%|
|Ação Bônus|-5%|
|Uma Ação|-10%|
|Reação|-15%|
|Duas Ações|-20%|
|Três Ações|-25%|
|Minutos (só fora de combate)|-50%|
|Salvaguarda que reduz o dano à metade em caso de sucesso|-15%|
|Salvaguarda que nega o efeito em caso de sucesso|-25%|
|Afeta somente você|-10%|

Desconto fixo, aplicado depois dos percentuais:

|Condição|Desconto|
|---|---|
|Sacrifício de PV (-1)|-0,5 PM|

## 2. Efeitos

### 2.1 Efeitos Instantâneos

|Efeito|Custo|
|---|---|
|1 de dano|0,25 PM|
|1 de cura|0,5 PM|
|1 PM restaurado|1,5 PM|
|Empurrar ou puxar o alvo (1,5 metros)|0,25 PM|
|Teletransporte (1,5 metros)|0,25 PM|
|Remover uma Condição negativa|Metade do preço da Condição por 1 Encontro|
|Condição Morto aplicada|200 PM|
|Reviver uma criatura Morta|100 PM|
|1 de PV em um servo invocado|0,1 PM|
|1 de CA em um servo invocado|0,25 PM|
|1 de dano em um servo invocado|0,1 PM|
|1 de BA em um servo invocado|0,25 PM|
|1,5 metros de Deslocamento em um servo invocado|0,25 PM|
|1 Ação de um servo invocado por Rodada (até 3)|3 PM|

Servos invocados sempre duram 1 Encontro e sempre agem logo após o mestre deles na Iniciativa.

### 2.2 Efeitos Temporários

| Efeito                                               | 1 Rodada | 2 Rodadas | 3 Rodadas | 4 Rodadas | 1 Encontro |
| ---------------------------------------------------- | -------- | --------- | --------- | --------- | ---------- |
| +1 de BD                                             | 0,1 PM   | 0,15 PM   | 0,2 PM    | 0,25 PM   | 0,5 PM     |
| +1 de Resistência (por tipo de dano)                 | 0,1 PM   | 0,15 PM   | 0,2 PM    | 0,25 PM   | 0,5 PM     |
| +1 de Fraqueza aplicada (por tipo de dano)           | 0,1 PM   | 0,15 PM   | 0,2 PM    | 0,25 PM   | 0,5 PM     |
| +1,5 metros de Alcance Corpo a Corpo                 | 2 PM     | 2,5 PM    | 3 PM      | 4 PM      | 5 PM       |
| +1,5 metros de Alcance de Ataques Mágicos            | 2 PM     | 2,5 PM    | 3 PM      | 4 PM      | 5 PM       |
| +1,5 metros de Deslocamento / -1,5 metros no alvo    | 1 PM     | 2 PM      | 2,5 PM    | 3 PM      | 4 PM       |
| Deslocamento do alvo reduzido pela metade            | 3 PM     | 6 PM      | 8 PM      | 9 PM      | 12 PM      |
| Deslocamento de Voo (1,5 metros)                     | 1 PM     | 2,5 PM    | 3 PM      | 3,5 PM    | 5 PM       |
| +1 em Teste de Perícia                               | 0,25 PM  | 0,3 PM    | 0,35 PM   | 0,4 PM    | 0,5 PM     |
| +1 em um Atributo                                    | 0,5 PM   | 0,9 PM    | 1,3 PM    | 1,6 PM    | 2,5 PM     |
| +1 de BA / retirar 1 de BA do alvo                   | 1 PM     | 1,5 PM    | 2 PM      | 3 PM      | 3 PM       |
| +1 de CA / retirar 1 de CA do alvo                   | 1 PM     | 1,5 PM    | 2 PM      | 3 PM      | 3 PM       |
| +1 na Margem de Ameaça                               | 0,3 PM   | 0,45 PM   | 0,6 PM    | 0,75 PM   | 1,5 PM     |
| 1 PV Temporário                                      | 0,3 PM   | 0,35 PM   | 0,4 PM    | 0,45 PM   | 0,5 PM     |
| 1 PM Temporário                                      | 0,75 PM  | 0,9 PM    | 1 PM      | 1,1 PM    | 1,25 PM    |
| 1 de Regeneração de PV                               | 0,5 PM   | 1,1 PM    | 1,8 PM    | 2,5 PM    | 6 PM       |
| 1 de Regeneração de PM                               | 1,5 PM   | 3,3 PM    | 5,4 PM    | 7,5 PM    | 18 PM      |
| 1 de Dano Contínuo                                   | 0,25 PM  | 0,55 PM   | 0,9 PM    | 1,25 PM   | 3 PM       |
| 1 de Dano Persistente em Área (multiplica pela Área) | 0,25 PM  | 0,5 PM    | 0,75 PM   | 1 PM      | 2 PM       |
| Efeito utilitário menor                              | 0,25 PM  | 0,4 PM    | 0,5 PM    | 0,6 PM    | 1 PM       |

Efeitos utilitários menores são efeitos situacionais, sem impacto direto no combate e que não são Condições, como respirar debaixo d'água, escalar paredes ou enxergar no escuro.

### 2.3 Condições

|Condição aplicada|1 Rodada|2 Rodadas|3 Rodadas|4 Rodadas|1 Encontro|
|---|---|---|---|---|---|
|Caído|5 PM|6 PM|7 PM|8 PM|10 PM|
|Agarrado|6 PM|12 PM|18 PM|24 PM|60 PM|
|Amedrontado|4 PM|7 PM|9 PM|12 PM|14 PM|
|Debilitado (visão)|6 PM|9 PM|12 PM|18 PM|18 PM|
|Encantado|14 PM|27 PM|41 PM|54 PM|135 PM|
|Incapacitado|15 PM|30 PM|45 PM|60 PM|150 PM|
|Petrificado|23 PM|45 PM|68 PM|90 PM|225 PM|
|Furtivo|2 PM|3 PM|4 PM|5 PM|6 PM|
|Invisível|3 PM|4 PM|5 PM|6 PM|8 PM|

A Condição Exausto dura até um Descanso Longo. O preço é pelo Valor de Exaustão aplicado, já incluindo os efeitos dos Valores anteriores.

|Valor de Exaustão|Custo|
|---|---|
|1|30 PM|
|2|50 PM|
|3|100 PM|
|4|150 PM|
|5|200 PM|
|6|200 PM|

### 2.4 Durações Longas

Para efeitos de bônus e penalidades, Condições, PVs e PMs Temporários e efeitos utilitários, multiplique o preço da coluna de 1 Encontro. PVs e PMs Temporários sem duração especificada contam como 1 hora. Dano Contínuo, Dano Persistente em Área e Regeneração não possuem durações maiores que 1 Encontro.

|Duração|Multiplicador|
|---|---|
|20 minutos|1,25x|
|1 hora|1,5x|
|8 horas|2x|
|24 horas|2,5x|

### 2.5 Equivalências

- **Vantagem ou Desvantagem**: em Ataques, em todas as Salvaguardas ou em todos os Testes, valem 5 pontos de BA. Em um único Atributo, Perícia ou tipo restrito de Teste, valem 2 pontos de BA.
- **Resistência**: Resistência a Dano Físico (Cortante, Perfurante e de Impacto juntos) custa 2x o preço de um tipo. Resistência a todos os tipos de dano custa 5x.
- **Imunidade a um tipo de dano**: custa como 20 pontos de Resistência.
- **Imunidade a uma Condição negativa**: custa metade do preço da Condição, na mesma duração.
- **Debilitado em outro sentido**: custa metade do preço de Debilitado (visão).
- **Valores de referência**: efeitos que somam o BP, o Nível ou um Modificador são cobrados com BP 8, Nível 6 e Modificador +4.