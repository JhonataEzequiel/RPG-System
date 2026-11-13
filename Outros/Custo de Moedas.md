Este documento calcula, em moedas, quanto valem os efeitos de Armas, Armaduras, Escudos, e outros itens. O principal intuito dele não é providenciar um balanceamento 100% correto, sempre sendo seguido à risca, mas sim uma ideia de como cada efeito contribui para o todo.

**Arredondamento dos Preços (Regra de Ouro)**: Ao finalizar o cálculo dos preços, é prudente arredondar o resultado. Caso o preço seja menor que 1 PO, ponha-o em PP e PC. Por exemplo, 9 PP 3 PC. Caso o preço seja maior ou igual a 1 PO e menor que 99 PO, utilize apenas PO. Caso o preço seja maior ou igual a 100 PO, coloque em PL e PO. Por exemplo, 205 PO viram 20 PL 5 PO. Por fim, sempre arredonde baseando-se na matemática básica, não na regra de arredondamento do Cap.1.

## 1. Custo Base

A moeda base usada será 1 PO. Um item de 1 PC não tem efeito mecânico algum, como a vestimenta básica. Os preços de BA e CA são iguais e arbitrários, visando um jogo mais barato nos Níveis baixos e mais caro nos Níveis altos.

|BA e CA|Preço|BA e CA|Preço|
|---|---|---|---|
|+1|1 PO|+6|75 PO|
|+2|5 PO|+7|100 PO|
|+3|10 PO|+8|150 PO|
|+4|25 PO|+9|300 PO|
|+5|50 PO|+10|750 PO|

Escalas não contam para esses números. Por enquanto, apenas Armaduras contribuem permanentemente para a CA, e nada contribui permanentemente para o BA, mas esses números estão aí como prevenção, caso um item assim exista.

### 1.1 Descontos

Alguns efeitos ruins conferem descontos aos itens:

|Efeito|Desconto|
|---|---|
|Desvantagem em uma Perícia|reduz 1/4 do custo total|
|-1,5 metros de Deslocamento|reduz 1/8 do custo total|
|Requer uma Ação e não é um Ataque/Arma|reduz 1/4 do custo total|
|Requer uma Reação e não é um Ataque/Arma|reduz 1/4 do custo total|
|Requer uma Ação Bônus e não é um Ataque/Arma|reduz 1/8 do custo total|
|Requer uma Salvaguarda para ter efeito e não é um Ataque/Arma|reduz 1/8 do custo total|
|Uma vez por Descanso Curto/por qualquer Descanso|reduz 1/16 do custo total|
|Uma vez por Descanso Longo|reduz 1/8 do custo total|
|Uma vez por Encontro|reduz 1/8 do custo total|
|Uma vez por Alvo|reduz 1/8 do custo total|

Sempre aplique os descontos percentuais acima antes dos descontos fixos que vêm a seguir. Caso um Desconto apareça mais de uma vez, por exemplo, -3 metros de Deslocamento, o equivalente é o Desconto de -1,5 metros aplicado duas vezes, ou seja, 1/4. Divide-se o denominador por 2 a cada repetição, até o máximo de 1/2 do custo total reduzido.

### 1.1.1 Requisitos

Quanto maior o requisito, menor o custo. Um requisito de valor X desconta X PO do item.

### 1.1.2 Peso

Quanto maior o Peso, menor o custo. Cada unidade de Peso reduz o valor do item em 5 PP.

## 2. Efeitos Concedidos por Itens

### 2.1 Efeitos Permanentes (Passivas)

| Efeito                                                                                                                  | Preço  | Justificativa e Acréscimos                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +1 de BD                                                                                                                | 2 PO   | Parece ok                                                                                                                                                      |
| +1 de Resistência a um tipo de dano                                                                                     | 3 PO   | Efeito contrário ao dano. O custo é superior ao dano por ter um impacto maior, já que não precisa "acertar" um Teste para que a resistência seja aplicada.     |
| +1,5 m de alcance corpo a corpo                                                                                         | 10 PO  | O preço triplica a cada iteração, ou seja, +4,5 m custaria 90 PO.                                                                                              |
| +1,5 m de alcance de Ataque à distância (até 9 m é gratuito para Armas à Distância, e depois de 48 m também é gratuito) | 1 PO   | O preço parece justo, no geral                                                                                                                                 |
| +1,5 m de Deslocamento                                                                                                  | 250 PO | Preço linear                                                                                                                                                   |
| +1 em um Teste de Perícia                                                                                               | 16 PO  | Preço cúbico com início em 2, ou seja, o X inicial é 2, que é elevado ao cubo. Para cada +1, aumenta-se o X em 1. Por exemplo, +2 seria 3 ao cubo que é 27 PO. |
| 1 de Regeneração de PV                                                                                                  | 375 PO | mesmo preço de um efeito desses que dure mais de uma hora                                                                                                      |
| 1 de Regeneração de PM                                                                                                  | 938 PO | 2.5x regeneração de PV                                                                                                                                         |

### 2.2 Efeitos Instantâneos

Efeitos que duram apenas um instante, por exemplo, no momento em que se consome uma poção. Itens consumíveis também entram aqui. Basicamente, são efeitos que ocorrem uma única vez e não perduram, portanto, são mais baratos. Causar 1 de dano, por exemplo, é diferente de ter +1 de BD.

| Efeito                                     | Preço     | Justificativa e Acréscimos                                |
| ------------------------------------------ | --------- | --------------------------------------------------------- |
| 1 de Cura (alvo único)                     | 2 PO      | 2x dano em alvo único                                     |
| 1 PM restaurado                            | 5 PO      | Mana tem mais implicações do que apenas 1 PV              |
| 1 de Dano causado (alvo único)             | 1 PO      | Preço base                                                |
| 1 de Dano causado (por 1,5 metros de área) | 1 PO 5 PP | 1,5x o dano em alvo único                                 |
| 1 de PV  Temporário                        | 188 PO    | mesmo preço de um efeito desses que dure mais de uma hora |
| 1 de PM  Temporário                        | 470 PO    | 2.5x PV Temporário                                        |

Caso um item conceda graus de cura, dano, ou restauração de PMs:

| Grau | Média | Preço de Cura | Preço de Dano | Preço de PMs restaurados |
| ---- | ----- | ------------- | ------------- | ------------------------ |
| 1    | 2,5   | 5 PO          | 2 PO 5 PP     | 12 PO 5 PP               |
| 2    | 3,5   | 7 PO          | 3 PO 5 PP     | 17 PO 5 PP               |
| 3    | 4,5   | 9 PO          | 4 PO 5 PP     | 22 PO 5 PP               |
| 4    | 5,5   | 11 PO         | 5 PO 5 PP     | 27 PO 5 PP               |
| 5    | 6,5   | 13 PO         | 6 PO 5 PP     | 32 PO 5 PP               |
| 6    | 7,0   | 14 PO         | 7 PO          | 35 PO                    |
| 7    | 9,0   | 18 PO         | 9 PO          | 45 PO                    |
| 8    | 11,0  | 22 PO         | 11 PO         | 55 PO                    |
| 9    | 13,0  | 26 PO         | 13 PO         | 65 PO                    |
| 10   | 16,5  | 33 PO         | 16 PO 5 PP    | 82 PO 5 PP               |

Aumentar em 1,5 m o raio da Área dos danos em área causados por um item multiplica o preço base por 1,5. Por exemplo: 3 metros de raio seria 1,5x o preço de 1,5 metros (2,25x o preço do alvo único), e 4,5 metros seria 2,25x o preço de 1,5 metros (3,375x o do alvo único). Para precificar um dano em área, multiplique o Preço de Dano da tabela acima por esse fator. Itens arremessados que causam dano em área exigem uma Salvaguarda de Destreza em vez de um Ataque, então os descontos de Ação e de Salvaguarda se aplicam a eles.

### 2.3 Efeitos Duradouros, mas Não Permanentes

Os efeitos são uma fração dos efeitos permanentes, por motivos óbvios. Quando existe um preço permanente correspondente, ele é o teto: um efeito temporário nunca custa mais que o permanente. A exceção são o BA e a CA, explicados a seguir.

BA e CA valem mais à medida que são acumulados, então o preço em 4 Rodadas é equivalente ao de um bônus de +4, em vez de +1. O aumento de Deslocamento também custará menos, 50 PO para 4 Rodadas.

Dano Contínuo é particularmente mais forte que dano normal. Uma vez atingido por Dano Contínuo, você continua recebendo dano. Ou seja, as instâncias se aplicam sem o alvo poder resistir com uma Salvaguarda ou com a CA. Dano que deixa de ser causado quando a criatura sai de uma área não é Dano Contínuo (veja a seção 2.4). Regeneração é similar, já que o efeito é passivo, não requerendo Ação, Ação Bônus, Reação ou sequer Ação Livre.

| Efeito                              | Preço por 1 Rodada | Preço por 2 Rodadas | Preço por 3 Rodadas | Preço por 4 Rodadas | Preço por 1 Encontro | Preço por 1 hora | Preço por mais de uma hora |
| ----------------------------------- | ------------------ | ------------------- | ------------------- | ------------------- | -------------------- | ---------------- | -------------------------- |
| 1 de Dano Contínuo                  | 1 PO               | 3 PO                | 6 PO                | 12 PO               | 24 PO                | 144 PO           | 250 PO                     |
| 1 de Regeneração de PV              | 1 PO 5 PP          | 5 PO                | 9 PO                | 18 PO               | 36 PO                | 216 PO           | 375 PO                     |
| 1 de Regeneração de PM              | 3 PO 8 PP          | 12 PO 5 pp          | 22 PO 5 PP          | 45 PO               | 90 PO                | 540 PO           | 938 PO                     |
| 1 de PV  Temporário                 | 7 PP               | 3 PO                | 5 PO                | 9 PO                | 18 PO                | 108 PO           | 188 PO                     |
| 1 de PM  Temporário                 | 1 PO 8 PP          | 8 PO                | 12 PO 5 PP          | 22 PO 5 PP          | 45 PO                | 270 PO           | 470 PO                     |
| +1 no BD                            | 5 PP               | 7 PP                | 9 PP                | 1 PO 5 PP           | 2 PO                 | 2 PO             | 2 PO                       |
| +1 no BA                            | 5 PO               | 10 PO               | 20 PO               | 25 PO               | 40 PO                | 240 PO           | 500 PO                     |
| +1 na CA                            | 5 PO               | 10 PO               | 20 PO               | 25 PO               | 40 PO                | 240 PO           | 500 PO                     |
| +1 de Resistência                   | 5 PP               | 8 PP                | 1 PO                | 1 PO 5 PP           | 3 PO                 | 3 PO             | 3 PO                       |
| Aumenta em 1 o valor de um Atributo | 1 PO               | 2 PO                | 3 PO                | 4 PO                | 5 PO                 | 30 PO            | 50 PO                      |
| +1,5 metros de Deslocamento         | 10 PO              | 20 PO               | 35 PO               | 50 PO               | 75 PO                | 250 PO           | 250 PO                     |
| Recebe uma Condição positiva        | 10 PO              | 15 PO               | 20 PO               | 25 PO               | 40 PO                | 240 PO           | 500 PO                     |
| Outros efeitos menores              | 4 PP               | 6 PP                | 8 PP                | 1 PO                | 1 PO 6 PP            | 9 PO 6 PP        | 20 PO                      |

Outros efeitos menores são efeitos situacionais ou de utilidade, sem impacto direto no combate e que não são Condições, como respirar debaixo d'água, escalar paredes ou enxergar no escuro. A linha tem 1/25 dos valores da linha de Condição positiva.

Considere PVs Temporários como tendo metade do preço da Regeneração. Isso se dá pelo fato de não contarem como instância de cura, ou seja, não diminuem o poder da Condição Morrendo, nem se beneficiam de Habilidades e efeitos que melhorem as curas.

PMs Temporários são 2.5x mais caros que PVs Temporários, assim como regeneração de PM é 2.5x mais cara que regeneração de PV.

### 2.4 Dano Persistente em Área

Dano causado no início de cada Turno apenas enquanto a criatura permanecer na área. Não é Dano Contínuo, pois basta sair da área para que ele deixe de ser causado. Cada instância é cobrada como dano instantâneo em área, uma por Rodada de duração, sem acréscimo. Para a duração de 1 Encontro, contam-se 8 instâncias, a mesma proporção da tabela de Dano Contínuo, em que 1 Encontro custa o dobro de 4 Rodadas.

Justificativa: em durações curtas, o Dano Contínuo custa cerca do dobro do dano instantâneo por instância, por não poder ser evitado. O Dano Persistente pode ser evitado saindo da área, e isso anula esse acréscimo.

## 3. Valor das Armas

### 3.1 Grau

O preço do Grau será relacionado ao preço do BD permanente (2 PO por ponto da média do dado, como em +1 de BD), acrescido de uma taxa arbitrária sobre o preço.

| Grau | Dado | Média | Preço | Taxa | Preço Final |
| ---- | ---- | ----- | ----- | ---- | ----------- |
| 1    | 1d4  | 2,5   | 5 PO  | 1x   | 5 PO        |
| 2    | 1d6  | 3,5   | 7 PO  | 1x   | 7 PO        |
| 3    | 1d8  | 4,5   | 9 PO  | 1x   | 9 PO        |
| 4    | 1d10 | 5,5   | 11 PO | 1x   | 11 PO       |
| 5    | 1d12 | 6,5   | 13 PO | 1x   | 13 PO       |
| 6    | 2d6  | 7,0   | 14 PO | 2x   | 28 PO       |
| 7    | 2d8  | 9,0   | 18 PO | 3x   | 54 PO       |
| 8    | 2d10 | 11,0  | 22 PO | 4x   | 88 PO       |
| 9    | 2d12 | 13,0  | 26 PO | 5x   | 130 PO      |
| 10   | 3d10 | 16,5  | 33 PO | 10x  | 330 PO      |

### 3.1.1 Aprimorar o Grau de uma Arma

O preço final de cada melhoria é mostrado pelas tabelas a seguir, cobrindo Armas, Armaduras, e Escudos, nessa ordem. O tempo para realizar uma melhoria, independente do patamar, é de 8 horas.

| Para chegar ao Grau (Armas) | Pedras | Custo das Pedras | Taxa do Ferreiro | Preço do Passo | Total Acumulado |
| --------------------------- | ------ | ---------------- | ---------------- | -------------- | --------------- |
| 1                           | 0      | 0                | 0                | 0              | 0               |
| 2                           | 1      | 10 PO            | 10 PO            | 20 PO          | 20 PO           |
| 3                           | 1      | 10 PO            | 10 PO            | 20 PO          | 40 PO           |
| 4                           | 1      | 10 PO            | 10 PO            | 20 PO          | 60 PO           |
| 5                           | 2      | 20 PO            | 20 PO            | 40 PO          | 100 PO          |
| 6                           | 2      | 20 PO            | 20 PO            | 40 PO          | 140 PO          |
| 7                           | 2      | 20 PO            | 20 PO            | 40 PO          | 180 PO          |
| 8                           | 3      | 30 PO            | 30 PO            | 60 PO          | 240 PO          |
| 9                           | 3      | 30 PO            | 30 PO            | 60 PO          | 300 PO          |
| 10                          | 5      | 50 PO            | 50 PO            | 100 PO         | 400 PO          |

| Para chegar ao CA (Armaduras) | Pedras | Custo das Pedras | Taxa do Ferreiro | Preço do Passo | Total Acumulado |
| ----------------------------- | ------ | ---------------- | ---------------- | -------------- | --------------- |
| +1                            | 0      | 0                | 0                | 0              | 0               |
| +2                            | 1      | 10 PO            | 30 PO            | 40 PO          | 40 PO           |
| +3                            | 1      | 10 PO            | 30 PO            | 40 PO          | 80 PO           |
| +4                            | 1      | 10 PO            | 30 PO            | 40 PO          | 120 PO          |
| +5                            | 2      | 20 PO            | 60 PO            | 80 PO          | 200 PO          |
| +6                            | 2      | 20 PO            | 60 PO            | 80 PO          | 280 PO          |
| +7                            | 2      | 20 PO            | 60 PO            | 80 PO          | 360 PO          |
| +8                            | 3      | 30 PO            | 90 PO            | 120 PO         | 480 PO          |
| +9                            | 3      | 30 PO            | 90 PO            | 120 PO         | 600 PO          |
| +10                           | 5      | 50 PO            | 150 PO           | 200 PO         | 800 PO          |

| Para chegar à Resistência (Escudos) | Pedras | Custo das Pedras | Taxa do Ferreiro | Preço do Passo | Total Acumulado |
| ----------------------------------- | ------ | ---------------- | ---------------- | -------------- | --------------- |
| +1                                  | 0      | 0                | 0                | 0              | 0               |
| +2                                  | 1      | 10 PO            | 5 PO             | 15 PO          | 15 PO           |
| +3                                  | 1      | 10 PO            | 5 PO             | 15 PO          | 30 PO           |
| +4                                  | 1      | 10 PO            | 5 PO             | 15 PO          | 45 PO           |
| +5                                  | 2      | 20 PO            | 10 PO            | 30 PO          | 75 PO           |
| +6                                  | 2      | 20 PO            | 10 PO            | 30 PO          | 105 PO          |
| +7                                  | 2      | 20 PO            | 10 PO            | 30 PO          | 135 PO          |
| +8                                  | 3      | 30 PO            | 15 PO            | 45 PO          | 180 PO          |
| +9                                  | 3      | 30 PO            | 15 PO            | 45 PO          | 225 PO          |
| +10                                 | 5      | 50 PO            | 25 PO            | 75 PO          | 300 PO          |

### 3.2 Escalas de Armas e Armaduras

Considera-se um Atributo em 10 para elas. Quaisquer bônus de Escala custarão metade do que deveriam custar, por conta da necessidade de gastar PAs e de esperar até estar em um Nível adequado para chegar aos patamares desejados. BAs e CAs de Escalas são gratuitos, custando apenas os PAs necessários para cada patamar.

Além dos bônus padrão, será aplicada uma taxa sobre o preço base cobrado. A taxa sobe conforme a Escala aumenta e diz respeito apenas a uma Arma ou Armadura encontrada naturalmente com essas Escalas, e não a uma Arma ou Armadura que foi melhorada aos poucos.

|Escala de Arma|Preço Base|Taxa|Preço final|
|---|---|---|---|
|D|5 PO|1x|5 PO|
|C|10 PO|2x|20 PO|
|B|15 PO|5x|75 PO|
|A|20 PO|15x|300 PO|
|S|25 PO|100x|2500 PO|

O preço das Escalas de Armadura será arredondado para cima.

|Escala de Armadura|Preço Base|Taxa|Preço final|
|---|---|---|---|
|D|8 PO|1x|8 PO|
|C|15 PO|1,5x|23 PO|
|B|23 PO|5x|115 PO|
|A|30 PO|15x|450 PO|
|S|38 PO|75x|2850 PO|

### 3.2.1 Aprimorar ou Mudar Escalas

O preço de uma Pedra de Infusão comum (Pesada, Afiada, Mágica, Transcendente, Charmosa, Vital e Sábia) é de 50 PO. As Pedras Mundana, de Qualidade, Bruta, e Branca custam 100 PO. O preço para Infundir depende do grau que a Escala terá após a Infusão.

| Grau Resultante | Preço da Pedra de Infusão Comum | Preço de Pedras Exclusivas | Preço para Infundir | Preço Final Comum | Preço Final Exclusivas |
| --------------- | ------------------------------- | -------------------------- | ------------------- | ----------------- | ---------------------- |
| C               | 50 PO                           | 100 PO                     | 20 PO               | 70 PO             | 120 PO                 |
| B               | 50 PO                           | 100 PO                     | 70 PO               | 120 PO            | 170 PO                 |
| A               | 50 PO                           | 100 PO                     | 300 PO              | 350 PO            | 400 PO                 |
| S               | 50 PO                           | 100 PO                     | 2400 PO             | 2450 PO           | 2500 PO                |

| Tipo de Pedra     | Total da Escala D até a S |
| ----------------- | ------------------------- |
| Pedras Exclusivas | 3190                      |
| Pedras            | 2990                      |

Para remover as Infusões de um item com a Pedra Branca, o preço é de 100 PO.

#### 3.2.1.1 Pedra Bruta

| Arma (BD) | Armadura (CA) | Preço para Infundir |
| --------- | ------------- | ------------------- |
| +BP       | +NV/4         | 150 PO              |

## 4. Habilidades de Escudos

Um Escudo concede **Resistência a Dano Físico e Mágico**. Ou seja, o preço de cada +1 de Resistência será dobrado (6 PO cada ponto de Resistência).

Cada Escudo traz uma Habilidade. Os valores abaixo são estimativas. Aparar adiciona +3 de CA efetiva (+15% de chance do Ataque errar), mas apenas por um instante. Golpe de Escudo custa uma Ação e rende o dano mais o -3 de BA do alvo por um Turno, com 65% de falha na Salvaguarda. Parede de Escudo rende +1 de Resistência na próxima instância.

|Habilidade de Escudo|Preço|Justificativa|
|---|---|---|
|Aparar (1 uso por Encontro)|6 PO 3 PP|Bruto de 10 PO: +3 de CA contra um Ataque custaria isso se fosse permanente. Descontos de Reação (1/4) e de uma vez por Encontro (1/8) reduzem 3/8: 6 PO 2,5 PP, arredondado para 6 PO 3 PP.|
|Golpe de Escudo (1 uso por alvo, já descontada a Ação)|9 PO 8 PP|Bruto de 19 PO 5 PP: Grau 3 de dano instantâneo (4 PO 5 PP) mais -3 no BA por 1 Rodada (15 PO, ou seja, 5 PO por ponto). Descontos de Ação (1/4), Salvaguarda (1/8) e uma vez por alvo (1/8) reduzem metade: 9 PO 7,5 PP, arredondado para 9 PO 8 PP.|
|Parede de Escudo|7 PO 9 PP|Bruto de 9 PO: Imunidade a Empurrão fica entre 5 e 10 PO, ficaremos com 7 PO; 1 de Resistência custa 1 PO 5 PP por 4 Rodadas, ficaremos com 2 PO. O desconto de Ação Bônus (1/8) dá 7 PO 8,75 PP, arredondado para 7 PO 9 PP.|

O Escudo também ocupa uma das mãos, o que não foi descontado.

## 5. Preço final

Para impedir preços muito baixos ou negativos, o preço final **nunca fica abaixo de 25% do preço bruto**. Ou seja, descontos só funcionam até certo ponto.

A fórmula é:

**Preço Final = max((Preço Bruto - Descontos em Porcentagem) - Descontos Fixos, 25% do Preço Bruto)**

## 6. Outras Observações

A Lâmina Gêmea possui um efeito particularmente forte de repetir metade do dano do Ataque após acertar. Só isso já aumentaria o custo dela em 1,5x.

Para efeitos particularmente poderosos, desconsideram-se os descontos de Peso e de requisitos. A Lâmina Gêmea é um desses efeitos.