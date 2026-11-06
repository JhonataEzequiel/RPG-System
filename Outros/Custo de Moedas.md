Este documento calcula o **preço em moedas** de Armaduras, Armas e Escudos a partir dos pontos de `Custos de Mana.md` e `Custo de PHs.md`. Ele usa os mesmos valores por efeito (em pt por Encontro) e acrescenta o que muda no preço: requisitos, peso, penalidades e a frequência de recarga dos efeitos que dependem de Descanso.

## 1. Moeda e unidade

- **1 pt por Encontro = 5 PP = 0,5 PO.**
- **1 PH (18 pt) = 90 PP = 9 PO.** Um bônus que custa 1 PH numa Habilidade custa cerca de 9 PO num equipamento.
- **Moedas.** Preços são arredondados ao PP mais próximo, e sempre que chegar a 10 moedas, troca-se pela moeda seguinte (10 PP = 1 PO, 10 PO = 1 PL). **Preço mínimo de qualquer equipamento: 1 PO.**
- **Munição.** 10 munições de qualquer tipo (flechas, virotes ou balas) custam 1 PP, ou seja, 1 PC cada.
- **Escala.** Todos os preços são proporcionais à conversão de pt para PP. Para deixar tudo mais barato ou mais caro, basta mudar essa conversão. O Equipamento Inicial não é um número fixo, e a sugestão está na §8.

## 2. Como calcular

1. **Poder bruto (pt)**: some o valor de cada componente (seções 4, 5 e 6).
2. **Descontos em pt**: subtraia o desconto de requisitos (§3.1) e, nas Armaduras, o de penalidade de Deslocamento (§3.3). Juntos, eles nunca reduzem mais de **50%** do poder bruto.
3. **Desconto de peso**: multiplique o resultado por `1 − desconto de peso` (§3.2).
4. **Preço** = resultado em pt × 5 PP, arredondado ao PP, com mínimo de 1 PO.

## 3. Descontos

### 3.1 Requisitos de Atributo

Um equipamento pode exigir de 0 a 10 em até dois Atributos. O desconto usa a mesma tabela de `Custo de PHs.md` (§4.1), que mede o que o requisito custa ao personagem:

|Requisito|Desconto (pt)|Desconto em moedas|
|---|---|---|
|0|0,0|0|
|1|1,1|6 PP|
|2|2,3|1 PO 2 PP|
|3|3,9|2 PO|
|4|5,6|2 PO 8 PP|
|5|7,9|4 PO|
|6|10,1|5 PO|
|7|12,9|6 PO 4 PP|
|8|15,8|7 PO 9 PP|
|9|19,1|9 PO 6 PP|
|10|22,5|1 PL 1 PO 2 PP|

**Dois requisitos:** some o desconto de cada um e acrescente **4,0 pt por PA de déficit**. O déficit é a soma de `max(0, requisito − valor do build típico)`, comparando o maior requisito com 10 e o menor com 8. Na prática, só o segundo requisito acima de 8 gera déficit: 9 gera 1 PA, e 10 gera 2 PAs.

Exemplos: For 6 e Des 6 = 10,1 + 10,1 = 20,3 pt. For 10 e Des 10 = 22,5 + 22,5 + 2 × 3,96 = 52,9 pt.

### 3.2 Peso

**Cada unidade de Peso reduz o preço em `45% ÷ Capacidade de Carga típica`, até o máximo de 40%.** Uma unidade de Peso ocupa `1 ÷ Capacidade de Carga` da sua capacidade, e só cerca de 45% dela costuma ser aproveitada para outros usos. Com a fórmula atual (15 + For + Con) e um personagem típico (Capacidade de ≈ 22), isso dá **2% por unidade**.

Se a fórmula de Capacidade de Carga mudar, só a Capacidade típica precisa ser trocada:

|Capacidade de Carga típica|Desconto por unidade de Peso|
|---|---|
|15|3,0%|
|22|2,0%|
|30|1,5%|
|40|1,1%|

O Peso total do que o personagem carrega precisa caber na Capacidade típica, senão há Sobrecarga (Capítulo 4). Por isso, os pesos dos exemplos abaixo são baixos.

### 3.3 Penalidade de Deslocamento (Armaduras)

**Cada −1,5 m de Deslocamento reduz o poder em 6,7 pt (33,5 PP, cerca de 3 PO e 4 PP).** Esse é o valor de +1,5 m de Deslocamento. Para uma penalidade maior, multiplique pelo número de passos de 1,5 m (por exemplo, −3 m = 2 passos = 13,4 pt).

## 4. Armaduras

**Poder bruto = 17,9 pt × CA + traço do tipo (§4.2) + efeitos adicionais.**

|Componente|Poder (pt)|Preço|
|---|---|---|
|+1 de CA|17,9|9 PO|
|+1 de BA em Ataques|18,5|9 PO 2 PP|
|+1 de BD|7,8|3 PO 9 PP|
|+1 de BA em uma Salvaguarda|1,3|6 PP|
|+1 de BA em um Teste de Perícia|1,4|7 PP|
|+1 Grau em qualquer Ataque|12,1|6 PO|
|+1 Grau em uma categoria de Ataque (Corpo a Corpo, à Distância, Mágicos ou Físicos)|9,1|4 PO 6 PP|
|+1 Grau em um tipo muito específico (Ataques Desarmados, magias de um tipo de dano)|6,1|3 PO|

Como os valores foram obtidos:

- **+1 de CA, de BA em Ataques e de BD** vêm direto da Tabela 1 de `Custo de PHs.md`.
- **+1 de BA em uma Salvaguarda** é 8,9 pt (todas as Salvaguardas) dividido por 7 Atributos.
- **+1 de BA em uma Perícia** é o preço de 1 PH (uma Perícia) dividido pelo BP médio dos 20 Níveis (12,5), ou seja, 18 ÷ 12,5.
- **+1 Grau** soma, em média, +1,56 de dano por acerto (média dos ganhos de Grau 1 até 10), o que dá 1,56 × 7,8 acertos por Encontro. Vale para qualquer Ataque. Para tipos restritos, aplica-se uma fração: **0,75** para uma categoria e **0,5** para um tipo muito específico, porque o efeito deixa de valer sempre.

### 4.1 PVs e PMs Temporários que voltam a cada Descanso

O efeito concede PVs ou PMs Temporários de um Grau ao fim de um Descanso. Eles não se acumulam e duram até serem gastos ou até o próximo Descanso. O valor de cada Grau é o da Tabela 2 de `Custo de PHs.md` (PV Temp. e PM Temp. por Encontro), multiplicado pelos usos por Encontro:

- **Só em Descanso Longo:** 0,25 uso por Encontro (um Descanso Longo a cada 4 Encontros).
- **Em Descanso Curto ou Longo:** 0,5 uso por Encontro (a mesma conta da Tabela 6 de `Custo de PHs.md` para "uma vez por Descanso"). É mais fácil de recuperar, então custa o dobro.

|Grau|Dado|PV Temp. (Longo)|PV Temp. (Curto ou Longo)|PM Temp. (Longo)|PM Temp. (Curto ou Longo)|
|---|---|---|---|---|---|
|1|1d4|9 PP|1 PO 8 PP|3 PP|6 PP|
|2|1d6|1 PO 3 PP|2 PO 6 PP|4 PP|9 PP|
|3|1d8|1 PO 6 PP|3 PO 3 PP|5 PP|1 PO 1 PP|
|4|1d10|2 PO|4 PO|7 PP|1 PO 3 PP|
|5|1d12|2 PO 3 PP|4 PO 7 PP|8 PP|1 PO 5 PP|
|6|2d6|2 PO 5 PP|5 PO|8 PP|1 PO 6 PP|
|7|2d8|3 PO 2 PP|6 PO 4 PP|1 PO|2 PO 1 PP|
|8|2d10|3 PO 8 PP|7 PO 7 PP|1 PO 2 PP|2 PO 5 PP|
|9|2d12|4 PO 5 PP|9 PO|1 PO 4 PP|2 PO 8 PP|
|10|3d10|5 PO 6 PP|1 PL 1 PO 2 PP|1 PO 8 PP|3 PO 5 PP|

O PM Temporário vale bem menos que o PV Temporário do mesmo Grau porque 1 PV evitado vale 3 pt, e 1 PM, 1 pt (`Custos de Mana.md`, §1).

### 4.2 Traço do tipo de Armadura

Cada tipo de Armadura (Capítulo 4) tem um traço fixo, que entra no poder bruto de todas as Armaduras dele:

|Tipo|Traço|Cálculo|Poder (pt)|Preço|
|---|---|---|---|---|
|Ágil|+3 de BA em Salvaguardas de Destreza e +4 de BA em Salvaguardas de Constituição|3 × 2,5 + 4 × 1,27|12,7|6 PO 4 PP|
|Rígida|+4 de BA em Salvaguardas de Constituição e Vantagem contra Empurrar|4 × 1,27 + 1,0|6,1|3 PO|
|Híbrida|+2 de BA em Salvaguardas de Força e Resistência a Ataques Críticos igual à metade do BP|2 × 1,27 + 3,5|6,0|3 PO|

- Uma Salvaguarda comum vale 1,27 pt por +1 (8,9 ÷ 7 Atributos). Destreza vale o dobro (2,5 pt por +1), por ser a Salvaguarda mais pedida por Magias em Área.
- **Sem Deslocamento:** uma Armadura não mágica não concede Deslocamento. O +1,5 m (6,7 pt) das Ágeis foi trocado por +4 em Salvaguardas de Constituição (5,1 pt). Com +5 (6,4 pt) o valor seria igual, mas a Ágil passaria a ter mais Constituição que a Rígida.
- **Resistência a Ataques Críticos:** ≈ 0,19 Ataque Crítico recebido por Encontro (2,5 instâncias de dano por Encontro, e 5 ÷ 65 dos acertos são críticos) × 3 pt por PV evitado × 6 de Resistência média (metade do BP médio de 12,5) = 3,5 pt.
- A Vantagem contra Empurrar vale ≈ 1 pt por ser rara. A Desvantagem em Furtividade das Rígidas e o teto de CA de cada tipo (+7 Ágil, +9 Híbrida) **não entram no preço**: a penalidade de Deslocamento já é descontada (§3.3).

### 4.3 Armaduras do Capítulo 4.1

Os preços do Capítulo 4.1 - Lista de Armaduras vêm desta tabela. O poder bruto já inclui o traço do tipo e os efeitos de cada item (por exemplo, +3 em Furtividade = 3 × 1,4 pt, e +3 em quatro Perícias de Carisma = 12 × 1,4 pt).

|Armadura|Poder bruto (pt)|Desc. requisitos e penalidade (pt)|Desc. de peso|Total (pt)|Preço|
|---|---|---|---|---|---|
|Couro (Ágil)|30,6|1,1|4%|28,3|1 PL 4 PO 2 PP|
|Armadura de Pele Camuflada (Ágil)|34,9|1,1|6%|31,8|1 PL 5 PO 9 PP|
|Couro Batido (Ágil)|48,5|2,3|8%|42,5|2 PL 1 PO 3 PP|
|Couro de Elite (Ágil)|48,5|1,1|4%|45,5|2 PL 2 PO 8 PP|
|Armadura Nobre (Ágil)|83,7|3,9|8%|73,4|3 PL 6 PO 7 PP|
|Camisão de Malha (Rígida)|41,9|9,0|10%|29,6|1 PL 4 PO 8 PP|
|Cota de Malha (Rígida)|77,7|12,3|16%|54,9|2 PL 7 PO 5 PP|
|Peitoral de Aço (Rígida)|77,7|14,6|12%|55,5|2 PL 7 PO 8 PP|
|Cota de Talas (Rígida)|95,6|23,5|18%|59,1|2 PL 9 PO 6 PP|
|Meia Armadura de Aço (Rígida)|95,6|26,3|20%|55,4|2 PL 7 PO 7 PP|
|Armadura Completa de Aço (Rígida)|113,5|29,2|24%|64,1|3 PL 2 PO|
|Gibão de Peles (Híbrida)|59,7|4,6|10%|49,6|2 PL 4 PO 8 PP|
|Brigantina (Híbrida)|77,6|7,8|14%|60,0|3 PL|
|Cota de Escamas (Híbrida)|95,5|11,2|16%|70,8|3 PL 5 PO 4 PP|
|Armadura de Lamelas (Híbrida)|113,4|15,7|18%|80,1|4 PL 1 PP|
|Armadura de Escamas de Dragão (Híbrida)|131,3|23,0|20%|86,6|4 PL 3 PO 3 PP|

**Conta do Couro:** poder bruto = 17,9 × 1 + 12,7 (traço Ágil) = 30,6 pt. Requisito Des 1 = −1,1 pt, e sobram 29,5 pt. Peso 2 = −4%, então 29,5 × 0,96 = 28,3 pt. Preço = 28,3 × 5 = 142 PP = **1 PL 4 PO 2 PP**.

## 5. Armas

**Poder bruto = Grau + Bônus de Atributo + alcance.**

### 5.1 Dano (Grau)

O valor é o ganho de dano médio sobre um Ataque Desarmado (Grau 1, média 2,5), multiplicado por 7,8 acertos por Encontro. O Grau 1 vale 0, já que o Ataque Desarmado é de graça. Essa é a base do preço mínimo de 1 PO para armas simples.

|Grau|Dado|Média|Ganho sobre o Desarmado|Poder (pt)|Preço|
|---|---|---|---|---|---|
|1|1d4|2,5|0|0,0|0|
|2|1d6|3,5|1|7,8|3 PO 9 PP|
|3|1d8|4,5|2|15,6|7 PO 8 PP|
|4|1d10|5,5|3|23,4|1 PL 1 PO 7 PP|
|5|1d12|6,5|4|31,2|1 PL 5 PO 6 PP|
|6|2d6|7|4,5|35,1|1 PL 7 PO 6 PP|
|7|2d8|9|6,5|50,7|2 PL 5 PO 3 PP|
|8|2d10|11|8,5|66,3|3 PL 3 PO 2 PP|
|9|2d12|13|10,5|81,9|4 PL 9 PP|
|10|3d10|16,5|14|109,2|5 PL 4 PO 6 PP|

### 5.2 Bônus de Atributo

Como a Arma soma os Modificadores dos seus Atributos de bônus ao BA e ao BD (Capítulo 4), o valor de cada Modificador é de 26,3 pt (18,5 do BA e 7,8 do BD).

- **Um Atributo de bônus:** valor de referência de 3,5 de Modificador (a média do Modificador principal ao longo dos 20 Níveis, com o build típico), ou 92,1 pt. Esse valor já está embutido no que o Ataque Desarmado oferece, então o preço da Arma **não** soma esses 92,1 pt.
- **Dois Atributos de bônus:** o segundo Modificador soma +1,5 de Modificador (cerca de 3 de Modificador, vezes 50% de chance de o jogador ter investido nos dois Atributos), ou **+39,5 pt (19 PO e 8 PP)**.
- **Sem Atributo de bônus, com BA fixo** (Bestas e Armas de Fogo): cada +1 de BA fixo vale 18,5 pt, e a Arma deixa de ter o valor de referência de 92,1 pt, que seria o Modificador. Então o componente é `18,5 × BA fixo − 92,1`, e pode ser negativo (desconto). Um BA fixo de +5 equivale a ≈ 0, e a Arma não soma BD de Modificador.

### 5.3 Alcance

|Componente|Poder (pt)|Preço|
|---|---|---|
|+1,5 m de alcance corpo a corpo|8,0|4 PO|
|Cada 1,5 m de alcance de uma Arma à Distância, até 48 m|2,0|1 PO|

**Teto de 48 m:** o alcance de uma Arma à Distância é cobrado até 48 m (32 passos, ou 64 pt, no máximo). O que passar disso é um bônus gratuito, porque não importa tanto na prática. Uma Arma de 60 m paga o mesmo que uma de 48 m.

### 5.4 Exemplos de Armas

Os itens abaixo servem de verificação. Não são os itens finais do livro.

|Arma|Poder bruto (pt)|Desc. requisitos (pt)|Desc. de peso|Total (pt)|Preço|
|---|---|---|---|---|---|
|Adaga (Leve): Grau 1, Des, Peso 1|0,0|0,0|2%|0,0|1 PO|
|Espada Longa (Comum): Grau 4, For e Des, req. For 4 e Des 2, Peso 3|62,9|7,9|6%|51,7|2 PL 5 PO 8 PP|
|Lança (Comum): Grau 3, For, req. For 2, +1,5 m de alcance, Peso 3|23,6|2,3|6%|20,0|1 PL|
|Montante (Empunhadura Dupla): Grau 8, For, req. For 8, Peso 6|66,3|15,8|12%|44,4|2 PL 2 PO 2 PP|
|Arco Longo (à Distância): Grau 4, Des, req. Des 4, alcance 27 m, Peso 2|59,4|5,6|4%|51,6|2 PL 5 PO 8 PP|
|Arco de Longo Alcance (à Distância): igual ao Arco Longo, mas com alcance 60 m (paga só 48 m)|87,4|5,6|4%|78,5|3 PL 9 PO 3 PP|
|Besta Leve (à Distância): Grau 5, sem Atributo, BA fixo +4, req. Des 2, alcance 24 m, Peso 3|45,2|2,3|6%|40,3|2 PL 1 PP|
|Pistola (à Distância): Grau 6, sem Atributo, BA fixo +5, req. Des 4, alcance 18 m, Peso 2|59,6|5,6|4%|51,8|2 PL 5 PO 9 PP|

**Conta da Espada Longa:** Grau 4 = 23,4 pt. Dois Atributos = +39,5 pt. Poder bruto = 62,9 pt. Requisitos For 4 e Des 2 = 5,6 + 2,3 = −7,9 pt, e sobram 55,0 pt. Peso 3 = −6%, então 55,0 × 0,94 = 51,7 pt. Preço = 51,7 × 5 = 258 PP = **2 PL 5 PO 8 PP**.

## 6. Escudos

Escudos não têm Grau. Eles concedem um valor de **Resistência** (de 1 em diante, sem limite superior) a um ou mais tipos de Dano, como Dano Físico, Dano Mágico, ou um tipo específico, como Dano Ígneo.

### 6.1 Valor da Resistência

+1 de Resistência contra **todos** os tipos de dano vale 7,5 pt por Encontro (Tabela 1 de `Custo de PHs.md`). Como um Escudo costuma cobrir só alguns tipos, o valor é multiplicado pela **fração do dano recebido que é daquele tipo**:

**Poder bruto = 7,5 pt × Resistência × fração do tipo**, somando um termo por tipo coberto (cada tipo pode ter um valor de Resistência diferente).

|Tipo de dano|Fração do dano recebido|Poder de +1 de Resistência (pt)|Preço de +1|
|---|---|---|---|
|Todos os tipos|1,00|7,50|3 PO 8 PP|
|Dano Físico (os três tipos)|0,50|3,75|1 PO 9 PP|
|Dano Cortante|0,20|1,50|8 PP|
|Dano Perfurante|0,15|1,12|6 PP|
|Dano de Impacto|0,15|1,12|6 PP|
|Dano Ácido|0,05|0,38|2 PP|
|Dano Venenoso|0,10|0,75|4 PP|
|Dano Mágico (os sete tipos)|0,35|2,62|1 PO 3 PP|
|Dano Ígneo, Elétrico ou Gélido (cada)|0,08|0,60|3 PP|
|Dano Luminoso, Sombrio ou Psíquico (cada)|0,03|0,22|1 PP|
|Dano Sanguíneo|0,02|0,15|1 PP|

As frações somam 1,00: Físico 0,50 (Cortante 0,20, Perfurante 0,15, Impacto 0,15), Ácido 0,05, Venenoso 0,10 e Mágico 0,35 (Ígneo, Elétrico e Gélido 0,08 cada, Luminoso, Sombrio e Psíquico 0,03 cada, Sanguíneo 0,02). Elas supõem que a maior parte dos inimigos ataca de forma física, e são o principal ajuste deste cálculo.

**Resistências muito altas.** Como cada instância de dano causa no mínimo 1 (Capítulo 1.7) e um acerto típico de Nível 20 causa ≈ 31, a Resistência vai perdendo valor conforme se aproxima do dano médio. Por isso, **os pontos de 1 a 20 valem o preço cheio, os de 21 a 30 valem metade, e acima de 30 não custam nada** (bônus gratuito).

Preço de um Escudo, só pela Resistência (antes dos descontos):

|Resistência|Todos os tipos|Dano Físico|Dano Mágico|Um tipo Elemental|
|---|---|---|---|---|
|1|3 PO 8 PP|1 PO 9 PP|1 PO 3 PP|3 PP|
|2|7 PO 5 PP|3 PO 8 PP|2 PO 6 PP|6 PP|
|3|1 PL 1 PO 2 PP|5 PO 6 PP|3 PO 9 PP|9 PP|
|5|1 PL 8 PO 8 PP|9 PO 4 PP|6 PO 6 PP|1 PO 5 PP|
|8|3 PL|1 PL 5 PO|1 PL 5 PP|2 PO 4 PP|
|10|3 PL 7 PO 5 PP|1 PL 8 PO 8 PP|1 PL 3 PO 1 PP|3 PO|
|15|5 PL 6 PO 2 PP|2 PL 8 PO 1 PP|1 PL 9 PO 7 PP|4 PO 5 PP|
|20|7 PL 5 PO|3 PL 7 PO 5 PP|2 PL 6 PO 2 PP|6 PO|
|25|8 PL 4 PO 4 PP|4 PL 2 PO 2 PP|2 PL 9 PO 5 PP|6 PO 8 PP|
|30|9 PL 3 PO 8 PP|4 PL 6 PO 9 PP|3 PL 2 PO 8 PP|7 PO 5 PP|

Os descontos de requisitos (§3.1) e de peso (§3.2) valem para Escudos. Escudos não têm penalidade de Deslocamento.

### 6.2 Exemplos de Escudos

Os itens abaixo servem de verificação. Não são os itens finais do livro.

|Escudo|Poder bruto (pt)|Desc. requisitos (pt)|Desc. de peso|Total (pt)|Preço|
|---|---|---|---|---|---|
|Escudo de Madeira: Dano Físico 2, For 2, Peso 3|7,5|2,3|6%|4,9|2 PO 4 PP|
|Escudo de Aço: Dano Físico 5, For 5, Peso 6|18,8|7,9|12%|9,5|4 PO 8 PP|
|Escudo Rúnico: Dano Físico 4 e Dano Ígneo 6, For 4, Peso 5|18,6|5,6|10%|11,7|5 PO 9 PP|
|Égide Arcana: Dano Mágico 8 e Dano Físico 4, Vin 6 e For 4, Peso 4|36,0|15,7|8%|18,7|9 PO 3 PP|
|Escudo-Torre: Dano Físico 12, For 8, Peso 10|45,0|15,8|20%|23,4|1 PL 1 PO 7 PP|

Um Escudo ocupa uma mão, o que impede de empunhar uma Arma com duas mãos ou usar duas Armas. Essa troca já existe no jogo e **não entra no preço**.

## 7. Munição

10 munições custam 1 PP (1 PC cada). Um arqueiro que usa 12 munições por Encontro (3 Ataques por Rodada) gasta cerca de 1 PP, e metade volta ao fim do Encontro. O custo é desprezível perto do valor da Arma, como esperado, e serve só para limitar o estoque.

## 8. Equipamento inicial

O Equipamento Inicial (Capítulo 2) não é fixo, então a conta parte do que o personagem deveria ter no Nível 1. O Balanceamento recomenda Grau 5 de Arma nos Níveis 1 a 3, e este é o kit mínimo que respeita isso, com uma Armadura de CA +3 que dá para usar no Nível 1:

|Item|Preço|
|---|---|
|Arma de Grau 5 com um Atributo, req. 2, Peso 3|1 PL 3 PO 6 PP|
|Gibão de Peles (Armadura Híbrida, CA +3)|2 PL 4 PO 8 PP|
|Escudo de Dano Físico 2, req. 2, Peso 3|2 PO 4 PP|
|**Total**|**4 PL 8 PP**|

**Sugestão: 50 PO.** Cobre o kit com folga de ≈ 9 PO para provisões, munição e Itens Consumíveis. Em PHs, 50 PO valem ≈ 5,6 PH de poder em equipamento, na mesma ordem dos 7 Pontos de Origem. Com 25 PO, o personagem não compraria nem a Arma de Grau 5 junto da Armadura mais barata (≈ 28 PO).

Se preferir manter 25 PO, divida todos os preços por 2 (1 PH = 4,5 PO). O kit passa a custar ≈ 20,4 PO.

## 9. Verificações de coerência

- **Equivalência com PHs:** +1 de CA numa Armadura (17,9 pt) custa ≈ 9 PO, e a Habilidade equivalente custa 0,99 PH. Como 1 PH = 9 PO, equipamento e Habilidades têm o mesmo preço por poder.
- **Pedras de Aprimoramento (Capítulo 4.9):** o ganho de Grau do Balanceamento vale, em PO por pedra: Grau 1→5, ≈ 3,9 PO (1 pedra por subida); 5→6, ≈ 1 PO (2 pedras para +0,5); 6→7, ≈ 3,9 PO (2 pedras); 7→8 e 8→9, ≈ 2,6 PO (3 pedras cada); 9→10, ≈ 2,3 PO (6 pedras). Uma pedra de ≈ 3 PO deixa a maioria das subidas coerentes com este documento. A subida 5→6 fica cara para o ganho de propósito, como freio no meio do jogo.
- **Escudo e Armadura:** +1 de CA (≈ 9 PO) vale ≈ 5 vezes mais que +1 de Resistência Física (≈ 1 PO e 9 PP). Como a CA evita o dano inteiro de um acerto e a Resistência só reduz uma parte dele, a diferença é esperada.

## 10. Suposições e pontos em aberto

1. **Escala de ouro.** Com 1 PH = 9 PO, a Armadura de Escamas de Dragão custa ≈ 43 PO, e um item com vários efeitos passa de 100 PO, longe dos 750 PO que o Halfling Mercador prevê para um item. Se a Campanha der muito mais ouro que isso, o equipamento passa a valer mais que as Habilidades. Para ajustar, mude a conversão de pt para PP (§1).
2. **Modificador de referência (3,5 e 1,5).** Define o preço do segundo Atributo de bônus e do BA fixo.
3. **Peso** a `45% ÷ Capacidade típica` por unidade, com teto de 40%. É um chute informado, e acompanha qualquer mudança na fórmula da Capacidade de Carga.
4. **Frações do +1 Grau** (0,75 e 0,5) e **usos por Encontro** (0,25 e 0,5) são ajustáveis.
5. **Frações de dano por tipo (Escudos).** Foram escolhidas por estimativa. Se o Guia dos Monstros mostrar que há muito mais dano mágico que físico, aumente as frações do Mágico.
6. **Resistência alta em Níveis baixos.** O preço não considera o Nível. Uma Resistência de 8 é cara no preço, mas anula quase todo o dano de um monstro de Nível 1. Sugestão: exigir Atributos altos nos Escudos com Resistência grande, já que o requisito só libera o item em Níveis mais altos (Limite de Atributo).
7. **Tipos de Arma** (Leve, Comum, Empunhadura Dupla) não alteram o preço. Duas Armas custam o dobro. A diferença da Empunhadura Dupla já aparece no Atributo de bônus.
8. **Bônus de BA vindos de equipamento** não contam para o teto de +8 de BA e +3 de CA de Habilidades, pois o teto vale só para Habilidades.
9. **Traços dos tipos de Armadura.** Híbridas ficaram com +2 de Salvaguarda de Força, e não +3: com o teto de CA +9, a Híbrida perde ≈ 18 pt contra a Rígida de CA +10, mas a Rígida paga ≈ 13 pt de penalidade de Deslocamento (−3 m) e Desvantagem em Furtividade. A diferença final é de ≈ 5 pt. Se na prática a Híbrida parecer fraca, passar para +3 soma só 1,3 pt ao preço.
10. **Preços das Armaduras Ágeis** ficaram mais altos por causa do traço (12,7 pt, ≈ 6 PO a mais). Isso compensa o teto de CA +7, mas encarece o Couro, que custa ≈ 14,2 PO.