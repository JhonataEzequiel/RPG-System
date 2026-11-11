Este documento calcula, **em moedas**, quanto valem os efeitos de Armas, Armaduras e Escudos. Ele usa os mesmos valores em pontos de `Custos de Mana.md` e de `Custo de PHs.md` (pt por Encontro, cenário típico do Nível 20), e acrescenta a conversão para moedas, o preço de cada efeito e os descontos por Peso, requisitos e penalidades. No fim (§9), estão os preços de todos os itens das listas dos Capítulos 4.1 a 4.3, que estavam sem preço.

**O que mudou em relação ao rascunho anterior.** As Armas e Armaduras agora têm Escalas (Capítulo 4), então o valor do item vem do Grau ou do bônus de CA mais o valor das Escalas, e não mais de "um bônus" ou "dois bônus" de Modificador. O dano do grupo subiu (ver `Balanceamento.md`), então +1 de BA e +1 de CA passaram de 17,9 e 18,5 para 57,7 pt por Encontro, enquanto os valores de dado (Graus) continuam os mesmos. O Escudo agora concede Resistência a Dano Físico e Mágico e traz uma Habilidade. O equipamento inicial passou de 50 PO para 150 PO (Capítulo 2).

Todos os preços seguem a regra de exibição descrita em §1: até 9 PP ficam como estão, e acima disso aparecem apenas em PO, arredondados para cima. A partir de 100 PO, passam a usar PL.

## 1. Conversão: pontos em moedas

**1 pt por Encontro = 19 PC.** Equivale a **1 PO ≈ 5,3 pt**.

Esse é o **botão principal** do documento. Ele foi escolhido para que os 150 PO iniciais (Capítulo 2) comprem uma Arma de Grau 4 com uma Escala D e uma Armadura Leve de +4 de CA com Escala D, com requisitos e Peso típicos (ver §7). Esse conjunto custa 146 PO. Se o preço geral estiver alto ou baixo, basta mudar este número: todo o resto escala junto.

Os cálculos são feitos em pt, com o valor exato. Só o preço exibido é arredondado, seguindo esta regra: se o preço for menor ou igual a 9 PP, ele fica como está. Se for maior, é representado apenas em PO, arredondando para cima. Por exemplo, 2 PL, 3 PO, 4 PP e 3 PC (23,43 PO) vira 24 PO.

Há uma ressalva: preços a partir de 100 PO passam a contar em PL (1 PL = 10 PO). Nesse caso, um valor secundário em PO continua sendo mostrado até 20 PL. Acima disso, o preço aparece só em PL, arredondando para cima. Por exemplos:

- 103 PO, 4 PP e 3 PC → 104 PO → 10 PL e 4 PO.
- 203 PO e 4 PP → 204 PO → 20 PL e 4 PO.
- 204 PO, 9 PP e 1 PC → 205 PO → 20 PL e 5 PO.

Como o arredondamento é para cima, somar os preços exibidos pode passar um pouco do valor exato, e as colunas de pt continuam sendo a referência.

|pt|PC|Moedas|
|---|---|---|
|1|19|1 PP e 9 PC|
|2|38|3 PP e 8 PC|
|5|95|9 PP e 5 PC|
|10|190|19 PP|
|20|380|38 PP|
|50|950|10 PO|
|100|1900|19 PO|

## 2. Valores usados (pt por Encontro)

|Efeito|pt por Encontro|Origem|
|---|---|---|
|Acertos por Encontro|7,8|1,95 acertos por Rodada × 4 Rodadas|
|+1 de BA em Ataques|57,7|`Custo de PHs.md`, Tabela 1|
|+1 de BD|7,8|`Custo de PHs.md`, Tabela 1|
|+1 de CA|57,7|`Custo de PHs.md`, Tabela 1|
|+1 de Resistência (todo dano)|18,9|`Custo de PHs.md`, Tabela 1|
|+1 de Resistência a Dano Físico (70% do dano)|13,2|Resistência × 0,70|
|+1 de Resistência a Dano Físico e Mágico (95% do dano)|18,0|Resistência × 0,95|
|+1,5 m de alcance corpo a corpo|25,0|`Custo de PHs.md`, Tabela 1|
|+1,5 m de alcance de Ataque à distância|6,3|`Custo de PHs.md`, Tabela 1 (alcance de Ataque Mágico)|
|+1,5 m de Deslocamento|20,8|`Custo de PHs.md`, Tabela 1|
|1 PA fora do plano do build|19,6|`Custos de Mana.md`, §9|

## 3. Valor das Armas

### 3.1 Grau

O dano de um Grau vale a média do dado vezes 7,8 acertos por Encontro. É o preço **bruto**, antes de descontos. Esses valores não mudaram, pois dependem só do dado.

|Grau|Dado|Média|pt|Preço|Diferença para o Grau anterior|
|---|---|---|---|---|---|
|1|1d4|2,5|19,5|37 PP|-|
|2|1d6|3,5|27,3|51 PP e 9 PC|14 PP e 8 PC|
|3|1d8|4,5|35,1|66 PP e 7 PC|14 PP e 8 PC|
|4|1d10|5,5|42,9|81 PP e 5 PC|14 PP e 8 PC|
|5|1d12|6,5|50,7|10 PO|14 PP e 8 PC|
|6|2d6|7,0|54,6|11 PO|7 PP e 4 PC|
|7|2d8|9,0|70,2|14 PO|29 PP e 6 PC|
|8|2d10|11,0|85,8|17 PO|29 PP e 6 PC|
|9|2d12|13,0|101,4|20 PO|29 PP e 6 PC|
|10|3d10|16,5|128,7|25 PO|51 PP e 9 PC|

**Cada +1 de média de dano vale 7,8 pt, ou 14 PP e 8 PC.** Isso é útil para o Capítulo 4.9: nas Pedras de Aprimoramento, as subidas com "ganho por pedra" igual a 1 (Graus 1 a 5 e 6→7) valem esse preço por Pedra. Já 5→6, 7→8, 8→9 e 9→10 rendem menos de 1 de média por Pedra, então, com preço fixo por Pedra, ficam mais caras do que o valor que entregam.

### 3.2 Escalas de Arma

Uma Arma tem até duas Escalas (Capítulo 4.2). Cada Escala concede, a cada valor par do Atributo até o 10, **+1 de BA e um BD igual à letra** (D = 1, C = 2, B = 3, A = 4, S = 5). Um passo de uma Escala vale então **57,7 pt (BA) mais 7,8 pt por ponto de BD da letra**. O BA domina o valor: uma Escala S vale só ≈ 48% a mais por passo que uma Escala D.

Quantos passos o dono da Arma realmente usa depende do Atributo dele. Foi adotado um **valor efetivo de 8 no Atributo da primeira Escala** (4 passos), a média entre um build alinhado (10) e um desalinhado (6), e **de 6 na segunda** (3 passos), a média entre um build alinhado (8) e um desalinhado (4). Isso equivale aos Modificadores efetivos de +4 e +3 do rascunho anterior. A Escala de maior letra conta como a primeira.

|Escala|pt por passo (+1 de BA e BD da letra)|1ª Escala (4 passos): pt|Preço|2ª Escala (3 passos): pt|Preço|
|---|---|---|---|---|---|
|D|65,5|262,0|50 PO|196,5|38 PO|
|C|73,3|293,2|56 PO|219,9|42 PO|
|B|81,1|324,4|62 PO|243,3|47 PO|
|A|88,9|355,6|68 PO|266,7|51 PO|
|S|96,7|386,8|74 PO|290,1|56 PO|

**Preço bruto de uma Arma = preço do Grau + preço das Escalas + alcance (§3.3) + efeitos adicionais (§8).** Em Armas à Distância que recarregam, o preço do Grau é multiplicado antes pelo fator de recarga (§8.2).

Para o Capítulo 4.9, subir uma letra de uma Escala é uma melhoria de +1 de BD por passo (as Escalas de Arma não mudam o BA ao subir de letra):

|Melhoria (Capítulo 4.9)|1ª Escala (pt)|Preço|2ª Escala (pt)|Preço|
|---|---|---|---|---|
|Subir uma letra em Escala de Arma|31,2|59 PP e 3 PC|23,4|44 PP e 5 PC|
|Subir uma letra em Escala de Armadura|52,9|11 PO|39,7|75 PP e 4 PC|

Empunhar uma Arma em duas mãos (Força dobrada, com Força excedente somando ao BD) e usar duas Armas ao mesmo tempo **não têm preço**: são escolhas de quem empunha, e custam a outra mão. Já Armas sem Escalas (Bestas e Armas de Fogo) simplesmente não somam o valor das Escalas, então ficam mais baratas.

### 3.3 Alcance

**Corpo a corpo**: cada +1,5 m acima do padrão de 1,5 m vale **25,0 pt, ou 47 PP e 5 PC**. O valor é linear.

|Alcance adicional|pt|Preço|
|---|---|---|
|+1.5 m|25,0|47 PP e 5 PC|
|+3 m|50,0|10 PO|
|+4.5 m|75,0|15 PO|
|+6 m|100,0|19 PO|

**À distância**: o alcance base é de **9 m**, e só o que passa disso é cobrado. Cada +1,5 m acima de 9 m vale **6,3 pt, ou 11 PP e 9 PC**. O alcance é cobrado **até 48 m (26 passos de 1,5 m acima de 9 m)**. O que passar disso é considerado bônus e não entra no preço.

|Alcance|pt|Preço|
|---|---|---|
|9 m ou menos|0,0|0|
|12 m|12,5|23 PP e 8 PC|
|18 m|37,5|71 PP e 2 PC|
|24 m|62,5|12 PO|
|30 m|87,5|17 PO|
|36 m|112,5|22 PO|
|42 m|137,5|27 PO|
|48 m|162,5|31 PO|
|48 m ou mais|162,5|31 PO|

## 4. Valor das Armaduras e dos Escudos

### 4.1 +1 de CA

Cada +1 de CA vale **57,7 pt, ou 11 PO**. O valor é linear. A tabela vale também para o Capítulo 4.9, já que as Pedras podem aumentar a CA.

|CA concedida|pt|Preço bruto|
|---|---|---|
|+1|57,7|11 PO|
|+2|115,4|22 PO|
|+3|173,1|33 PO|
|+4 (teto da Leve)|230,8|44 PO|
|+5|288,5|55 PO|
|+6 (teto da Média)|346,2|66 PO|
|+7|403,8|77 PO|
|+8 (teto da Pesada)|461,5|88 PO|
|+9|519,2|99 PO|
|+10|576,9|11 PL|

### 4.2 Escalas de Armadura

Uma Armadura (ou Roupa) tem até duas Escalas. Cada Escala concede, a cada valor par do Atributo até o 10, **+1 de CA e Resistência a Dano Físico igual à letra**. Foi assumido que **70%** do dano recebido é Dano Físico, então +1 de Resistência a Dano Físico vale 13,2 pt. Os passos efetivos são os mesmos da §3.2: 4 na primeira Escala e 3 na segunda.

|Escala|pt por passo (+1 de CA e Resistência da letra)|1ª Escala (4 passos): pt|Preço|2ª Escala (3 passos): pt|Preço|
|---|---|---|---|---|---|
|D|70,9|283,7|54 PO|212,8|41 PO|
|C|84,1|336,6|64 PO|252,4|48 PO|
|B|97,4|389,5|75 PO|292,1|56 PO|
|A|110,6|442,4|85 PO|331,8|64 PO|
|S|123,8|495,3|95 PO|371,5|71 PO|

### 4.3 Escudos

Um Escudo concede **Resistência a Dano Físico e Mágico** (Capítulo 4.3). Foi assumido que **70%** do dano é Físico, **25%** é Mágico e **5%** é Ácido ou Venenoso, então o Escudo cobre 95% do dano. Cada +1 de Resistência vale **18,0 pt, ou 34 PP e 1 PC**.

|Resistência|pt|Preço bruto|
|---|---|---|
|+1|18,0|34 PP e 1 PC|
|+2|35,9|68 PP e 2 PC|
|+3|53,9|11 PO|
|+4|71,8|14 PO|
|+5|89,8|18 PO|
|+6|107,7|21 PO|
|+7|125,7|24 PO|
|+8|143,6|28 PO|
|+9|161,6|31 PO|
|+10|179,5|35 PO|

Cada Escudo traz uma Habilidade. Os valores abaixo são estimativas. Aparar anula um acerto em ≈ 23% dos casos (-3 de BA sobre os 13 resultados que acertam), e um acerto vale ≈ 39,7 de dano. Golpe de Escudo custa uma Ação e rende o dano mais o -3 de BA do alvo por um Turno, com 65% de falha na Salvaguarda. Parede de Escudo rende +1 de Resistência na próxima instância.

|Habilidade de Escudo|pt|Preço|
|---|---|---|
|Aparar (1 uso por Encontro)|88,8|17 PO|
|Golpe de Escudo (1 uso por alvo, já descontada a Ação)|56,2|11 PO|
|Parede de Escudo|6,8|12 PP e 9 PC|

O Escudo também ocupa uma das mãos, o que não foi descontado.

## 5. Descontos

Os descontos são **subtraídos** do preço bruto, em pt (e depois convertidos).

### 5.1 Requisitos

Os requisitos são valores de Atributo. Eles usam o mesmo cálculo de `Custo de PHs.md` §4.1: o requisito é o custo de oportunidade dos PAs que o PDJ precisa gastar naquele Atributo, e esse custo vira desconto. Cada PA forçado vale 19,6 pt.

**Um requisito**

|Valor do requisito|Desconto (pt)|Desconto|**+1 de requisito** (pt)|**+1 de requisito**|
|---|---|---|---|---|
|1|2,8|5 PP e 3 PC|2,8|5 PP e 3 PC|
|2|5,6|10 PP e 7 PC|2,8|5 PP e 3 PC|
|3|9,8|18 PP e 7 PC|4,2|8 PP|
|4|14,0|26 PP e 7 PC|4,2|8 PP|
|5|19,6|37 PP e 3 PC|5,6|10 PP e 7 PC|
|6|25,3|48 PP|5,6|10 PP e 7 PC|
|7|32,3|61 PP e 3 PC|7,0|13 PP e 3 PC|
|8|39,3|74 PP e 7 PC|7,0|13 PP e 3 PC|
|9|47,7|10 PO|8,4|16 PP|
|10|56,1|11 PO|8,4|16 PP|

Na média, **+1 de requisito vale 5,9 pt, ou 11 PP e 3 PC**. O primeiro ponto vale pouco, e o último, bastante.

**Vários requisitos (cada um é um Atributo diferente)**: some o desconto de cada requisito na tabela acima e acrescente **9,8 pt (18 PP e 7 PC) por PA de déficit**. O déficit compara os requisitos, do maior para o menor, com o build típico de 30 PAs (10, 8, 6, 4, 2, 0, 0), e é a soma de `max(0, requisito − valor do build)`.

|Requisitos|Desconto (pt)|Desconto|
|---|---|---|
|3 e 1|12,6|24 PP|
|4 e 4|28,1|53 PP e 3 PC|
|5 e 5|39,3|74 PP e 7 PC|
|6 e 6|50,5|10 PO|
|8 e 8|78,6|15 PO|
|10 e 10|131,9|26 PO|
|5 e 5 e 5|58,9|12 PO|
|8 e 8 e 8|137,5|27 PO|

### 5.2 Peso

Cada unidade de Peso ocupa a Capacidade de Carga (10 + For × NV). Como +1 de Modificador de For dá +NV de Capacidade e custa 2 PAs, no **Nível 10** (meio da campanha) 1 Peso equivale a 0,2 PA, ou **3,9 pt**.

**Cada unidade de Peso desconta 3,9 pt, ou 7 PP e 5 PC.**

|Peso|Desconto (pt)|Desconto|
|---|---|---|
|1|3,9|7 PP e 5 PC|
|2|7,9|14 PP e 9 PC|
|3|11,8|22 PP e 4 PC|
|4|15,7|29 PP e 9 PC|
|5|19,6|37 PP e 3 PC|
|10|39,3|74 PP e 7 PC|
|15|58,9|12 PO|
|20|78,6|15 PO|

### 5.3 Penalidades

**Desvantagem em Furtividade** (Armaduras Médias e Pesadas): uma Desvantagem equivale a ≈ -3,3 no Teste. Foi assumido um Teste de Furtividade por Encontro (o esconder inicial). Cada ponto de BA em Perícia vale 3,1 pt por uso (5 pontos percentuais de uma Ação), então 3,3 × 3,1 = 10,3 pt.

**Desconto: 10,3 pt, ou 19 PP e 6 PC.**

**Penalidade de Deslocamento** (Armaduras Pesadas): -1,5 m de Deslocamento é o oposto de +1,5 m, que vale 20,8 pt por Encontro.

**Desconto: 20,8 pt, ou 39 PP e 6 PC, a cada -1,5 m.** O valor é linear.

|Penalidade|Desconto (pt)|Desconto|
|---|---|---|
|-1.5 m|20,8|39 PP e 6 PC|
|-3 m|41,7|79 PP e 2 PC|
|-4.5 m|62,5|12 PO|
|-6 m|83,3|16 PO|

## 6. Preço final

**Preço = preço bruto − Peso − requisitos − penalidades**

Para impedir preços muito baixos ou negativos, o preço final **nunca fica abaixo de 25% do preço bruto**.

## 7. Exemplos

|Item|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Espada Longa|549,7|17,4|532,3|10 PL e 2 PO|
|Katana|524,7|20,2|504,5|96 PO|
|Claymore|563,7|53,0|510,7|98 PO|
|Lâmina Gêmea|685,3|29,5|655,9|12 PL e 5 PO|
|Arco Longo Composto|635,6|23,0|612,6|11 PL e 7 PO|
|Besta Pesada|134,0|15,7|118,2|23 PO|
|Couro Fervido|514,4|29,5|485,0|93 PO|
|Brigantina|895,5|49,3|846,2|16 PL e 1 PO|
|Armadura Gótica Completa de Placas|1050,6|88,1|962,4|18 PL e 3 PO|
|Broquel|106,7|6,7|100,0|19 PO|
|Escudo Torre de Ferro|78,6|51,9|26,7|50 PP e 7 PC|

O conjunto de calibração, uma Arma de Grau 4 com uma Escala D (requisito 3 de For, Peso 3, 283,3 pt) e uma Armadura Leve de +4 de CA com Escala D (requisito 3 de Des, Peso 5, 485,0 pt), soma **768,2 pt, ou 146 PO**, dentro dos 150 PO iniciais.

## 8. Efeitos adicionais

### 8.1 Dano adicional igual à metade do dano do Ataque

O adicional é calculado **depois de todos os cálculos** do dano, então vale 50% do dano por acerto. No cenário típico do Nível 20, o dano por acerto é ≈ 96,2 (`Custos de Mana.md` §2), ou seja, o adicional é de ≈ 48,1 por acerto. Como a Lâmina Gêmea diz que o adicional leva Ataques Críticos em consideração, ele também é ampliado pelo crítico, o que soma ≈ 7,7%.

**pt = 0,5 × dano por acerto × 7,8 acertos por Encontro × 1,077 = 403,9 pt (77 PO).**

O preço usa o dano típico do Nível 20, e não o da própria Lâmina Gêmea (Grau 1 e Escala D), porque o dano dela cresce com o Aprimoramento. Por isso, ela é a Arma mais cara da lista. Se o efeito não vale em todo acerto, use as frequências de `Custo de PHs.md` §2.1: uma vez por Rodada (×4), só em Ataque Crítico (×0,2) ou uma vez por Encontro (×1).

Alerta: o efeito sempre ligado custa mais que uma Escala C inteira e escala com o dano do PDJ, ampliando todos os outros bônus. Vale limitar a frequência.

### 8.2 Recarregar a cada X tiros

**Valor real.** Um Encontro tem 12 Ações (3 por Rodada × 4). Recarregar custa uma Ação, e a Arma começa carregada. Os tiros que cabem em um Encontro são **13X ÷ (X + 1)**, com máximo de 12. Uma Besta (X = 1) dispara ≈ 6,5 vezes (54% do máximo), e uma Arma que não recarrega em um Encontro (X ≥ 12, como os Arcos) dispara 12.

**Fator de recarga.** O preço do Grau é multiplicado por:

**f(X) = 0,5 + 0,5 × ((X − 1) ÷ 11)^1,5**, com f = 1 para X ≥ 12.

Os extremos vêm do valor real (Besta ≈ 50%, sem recarga = 100%). O expoente 1,5 faz o preço **subir mais a cada tiro adicional**. Para um aumento mais suave, use o expoente 1 (linear). Para um mais íngreme, 2.

|X (tiros por recarga)|Fator|Preço do Grau 5|
|---|---|---|
|1 (Besta)|0,500|48 PP e 2 PC|
|2|0,514|49 PP e 5 PC|
|3|0,539|51 PP e 9 PC|
|4|0,571|55 PP|
|5|0,610|58 PP e 7 PC|
|6|0,653|62 PP e 9 PC|
|7|0,701|67 PP e 6 PC|
|8|0,754|72 PP e 6 PC|
|9|0,810|78 PP|
|10|0,870|83 PP e 8 PC|
|11|0,933|89 PP e 9 PC|
|12 ou mais (Arco)|1,000|10 PO|

- O fator vale só para o preço do **Grau**. Alcance, Escalas e requisitos seguem as outras seções.
- Com duas Armas à Distância ao mesmo tempo, cada Ataque gasta um tiro de cada Arma, então X conta Ataques.
- **Conflito com o valor real:** pelo cálculo de Ações, os primeiros tiros valem mais que os últimos (X = 2 já chegaria a 0,72, e X = 10 a 0,98). A curva crescente é uma escolha de design, e não sai da economia de Ações.

### 8.3 Ganhar PVs ou PMs Temporários

Foi considerado "ganhar PVs ou PMs Temporários do Grau indicado", recebidos pelo item e válidos até o fim do Encontro. Para efeitos de **uma vez por Descanso Longo**, multiplique o preço por **0,25** (4 Encontros por dia, `Balanceamento.md`). Os valores saem de `Custos de Mana.md` §5.3 (PV Temporário com o fator 9,7 de cura e PM Temporário a 3,125 pt por PM). A diferença entre duas linhas seguidas é o preço de **aumentar em +1 Grau** um efeito que já existe.

|Grau|PV Temp. (uma vez por Encontro)|PM Temp. (uma vez por Encontro)|PV Temp. (por Rodada, dura 1 Rodada)|PM Temp. (por Rodada, dura 1 Rodada)|
|---|---|---|---|---|
|1 (1d4)|45 PP e 3 PC|14 PP e 5 PC|17 PO|48 PP e 6 PC|
|2 (1d6)|63 PP|20 PP|22 PO|63 PP|
|3 (1d8)|80 PP e 5 PC|25 PP e 5 PC|27 PO|75 PP e 2 PC|
|4 (1d10)|10 PO|30 PP e 9 PC|31 PO|85 PP e 5 PC|
|5 (1d12)|12 PO|36 PP e 1 PC|35 PO|10 PO|
|6 (2d6)|13 PO|38 PP e 7 PC|37 PO|10 PO|
|7 (2d8)|16 PO|48 PP e 7 PC|44 PO|12 PO|
|8 (2d10)|19 PO|58 PP e 4 PC|49 PO|12 PO|
|9 (2d12)|23 PO|67 PP e 6 PC|53 PO|13 PO|
|10 (3d10)|28 PO|82 PP e 9 PC|59 PO|14 PO|

O PV Temporário vale ≈ 3× o PM Temporário do mesmo Grau. A Túnica de Mago (Grau 1 de PMs Temporários por Descanso) usa essa tabela com o fator 0,25.

### 8.4 Aumentar em 1 o Grau de um tipo de Ataque

O ganho é a diferença de média entre os dois Graus vezes 7,8 acertos por Encontro. É a mesma diferença da tabela do §3.1. Em seguida aplica-se um **fator de uso**, porque o aumento só vale para os Ataques daquele tipo (`Custo de PHs.md` §2.1):

- **×0,8**: o tipo é o Ataque principal do build (Armas Leves, Comuns, de Empunhadura Dupla ou à Distância).
- **×0,4**: o tipo é secundário ou situacional (Ataques Desarmados, Arremessar). A Túnica de Monge usa esse fator.

|Grau inicial → final|Ganho de média|pt (100%)|Preço (100%)|Preço ×0,8|Preço ×0,4|
|---|---|---|---|---|---|
|1 → 2|+1,0|7,8|14 PP e 8 PC|11 PP e 9 PC|5 PP e 9 PC|
|2 → 3|+1,0|7,8|14 PP e 8 PC|11 PP e 9 PC|5 PP e 9 PC|
|3 → 4|+1,0|7,8|14 PP e 8 PC|11 PP e 9 PC|5 PP e 9 PC|
|4 → 5|+1,0|7,8|14 PP e 8 PC|11 PP e 9 PC|5 PP e 9 PC|
|5 → 6|+0,5|3,9|7 PP e 4 PC|5 PP e 9 PC|3 PP|
|6 → 7|+2,0|15,6|29 PP e 6 PC|23 PP e 7 PC|11 PP e 9 PC|
|7 → 8|+2,0|15,6|29 PP e 6 PC|23 PP e 7 PC|11 PP e 9 PC|
|8 → 9|+2,0|15,6|29 PP e 6 PC|23 PP e 7 PC|11 PP e 9 PC|
|9 → 10|+3,5|27,3|51 PP e 9 PC|41 PP e 5 PC|20 PP e 7 PC|

O Grau não passa de 10 (Capítulo 1.5), então não há preço a partir do Grau 10.

## 9. Preços das listas atuais

Os preços saem das fórmulas acima, com Escalas de passos efetivos 4 e 3 e a conversão de 1 pt = 19 PC. Os Pesos, requisitos e penalidades são os das listas dos Capítulos 4.1 a 4.3.

### 9.1 Armas Corpo a Corpo

|Arma|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Manopla de Ferro|281,5|9,5|271,9|52 PO|
|Soco Inglês|281,5|6,7|274,7|53 PO|
|Katar|281,5|6,7|274,7|53 PO|
|Adaga|281,5|3,9|277,5|53 PO|
|Espada Curta|485,7|13,5|472,3|90 PO|
|Clava|289,3|10,7|278,6|53 PO|
|Cajado|281,5|3,9|277,5|53 PO|
|Rapieira|289,3|9,5|279,7|54 PO|
|Maça|297,1|17,4|279,7|54 PO|
|Maça-Estrela|297,1|17,4|279,7|54 PO|
|Chicote|328,3|10,7|317,6|61 PO|
|Cimitarra|297,1|13,5|283,6|54 PO|
|Espada Longa|549,7|17,4|532,3|10 PL e 2 PO|
|Machado de Batalha|328,3|25,5|302,7|58 PO|
|Katana|524,7|20,2|504,5|96 PO|
|Lança|378,3|21,6|356,7|68 PO|
|Alabarda|361,1|33,7|327,4|63 PO|
|Glaive|361,1|25,5|335,5|64 PO|
|Clava Pesada|304,9|45,5|259,4|50 PO|
|Clava Imensa|343,9|58,9|284,9|55 PO|
|Claymore|563,7|53,0|510,7|98 PO|
|Espada Colossal|368,9|64,6|304,3|58 PO|
|Lança de Cavalaria|393,9|37,6|356,3|68 PO|
|Martelo de Guerra|343,9|47,2|296,7|57 PO|
|Lâmina Gêmea|685,3|29,5|655,9|12 PL e 5 PO|

### 9.2 Armas à Distância

|Arma|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Arco Curto|319,0|6,7|312,2|60 PO|
|Arco Curto Composto|383,0|13,5|369,5|71 PO|
|Arco Longo|548,2|13,5|534,8|10 PL e 2 PO|
|Arco Longo Composto|635,6|23,0|612,6|11 PL e 7 PO|
|Besta Leve|84,0|7,9|76,1|15 PO|
|Besta Pesada|134,0|15,7|118,2|23 PO|
|Pistola|106,6|17,7|88,9|17 PO|
|Escopeta|65,5|35,4|30,2|57 PP e 3 PC|
|Canhão de Mão|47,6|74,4|11,9|22 PP e 6 PC|
|Rifle de Precisão|205,4|70,5|134,9|26 PO|

### 9.3 Armaduras

|Armadura|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Armadura de Tecido Acolchoado|341,4|11,8|329,6|63 PO|
|Gambeson|611,8|21,3|590,5|11 PL e 3 PO|
|Couro Curtido|399,1|21,3|377,7|72 PO|
|Armadura de Peles|456,8|25,3|431,5|82 PO|
|Couro Fervido|514,4|29,5|485,0|93 PO|
|Cota de Anéis|784,9|38,4|746,5|14 PL e 2 PO|
|Cota de Malha|837,8|42,6|795,2|15 PL e 2 PO|
|Armadura Lamelar|877,5|45,1|832,4|15 PL e 9 PO|
|Brigantina|895,5|49,3|846,2|16 PL e 1 PO|
|Armadura Parcial de Placas|895,5|53,3|842,2|16 PL e 1 PO|
|Armadura de Tiras|900,3|64,3|836,0|15 PL e 9 PO|
|Peitoral de Aço|992,9|68,5|924,4|17 PL e 6 PO|
|Armadura Completa de Placas|953,2|72,4|880,8|16 PL e 8 PO|
|Armadura Completa de Aço|1010,9|101,1|909,8|17 PL e 3 PO|
|Armadura Gótica Completa de Placas|1050,6|88,1|962,4|18 PL e 3 PO|

### 9.4 Roupas

A Roupa Comum custa 1 PC. As Roupas com Escalas valem como uma Armadura de +0 de CA, sem BP.

|Roupa|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|
|Túnica de Mago|285,6|2,8|282,8|54 PO|
|Túnica de Monge|286,8|2,8|284,0|54 PO|

### 9.5 Escudos

|Escudo|Habilidade|Preço bruto (pt)|Descontos (pt)|Preço (pt)|Preço|
|---|---|---|---|---|---|
|Broquel|Aparar|106,7|6,7|100,0|19 PO|
|Targe|Aparar|106,7|6,7|100,0|19 PO|
|Hoplon|Golpe de Escudo|92,1|17,4|74,7|15 PO|
|Escudo Gota|Golpe de Escudo|92,1|17,4|74,7|15 PO|
|Scutum|Parede de Escudo|60,6|39,9|20,8|39 PP e 5 PC|
|Escudo Torre de Ferro|Parede de Escudo|78,6|51,9|26,7|50 PP e 7 PC|

### 9.6 Munições

As Munições mantêm o preço da lista (10 Flechas, 10 Virotes e 10 Balas por 1 PP cada).

## 10. Observações e pontos em aberto

1. **Todos os valores partem do Nível 20.** +1 de BA e +1 de CA valem proporcionalmente menos nos Níveis baixos (`Custos de Mana.md` §6), então Armaduras são relativamente caras no começo. O preço não varia com o Nível, e o equipamento inicial é o que sustenta a calibração.
2. **Escalas de letra S, A e B não existem nas listas.** As Armas e Armaduras listadas só têm Escalas C e D. As letras maiores vêm do Aprimoramento (Capítulo 4.9), e os 75 de BD do `Balanceamento.md` dependem delas.
3. **Valor efetivo dos Atributos das Escalas (8 e 6).** Se preferir cobrar mais da primeira Escala, suba o valor efetivo. Com 10 nas duas, uma Espada Longa já custaria bem mais.
4. **O Ataque Desarmado não foi usado como base.** O Capítulo 1.6 só diz que ele é Dano de Impacto de Grau 1. Se ele somar o Modificador de For ou Des no BA e no BD, a primeira Escala D de uma Arma deixaria de ser uma vantagem e poderia ser gratuita, como no rascunho anterior.
5. **Escudo:** 70% do dano como Físico, 25% como Mágico e a estimativa das Habilidades são premissas. Ocupar uma das mãos (perder o Ataque com duas Armas) não foi descontado.
6. **Peso:** usa o Nível 10 como referência. Nos Níveis baixos a Capacidade de Carga aperta mais e o Peso valeria mais.
7. **Alcance à distância** usa o valor de alcance de Ataque Mágico (baixa confiança). O alcance base é de 9 m, e só o que passa disso é cobrado.
8. **Furtividade:** conta só o uso em combate. O valor em exploração não foi incluído.
9. **Piso de 25%** do preço bruto é um chute informado, para não zerar o preço de itens com muitos requisitos.
10. **Bestas e Armas de Fogo não têm Escalas**, então o BA delas é só o BP mais Habilidades, e o BD é só o Grau. O preço baixo reflete isso. Elas só competem com Armas de Escala por meio de Habilidades (Arquétipo Bucaneiro).
11. **Armaduras valem muito mais que Armas de Grau.** Um passo de Escala vale 57,7 pt de CA, e uma Armadura Pesada chega a ≈ 183 PO. Isso vem do teto de CA mais alto (ver `Balanceamento.md`).
12. **Escudos pesados caem no piso de 25%.** O Scutum e o Escudo Torre de Ferro têm muito Peso e requisito, então os descontos passam do preço bruto e o piso vale. Vale aumentar o valor da Parede de Escudo ou reduzir o desconto de Peso para Escudos.
13. **Lâmina Gêmea** é um valor fora da curva (§8.1) e merece revisão do efeito ou do preço.
14. **Ainda sem preço:** a Margem de Ameaça das Armas Comuns e os Itens Consumíveis.