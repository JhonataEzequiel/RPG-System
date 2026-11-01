Rascunho de balanceamento. O foco são os números do NV 20, mais uma maneira de extrapolá-los para outros Níveis e para Monstros. Tudo aqui precisa ser validado em playtest.

BA: Bônus de Acerto BP: Bônus de Proficiência Modificador (Mod): valor do Atributo dividido por dois, arredondado para baixo Habilidades: bônus concedido por Habilidades DPR: dano por Rodada esperado, já contando a chance de acerto

## Premissas e parâmetros

O objetivo é que 1 Monstro de NV X seja um desafio mediano para um grupo de 4 PDJs de NV X. Ele deve sobreviver a 4 Rodadas de combate, e deve acabar com cerca de 20% dos recursos do grupo em um Encontro. Serão 4 Encontros em média antes de um Descanso. Descansos curtos podem deixar os Encontros seguintes mais difíceis, e ficam a critério do Mestre.

Os balanceamentos são pensados para os PVs e PMs **medianos**, sem a Habilidade de PVs.

|Parâmetro|Valor|Faixa de ajuste|
|---|---|---|
|Grupo de referência|4 PDJs: 2 focados em dano e 2 não focados||
|P: dano do Monstro por Rodada, em % dos PVs do grupo|10%|7% a 15%|
|E: eficiência do grupo (parte do dano máximo que ele realmente causa)|100%|70% a 100%|
|Duração de um Encontro|4 Rodadas||
|Chance de acerto de PDJs e Monstros, quando equilibrados|65%||

Se os Monstros ficarem fracos em playtest, aumente P para 15%. Se ficarem fortes demais, diminua para 7%. Se os Encontros durarem mais de 4 Rodadas, diminua E.

## PDJs no NV 20

### PVs e PMs

O Dado de Vida e o Dado de Mana são escolhidos na criação (Capítulo 2), e vão de d4 a d12. A média do dado é arredondada para cima: d4 = 3, d6 = 4, d8 = 5, d10 = 6, d12 = 7. Um Modificador negativo não é somado. O Modificador de Constituição (ou de Sabedoria) vale para todos os Níveis, inclusive os anteriores.

**PVs Máximos = Maior valor do Dado de Vida + (NV - 1) × Média do Dado + NV × Mod de Con** **PMs Máximos = Maior valor do Dado de Mana + (NV - 1) × Média do Dado + NV × Mod de Sab**

PVs (ou PMs) no NV 20, por dado e por Modificador (Atributo 0-1 = +0, 2-3 = +1, 4-5 = +2, 6-7 = +3, 8-9 = +4, 10 = +5):

|Dado|+0|+1|+2|+3|+4|+5|
|---|---|---|---|---|---|---|
|d4|61|81|101|121|141|161|
|d6|82|102|122|142|162|182|
|d8|103|123|143|163|183|203|
|d10|124|144|164|184|204|224|
|d12|145|165|185|205|225|245|

||Menor|Mediano|Maior|
|---|---|---|---|
|PVs, sem a Habilidade de PVs|61|**153**|245|
|PVs, com a Habilidade de PVs|63|168|273|
|PMs|61|**153**|245|

A mediana é a das 30 combinações de dado e Modificador, e equivale a um d8 com Modificador +2.5.

Faixas esperadas:

- **Marcial:** 150 a 200 PVs e 100 a 110 PMs. Exemplo: d8 com Con 8 ou 9 (183 PVs) e d8 com Sab 0 ou 1 (103 PMs).
- **Conjurador:** cerca de 230 PMs e 100 a 150 PVs. Exemplo: d12 com Sab 8 a 10 (225 a 245 PMs) e d6 com Con 4 a 7 (122 a 142 PVs).

**Habilidade de PVs (a única, e fraca):** em cada Nível, você rola o Dado de Vida duas vezes e escolhe o maior. Em relação a quem escolhe a média, ela rende no NV 20 cerca de +2 PVs (d4), +9 (d6), +15 (d8), +22 (d10) e +28 (d12). Não existem Habilidades que aumentem os PMs Máximos.

### CA e BA

**CA = 10 + Mod (For ou Des) + BP + Armadura + Habilidades**

A Armadura concede de +4 a +10 de CA, e usaremos +8 como referência. O limite de Habilidades na CA é +3. Para um jogador médio:

**CA = 10 + 5 + 6 + 8 + 3 = 32**

**BA = BP + Modificadores + Habilidades**

Uma Arma pode ser melhorada para somar um segundo Atributo ao bônus (limite de 2), então um marcial soma até dois Modificadores. O limite de Habilidades no BA de Ataques é +8.

**BA = 6 + 10 + 8 = 24**

Conjuradores têm a mesma conta com uma Habilidade de custo 2: "Caso uma Magia use apenas um Modificador como bônus no BA, você poderá utilizar também seu Modificador de Sabedoria". Assim, BA = 6 + Arc 5 + Sab 5 + 8 = 24.

Contra uma CA 32, um BA 24 precisa de 8 ou mais no d20, ou seja, **65% de acerto**. O inverso vale para os Monstros: um BA 24 contra uma CA 32 de PDJ também acerta 65%.

### Dano

O dado de dano é definido pelo Grau de Dano (Capítulo 1.6). Armas e Magias de dano têm um Grau, e Habilidades podem aumentá-lo, até o limite de 10.

| Grau de Dano | Dado de Dano | Média |
| ------------ | ------------ | ----- |
| 1            | 1d4          | 2.5   |
| 2            | 1d6          | 3.5   |
| 3            | 1d8          | 4.5   |
| 4            | 1d10         | 5.5   |
| 5            | 1d12         | 6.5   |
| 6            | 2d6          | 7     |
| 7            | 2d8          | 9     |
| 8            | 2d10         | 11    |
| 9            | 2d12         | 13    |
| 10           | 3d10         | 16.5  |

**Dano = Dado de Dano + Modificadores + Habilidades**

Um exemplo de como uma Arma seria descrita:

|Arma|Dano|Bônus|Requisitos|
|---|---|---|---|
|Espada Longa Suprema|Grau de Dano 10|Força, Destreza|10 de Força, 10 de Destreza|

No NV 20, um PDJ focado em dano usa uma Arma de Grau 9, soma dois Modificadores (+10) e tem cerca de +7 de dano vindo de Habilidades, sobretudo as que aumentam o Grau:

||Mínimo|Médio|Máximo|
|---|---|---|---|
|Dano por acerto|19|**30**|41|

- **Por Ataque, a 65% de acerto:** 30 × 0.65 = 19.5.
- **Por Rodada, com 3 Ataques sem penalidade (as duas Habilidades de Ataque Extra):** 58.5.
- **PDJ não focado em dano:** cerca de 70% disso, ou 41 por Rodada.
- **Grupo de referência:** 2 × 58.5 + 2 × 41 = 199, ou cerca de **200 por Rodada**.

Armaduras concedem apenas CA. Resistências vêm de Magias, Habilidades e efeitos.

## Monstros de referência

**PVs do Monstro = 4 × Dano do grupo por Rodada × E**, ou 4 × 199 × 100% ≈ **800 PVs** no NV 20.

**Dano do Monstro por Rodada = P × PVs do grupo**. O grupo tem 4 × 153 = 612 PVs, então P = 10% dá **61 por Rodada** (43 com P = 7%, e 92 com P = 15%).

O DPR é dividido pelos acertos esperados na Rodada para chegar ao dano por acerto:

|Perfil de Ataque|Acertos esperados|Dano por acerto (P = 10%)|
|---|---|---|
|1 Ataque|0.65|94|
|2 Ataques (com Penalidade de Ataques)|0.65 + 0.40 = 1.05|58|
|3 Ataques (com Penalidade de Ataques)|0.65 + 0.40 + 0.15 = 1.20|51|
|3 Ataques sem penalidade (Multiataque)|3 × 0.65 = 1.95|31|

O BD do Monstro é livre: BD = dano por acerto - média do Grau de Dano. Prefira 2 ou 3 Ataques, pois um único acerto de 94 tira 61% dos PVs de um PDJ mediano.

Valores de referência por NV, que crescem de forma linear entre o NV 1 e o NV 20 (arredondados):

|NV|PVs|DPR (P = 10%)|CA|BA|Dano por acerto de um PDJ (H)|
|---|---|---|---|---|---|
|1|40|4|12|8|5|
|5|200|16|16|11|10|
|10|400|31|22|16|17|
|15|600|46|27|20|23|
|20|800|61|32|24|30|

**PVs de referência = 40 × NV** **DPR de referência = P × (12 + 30 × NV)** **CA de referência = 11 + 1.05 × NV** **BA de referência = 7 + 0.85 × NV** **H = 3.7 + 1.3 × NV**

## PVs dos Monstros

Os Monstros usam um Dado de Vida definido pelo Tamanho. O fator 4 representa o grupo de PDJs: um Monstro tem os PVs de 4 PDJs.

**PVs médios = 4 × NV × (Média do Dado do Tamanho + Mod de Con)**

A média do dado é arredondada para cima, e um Modificador de Constituição negativo não é somado. Cada ponto de Modificador de Constituição soma 4 × NV PVs.

|Tamanho|Dado de Vida|Média|PVs no NV 20, com Con 8 (+4)|Em relação ao Médio|
|---|---|---|---|---|
|Minúsculo|d4|3|560|0.7|
|Pequeno|d6|4|640|0.8|
|Médio|d10|6|**800**|1.0|
|Grande|2d8|9|1040|1.3|
|Enorme|2d12|13|1360|1.7|
|Colossal|3d10|17|1680|2.1|

Um Monstro Médio com Con 8 tem exatamente os 40 PVs por NV de referência. Se o Mestre quiser variância, pode rolar NV dados do Tamanho e usar **PVs = 4 × (soma dos dados + NV × Mod de Con)**.

**Compensação por Tamanho:** os PVs que sobram ou faltam são compensados por outros fatores, para que o NV continue o mesmo. Valores típicos, calculados com a fórmula de NV abaixo:

|Tamanho|Compensação sugerida|
|---|---|
|Minúsculo|CA +4|
|Pequeno|CA +3|
|Médio|nenhuma|
|Grande|CA -4, ou dano cerca de 30% menor|
|Enorme|CA -5 e dano cerca de 22% menor|
|Colossal|CA -5, Fraqueza e dano cerca de 38% menor|

Monstros menores também podem compensar com Resistências e Atributos de dano altos, e os maiores com Vulnerabilidades e dano baixo.

## NV de um Monstro

Cada característica vale **pontos**, e 1 ponto equivale a 1% de PVs efetivos, de dano efetivo ou de NV, conforme a tabela. As bases (PVs, CA, BA, H) dependem do NV, então escolha um NV alvo, calcule o NV real e ajuste até os dois coincidirem.

### Passo a passo

1. **PVs efetivos = PVs × (1 + D / 100) + 4 × Regeneração**, onde D é a soma dos pontos defensivos.
2. **DPR efetivo = DPR × (1 + O / 100)**, onde O é a soma dos pontos ofensivos. O DPR é a soma de (chance de acerto × dano por acerto) de todos os Ataques da Rodada.
3. **NV defensivo = PVs efetivos / 40**
4. **NV ofensivo = (DPR efetivo / P - 12) / 30**
5. **NV = [ NV defensivo + NV ofensivo ] / 2 × (1 + U / 100)**, arredondado para baixo, onde U é a soma dos pontos de utilidade (máximo 50).

**Chance de acerto dos Ataques:** 65% no primeiro Ataque, e -25 pontos percentuais para cada Ataque extra, a menos que o Monstro tenha Multiataque. Em Área, os acertos esperados são 0.65 × a quantidade de alvos atingidos (use 2 por padrão).

### Pontos defensivos (D)

**CA em relação à CA de referência do NV (ΔCA):**

|ΔCA|-5|-4|-3|-2|-1|0|+1|+2|+3|+4|+5|+6|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D|-28|-24|-19|-13|-7|0|+8|+18|+30|+44|+62|+86|

**Resistência e Fraqueza (valor fixo R ou F), por tipo de dano.** Cada tipo tem um peso w, que é a parte esperada do dano do grupo que vem dele:

|Tipo de dano|Peso w|
|---|---|
|Físico (Cortante + Perfurante + Impacto)|0.60 (0.20 cada)|
|Mágico (cada um dos 7 tipos)|0.05 (0.35 no total)|
|Ácido|0.02|
|Venenoso|0.03|

**Resistência: D = 100 × [ H / (H - w × R) - 1 ]** **Fraqueza: D = 100 × [ H / (H + w × F) - 1 ]** (resulta em um valor negativo)

Exemplos no NV 20 (H ≈ 30):

||R ou F = 5|R ou F = 10|R ou F = 15|R ou F = 20|
|---|---|---|---|---|
|Resistência a todo dano (w = 1)|+20|+51|+102|+206|
|Resistência a Físico (w = 0.6)|+11|+25|+43|+68|
|Resistência a um tipo Físico (w = 0.2)|+3|+7|+11|+16|
|Resistência a um tipo Mágico (w = 0.05)|+1|+2|+3|+3|
|Fraqueza a todo dano|-14|-25|-|-|
|Fraqueza a Físico|-9|-17|-|-|
|Fraqueza a um tipo Físico|-3|-6|-|-|

**Imunidade: D = 100 × [ 1 / (1 - w) - 1 ]**

|Imune a|Pontos|
|---|---|
|Cortante, Perfurante ou Impacto (cada)|+25|
|Todo dano Físico|+150|
|Um tipo Mágico (cada)|+5|
|Dano Elemental (Ígneo, Elétrico e Gélido)|+18|
|Todo dano Mágico|+54|
|Ácido|+2|
|Venenoso|+3|

**Outras características defensivas:**

|Característica|Pontos|
|---|---|
|Imunidade a uma Condição Negativa (máximo 12)|+2 cada|
|Deslocamento Aéreo (CA +3 contra Corpo-a-Corpo de quem não voa)|+10|
|Regeneração de R PVs por Rodada|+4 × R PVs efetivos (valor fixo, fora de D)|

### Pontos ofensivos (O)

|Característica|Pontos|
|---|---|
|BA acima ou abaixo da referência (ΔBA)|+8, +15, +23, +31, +38 para +1 a +5 (e os mesmos valores negativos)|
|Margem de Ameaça|+5 por ponto|
|Ataque à Distância|+5|
|Dano Contínuo, ou dano extra por efeito|converta em dano esperado e some ao DPR|

### Pontos de utilidade (U)

Controle de grupo, efeitos e outras características que não são dano nem PVs aumentam o NV final:

|Característica|Pontos|
|---|---|
|Controle leve (Agarrado, Caído, Amedrontado ou Debilitado), um alvo, com Salvaguarda|+3|
|Controle forte (Incapacitado, Encantado ou Petrificado), um alvo, com Salvaguarda|+10|
|Controle forte sem Salvaguarda|+20|
|Controle em área|dobra os pontos acima|
|Aura, Terreno Difícil ou dano ambiental|+3|
|Invocar ou duplicar aliados|+5 por criatura equivalente a 1/4 do NV|
|Curar ou fortalecer aliados|+5|
|Teleporte ou Intangibilidade|+5|
|Efeito ao morrer|+3|

## Exemplos no NV 20

|Monstro|Tamanho e Con|PVs|CA|BA|Ataques|PVs efetivos|NV defensivo|DPR efetivo|NV ofensivo|NV|
|---|---|---|---|---|---|---|---|---|---|---|
|Soldado (referência)|Médio, Con 8|800|32|24|2 Ataques de 58|800|20.0|61.2|20.0|**20**|
|Espreitador|Pequeno, Con 8|640|35|24|2 Ataques de 58|832|20.8|61.2|20.0|**20** (20.4)|
|Colosso|Colossal, Con 8|1680|27|24|1 Ataque de 59, Fraqueza 10 a Impacto|1109|27.7|38.1|12.3|**20**|
|Hipnotizador|Médio, Con 8|800|32|24|2 Ataques de 58, controle forte com Salvaguarda, imune a Amedrontado e Encantado|832|20.8|61.2|20.0|**22** (20.4 × 1.10)|

## Conteúdo descartado

- Escalas de Armas e de Armaduras, e as Resistências por Escala.
- Papéis de Tanque, DPS e Suporte. Os cálculos agora usam Marcial e Conjurador, com PVs e PMs medianos.
- Dado de Vida e de Mana definidos pela Constituição e pela Sabedoria. Eles agora são escolhidos na criação.
- Grau de Arma (agora Grau de Dano) com valores de até 4d12, e o orçamento de dano de Habilidades de 36.
- PVs de 750 a 850 para o Tanque, e a fórmula antiga de PVs por Nível.

## A validar

- A meta de 20% dos recursos por Encontro contra P = 10% por Rodada: em 4 Rodadas, o Monstro causaria até 40% dos PVs do grupo. Os PMs e as demais fontes de recurso entram na meta, mas isso precisa de playtest.
- A Armadura média de +8 foi escolhida para que a CA 32 e o BA 24 deem exatamente 65%. Com +10, a CA média seria 34 e o BA precisaria de 26.
- As bases por NV são uma interpolação linear entre o NV 1 e o NV 20, ainda não testada nos Níveis intermediários.
- Os pesos dos tipos de dano, os pontos de utilidade e os pontos de Condição são estimativas.
- Salvaguardas dos Monstros ainda não entram na fórmula.
- Proposta em aberto: atacar com duas Armas ao mesmo tempo custa 2 ou 3 Ações.
- A Habilidade de conjuradores só afeta o BA. As Magias em Área usam Salvaguarda, então talvez precisem de uma regra equivalente para a CD.