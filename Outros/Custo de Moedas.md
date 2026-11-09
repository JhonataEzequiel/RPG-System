Este documento calcula, **em moedas**, quanto valem os efeitos de Armas, Armaduras e Escudos. Ele usa os mesmos valores em pontos de `Custos de Mana.md` e de `Custo de PHs.md` (pt por Encontro, cenário típico do Nível 20), e acrescenta a conversão para moedas, o preço de cada efeito e os descontos por Peso, requisitos e penalidades.

Todos os preços seguem a regra de exibição descrita em §1: até 9 PP ficam como estão, e acima disso aparecem apenas em PO, arredondados para cima. A partir de 100 PO, passam a usar PL.

## 1. Conversão: pontos em moedas

**1 pt por Encontro = 50 PC.** Equivale a **1 PO = 2 pt**.

Esse é o **botão principal** do documento. Ele foi escolhido para que os 50 PO iniciais (Capítulo 2) comprem uma Arma de Grau 4 e uma Armadura Leve com requisitos e Peso típicos (ver §7). Se o preço geral estiver alto ou baixo, basta mudar este número: todo o resto escala junto.

Os cálculos são feitos em pt, com o valor exato. Só o preço exibido é arredondado, seguindo esta regra: se o preço for menor ou igual a 9 PP, ele fica como está. Se for maior, é representado apenas em PO, arredondando para cima. Por exemplo, 2 PL, 3 PO, 4 PP e 3 PC (23,43 PO) vira 24 PO.

Há uma ressalva: preços a partir de 100 PO passam a contar em PL (1 PL = 10 PO). Nesse caso, um valor secundário em PO continua sendo mostrado até 20 PL. Acima disso, o preço aparece só em PL, arredondando para cima. Por exemplos:

- 103 PO, 4 PP e 3 PC → 104 PO → 10 PL e 4 PO.
- 203 PO e 4 PP → 204 PO → 20 PL e 4 PO.
- 204 PO, 9 PP e 1 PC → 205 PO → 20 PL e 5 PO.

Como o arredondamento é para cima, somar os preços exibidos pode passar um pouco do valor exato, e as colunas de pt continuam sendo a referência.

|pt|PC|Moedas|
|---|---|---|
|1|50|5 PP|
|2|100|1 PO|
|5|250|3 PO|
|10|500|5 PO|
|20|1.000|10 PO|
|50|2.500|25 PO|
|100|5.000|50 PO|

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
|1|1d4|2,5|19,5|10 PO|-|
|2|1d6|3,5|27,3|14 PO|4 PO|
|3|1d8|4,5|35,1|18 PO|4 PO|
|4|1d10|5,5|42,9|22 PO|4 PO|
|5|1d12|6,5|50,7|26 PO|4 PO|
|6|2d6|7,0|54,6|28 PO|2 PO|
|7|2d8|9,0|70,2|36 PO|8 PO|
|8|2d10|11,0|85,8|43 PO|8 PO|
|9|2d12|13,0|101,4|51 PO|8 PO|
|10|3d10|16,5|128,7|65 PO|14 PO|

**Cada +1 de média de dano vale 7,8 pt, ou 4 PO.** Isso é útil para o Capítulo 4.9: nas Pedras de Aprimoramento, as subidas com "ganho por pedra" igual a 1 (Graus 1 a 5 e 6→7) custam 4 PO por Pedra. Já 5→6, 7→8, 8→9 e 9→10 rendem menos de 1 de média por Pedra, então, com preço fixo por Pedra, ficam mais caras do que o valor que entregam.

### 3.2 Um bônus e dois bônus

Cada +1 no Modificador que a Arma deixa você somar vale **26,3 pt** (18,5 do BA mais 7,8 do BD), ou **14 PO**.

- **Um bônus**: preço adicional de **0**. O Ataque Desarmado já soma For ou Des, então o primeiro bônus não é uma vantagem da Arma: é só a condição para ela valer mais que desarmado.
- **Dois bônus**: o segundo Atributo é um ganho real. Foi adotado um Modificador efetivo de **+3** para ele (a média entre um build alinhado, ≈ +4, e um desalinhado, ≈ +2).

|Modificador efetivo do segundo bônus|pt|Preço adicional|
|---|---|---|
|+1|26,3|14 PO|
|+2|52,6|27 PO|
|**+3 (adotado)**|**78,9**|**40 PO**|
|+4|105,2|53 PO|
|+5|131,5|66 PO|

**Preço bruto de uma Arma = preço do Grau + preço adicional dos bônus + alcance (§3.3) + efeitos adicionais (§8).** Em Armas à Distância que recarregam, o preço do Grau é multiplicado antes pelo fator de recarga (§8.2).

### 3.3 Alcance

**Corpo a corpo**: cada +1,5 m acima do padrão de 1,5 m vale **8,0 pt, ou 4 PO**. O valor é linear.

|Alcance adicional|Preço|
|---|---|
|+1,5 m|4 PO|
|+3 m|8 PO|
|+4,5 m|12 PO|
|+6 m|16 PO|

**À distância**: o alcance base é de **9 m**, e só o que passa disso é cobrado. Cada +1,5 m acima de 9 m vale **2,0 pt, ou 1 PO**. O alcance é cobrado **até 48 m (26 passos de 1,5 m acima de 9 m)**. O que passar disso é considerado bônus e não entra no preço.

|Alcance|Preço|
|---|---|
|9 m ou menos|0|
|12 m|2 PO|
|18 m|6 PO|
|24 m|10 PO|
|30 m|14 PO|
|36 m|18 PO|
|42 m|22 PO|
|48 m ou mais|26 PO|

## 4. Valor das Armaduras e dos Escudos

### 4.1 +1 de CA

Cada +1 de CA vale **17,9 pt, ou 9 PO**. O valor é linear. A tabela vale também para o Capítulo 4.9, já que as Pedras aumentam a CA.

|CA concedida|pt|Preço bruto|
|---|---|---|
|+1|17,9|9 PO|
|+2|35,8|18 PO|
|+3|53,7|27 PO|
|**+4 (teto da Leve)**|71,6|36 PO|
|+5|89,5|45 PO|
|**+6 (teto da Média)**|107,4|54 PO|
|+7|125,3|63 PO|
|**+8 (teto da Pesada)**|143,2|72 PO|
|+9|161,1|81 PO|
|+10|179,0|90 PO|

### 4.2 +1 de Resistência a Dano Físico do Escudo

Cada +1 de Resistência vale 7,5 pt por Encontro. Duas correções:

- **Só Dano Físico**: foi assumido que **70%** do dano recebido é Dano Físico. Isso reduz para **5,25 pt**.
- **Ação Bônus para levantar**: o `Custo de PHs.md` trata a Ação Bônus como custo 0, então não há desconto por ela. Como o Escudo dura até o início do próximo Turno, a Resistência vale em toda Rodada, e 7,5 pt já é o valor das 4 Rodadas.

Cada +1 de Resistência vale **5,25 pt, ou 3 PO**.

|Resistência|pt|Preço bruto|
|---|---|---|
|+1|5,25|3 PO|
|+2|10,5|6 PO|
|+3|15,75|8 PO|
|+4|21,0|11 PO|
|+5|26,25|14 PO|
|+6|31,5|16 PO|
|+7|36,75|19 PO|
|+8|42,0|21 PO|
|+9|47,25|24 PO|
|+10|52,5|27 PO|

## 5. Descontos

Os descontos são **subtraídos** do preço bruto, em pt (e depois convertidos).

### 5.1 Requisitos

Os requisitos são valores de Atributo. Eles usam o mesmo cálculo de `Custo de PHs.md` §4.1: o requisito é o custo de oportunidade dos PAs que o PDJ precisa gastar naquele Atributo, e esse custo vira desconto.

**Um requisito**

|Valor do requisito|Desconto (pt)|Desconto|**+1 de requisito** (pt)|**+1 de requisito**|
|---|---|---|---|---|
|1|1,1|5 PP e 5 PC|1,1|5 PP e 5 PC|
|2|2,3|2 PO|1,2|6 PP|
|3|3,9|2 PO|1,6|8 PP|
|4|5,6|3 PO|1,7|8 PP e 5 PC|
|5|7,9|4 PO|2,3|2 PO|
|6|10,1|6 PO|2,2|2 PO|
|7|12,9|7 PO|2,8|2 PO|
|8|15,8|8 PO|2,9|2 PO|
|9|19,1|10 PO|3,3|2 PO|
|10|22,5|12 PO|3,4|2 PO|

Na média, **+1 de requisito vale 2,25 pt, ou 2 PO**. O primeiro ponto vale pouco (5 PP e 5 PC), e o último, bastante (2 PO).

**Vários requisitos (cada um é um Atributo diferente)**: some o desconto de cada requisito na tabela acima e acrescente **3,96 pt (2 PO) por PA de déficit**. O déficit compara os requisitos, do maior para o menor, com o build típico de 30 PAs (10, 8, 6, 4, 2, 0, 0), e é a soma de `max(0, requisito − valor do build)`.

|Requisitos|Desconto (pt)|Desconto|
|---|---|---|
|3 e 1|5,0|3 PO|
|4 e 4|11,3|6 PO|
|5 e 5|15,8|8 PO|
|6 e 6|20,3|11 PO|
|8 e 8|31,5|16 PO|
|10 e 10|52,9|27 PO|
|5, 5 e 5|23,6|12 PO|
|8, 8 e 8|55,1|28 PO|

### 5.2 Peso

Cada unidade de Peso ocupa a Capacidade de Carga (10 + For × NV). Como +1 de Modificador de For dá +NV de Capacidade e custa 2 PAs, no **Nível 10** (meio da campanha) 1 Peso equivale a 0,2 PA, ou **1,6 pt**.

**Cada unidade de Peso desconta 1,6 pt, ou 8 PP.**

|Peso|Desconto (pt)|Desconto|
|---|---|---|
|1|1,6|8 PP|
|2|3,2|2 PO|
|3|4,8|3 PO|
|4|6,4|4 PO|
|5|8,0|4 PO|
|10|16,0|8 PO|
|15|24,0|12 PO|
|20|32,0|16 PO|

### 5.3 Penalidades

**Desvantagem em Furtividade** (Armaduras Médias e Pesadas): uma Desvantagem equivale a ≈ -3,3 no Teste. Foi assumido um Teste de Furtividade por Encontro (o esconder inicial), e um Teste vale ≈ 20 pt (uma Ação). Cada ponto de BA em Perícia vale 1,0 pt por uso, então 3,3 × 1,0 = 3,3 pt.

**Desconto: 3,3 pt, ou 2 PO.**

**Penalidade de Deslocamento** (Armaduras Pesadas): -1,5 m de Deslocamento é o oposto de +1,5 m, que vale 6,7 pt por Encontro.

**Desconto: 6,7 pt, ou 4 PO, a cada -1,5 m.** O valor é linear.

|Penalidade|Desconto (pt)|Desconto|
|---|---|---|
|-1,5 m|6,7|4 PO|
|-3 m|13,4|7 PO|
|-4,5 m|20,1|11 PO|
|-6 m|26,8|14 PO|

## 6. Preço final

**Preço = preço bruto − Peso − requisitos − penalidades**

Para impedir preços muito baixos ou negativos, o preço final **nunca fica abaixo de 25% do preço bruto**.

## 7. Exemplos

|Item|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Arma de Grau 4, um bônus, requisito For 3, Peso 3|42,9|3,9 + 4,8 = 8,7|34,2|18 PO|
|Arma de Grau 4, dois bônus, requisitos For 3 e Des 3, Peso 3|42,9 + 78,9 = 121,8|7,8 + 4,8 = 12,6|109,2|55 PO|
|Arco de Grau 5, alcance 18 m, um bônus, requisito Des 3, Peso 2|50,7 + 12,0 = 62,7|3,9 + 3,2 = 7,1|55,6|28 PO|
|Armadura Leve +4, requisito Des 3, Peso 5|71,6|3,9 + 8,0 = 11,9|59,7|30 PO|
|Armadura Média +6, requisito For 4, Peso 10, Desvantagem em Furtividade|107,4|5,6 + 16,0 + 3,3 = 24,9|82,5|42 PO|
|Armadura Pesada +8, requisitos For 6 e Con 4, Peso 20, Desvantagem em Furtividade, -3 m de Deslocamento|143,2|15,7 + 32,0 + 3,3 + 13,4 = 64,4|78,8|40 PO|
|Escudo com Resistência 4, requisito For 4, Peso 5|21,0|5,6 + 8,0 = 13,6|7,4|4 PO|

Uma Arma de Grau 4 (um bônus) e uma Armadura Leve, como nos dois primeiros exemplos de Arma e Armadura acima, somam **48 PO** (18 PO e 30 PO), dentro dos 50 PO iniciais.

## 8. Efeitos adicionais

### 8.1 Dano adicional igual à metade do dano do Ataque

O adicional é calculado **depois de todos os cálculos** do dano, então vale 50% do dano por acerto. No cenário típico do Nível 20, o dano por acerto é ≈ 30,8 (`Custos de Mana.md` §2), ou seja, o adicional é de ≈ 15,4 por acerto.

**pt = 0,5 × dano por acerto × 7,8 acertos por Encontro = 3,9 × dano por acerto.**

|Dano por acerto|Adicional por acerto|pt (todos os acertos)|Preço|
|---|---|---|---|
|10|5|39,0|20 PO|
|20|10|78,0|39 PO|
|30,8 (Nível 20)|15,4|120,1|61 PO|
|40|20|156,0|78 PO|

Se o efeito não vale em todo acerto, use as frequências de `Custo de PHs.md` §2.1 (dano por acerto de 30,8):

|Frequência|pt|Preço|
|---|---|---|
|Todo acerto|120,1|61 PO|
|Uma vez por Rodada (×4)|61,6|31 PO|
|Só em Ataque Crítico (×0,2)|24,0|12 PO|
|Uma vez por Encontro (×1)|15,4|8 PO|

**Adicional calculado depois do crítico:** se o adicional de 50% é aplicado depois do dobro do Ataque Crítico, o crítico também o amplia. Como ≈ 5% dos Ataques são críticos, o valor sobe ≈ 7,7%: multiplique os pt acima por 1,077 (todo acerto: 129,3 pt, ou 65 PO).

Alerta: o efeito sempre ligado custa quase o mesmo que um Grau 10 inteiro (128,7 pt) e escala com o dano do PDJ, ampliando todos os outros bônus. Vale limitar a frequência.

### 8.2 Recarregar a cada X tiros

**Valor real.** Um Encontro tem 12 Ações (3 por Rodada × 4). Recarregar custa uma Ação, e a Arma começa carregada. Os tiros que cabem em um Encontro são **13X ÷ (X + 1)**, com máximo de 12. Uma Besta (X = 1) dispara ≈ 6,5 vezes (54% do máximo), e uma Arma que não recarrega em um Encontro (X ≥ 12, como os Arcos) dispara 12.

**Fator de recarga.** O preço do Grau é multiplicado por:

**f(X) = 0,5 + 0,5 × ((X − 1) ÷ 11)^1,5**, com f = 1 para X ≥ 12.

Os extremos vêm do valor real (Besta ≈ 50%, sem recarga = 100%). O expoente 1,5 faz o preço **subir mais a cada tiro adicional**, como pedido: o passo de X = 1 para 2 é de 1,4 ponto percentual, e o de X = 11 para 12 é de 6,7. Para um aumento mais suave, use o expoente 1 (linear); para um mais íngreme, 2.

O exemplo é o preço do Grau de uma Arma de Grau 5 (26 PO sem recarga):

|X (tiros por recarga)|Fator|Preço do Grau 5|
|---|---|---|
|1 (Besta)|0,500|13 PO|
|2|0,514|14 PO|
|3|0,539|14 PO|
|4|0,571|15 PO|
|5|0,610|16 PO|
|6|0,653|17 PO|
|7|0,701|18 PO|
|8|0,754|20 PO|
|9|0,810|21 PO|
|10|0,870|23 PO|
|11|0,933|24 PO|
|12 ou mais (Arco)|1,000|26 PO|

- O fator vale só para o preço do **Grau**. Alcance, bônus e requisitos seguem as outras seções.
- Com duas Armas à Distância ao mesmo tempo, cada Ataque gasta um tiro de cada Arma, então X conta Ataques.
- **Conflito com o valor real:** pelo cálculo de Ações, os primeiros tiros valem mais que os últimos (X = 2 já chegaria a 0,72, e X = 10 a 0,98). A curva crescente é uma escolha de design, e não sai da economia de Ações.

### 8.3 Ganhar 1 Grau de PVs ou PMs Temporários

Foi considerado "ganhar PVs ou PMs Temporários de Grau 1", recebidos pelo item e válidos até o fim do Encontro. Para efeitos de **uma vez por Descanso Longo**, multiplique o preço por **0,25** (4 Encontros por dia, `Balanceamento.md`). Os valores saem de `Custos de Mana.md` §5.3 (PV Temporário com o fator 3 de cura e PM Temporário 1:1). A tabela traz também os demais Graus, e a diferença entre duas linhas seguidas é o preço de **aumentar em +1 Grau** um efeito que já existe.

|Grau|PV Temp. (uma vez por Encontro)|PM Temp. (uma vez por Encontro)|PV Temp. (por Rodada, dura 1 Rodada)|PM Temp. (por Rodada, dura 1 Rodada)|
|---|---|---|---|---|
|**1 (1d4)**|**4 PO**|**2 PO**|**14 PO**|**4 PO**|
|2 (1d6)|6 PO|2 PO|18 PO|6 PO|
|3 (1d8)|7 PO|3 PO|22 PO|7 PO|
|4 (1d10)|8 PO|3 PO|26 PO|8 PO|
|5 (1d12)|10 PO|4 PO|29 PO|8 PO|
|6 (2d6)|11 PO|4 PO|30 PO|9 PO|
|7 (2d8)|13 PO|5 PO|36 PO|10 PO|
|8 (2d10)|16 PO|5 PO|40 PO|10 PO|
|9 (2d12)|18 PO|6 PO|43 PO|11 PO|
|10 (3d10)|23 PO|7 PO|48 PO|12 PO|

O PV Temporário vale ≈ 3× o PM Temporário do mesmo Grau, pelo mesmo motivo da cura (§1 de `Custos de Mana.md`). A subida do Grau 5 para o 6 só vale +1,4 pt de PV Temporário (a média sobe 0,5), enquanto a do 9 para o 10 vale +8,7.

### 8.4 Aumentar em 1 o Grau de um tipo de Ataque

O ganho é a diferença de média entre os dois Graus vezes 7,8 acertos por Encontro. É a mesma diferença da tabela do §3.1. Em seguida aplica-se um **fator de uso**, porque o aumento só vale para os Ataques daquele tipo (`Custo de PHs.md` §2.1):

- **×0,8**: o tipo é o Ataque principal do build (Armas Leves, Comuns, de Empunhadura Dupla ou à Distância).
- **×0,4**: o tipo é secundário ou situacional (Ataques Desarmados, Arremessar).

|Grau inicial → final|Ganho de média|pt (100%)|Preço (100%)|Preço ×0,8|Preço ×0,4|
|---|---|---|---|---|---|
|1 → 2|+1,0|7,8|4 PO|4 PO|2 PO|
|2 → 3|+1,0|7,8|4 PO|4 PO|2 PO|
|3 → 4|+1,0|7,8|4 PO|4 PO|2 PO|
|4 → 5|+1,0|7,8|4 PO|4 PO|2 PO|
|5 → 6|+0,5|3,9|2 PO|2 PO|7 PP e 8 PC|
|6 → 7|+2,0|15,6|8 PO|7 PO|4 PO|
|7 → 8|+2,0|15,6|8 PO|7 PO|4 PO|
|8 → 9|+2,0|15,6|8 PO|7 PO|4 PO|
|9 → 10|+3,5|27,3|14 PO|11 PO|6 PO|

O Grau não passa de 10 (Capítulo 1.5), então não há preço a partir do Grau 10.

### 8.5 Empunhadura Dupla e Armas sem bônus de BD

Duas regras usadas para precificar os Capítulos 4.1 e 4.2. Elas usam um Modificador efetivo de **+4** para o primeiro bônus de Atributo (a mistura entre um build alinhado, +5, e um desalinhado, +3) e de **+3** para o segundo (§3.2).

- **Empunhadura Dupla:** somar o valor completo do Atributo ao BD equivale ao que uma Arma Comum ou Leve ganha ao ser empunhada com duas mãos (Capítulo 4), então esse benefício **não é cobrado** quando a Arma tem um bônus só. Com **dois bônus**, a Arma Comum empunhada com duas mãos dobra só a Força, e a Arma de Empunhadura Dupla dobra os dois Atributos. A diferença é o Modificador do segundo Atributo: **+3 × 7,8 = 23,4 pt (12 PO)**, somados ao preço bruto.
- **Armas sem bônus de BD** (Bestas e Armas de Fogo, que somam Destreza só no BA): o Ataque Desarmado já soma For ou Des no BD, então essas Armas perdem esse bônus. **Desconto de 4 × 7,8 = 31,2 pt (16 PO).**

## 9. Observações e pontos em aberto

1. **Todos os valores partem do Nível 20.** +1 de BA e +1 de CA valem proporcionalmente menos nos Níveis baixos (`Custos de Mana.md` §6), então Armaduras são relativamente caras no começo e o BD fixo vale mais cedo. O preço não varia com o Nível, e o equipamento inicial é o que sustenta a calibração.
2. **O primeiro bônus de Atributo é gratuito** e o segundo vale +3 de Modificador. Se preferir cobrar o primeiro bônus também, o Grau 5 de uma Arma com bônus já passaria de 50 PO.
3. **Escudo:** 70% do dano como físico e Ação Bônus de custo 0 são premissas. Ocupar uma das mãos (perder o Ataque com duas Armas) não foi descontado.
4. **Peso:** usa o Nível 10 como referência. Nos Níveis baixos a Capacidade de Carga aperta mais e o Peso valeria mais.
5. **Alcance à distância** usa o valor de alcance de Ataque Mágico (baixa confiança). O alcance base é de 9 m, e só o que passa disso é cobrado.
6. **Furtividade:** conta só o uso em combate. O valor em exploração não foi incluído.
7. **Piso de 25%** do preço bruto é um chute informado, para não zerar o preço de itens com muitos requisitos.
8. **Ainda sem preço:** a Margem de Ameaça das Armas Comuns, a Munição e os Itens Consumíveis.