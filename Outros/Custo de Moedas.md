Este documento calcula, **em moedas**, quanto valem os efeitos de Armas, Armaduras e Escudos. Ele usa os mesmos valores em pontos de `Custos de Mana.md` e de `Custo de PHs.md` (pt por Encontro, cenário típico do Nível 20), e acrescenta a conversão para moedas, o preço de cada efeito e os descontos por Peso, requisitos e penalidades.

Todos os preços estão escritos usando as moedas de maior valor possível, ou seja, 50 PO e 9 PP aparece como 5 PL e 9 PP.

## 1. Conversão: pontos em moedas

**1 pt por Encontro = 50 PC.** Equivale a **1 PO = 2 pt**.

Esse é o **botão principal** do documento. Ele foi escolhido para que os 50 PO iniciais (Capítulo 2) comprem uma Arma de Grau 4 e uma Armadura Leve com requisitos e Peso típicos (ver §7). Se o preço geral estiver alto ou baixo, basta mudar este número: todo o resto escala junto.

Os preços são arredondados para a PC mais próxima (0,5 sobe).

|pt|PC|Moedas|
|---|---|---|
|1|50|5 PP|
|2|100|1 PO|
|5|250|2 PO e 5 PP|
|10|500|5 PO|
|20|1.000|1 PL|
|50|2.500|2 PL e 5 PO|
|100|5.000|5 PL|

## 2. Valores usados (pt por Encontro)

|Efeito|pt por Encontro|Origem|
|---|---|---|
|Acertos por Encontro|7,8|1,95 acertos por Rodada × 4 Rodadas|
|+1 de BA em Ataques|18,5|`Custo de PHs.md`, Tabela 1|
|+1 de BD|7,8|`Custo de PHs.md`, Tabela 1|
|+1 de CA|17,9|`Custo de PHs.md`, Tabela 1|
|+1 de Resistência|7,5|`Custo de PHs.md`, Tabela 1|
|+1,5 m de alcance corpo a corpo|8,0|`Custo de PHs.md`, Tabela 1|
|+1,5 m de alcance de Ataque à distância|2,0|`Custo de PHs.md`, Tabela 1 (alcance de Ataque Mágico)|
|+1,5 m de Deslocamento|6,7|`Custo de PHs.md`, Tabela 1|
|1 PA fora do plano do build|7,9|`Custos de Mana.md`, §9|

## 3. Valor das Armas

### 3.1 Grau

O dano de um Grau vale a média do dado vezes 7,8 acertos por Encontro. É o preço **bruto**, antes de descontos.

|Grau|Dado|Média|pt|Preço|Diferença para o Grau anterior|
|---|---|---|---|---|---|
|1|1d4|2,5|19,5|9 PO, 7 PP e 5 PC|-|
|2|1d6|3,5|27,3|1 PL, 3 PO, 6 PP e 5 PC|3 PO e 9 PP|
|3|1d8|4,5|35,1|1 PL, 7 PO, 5 PP e 5 PC|3 PO e 9 PP|
|4|1d10|5,5|42,9|2 PL, 1 PO, 4 PP e 5 PC|3 PO e 9 PP|
|5|1d12|6,5|50,7|2 PL, 5 PO, 3 PP e 5 PC|3 PO e 9 PP|
|6|2d6|7,0|54,6|2 PL, 7 PO e 3 PP|1 PO, 9 PP e 5 PC|
|7|2d8|9,0|70,2|3 PL, 5 PO e 1 PP|7 PO e 8 PP|
|8|2d10|11,0|85,8|4 PL, 2 PO e 9 PP|7 PO e 8 PP|
|9|2d12|13,0|101,4|5 PL e 7 PP|7 PO e 8 PP|
|10|3d10|16,5|128,7|6 PL, 4 PO, 3 PP e 5 PC|1 PL, 3 PO, 6 PP e 5 PC|

**Cada +1 de média de dano vale 7,8 pt, ou 3 PO e 9 PP.** Isso é útil para o Capítulo 4.9: nas Pedras de Aprimoramento, as subidas de "ganho por pedra" igual a 1 (Graus 1 a 5 e 6 a 7) custam 3 PO e 9 PP por Pedra. Já 5→6, 7→8, 8→9 e 9→10 rendem menos de 1 de média por Pedra, então, com preço fixo por Pedra, ficam mais caras do que o valor que entregam.

### 3.2 Um bônus e dois bônus

Cada +1 no Modificador que a Arma deixa você somar vale **26,3 pt** (18,5 do BA mais 7,8 do BD), ou **1 PL, 3 PO, 1 PP e 5 PC**.

- **Um bônus**: preço adicional de **0**. O Ataque Desarmado já soma For ou Des, então o primeiro bônus não é uma vantagem da Arma: é só a condição para ela valer mais que desarmado.
- **Dois bônus**: o segundo Atributo é um ganho real. Foi adotado um Modificador efetivo de **+3** para ele (a média entre um build alinhado, ≈ +4, e um desalinhado, ≈ +2).

|Modificador efetivo do segundo bônus|pt|Preço adicional|
|---|---|---|
|+1|26,3|1 PL, 3 PO, 1 PP e 5 PC|
|+2|52,6|2 PL, 6 PO e 3 PP|
|**+3 (adotado)**|**78,9**|**3 PL, 9 PO, 4 PP e 5 PC**|
|+4|105,2|5 PL, 2 PO e 6 PP|
|+5|131,5|6 PL, 5 PO, 7 PP e 5 PC|

**Preço bruto de uma Arma = preço do Grau + preço adicional dos bônus + alcance (§3.3).**

### 3.3 Alcance

**Corpo a corpo**: cada +1,5 m acima do padrão de 1,5 m vale **8,0 pt, ou 4 PO**. O valor é linear.

|Alcance adicional|Preço|
|---|---|
|+1,5 m|4 PO|
|+3 m|8 PO|
|+4,5 m|1 PL e 2 PO|
|+6 m|1 PL e 6 PO|

**À distância**: cada +1,5 m de alcance vale **2,0 pt, ou 1 PO**, contado desde 0 m. O alcance é cobrado **até 48 m (32 passos de 1,5 m)**. O que passar disso é considerado bônus e não entra no preço.

|Alcance|Preço|
|---|---|
|9 m|6 PO|
|12 m|8 PO|
|18 m|1 PL e 2 PO|
|24 m|1 PL e 6 PO|
|30 m|2 PL|
|36 m|2 PL e 4 PO|
|42 m|2 PL e 8 PO|
|48 m ou mais|3 PL e 2 PO|

## 4. Valor das Armaduras e dos Escudos

### 4.1 +1 de CA

Cada +1 de CA vale **17,9 pt, ou 8 PO, 9 PP e 5 PC**. O valor é linear. A tabela vale também para o Capítulo 4.9, já que as Pedras aumentam a CA.

|CA concedida|pt|Preço bruto|
|---|---|---|
|+1|17,9|8 PO, 9 PP e 5 PC|
|+2|35,8|1 PL, 7 PO e 9 PP|
|+3|53,7|2 PL, 6 PO, 8 PP e 5 PC|
|**+4 (teto da Leve)**|71,6|3 PL, 5 PO e 8 PP|
|+5|89,5|4 PL, 4 PO, 7 PP e 5 PC|
|**+6 (teto da Média)**|107,4|5 PL, 3 PO e 7 PP|
|+7|125,3|6 PL, 2 PO, 6 PP e 5 PC|
|**+8 (teto da Pesada)**|143,2|7 PL, 1 PO e 6 PP|
|+9|161,1|8 PL e 5 PP e 5 PC|
|+10|179,0|8 PL, 9 PO e 5 PP|

### 4.2 +1 de Resistência a Dano Físico do Escudo

Cada +1 de Resistência vale 7,5 pt por Encontro. Duas correções:

- **Só Dano Físico**: foi assumido que **70%** do dano recebido é Dano Físico. Isso reduz para **5,25 pt**.
- **Ação Bônus para levantar**: o `Custo de PHs.md` trata a Ação Bônus como custo 0, então não há desconto por ela. Como o Escudo dura até o início do próximo Turno, a Resistência vale em toda Rodada, e 7,5 pt já é o valor das 4 Rodadas.

Cada +1 de Resistência vale **5,25 pt, ou 2 PO, 6 PP e 3 PC**.

|Resistência|pt|Preço bruto|
|---|---|---|
|+1|5,25|2 PO, 6 PP e 3 PC|
|+2|10,5|5 PO, 2 PP e 5 PC|
|+3|15,75|7 PO, 8 PP e 8 PC|
|+4|21,0|1 PL e 5 PP|
|+5|26,25|1 PL, 3 PO, 1 PP e 3 PC|
|+6|31,5|1 PL, 5 PO, 7 PP e 5 PC|
|+7|36,75|1 PL, 8 PO, 3 PP e 8 PC|
|+8|42,0|2 PL e 1 PO|
|+9|47,25|2 PL, 3 PO, 6 PP e 3 PC|
|+10|52,5|2 PL, 6 PO, 2 PP e 5 PC|

## 5. Descontos

Os descontos são **subtraídos** do preço bruto, em pt (e depois convertidos).

### 5.1 Requisitos

Os requisitos são valores de Atributo. Eles usam o mesmo cálculo de `Custo de PHs.md` §4.1: o requisito é o custo de oportunidade dos PAs que o PDJ precisa gastar naquele Atributo, e esse custo vira desconto.

**Um requisito**

|Valor do requisito|Desconto (pt)|Desconto|**+1 de requisito** (pt)|**+1 de requisito**|
|---|---|---|---|---|
|1|1,1|5 PP e 5 PC|1,1|5 PP e 5 PC|
|2|2,3|1 PO, 1 PP e 5 PC|1,2|6 PP|
|3|3,9|1 PO, 9 PP e 5 PC|1,6|8 PP|
|4|5,6|2 PO e 8 PP|1,7|8 PP e 5 PC|
|5|7,9|3 PO, 9 PP e 5 PC|2,3|1 PO, 1 PP e 5 PC|
|6|10,1|5 PO e 5 PC|2,2|1 PO e 1 PP|
|7|12,9|6 PO, 4 PP e 5 PC|2,8|1 PO e 4 PP|
|8|15,8|7 PO e 9 PP|2,9|1 PO, 4 PP e 5 PC|
|9|19,1|9 PO, 5 PP e 5 PC|3,3|1 PO, 6 PP e 5 PC|
|10|22,5|1 PL, 1 PO, 2 PP e 5 PC|3,4|1 PO e 7 PP|

Na média, **+1 de requisito vale 2,25 pt, ou 1 PO, 1 PP e 3 PC**. O primeiro ponto vale pouco (5 PP e 5 PC), e o último, bastante (1 PO e 7 PP).

**Vários requisitos (cada um é um Atributo diferente)**: some o desconto de cada requisito na tabela acima e acrescente **3,96 pt (1 PO, 9 PP e 8 PC) por PA de déficit**. O déficit compara os requisitos, do maior para o menor, com o build típico de 30 PAs (10, 8, 6, 4, 2, 0, 0), e é a soma de `max(0, requisito − valor do build)`.

|Requisitos|Desconto (pt)|Desconto|
|---|---|---|
|3 e 1|5,0|2 PO e 5 PP|
|4 e 4|11,3|5 PO, 6 PP e 5 PC|
|5 e 5|15,8|7 PO e 9 PP|
|6 e 6|20,3|1 PL, 1 PP e 5 PC|
|8 e 8|31,5|1 PL, 5 PO, 7 PP e 5 PC|
|10 e 10|52,9|2 PL, 6 PO, 4 PP e 5 PC|
|5, 5 e 5|23,6|1 PL, 1 PO e 8 PP|
|8, 8 e 8|55,1|2 PL, 7 PO, 5 PP e 5 PC|

### 5.2 Peso

Cada unidade de Peso ocupa a Capacidade de Carga (10 + For × NV). Como +1 de Modificador de For dá +NV de Capacidade e custa 2 PAs, no **Nível 10** (meio da campanha) 1 Peso equivale a 0,2 PA, ou **1,6 pt**.

**Cada unidade de Peso desconta 1,6 pt, ou 8 PP.**

|Peso|Desconto (pt)|Desconto|
|---|---|---|
|1|1,6|8 PP|
|2|3,2|1 PO e 6 PP|
|3|4,8|2 PO e 4 PP|
|4|6,4|3 PO e 2 PP|
|5|8,0|4 PO|
|10|16,0|8 PO|
|15|24,0|1 PL e 2 PO|
|20|32,0|1 PL e 6 PO|

### 5.3 Penalidades

**Desvantagem em Furtividade** (Armaduras Médias e Pesadas): uma Desvantagem equivale a ≈ -3,3 no Teste. Foi assumido um Teste de Furtividade por Encontro (o esconder inicial), e um Teste vale ≈ 20 pt (uma Ação). Cada ponto de BA em Perícia vale 1,0 pt por uso, então 3,3 × 1,0 = 3,3 pt.

**Desconto: 3,3 pt, ou 1 PO, 6 PP e 5 PC.**

**Penalidade de Deslocamento** (Armaduras Pesadas): -1,5 m de Deslocamento é o oposto de +1,5 m, que vale 6,7 pt por Encontro.

**Desconto: 6,7 pt, ou 3 PO, 3 PP e 5 PC, a cada -1,5 m.** O valor é linear.

|Penalidade|Desconto (pt)|Desconto|
|---|---|---|
|-1,5 m|6,7|3 PO, 3 PP e 5 PC|
|-3 m|13,4|6 PO e 7 PP|
|-4,5 m|20,1|1 PL e 5 PC|
|-6 m|26,8|1 PL, 3 PO e 4 PP|

## 6. Preço final

**Preço = preço bruto − Peso − requisitos − penalidades**

Para impedir preços muito baixos ou negativos, o preço final **nunca fica abaixo de 25% do preço bruto**.

## 7. Exemplos

|Item|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Arma de Grau 4, um bônus, requisito For 3, Peso 3|42,9|3,9 + 4,8 = 8,7|34,2|1 PL, 7 PO e 1 PP|
|Arma de Grau 4, dois bônus, requisitos For 3 e Des 3, Peso 3|42,9 + 78,9 = 121,8|7,8 + 4,8 = 12,6|109,2|5 PL, 4 PO e 6 PP|
|Arco de Grau 5, alcance 18 m, um bônus, requisito Des 3, Peso 2|50,7 + 24,0 = 74,7|3,9 + 3,2 = 7,1|67,6|3 PL, 3 PO e 8 PP|
|Armadura Leve +4, requisito Des 3, Peso 5|71,6|3,9 + 8,0 = 11,9|59,7|2 PL, 9 PO, 8 PP e 5 PC|
|Armadura Média +6, requisito For 4, Peso 10, Desvantagem em Furtividade|107,4|5,6 + 16,0 + 3,3 = 24,9|82,5|4 PL, 1 PO, 2 PP e 5 PC|
|Armadura Pesada +8, requisitos For 6 e Con 4, Peso 20, Desvantagem em Furtividade, -3 m de Deslocamento|143,2|15,7 + 32,0 + 3,3 + 13,4 = 64,4|78,8|3 PL, 9 PO e 4 PP|
|Escudo com Resistência 4, requisito For 4, Peso 5|21,0|5,6 + 8,0 = 13,6|7,4|3 PO e 7 PP|

Os dois primeiros itens de equipamento inicial (Arma de Grau 4 e Armadura Leve) somam **4 PL, 6 PO, 9 PP e 5 PC**, dentro dos 50 PO iniciais.

## 8. Observações e pontos em aberto

1. **Todos os valores partem do Nível 20.** +1 de BA e +1 de CA valem proporcionalmente menos nos Níveis baixos (`Custos de Mana.md` §6), então Armaduras são relativamente caras no começo e o BD fixo vale mais cedo. O preço não varia com o Nível, e o equipamento inicial é o que sustenta a calibração.
2. **O primeiro bônus de Atributo é gratuito** e o segundo vale +3 de Modificador. Se preferir cobrar o primeiro bônus também, o Grau 5 de uma Arma com bônus já passaria de 50 PO.
3. **Escudo:** 70% do dano como físico e Ação Bônus de custo 0 são premissas. Ocupar uma das mãos (perder o Ataque com duas Armas) não foi descontado.
4. **Peso:** usa o Nível 10 como referência. Nos Níveis baixos a Capacidade de Carga aperta mais e o Peso valeria mais.
5. **Alcance à distância** usa o valor de alcance de Ataque Mágico (baixa confiança), assumindo que o alcance é cobrado desde 0 m.
6. **Furtividade:** conta só o uso em combate. O valor em exploração não foi incluído.
7. **Piso de 25%** do preço bruto é um chute informado, para não zerar o preço de itens com muitos requisitos.
8. **Ainda sem preço:** Empunhadura Dupla (BD com o valor completo do Atributo), Margem de Ameaça das Armas Comuns, Munição e Itens Consumíveis.