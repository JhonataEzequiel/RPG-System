Este documento calcula o **custo em PHs** de uma Habilidade a partir dos pontos de `Custos de Mana.md`. Ele usa os mesmos efeitos, os mesmos valores e as mesmas durações, e acrescenta o que muda no PH: se a Habilidade é ativa ou passiva, quantas vezes ela pode ser usada, quais Atributos ela exige e se ela exige outra Habilidade.

## 1. Orçamento e unidade

Um PDJ recebe **25 PHs** ao longo dos 20 Níveis: 2 no Nível 1, +1 em cada Nível que não é 5, 10, 15 ou 20 (15 Níveis) e +2 nesses quatro (8 PHs). Cada Habilidade custa de **1 a 3 PHs** (Capítulo 1.14).

|Nível|Limite de Atributo|PHs acumulados|PAs acumulados|
|---|---|---|---|
|1|3|2|7|
|2|4|3|8|
|3|4|4|9|
|4|5|5|10|
|5|5|7|12|
|6|6|8|13|
|8|7|10|15|
|10|8|13|18|
|12|9|15|20|
|14|10|17|22|
|15|10|19|24|
|16|10|20|25|
|18|10|22|27|
|20|10|25|30|

**Unidade.** **1 PH = 18 pt por Encontro de poder permanente.** Isso é o que uma Habilidade simples de custo 1 oferece: **+1 de BA em Ataques passivo** (18,5 pt por Encontro) ou **+1 de CA** (17,9). Um Encontro tem 4 Rodadas, então 1 PH ≈ 4,5 pt por Rodada.

Os tetos do Capítulo 1.14 já limitam quanto das 25 PHs pode ir para os bônus mais fortes:

|Categoria|Limite|PHs equivalentes|
|---|---|---|
|+BA em Ataques vindo de Habilidades|+8 (Cap. 1.14)|8,2|
|+CA vindo de Habilidades|+3 (Cap. 1.14)|3,0|
|Total que os tetos de BA e de CA permitem gastar||11,2|
|Orçamento total do PDJ|25 PHs|25,0|

Sobram ≈ 14 PHs para tudo o resto (dano, controle, cura, mobilidade, utilidade). **Perícias** (Perito) custam 1 PH cada (Capítulo 2.1) e ficam fora desta conta, pois o valor delas é de exploração.

## 2. Como calcular o custo

1. **Poder bruto (PP)**: some, em pt por Encontro, o valor de cada efeito da Habilidade.
    - **Passiva**: use a Tabela 1 (efeitos permanentes, já em pt por Encontro) e multiplique pela fração do tempo em que o efeito está de fato ligado (ver §2.1).
    - **Ativa**: calcule o **ganho líquido por uso** `G = valor do efeito − 20 × Ações gastas` (nunca abaixo de 0; Ação Livre, Ação Bônus e Reação gastam 0), usando as Tabelas 2 a 5. Depois, `PP = G × u × fator de PM`, com u e o fator de PM da Tabela 6.
2. **Fator de Nível**: se a Habilidade exige um Nível específico, multiplique o PP por um fator menor que 1 (§4.3). Sem exigência de Nível, o fator é 1.
3. **Bônus de requisitos (B)**: some o poder adicional dos requisitos de Atributo (§4.1) e das Habilidades requisitadas (§4.2).
4. **PHs brutos** = (PP × fator de Nível − B) ÷ 18. O **custo** é esse número arredondado para o inteiro mais próximo (0,5 sobe), entre **1 e 3**. Se passar de 3,5, a Habilidade tem poder demais: divida em duas ou reduza.

Em outras palavras: o **poder máximo de uma Habilidade de custo c** é `(18 × c + B) ÷ fator de Nível`. Quanto mais requisitos, mais forte ela pode ser pelo mesmo custo.

Habilidades com vários efeitos somam o PP de cada efeito **antes** de aplicar o bônus de requisitos uma única vez. **Aprimoramentos** (pagos em Mana adicional) não somam PHs.

### 2.1 Passivas condicionais

A Tabela 1 vale para um efeito **sempre ligado em combate**. Se ele depende de uma condição, multiplique pelo tempo em que ela costuma valer:

|Condição|Fator|
|---|---|
|Sempre|1,0|
|Exige empunhar um tipo de Arma ou usar um tipo de Armadura|0,8|
|Depende de um gatilho comum (ex.: depois de acertar um Ataque)|0,6|
|Depende de uma situação que dura metade do Encontro (ex.: PVs abaixo de 50%)|0,4|
|Depende de uma situação rara (ex.: Sucesso Crítico)|0,2|
|Só vale na primeira Rodada do Encontro|0,25|

Efeitos de Grau aplicados por gatilho usam a Tabela 2 e multiplicam pela frequência: por Encontro ×1, por Rodada ×4, por acerto de Ataque ×7,8 (1,95 acertos por Rodada × 4).

## 3. Tabelas de efeitos

### Tabela 1 — Efeitos passivos permanentes

| Efeito (passivo e permanente)                     | pt por Rodada | pt por Encontro | PHs                                 |
| ------------------------------------------------- | ------------- | --------------- | ----------------------------------- |
| +1 de BA em Ataques                               | 4,6           | 18,5            | 1,03                                |
| +1 de BA em Salvaguardas                          | 2,2           | 8,9             | 0,50                                |
| +1 de BA em Testes de Perícia                     | 1,0           | 4,0             | 0,22                                |
| **+1 de BA geral**                                | 7,8           | 31,4            | 1,74                                |
| +1 de CA                                          | 4,5           | 17,9            | 0,99                                |
| +1 de BD                                          | 2,0           | 7,8             | 0,43                                |
| +1 de cura (0,5 instância/Rodada)                 | 1,5           | 6,0             | 0,33                                |
| +1 de Resistência                                 | 1,9           | 7,5             | 0,42                                |
| +1,5 m de Deslocamento                            | 1,7           | 6,7             | 0,37                                |
| +1,5 m de alcance corpo a corpo                   | 2,0           | 8,0             | 0,44                                |
| +1,5 m de alcance de Ataque Mágico                | 0,5           | 2,0             | 0,11                                |
| +1,5 m de alcance de magia de área                | 0,5           | 2,0             | 0,11                                |
| +1,5 m de raio de magia de área                   | 4,0           | 16,0            | 0,89                                |
| +1 Ação Bônus extra por Turno                     | 7,0           | 28,0            | 1,56                                |
| +1 Reação extra por Rodada                        | 4,8           | 19,2            | 1,07                                |
| **+1 Ação no Turno**                              | 20,0          | 80,0            | 4,44 (**não cabe numa Habilidade**) |
| −1,5 m de Deslocamento dos inimigos (por inimigo) | 1,3           | 5,3             | 0,30                                |
| Terreno Difícil de raio 1,5 m ao seu redor        | 2,0           | 8,0             | 0,44                                |

- Passivas **ligadas o tempo todo** são o jeito mais barato de gastar PH (o PP é tudo o que ela dá, sem PM nem Ação). Por isso, passivas são as que mais dependem dos tetos do Capítulo 1.14.
- **+1 Ação no Turno** passivo custaria ≈ 4,44 PHs: **não cabe numa Habilidade** (teto de 3 PHs, mais requisitos). Só deve existir como Ativa com Limite de Usos.
- **+1 Ação Bônus extra** e **+1 Reação extra** passivos custam entre 1,1 e 1,6 PHs e dependem de haver o que fazer com elas (premissa de §5.5 do Custos de Mana).

### Tabela 2 — Valor de cada Grau (PHs por uso, ou por Encontro)

|Grau|Dado|Média|Dano (garantido)|Dano (com Ataque)|Cura|PV Temp. (Encontro)|PM Temp. (Encontro)|Resistência (Encontro)|Dano contínuo (Encontro)|
|---|---|---|---|---|---|---|---|---|---|
|1|1d4|2,5|0,14|0,09|0,42|0,41|0,14|1,05|0,69|
|2|1d6|3,5|0,19|0,13|0,58|0,57|0,19|1,47|0,97|
|3|1d8|4,5|0,25|0,16|0,75|0,73|0,24|1,89|1,25|
|4|1d10|5,5|0,31|0,20|0,92|0,88|0,29|2,31|1,53|
|5|1d12|6,5|0,36|0,23|1,08|1,04|0,34|2,73|1,81|
|6|2d6|7,0|0,39|0,25|1,17|1,12|0,36|2,93|1,94|
|7|2d8|9,0|0,50|0,33|1,50|1,42|0,46|3,77|2,50|
|8|2d10|11,0|0,61|0,40|1,83|1,71|0,55|4,61|3,06|
|9|2d12|13,0|0,72|0,47|2,17|1,99|0,63|5,45|3,61|
|10|3d10|16,5|0,92|0,60|2,75|2,48|0,78|6,92|4,58|

"PHs por uso" para Dano, Cura, PV Temporários e PM Temporários, e "por Encontro" para Resistência passiva e dano contínuo, ambos para 1 Encontro de duração. Para outras durações, use as Tabelas 4 a 5. "Dano (com Ataque)" aplica o fator de 65% de acerto.

### Tabela 3 — Bônus × duração (ativa, 0 Ações, 1 uso)

|Efeito|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|+1 BA em Ataques|0,13|0,38|0,64|0,90|1,03|0,13|0,38|0,26|
|+1 BA em Salvaguardas|0,06|0,19|0,31|0,43|0,50|0,12|0,19|0,19|
|+1 BA em Perícias|0,03|0,08|0,14|0,19|0,22|0,03|0,08|0,06|
|**+1 BA geral**|0,22|0,65|1,09|1,53|1,74|0,28|0,65|0,50|
|+1 CA|0,12|0,37|0,62|0,87|0,99|0,25|0,37|0,37|
|+1 BD|0,05|0,16|0,27|0,38|0,43|0,05|0,16|0,11|
|+1 de cura (0,5 inst./Rodada)|0,04|0,12|0,21|0,29|0,33|0,08|0,12|0,12|
|+1 Resistência|0,05|0,16|0,26|0,37|0,42|0,10|0,16|0,16|
|+1,5 m Deslocamento|0,05|0,14|0,23|0,32|0,37|0,05|0,14|0,09|
|+1,5 m alcance corpo a corpo|0,06|0,17|0,28|0,39|0,44|0,06|0,17|0,11|
|+1,5 m alcance Ataque Mágico|0,01|0,04|0,07|0,10|0,11|0,01|0,04|0,03|
|+1,5 m alcance de área|0,01|0,04|0,07|0,10|0,11|0,01|0,04|0,03|
|+1,5 m raio de área|0,11|0,33|0,56|0,78|0,89|0,11|0,33|0,22|
|+1 Ação Bônus extra (por Turno do alvo)|0,39|0,78|1,17|1,56|1,56|0,39|0,78|0,39|
|+1 Reação extra (por Rodada)|0,13|0,40|0,67|0,93|1,07|0,27|0,40|0,40|
|**+1 Ação no Turno**|1,11|2,22|3,33|4,44|4,44|1,11|2,22|1,11|

**Se a Habilidade gasta Ações**, subtraia 1,1 PH (20 pt) por Ação antes de aplicar o fator de uso. Quase todos os bônus acima valem **menos** que 1 PH, então eles só fazem sentido como **Ação Bônus**, **Ação Livre** ou **Reação**, e não como Ação.

### Tabela 4 — Graus como PV Temporários, PM Temporários, Resistência e dano contínuo × duração (PHs por uso)

**PV Temporários**

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,37|0,40|0,41|0,41|0,41|0,39|0,40|0,40|
|Grau 2 (1d6)|0,49|0,55|0,56|0,57|0,57|0,53|0,55|0,55|
|Grau 3 (1d8)|0,60|0,69|0,72|0,73|0,73|0,67|0,69|0,69|
|Grau 4 (1d10)|0,70|0,84|0,87|0,88|0,88|0,80|0,84|0,84|
|Grau 5 (1d12)|0,79|0,97|1,01|1,03|1,04|0,92|0,97|0,97|
|Grau 6 (2d6)|0,83|1,04|1,09|1,11|1,12|0,98|1,04|1,04|
|Grau 7 (2d8)|0,98|1,29|1,37|1,40|1,42|1,20|1,29|1,29|
|Grau 8 (2d10)|1,10|1,53|1,64|1,69|1,71|1,40|1,53|1,53|
|Grau 9 (2d12)|1,19|1,75|1,90|1,97|1,99|1,58|1,75|1,75|
|Grau 10 (3d10)|1,32|2,10|2,33|2,44|2,48|1,85|2,10|2,10|

**PM Temporários**

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,11|0,13|0,13|0,13|0,14|0,11|0,13|0,13|
|Grau 2 (1d6)|0,15|0,18|0,18|0,19|0,19|0,15|0,18|0,17|
|Grau 3 (1d8)|0,18|0,22|0,23|0,24|0,24|0,18|0,22|0,21|
|Grau 4 (1d10)|0,20|0,26|0,28|0,29|0,29|0,20|0,26|0,25|
|Grau 5 (1d12)|0,22|0,30|0,32|0,33|0,34|0,22|0,30|0,28|
|Grau 6 (2d6)|0,23|0,32|0,35|0,36|0,36|0,23|0,32|0,29|
|Grau 7 (2d8)|0,26|0,39|0,43|0,45|0,46|0,26|0,39|0,35|
|Grau 8 (2d10)|0,28|0,46|0,51|0,54|0,55|0,28|0,46|0,40|
|Grau 9 (2d12)|0,30|0,51|0,59|0,62|0,63|0,30|0,51|0,44|
|Grau 10 (3d10)|0,31|0,60|0,71|0,76|0,78|0,31|0,60|0,50|

**Resistência** (rolada a cada instância de dano)

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,13|0,39|0,66|0,92|1,05|0,26|0,39|0,39|
|Grau 2 (1d6)|0,18|0,55|0,92|1,28|1,47|0,37|0,55|0,55|
|Grau 3 (1d8)|0,24|0,71|1,18|1,65|1,89|0,47|0,71|0,71|
|Grau 4 (1d10)|0,29|0,86|1,44|2,02|2,31|0,58|0,86|0,86|
|Grau 5 (1d12)|0,34|1,02|1,70|2,38|2,73|0,68|1,02|1,02|
|Grau 6 (2d6)|0,37|1,10|1,83|2,57|2,93|0,73|1,10|1,10|
|Grau 7 (2d8)|0,47|1,41|2,36|3,30|3,77|0,94|1,41|1,41|
|Grau 8 (2d10)|0,58|1,73|2,88|4,04|4,61|1,15|1,73|1,73|
|Grau 9 (2d12)|0,68|2,04|3,41|4,77|5,45|1,36|2,04|2,04|
|Grau 10 (3d10)|0,86|2,59|4,32|6,05|6,92|1,73|2,59|2,59|

**Dano contínuo** (alvo inimigo)

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo|
|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,21|0,35|0,49|0,62|0,69|0,28|0,28|
|Grau 2 (1d6)|0,29|0,49|0,68|0,88|0,97|0,39|0,39|
|Grau 3 (1d8)|0,38|0,62|0,88|1,12|1,25|0,50|0,50|
|Grau 4 (1d10)|0,46|0,76|1,07|1,38|1,53|0,61|0,61|
|Grau 5 (1d12)|0,54|0,90|1,26|1,62|1,81|0,72|0,72|
|Grau 6 (2d6)|0,58|0,97|1,36|1,75|1,94|0,78|0,78|
|Grau 7 (2d8)|0,75|1,25|1,75|2,25|2,50|1,00|1,00|
|Grau 8 (2d10)|0,92|1,53|2,14|2,75|3,06|1,22|1,22|
|Grau 9 (2d12)|1,08|1,81|2,53|3,25|3,61|1,44|1,44|
|Grau 10 (3d10)|1,38|2,29|3,21|4,12|4,58|1,83|1,83|

### Tabela 5 — Debuffs e dano contínuo fixo (alvo inimigo, PHs por uso)

|Efeito (alvo inimigo)|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo|
|---|---|---|---|---|---|---|---|
|−1,5 m Deslocamento|0,04|0,11|0,19|0,26|0,30|0,07|0,07|
|Terreno Difícil (raio 1,5 m)|0,06|0,17|0,28|0,39|0,44|0,11|0,11|
|1 de dano contínuo|0,08|0,14|0,19|0,25|0,28|0,11|0,11|

### Tabela 6 — Quantos usos e quanto o PM cobre

`PP de uma ativa = G × u × fator de PM`. O **fator de PM** é 0,30: o PM paga 70% do valor, e o PH só precisa pagar o acesso e a flexibilidade. É o **botão principal** das ativas, e deve ser recalibrado quando o custo em PM estiver pronto.

|Situação da Habilidade ativa|Usos por Encontro (u)|Fator de PM|Multiplica o ganho líquido G por|
|---|---|---|---|
|Limite de Usos: 1 por Encontro, sem Mana|1,0|1,0|1,0|
|Limite de Usos: 1 por Descanso, sem Mana|0,5|1,0|0,5|
|Com Mana, sem Limite de Usos|2,0|0,30|0,60|
|Com Mana e Limite de 1 por Encontro|1,0|0,30|0,30|
|Reação, sem Mana e sem Limite (≈ 1 gatilho a cada 2 Rodadas)|2,0|1,0|2,0|
|Reação, com Mana|2,0|0,30|0,60|
|Ação Bônus ou Ação, sem Mana e sem Limite (1 vez por Rodada)|4,0|1,0|4,0 (evitar)|

## 4. Requisitos

### 4.1 Requisitos de Atributo

Uma Habilidade pode exigir **zero ou mais Atributos, com valor de 0 a 10 em cada um**. Cada requisito exige o valor no Atributo, e o Nível mínimo para cumprir é `2 × (valor − 3)`, pelo Limite de Atributo. Os valores de `Custos de Mana.md` (§9) mostram que o requisito custa pouco a quem tem build alinhada e mais a quem não tem, e essa média vira **poder adicional** para a Habilidade.

|Requisito (valor)|Nível mínimo|pt por Encontro|PHs de poder adicional|
|---|---|---|---|
|0|1|0,0|0,00|
|1|1|1,1|0,06|
|2|1|2,3|0,13|
|3|1|3,9|0,22|
|4|2|5,6|0,31|
|5|4|7,9|0,44|
|6|6|10,1|0,56|
|7|8|12,9|0,72|
|8|10|15,8|0,88|
|9|12|19,1|1,06|
|10|14|22,5|1,25|

**Vários requisitos**: some o poder de cada requisito (tabela acima) e acrescente **0,22 PH por PA de déficit**. O déficit compara os requisitos, do maior para o menor, com o build típico de 30 PAs (10, 8, 6, 4, 2, 0, 0): é a soma de `max(0, requisito − valor do build)`. Esta regra reproduz o cálculo exato (diferença máxima de 0,00 PH em 400 combinações testadas).

|Requisitos|Nível mínimo|pt por Encontro (exato)|PHs de poder adicional|Pela regra da soma|
|---|---|---|---|---|
|6|6|10,1|0,56|0,56|
|10|14|22,5|1,25|1,25|
|4 + 4|2|11,3|0,63|0,63|
|6 + 6|6|20,3|1,13|1,13|
|8 + 8|10|31,5|1,75|1,75|
|10 + 10|14|52,9|2,94|2,94|
|5 + 5 + 5|4|23,6|1,31|1,31|
|8 + 6 + 4|10|31,5|1,75|1,75|
|10 + 8 + 6|14|48,4|2,69|2,69|
|8 + 8 + 8|10|55,1|3,06|3,06|
|10 + 10 + 10|14|91,2|5,06|5,06|
|6 + 6 + 6 + 6|6|48,4|2,69|2,69|
|10 + 10 + 10 + 10 + 10 + 10 + 10|14|315,1|17,51|17,51|

Valores de requisito **ímpares** são menos eficientes (o Modificador só sobe nos pares), então requisitos pares são os naturais. Requisitos de **1 ou 2** praticamente não dão poder, então não vale a pena listá-los.

### 4.2 Habilidade requisitada

Exigir outra Habilidade (de qualquer custo) dá poder adicional igual a **30% do custo dela**, já que o PDJ é forçado a comprá-la mesmo quando não a quereria. Quanto mais cara a requisitada, mais forte a nova Habilidade. Requisitos de várias Habilidades somam. A cadeia inteira não é recontada: o custo de uma Habilidade intermediária já inclui os dela.

|Habilidade requisitada (custo em PHs)|pt por Encontro|PHs de poder adicional|
|---|---|---|
|1|5,4|0,30|
|2|10,8|0,60|
|3|16,2|0,90|
|3 + 3 (duas Habilidades)|32,4|1,80|

### 4.3 Requisito de Nível

Algumas Habilidades podem exigir um **Nível específico**. Muitas já têm um Nível mínimo implícito pelos Atributos (Limite de Atributo: `2 × (valor − 3)`, ex.: 7 só no Nível 8). O requisito de Nível só compensa a **lacuna** entre o Nível exigido e esse mínimo implícito.

**Fator de Nível = 1 − 0,02 × lacuna**, com mínimo de **0,70** (poder máximo de +43%). Cada Nível de espera custa 1/20 do tempo de uso da Habilidade, mas, como o PH pode ser gasto em outra coisa enquanto isso, só 40% dessa perda é compensada. A Habilidade com exigência de Nível pode ser mais forte: o PP é multiplicado pelo fator antes de entrar no custo.

|Nível exigido|Nível implícito 1 (sem Atributo)|Implícito 4 (Atributo 5)|Implícito 8 (Atributo 7)|Implícito 14 (Atributo 10)|
|---|---|---|---|---|
|5|0,92 (+9%)|0,98 (+2%)|—|—|
|8|0,86 (+16%)|0,92 (+9%)|—|—|
|10|0,82 (+22%)|0,88 (+14%)|0,96 (+4%)|—|
|12|0,78 (+28%)|0,84 (+19%)|0,92 (+9%)|—|
|14|0,74 (+35%)|0,80 (+25%)|0,88 (+14%)|—|
|16|0,70 (+43%)|0,76 (+32%)|0,84 (+19%)|0,96 (+4%)|
|18|0,70 (+43%)|0,72 (+39%)|0,80 (+25%)|0,92 (+9%)|
|20|0,70 (+43%)|0,70 (+43%)|0,76 (+32%)|0,88 (+14%)|

Duas orientações:

- **Bônus fixos** (BD, Resistência, +1 de cura) valem proporcionalmente mais nos Níveis baixos. Se uma Habilidade concede um desses em valor alto, exija Nível, e o fator de Nível já corrige o preço.
- Exigir um Nível menor que o implícito pelos Atributos não muda nada (ex.: Atributo 7 já exige o Nível 8).

### 4.4 Poder máximo por custo

O poder máximo para cada custo, já com os requisitos (em pt por Encontro, e em PHs entre parênteses):

|Requisitos|Bônus (pt)|Poder máximo, custo 1|custo 2|custo 3|
|---|---|---|---|---|
|Sem requisitos|0,0|18,0 (1,00)|36,0 (2,00)|54,0 (3,00)|
|Um Atributo 6|10,1|28,1 (1,56)|46,1 (2,56)|64,1 (3,56)|
|Um Atributo 10|22,5|40,5 (2,25)|58,5 (3,25)|76,5 (4,25)|
|Dois Atributos 6 + 6|20,3|38,3 (2,13)|56,3 (3,13)|74,3 (4,13)|
|Dois Atributos 10 + 10|52,9|70,9 (3,94)|88,9 (4,94)|106,9 (5,94)|
|Habilidade requisitada de 1 PH|5,4|23,4 (1,30)|41,4 (2,30)|59,4 (3,30)|
|Habilidade requisitada de 3 PHs|16,2|34,2 (1,90)|52,2 (2,90)|70,2 (3,90)|
|Atributo 6 + Habilidade de 2 PHs|20,9|38,9 (2,16)|56,9 (3,16)|74,9 (4,16)|
|Atributos 8 + 8 + Habilidade de 3 PHs|47,7|65,7 (3,65)|83,7 (4,65)|101,7 (5,65)|

Um bom teto prático: **a soma dos requisitos (Atributos e Habilidades) não deve passar de ≈ 3 PHs de poder adicional**, ou a Habilidade de 3 PHs fica com mais de 6 PHs de poder, o dobro do padrão.

## 5. Exemplos

|#|Habilidade|Poder bruto (pt)|Bônus de requisitos (pt)|PHs (bruto)|Custo|
|---|---|---|---|---|---|
|1|Passiva: +1 de BA em Ataques. Sem requisitos.|18,5|0,0|1,03|1|
|2a|Passiva: +2 de BA em Ataques e +1 de CA. Sem requisitos.|54,8|0,0|3,04|3|
|2b|A mesma, com requisitos For 6 e Des 6.|54,8|20,3|1,92|2|
|3|Passiva: +1 de BA geral e +1 de BD. Requer Arc 8 e uma Habilidade de 2 PHs.|39,2|26,6|0,70|1|
|4|Passiva: Resistência Grau 3 (rolada a cada instância de dano). Sem requisitos.|34,0|0,0|1,89|2|
|5|Ativa, Ação Bônus, sem Mana, 1 por Encontro: +1 de BA em Ataques e +1 de CA até o fim do Encontro.|36,3|0,0|2,02|2|
|6|A mesma, mas com Mana e sem Limite de Usos.|21,8|0,0|1,21|1|
|7|Ativa, Uma Ação, com Mana: Ataque Mágico de Grau 10 em 3 alvos (G = 32,2 − 20 = 12,2).|7,3|0,0|0,41|1|
|8|Reação, sem Mana, 1 por Encontro: cura Grau 6 em um aliado.|21,0|0,0|1,17|1|
|9|Ação Livre, 1 por Encontro: +1 Ação no Turno por 1 Rodada (O' = 1).|20,0|0,0|1,11|1|
|10|Passiva: +1 de BA geral. Requer Arc 6 e uma Habilidade de 3 PHs.|31,4|26,3|0,28|1|

- Os exemplos 2a e 2b mostram o efeito dos requisitos: o mesmo poder (54,8 pt) custa 3 PHs sem requisitos e 2 PHs com For 6 e Des 6.
- O exemplo 6 mostra por que ativas com Mana são baratas em PH: o PM paga o resto. O custo real delas aparece em PM, que vem a seguir.
- Os exemplos 5, 8 e 9 mostram que ativas "grátis" com Limite de Usos de 1 por Encontro ficam em 1 a 2 PHs.
- O exemplo 7 mostra o problema da Ação: um Ataque Mágico de Grau 10 em 3 alvos só rende 12,2 pt a mais que atacar normalmente, então vira só 1 PH.

## 7. Observações e pontos em aberto

1. **O fator de PM (0,30) é um chute informado.** Ele deve ser recalibrado quando a conversão pt → PM existir: se o PM cobrar 100% do valor, as ativas com Mana viram sempre 1 PH.
2. **Ativas com Mana sem Limite de Usos** só dão 1 a 2 PHs mesmo sendo fortes: o freio delas é o PM e o custo de Ações, não o PH.
3. **Ativas sem Mana, sem Limite de Usos e que não gastam Ação** (Ação Livre, Reação ou Ação Bônus ilimitadas) valem até 4× mais do que uma por Encontro, e são as que mais quebram o sistema. Sugiro proibir ou exigir Limite de Usos.
4. Os valores partem do **Nível 20**. Em Níveis baixos, +1 de BD e +1 de cura valem proporcionalmente mais (ver §6 de `Custos de Mana.md`), mas o PH é o mesmo para todos os Níveis: Habilidades baratas de bônus fixo são mais fortes cedo.
5. O limite de **8 de BA e 3 de CA** por Habilidades já consome ≈ 11 dos 25 PHs se o PDJ quiser tudo: vale decidir se o PH desse bônus deve ficar mais caro para não dominar o orçamento.
6. Efeitos ainda não listados (Condições, Vantagem/Desvantagem, Margem de Ameaça, invisibilidade etc.) entram nas duas tabelas quando você os definir em `Custos de Mana.md`.