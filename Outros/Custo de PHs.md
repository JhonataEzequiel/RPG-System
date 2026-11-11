Este documento calcula o **custo em PHs** de uma Habilidade a partir dos pontos de `Custos de Mana.md`. Ele usa os mesmos efeitos, os mesmos valores e as mesmas durações, e acrescenta o que muda no PH: se a Habilidade é ativa ou passiva, quantas vezes ela pode ser usada, quais Atributos ela exige e se ela exige outra Habilidade.

**O que mudou em relação ao rascunho anterior.** A unidade de PH passou de 18 para 57,7 pt, porque o dano do grupo subiu (ver `Balanceamento.md`). Como BA e CA escalam junto, o custo em PHs deles não mudou. O que mudou foi o resto: bônus que dependem de dados (BD, Graus de dano) ficaram bem mais baratos em PHs, o teto de BA de Habilidades subiu de +8 para +10 (Capítulo 1.14) e o valor de uma Ação passou de 20 para 62,5 pt.

## 1. Orçamento e unidade

Um PDJ recebe **25 PHs** ao longo dos 20 Níveis: 2 no Nível 1, +1 em cada Nível que não é 5, 10, 15 ou 20 (15 Níveis) e +2 nesses quatro (8 PHs). Cada Habilidade custa de **1 a 3 PHs** (Capítulo 1.14). Os Pontos de Origem podem ser trocados por até 7 PHs adicionais na criação (Capítulo 2), mas eles competem com Dados de Vida, Dados de Mana e Proficiências, então a conta usa só os 25.

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

**Unidade.** **1 PH = 57,7 pt por Encontro de poder permanente.** Isso é o que uma Habilidade simples de custo 1 oferece: **+1 de BA em Ataques passivo** (57,7 pt por Encontro) ou **+1 de CA** (57,7). Um Encontro tem 4 Rodadas, então 1 PH ≈ 14,4 pt por Rodada.

Os tetos do Capítulo 1.14 já limitam quanto das 25 PHs pode ir para os bônus mais fortes:

|Categoria|Limite|PHs equivalentes|
|---|---|---|
|+BA em Ataques vindo de Habilidades|+10 (Cap. 1.14)|10,0|
|+CA vindo de Habilidades|+3 (Cap. 1.14)|3,0|
|Total que os tetos de BA e de CA permitem gastar||13,0|
|Orçamento total do PDJ|25 PHs|25,0|

Sobram ≈ 12 PHs para tudo o resto (dano, controle, cura, mobilidade, utilidade). Passando de +10 de BA, cada 2 pontos valem 1, então o teto é suave. **Perícias** (Perito) custam 1 PH cada (Capítulo 2.1) e ficam fora desta conta, pois o valor delas é de exploração. As Habilidades de Raça são gratuitas e não entram nos tetos.

## 2. Como calcular o custo

1. **Poder bruto (PP)**: some, em pt por Encontro, o valor de cada efeito da Habilidade.
    - **Passiva**: use a Tabela 1 (efeitos permanentes, já em pt por Encontro) e multiplique pela fração do tempo em que o efeito está de fato ligado (ver §2.1).
    - **Ativa**: calcule o **ganho líquido por uso** `G = valor do efeito − 62,5 × Ações gastas` (nunca abaixo de 0; Ação Livre, Ação Bônus e Reação gastam 0), usando as Tabelas 2 a 5. Depois, `PP = G × u × fator de PM`, com u e o fator de PM da Tabela 6.
2. **Fator de Nível**: se a Habilidade exige um Nível específico, multiplique o PP por um fator menor que 1 (§4.3). Sem exigência de Nível, o fator é 1.
3. **Bônus de requisitos (B)**: some o poder adicional dos requisitos de Atributo (§4.1) e das Habilidades requisitadas (§4.2).
4. **PHs brutos** = (PP × fator de Nível − B) ÷ 57,7. O **custo** é esse número arredondado para o inteiro mais próximo (0,5 sobe), entre **1 e 3**. Se passar de 3,5, a Habilidade tem poder demais: divida em duas ou reduza.

Em outras palavras: o **poder máximo de uma Habilidade de custo c** é `(57,7 × c + B) ÷ fator de Nível`. Quanto mais requisitos, mais forte ela pode ser pelo mesmo custo.

Habilidades com vários efeitos somam o PP de cada efeito **antes** de aplicar o bônus de requisitos uma única vez. **Aprimoramentos** (pagos em Mana adicional) não somam PHs.

### 2.1 Passivas condicionais

A Tabela 1 vale para um efeito **sempre ligado em combate**. Se ele depende de uma condição, multiplique pelo tempo em que ela costuma valer:

|Condição|Fator|
|---|---|
|Sempre|1,0|
|Exige empunhar um tipo de Arma ou usar um tipo de Armadura|0,8|
|Depende de um gatilho comum (por exemplo, depois de acertar um Ataque)|0,6|
|Depende de uma situação que dura metade do Encontro (por exemplo, PVs abaixo de 50%)|0,4|
|Depende de uma situação rara (por exemplo, Sucesso Crítico)|0,2|
|Só vale na primeira Rodada do Encontro|0,25|

Efeitos de Grau aplicados por gatilho usam a Tabela 2 e multiplicam pela frequência: por Encontro ×1, por Rodada ×4, por acerto de Ataque ×7,8 (1,95 acertos por Rodada × 4).

## 3. Tabelas de efeitos

### Tabela 1 — Efeitos passivos permanentes

|Efeito (passivo e permanente)|pt por Rodada|pt por Encontro|PHs|
|---|---|---|---|
|+1 de BA em Ataques|14,4|57,7|1,00|
|+1 de BA em Salvaguardas|7,2|28,8|0,50|
|+1 de BA em Testes de Perícia|3,1|12,5|0,22|
|**+1 de BA geral**|24,8|99,0|1,72|
|+1 de CA|14,4|57,7|1,00|
|+1 de BD|2,0|7,8|0,14|
|+1 de cura (0,5 instância/Rodada)|4,8|19,4|0,34|
|+1 de Resistência|4,7|18,9|0,33|
|+1,5 m de Deslocamento|5,2|20,8|0,36|
|+1,5 m de alcance corpo a corpo|6,3|25,0|0,43|
|+1,5 m de alcance de Ataque Mágico|1,6|6,3|0,11|
|+1,5 m de alcance de magia de área|1,6|6,3|0,11|
|+1,5 m de raio de magia de área|12,5|50,0|0,87|
|+1 Ação Bônus extra por Turno|21,9|87,5|1,52|
|+1 Reação extra por Rodada|15,0|60,0|1,04|
|**+1 Ação no Turno**|62,5|250,0|4,33 (**não cabe numa Habilidade**)|
|−1,5 m de Deslocamento dos inimigos (por inimigo)|4,2|16,7|0,29|
|Terreno Difícil de raio 1,5 m ao seu redor|6,3|25,0|0,43|

- Passivas **ligadas o tempo todo** são o jeito mais barato de gastar PH (o PP é tudo o que ela dá, sem PM nem Ação). Por isso, passivas são as que mais dependem dos tetos do Capítulo 1.14.
- **+1 Ação no Turno** passivo custaria ≈ 4,33 PHs: **não cabe numa Habilidade** (teto de 3 PHs, mais requisitos). Só deve existir como Ativa com Limite de Usos.
- **+1 Ação Bônus extra** e **+1 Reação extra** passivos custam entre 1,0 e 1,6 PHs e dependem de haver o que fazer com elas (premissa de §5.5 do `Custos de Mana.md`).
- **+1 de BD custa só 0,14 PH**, contra 1,00 do +1 de BA. É o efeito mais barato da lista que ainda soma dano. Com o dano por acerto em ≈ 96, vale rever se Habilidades de BD precisam de valores maiores (por exemplo, +5 de BD por PH).

### Tabela 2 — Valor de cada Grau (PHs por uso, ou por Encontro)

|Grau|Dado|Média|Dano (garantido)|Dano (com Ataque)|Cura|PV Temp. (Encontro)|PM Temp. (Encontro)|Resistência (Encontro)|Dano contínuo (Encontro)|
|---|---|---|---|---|---|---|---|---|---|
|1|1d4|2,5|0,04|0,03|0,42|0,41|0,13|0,82|0,22|
|2|1d6|3,5|0,06|0,04|0,59|0,57|0,18|1,15|0,30|
|3|1d8|4,5|0,08|0,05|0,76|0,73|0,23|1,47|0,39|
|4|1d10|5,5|0,10|0,06|0,92|0,89|0,28|1,80|0,48|
|5|1d12|6,5|0,11|0,07|1,09|1,05|0,33|2,13|0,56|
|6|2d6|7,0|0,12|0,08|1,18|1,12|0,35|2,29|0,61|
|7|2d8|9,0|0,16|0,10|1,51|1,43|0,44|2,95|0,78|
|8|2d10|11,0|0,19|0,12|1,85|1,72|0,53|3,60|0,95|
|9|2d12|13,0|0,23|0,15|2,18|2,01|0,62|4,26|1,13|
|10|3d10|16,5|0,29|0,19|2,77|2,50|0,76|5,40|1,43|

"PHs por uso" para Dano, Cura, PV Temporários e PM Temporários, e "por Encontro" para Resistência passiva e dano contínuo, ambos para 1 Encontro de duração. Para outras durações, use as Tabelas 4 a 5. "Dano (com Ataque)" aplica o fator de 65% de acerto. **Um Grau de dano vale menos de 0,3 PH**: o dado do Grau é pequeno perto de um Ataque com Arma (ver `Custos de Mana.md`, §7, item 7).

### Tabela 3 — Bônus × duração (ativa, 0 Ações, 1 uso)

|Efeito|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|+1 BA em Ataques|0,13|0,38|0,63|0,88|1,00|0,13|0,38|0,25|
|+1 BA em Salvaguardas|0,06|0,19|0,31|0,44|0,50|0,13|0,19|0,19|
|+1 BA em Perícias|0,03|0,08|0,14|0,19|0,22|0,03|0,08|0,05|
|**+1 BA geral**|0,21|0,64|1,07|1,50|1,72|0,28|0,64|0,49|
|+1 CA|0,13|0,38|0,63|0,88|1,00|0,25|0,38|0,38|
|+1 BD|0,02|0,05|0,08|0,12|0,14|0,02|0,05|0,03|
|+1 de cura (0,5 inst./Rodada)|0,04|0,13|0,21|0,29|0,34|0,08|0,13|0,13|
|+1 Resistência|0,04|0,12|0,20|0,29|0,33|0,08|0,12|0,12|
|+1,5 m Deslocamento|0,05|0,14|0,23|0,32|0,36|0,05|0,14|0,09|
|+1,5 m alcance corpo a corpo|0,05|0,16|0,27|0,38|0,43|0,05|0,16|0,11|
|+1,5 m alcance Ataque Mágico|0,01|0,04|0,07|0,09|0,11|0,01|0,04|0,03|
|+1,5 m alcance de área|0,01|0,04|0,07|0,09|0,11|0,01|0,04|0,03|
|+1,5 m raio de área|0,11|0,33|0,54|0,76|0,87|0,11|0,33|0,22|
|**+1 Ação no Turno**|1,08|2,17|3,25|4,33|4,33|1,08|2,17|1,08|
|+1 Ação Bônus extra por Turno|0,38|0,76|1,14|1,52|1,52|0,38|0,76|0,38|
|+1 Reação extra por Rodada|0,13|0,39|0,65|0,91|1,04|0,26|0,39|0,39|

**Se a Habilidade gasta Ações**, subtraia 1,08 PH (62,5 pt) por Ação antes de aplicar o fator de uso. Quase todos os bônus acima valem **menos** que 1 PH, então eles só fazem sentido como **Ação Bônus**, **Ação Livre** ou **Reação**, e não como Ação.

### Tabela 4 — Graus como PV Temporários, PM Temporários, Resistência e dano contínuo × duração (PHs por uso)

**PV Temporários**

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,37|0,40|0,41|0,41|0,41|0,39|0,40|0,40|
|Grau 2 (1d6)|0,49|0,55|0,57|0,57|0,57|0,54|0,55|0,55|
|Grau 3 (1d8)|0,60|0,70|0,72|0,73|0,73|0,67|0,70|0,70|
|Grau 4 (1d10)|0,70|0,84|0,87|0,89|0,89|0,80|0,84|0,84|
|Grau 5 (1d12)|0,79|0,98|1,02|1,04|1,05|0,93|0,98|0,98|
|Grau 6 (2d6)|0,84|1,04|1,09|1,12|1,12|0,99|1,04|1,04|
|Grau 7 (2d8)|0,98|1,30|1,38|1,42|1,43|1,21|1,30|1,30|
|Grau 8 (2d10)|1,10|1,54|1,65|1,71|1,72|1,41|1,54|1,54|
|Grau 9 (2d12)|1,20|1,76|1,91|1,99|2,01|1,59|1,76|1,76|
|Grau 10 (3d10)|1,33|2,11|2,35|2,46|2,50|1,86|2,11|2,11|

**PM Temporários**

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,11|0,13|0,13|0,13|0,13|0,11|0,13|0,12|
|Grau 2 (1d6)|0,14|0,17|0,18|0,18|0,18|0,14|0,17|0,16|
|Grau 3 (1d8)|0,17|0,22|0,23|0,23|0,23|0,17|0,22|0,20|
|Grau 4 (1d10)|0,20|0,26|0,27|0,28|0,28|0,20|0,26|0,24|
|Grau 5 (1d12)|0,21|0,30|0,32|0,33|0,33|0,21|0,30|0,27|
|Grau 6 (2d6)|0,22|0,31|0,34|0,35|0,35|0,22|0,31|0,29|
|Grau 7 (2d8)|0,25|0,38|0,42|0,44|0,44|0,25|0,38|0,34|
|Grau 8 (2d10)|0,27|0,45|0,50|0,52|0,53|0,27|0,45|0,39|
|Grau 9 (2d12)|0,29|0,50|0,57|0,61|0,62|0,29|0,50|0,43|
|Grau 10 (3d10)|0,30|0,59|0,69|0,74|0,76|0,30|0,59|0,49|

**Resistência** (rolada a cada instância de dano)

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,10|0,31|0,51|0,72|0,82|0,20|0,31|0,31|
|Grau 2 (1d6)|0,14|0,43|0,72|1,00|1,15|0,29|0,43|0,43|
|Grau 3 (1d8)|0,18|0,55|0,92|1,29|1,47|0,37|0,55|0,55|
|Grau 4 (1d10)|0,23|0,68|1,13|1,58|1,80|0,45|0,68|0,68|
|Grau 5 (1d12)|0,27|0,80|1,33|1,86|2,13|0,53|0,80|0,80|
|Grau 6 (2d6)|0,29|0,86|1,43|2,01|2,29|0,57|0,86|0,86|
|Grau 7 (2d8)|0,37|1,11|1,84|2,58|2,95|0,74|1,11|1,11|
|Grau 8 (2d10)|0,45|1,35|2,25|3,15|3,60|0,90|1,35|1,35|
|Grau 9 (2d12)|0,53|1,60|2,66|3,73|4,26|1,06|1,60|1,60|
|Grau 10 (3d10)|0,68|2,03|3,38|4,73|5,40|1,35|2,03|2,03|

**Dano contínuo** (alvo inimigo)

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo|
|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|0,07|0,11|0,15|0,20|0,22|0,09|0,09|
|Grau 2 (1d6)|0,09|0,15|0,21|0,27|0,30|0,12|0,12|
|Grau 3 (1d8)|0,12|0,20|0,27|0,35|0,39|0,16|0,16|
|Grau 4 (1d10)|0,14|0,24|0,33|0,43|0,48|0,19|0,19|
|Grau 5 (1d12)|0,17|0,28|0,39|0,51|0,56|0,23|0,23|
|Grau 6 (2d6)|0,18|0,30|0,42|0,55|0,61|0,24|0,24|
|Grau 7 (2d8)|0,23|0,39|0,55|0,70|0,78|0,31|0,31|
|Grau 8 (2d10)|0,29|0,48|0,67|0,86|0,95|0,38|0,38|
|Grau 9 (2d12)|0,34|0,56|0,79|1,01|1,13|0,45|0,45|
|Grau 10 (3d10)|0,43|0,72|1,00|1,29|1,43|0,57|0,57|

### Tabela 5 — Debuffs e dano contínuo fixo (alvo inimigo, PHs por uso)

|Efeito (alvo inimigo)|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo|
|---|---|---|---|---|---|---|---|
|−1,5 m Deslocamento|0,04|0,11|0,18|0,25|0,29|0,07|0,07|
|Terreno Difícil (raio 1,5 m)|0,05|0,16|0,27|0,38|0,43|0,11|0,11|
|1 de dano contínuo|0,03|0,04|0,06|0,08|0,09|0,03|0,03|

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

Uma Habilidade pode exigir **zero ou mais Atributos, com valor de 0 a 10 em cada um**. Cada requisito exige o valor no Atributo, e o Nível mínimo para cumprir é `2 × (valor − 3)`, pelo Limite de Atributo. Os valores de `Custos de Mana.md` (§9) mostram que o requisito custa pouco a quem tem build alinhada e mais a quem não tem, e essa média vira **poder adicional** para a Habilidade. Cada PA forçado fora do plano vale 19,6 pt por Encontro.

|Requisito (valor)|Nível mínimo|pt por Encontro|PHs de poder adicional|
|---|---|---|---|
|1|1|2,8|0,05|
|2|1|5,6|0,10|
|3|1|9,8|0,17|
|4|2|14,0|0,24|
|5|4|19,6|0,34|
|6|6|25,3|0,44|
|7|8|32,3|0,56|
|8|10|39,3|0,68|
|9|12|47,7|0,83|
|10|14|56,1|0,97|

**Vários requisitos**: some o poder de cada requisito (tabela acima) e acrescente **0,17 PH por PA de déficit**. O déficit compara os requisitos, do maior para o menor, com o build típico de 30 PAs (10, 8, 6, 4, 2, 0, 0): é a soma de `max(0, requisito − valor do build)`. Esta regra reproduz o cálculo exato.

|Requisitos|Nível mínimo|pt por Encontro (exato)|PHs de poder adicional|Pela regra da soma|
|---|---|---|---|---|
|6|6|25,3|0,44|0,44|
|10|14|56,1|0,97|0,97|
|4 + 4|2|28,1|0,49|0,49|
|6 + 6|6|50,5|0,88|0,88|
|8 + 8|10|78,6|1,36|1,36|
|10 + 10|14|131,9|2,29|2,29|
|5 + 5 + 5|4|58,9|1,02|1,02|
|8 + 6 + 4|10|78,6|1,36|1,36|
|10 + 8 + 6|14|120,7|2,09|2,09|
|8 + 8 + 8|10|137,5|2,38|2,38|
|10 + 10 + 10|14|227,4|3,94|3,94|
|6 + 6 + 6 + 6|6|120,7|2,09|2,09|
|10 + 10 + 10 + 10 + 10 + 10 + 10|14|785,9|13,62|13,62|

Valores de requisito **ímpares** são menos eficientes (o Modificador só sobe nos pares), então requisitos pares são os naturais. Requisitos de **1 ou 2** praticamente não dão poder, então não vale a pena listá-los.

### 4.2 Habilidade requisitada

Exigir outra Habilidade (de qualquer custo) dá poder adicional igual a **30% do custo dela**, já que o PDJ é forçado a comprá-la mesmo quando não a quereria. Quanto mais cara a requisitada, mais forte a nova Habilidade. Requisitos de várias Habilidades somam. A cadeia inteira não é recontada: o custo de uma Habilidade intermediária já inclui os dela.

|Habilidade requisitada (custo em PHs)|pt por Encontro|PHs de poder adicional|
|---|---|---|
|1|17,3|0,30|
|2|34,6|0,60|
|3|51,9|0,90|
|3 + 3 (duas Habilidades)|103,8|1,80|

### 4.3 Requisito de Nível

Algumas Habilidades podem exigir um **Nível específico**. Muitas já têm um Nível mínimo implícito pelos Atributos (Limite de Atributo: `2 × (valor − 3)`, por exemplo, 7 só no Nível 8). O requisito de Nível só compensa a **lacuna** entre o Nível exigido e esse mínimo implícito.

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
- Exigir um Nível menor que o implícito pelos Atributos não muda nada (por exemplo, Atributo 7 já exige o Nível 8).

### 4.4 Poder máximo por custo

O poder máximo para cada custo, já com os requisitos (em pt por Encontro, e em PHs entre parênteses):

|Requisitos|Bônus (pt)|Poder máximo, custo 1|custo 2|custo 3|
|---|---|---|---|---|
|Sem requisitos|0,0|57,7 (1,00)|115,4 (2,00)|173,1 (3,00)|
|Um Atributo 6|25,3|83,0 (1,44)|140,6 (2,44)|198,3 (3,44)|
|Um Atributo 10|56,1|113,8 (1,97)|171,5 (2,97)|229,2 (3,97)|
|Dois Atributos 6 + 6|50,5|108,2 (1,88)|165,9 (2,88)|223,6 (3,88)|
|Dois Atributos 10 + 10|131,9|189,6 (3,29)|247,3 (4,29)|305,0 (5,29)|
|Habilidade requisitada de 1 PH|17,3|75,0 (1,30)|132,7 (2,30)|190,4 (3,30)|
|Habilidade requisitada de 3 PHs|51,9|109,6 (1,90)|167,3 (2,90)|225,0 (3,90)|
|Atributo 6 + Habilidade de 2 PHs|59,9|117,6 (2,04)|175,3 (3,04)|233,0 (4,04)|
|Atributos 8 + 8 + Habilidade de 3 PHs|130,5|188,2 (3,26)|245,9 (4,26)|303,6 (5,26)|

Um bom teto prático: **a soma dos requisitos (Atributos e Habilidades) não deve passar de ≈ 3 PHs de poder adicional**, ou a Habilidade de 3 PHs fica com mais de 6 PHs de poder, o dobro do padrão.

## 5. Exemplos

|#|Habilidade|Poder bruto (pt)|Bônus de requisitos (pt)|PHs (bruto)|Custo|
|---|---|---|---|---|---|
|1|Passiva: +1 de BA em Ataques. Sem requisitos.|57,7|0,0|1,00|1|
|2a|Passiva: +2 de BA em Ataques e +1 de CA. Sem requisitos.|173,1|0,0|3,00|3|
|2b|A mesma, com requisitos For 6 e Des 6.|173,1|50,5|2,12|2|
|3|Passiva: +1 de BA geral e +1 de BD. Requer Arc 8 e uma Habilidade de 2 PHs.|106,8|73,9|0,57|1|
|4|Passiva: Resistência Grau 3 (rolada a cada instância de dano). Sem requisitos.|85,0|0,0|1,47|1|
|5|Ativa, Ação Bônus, sem Mana, 1 por Encontro: +1 de BA em Ataques e +1 de CA até o fim do Encontro.|115,4|0,0|2,00|2|
|6|A mesma, mas com Mana e sem Limite de Usos.|69,2|0,0|1,20|1|
|7|Ativa, Uma Ação, com Mana: Ataque Mágico de Grau 10 em 3 alvos (valor 32,2 − 62,5 da Ação, G = 0).|0,0|0,0|0,00|1|
|8|Reação, sem Mana, 1 por Encontro: cura Grau 6 em um aliado.|67,8|0,0|1,18|1|
|9|Ação Livre, 1 por Encontro: +1 Ação no Turno por 1 Rodada (O' = 1).|62,5|0,0|1,08|1|
|10|Passiva: +1 de BA geral. Requer Arc 6 e uma Habilidade de 3 PHs.|99,0|77,2|0,38|1|

- Os exemplos 2a e 2b mostram o efeito dos requisitos: o mesmo poder (173,1 pt) custa 3 PHs sem requisitos e 2 PHs com For 6 e Des 6.
- O exemplo 6 mostra por que ativas com Mana são baratas em PH: o PM paga o resto. O custo real delas aparece em PM, que vem a seguir.
- Os exemplos 5, 8 e 9 mostram que ativas "grátis" com Limite de Usos de 1 por Encontro ficam em 1 a 2 PHs.
- O exemplo 7 mostra o problema da Ação: um Ataque Mágico de Grau 10 em 3 alvos rende só 32,2 pt, menos que os 62,5 pt de uma Ação. Atacar com Arma já é melhor, então o ganho líquido é 0 e a Habilidade cai no custo mínimo de 1 PH.

## 6. Observações e pontos em aberto

1. **O fator de PM (0,30) é um chute informado.** Ele deve ser recalibrado quando a conversão pt → PM existir: se o PM cobrar 100% do valor, as ativas com Mana viram sempre 1 PH.
2. **Ativas com Mana sem Limite de Usos** só dão 1 a 2 PHs mesmo sendo fortes: o freio delas é o PM e o custo de Ações, não o PH.
3. **Ativas sem Mana, sem Limite de Usos e que não gastam Ação** (Ação Livre, Reação ou Ação Bônus ilimitadas) valem até 4× mais do que uma por Encontro, e são as que mais quebram o sistema. Sugiro proibir ou exigir Limite de Usos.
4. Os valores partem do **Nível 20**. Em Níveis baixos, +1 de BD e +1 de cura valem proporcionalmente mais (ver §6 de `Custos de Mana.md`), mas o PH é o mesmo para todos os Níveis: Habilidades baratas de bônus fixo são mais fortes cedo.
5. O limite de **+10 de BA e +3 de CA** por Habilidades já consome 13 dos 25 PHs se o PDJ quiser tudo: vale decidir se o PH desse bônus deve ficar mais caro para não dominar o orçamento.
6. **BD e Graus de dano ficaram baratos em PHs.** Como as Escalas de Armas dão +75 de BD, um ponto de BD vale pouco, e Habilidades de dano precisam de valores grandes para fazerem diferença. Decidir se Habilidades dão BD em múltiplos maiores (por exemplo, +5 de BD).
7. Efeitos ainda não listados (Condições, Vantagem/Desvantagem, Margem de Ameaça, invisibilidade etc.) entram nas duas tabelas quando você os definir em `Custos de Mana.md`.