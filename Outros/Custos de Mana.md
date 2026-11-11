Este documento atribui uma **pontuação** a cada efeito que uma Habilidade pode ter, para que o custo de Mana de cada Habilidade possa ser calculado depois, somando os pontos dos seus efeitos. Aqui ainda **não há conversão para PMs**: a primeira etapa é só garantir que os efeitos estejam proporcionais entre si e testar como os valores se comportam com cada duração.

Todos os números foram derivados do `Balanceamento.md` (cenário típico no Nível 20, Rodada de 3 Ações, Encontro de 4 Rodadas). Eles estão no fim, em §2, como premissas explícitas. Se uma premissa mudar, os valores mudam com ela.

**O que mudou em relação ao rascunho anterior.** O dano dos PDJs agora inclui +75 de BD vindo de Escalas de Armas, então o dano por acerto passou de ≈ 30,8 para ≈ 96,2 e o dano por Rodada, de 60 para 187,5. Os PVs do monstro Médio de Nível 20 passaram de 960 para 3.000. Tudo o que depende desses números foi recalculado. Os efeitos que dependem de dados (Graus) não mudaram em PVs, então ficaram menores perto do resto.

## 1. A unidade: o ponto (pt)

- **1 pt = 1 PV de dano causado** a um inimigo.
- **1 PM = 3,125 pt (provisório).** Um Turno vale 3 Ações, ou 187,5 pt, e gasta ≈ 12 PM. Mantive a razão do rascunho anterior, em que 1 PM valia 1/60 de um Turno. Se a conversão de pontos em PMs for definida de outra forma, basta mudar este número (só afeta PMs restaurados e PM Temporários).
- **1 PV curado, absorvido ou evitado vale ≈ 9,7 pt.** Motivo: um monstro Médio de Nível 20 tem 3.000 PVs e causa ≈ 310 de dano por Encontro (77,4 × 4 Rodadas), ou seja, ≈ 9,7× mais PVs do que dano. Cada PV de dano que você causa remove ≈ 0,10 PV de dano futuro que ele causaria. Logo, para valer o mesmo, 1 PV de dano evitado precisa ser contado como ≈ 9,7 PVs de dano causado.
- Esse fator (9,7) é o **botão principal** do sistema. Ele afeta: Cura, PV Temporários, Resistência, +1 de CA, +1 de BA em Salvaguardas e +1 de cura. Ele **não** afeta: Dano, BA em Ataques, BD, Ação, Deslocamento e PMs. Se preferir que 1 PV curado valha o mesmo que 1 PV de dano, basta dividir essas seis linhas pelo fator (ver §7). No rascunho anterior o fator era 3.

## 2. Premissas (Nível 20)

|Premissa|Valor|Origem|
|---|---|---|
|Dano-alvo do PDJ por Rodada|187,5|`Balanceamento.md`|
|Ataques por Rodada / chance média de acerto|3 / 65% (≈ 1,95 acertos)|`Balanceamento.md` (cenário típico)|
|Dano por acerto|≈ 96,2|187,5 ÷ 1,95 (Grau 10 + 75 de Escalas + Habilidades)|
|Dano recebido por PDJ por Rodada|19,35|10% do total do grupo (77,4) ÷ 4 PDJs|
|Instâncias de dano recebidas por PDJ por Rodada|≈ 0,49|o monstro faz 3 Ataques com 65% de acerto (1,95 por Rodada) ÷ 4 PDJs|
|Dano por instância recebida|≈ 39,7|77,4 ÷ 1,95 (dano líquido, depois de Resistências)|
|Variação de +1 de BA ou CA|+5 pp (≈ +7,7% do valor relativo)|d20, chance base de 65%|
|Valor de 1 Ação|62,5 pt|187,5 ÷ 3 Ações|
|PM gastos por Turno|≈ 12|193,5 PMs Máximos ÷ 16 Rodadas (4 Encontros)|
|Duração de um Encontro|4 Rodadas|`Balanceamento.md`|

Duas mudanças de método em relação ao rascunho anterior. Primeiro, o dano por instância recebida deixou de ser igual ao dano por acerto do PDJ, porque o PDJ agora causa muito mais dano do que o monstro. Segundo, os valores de posicionamento (Deslocamento, alcances, Terreno Difícil, Ação Bônus e Reação extras, Perícias) são frações do valor de uma Ação e foram multiplicados por 3,125, para manter a proporção do rascunho.

## 3. Valores base

|Efeito|Pontos|Unidade de contagem|Confiança|
|---|---|---|---|
|+1 de BA em Ataques|14,4|por Turno próprio|Alta|
|+1 de BA em Salvaguardas (todas)|7,2|por ciclo de inimigos (Rodada)|Média|
|+1 de BA em Testes de Perícia|3,1|por Turno próprio (em combate)|Baixa|
|**+1 de BA geral** (Ataques + Salvaguardas + Perícias)|24,8|Rodada (soma das três linhas acima)|Média|
|+1 de CA|14,4|por ciclo de inimigos (Rodada)|Alta|
|+1 de BD (dano por instância)|2,0 (1,0 por instância)|por Turno próprio (≈ 1,95 acertos)|Alta|
|+1 de cura (por instância de cura)|9,7|por instância de cura recebida|Alta|
|+1 de Resistência (por instância de dano)|4,7 por Rodada|por ciclo de inimigos (≈ 0,49 instâncias/Rodada)|Média|
|+1,5 m de Deslocamento|5,2|por Turno próprio|Baixa|
|−1,5 m de Deslocamento (debuff no inimigo)|4,2|por Turno do inimigo|Baixa|
|+1,5 m de alcance em Ataques corpo a corpo|6,3|por Turno próprio|Baixa|
|+1,5 m de alcance em Ataques Mágicos|1,56|por Turno próprio|Baixa|
|+1,5 m de alcance em magias de área (distância até o ponto)|1,56|por Turno próprio|Baixa|
|_(extra)_ +1,5 m no raio de uma magia de área|12,5|por Turno próprio, se você usa área com frequência|Muito baixa|
|Terreno Difícil em área circular de raio 1,5 m|6,3|por Turno de inimigo (≈ 1,5 criaturas atravessando)|Baixa|
|**+1 Ação no Turno**|62,5|por Turno próprio (Ação não-Ataque)|Alta (como teto)|
|+1 Ação Bônus extra (no próximo Turno do alvo)|21,9|por Turno do alvo|Baixa|
|+1 Reação extra (nessa Rodada, resto dela)|7,5 (15,0 por Rodada cheia)|uma vez|Baixa|
|1 de dano contínuo|1,0 por instância|ver §5.4: 1 + Turnos do alvo afetados|Alta|

Leitura rápida:

- **+1 de BA em Ataques (14,4) e +1 de CA (14,4) saem iguais.** Isso não foi forçado: sai da razão entre PVs do monstro e dano que ele causa (o fator 9,7), e os PVs do monstro foram calculados a partir do dano do grupo. É um bom sinal de que o sistema de BA/CA está coerente.
- **+1 Ação (62,5 pt) vale ≈ 2,5× o +1 de BA geral e ≈ 4,3× o +1 de BA em Ataques.** É de longe o efeito mais forte da lista e deve ser o mais caro (ver §7).
- **+1 de BD (2,0) agora vale ≈ 7,4× menos que +1 de BA em Ataques.** Com o dano por acerto em ≈ 96, um ponto de BD é pouco e um ponto de BA é muito. No rascunho anterior a diferença era de 2,3×.
- Os efeitos de **posicionamento** (Deslocamento, alcances, Terreno Difícil) são os de menor confiança: o valor depende de mapa e de tática, não de números.

## 4. Valor de cada Grau

Os valores são do **dado do Grau** (média), sem modificadores. "Garantido" assume que não há teste. Efeitos com Ataque devem usar a coluna de ×0,65. Efeitos com Salvaguarda ficam entre as duas colunas, dependendo do dano em caso de sucesso. As colunas de Cura e de PV Temporários já têm o fator 9,7, e as de PM, o fator 3,125.

|Grau|Dado|Média|Dano (garantido)|Dano (com Ataque, ×0,65)|Cura (pt)|PM restaurados (pt)|PV Temp. (valor máx.)|PM Temp. (valor máx.)|
|---|---|---|---|---|---|---|---|---|
|1|1d4|2,5|2,5|1,6|24,2|7,8|24,2|7,8|
|2|1d6|3,5|3,5|2,3|33,9|10,9|33,9|10,9|
|3|1d8|4,5|4,5|2,9|43,6|14,1|43,6|14,1|
|4|1d10|5,5|5,5|3,6|53,3|17,2|53,3|17,2|
|5|1d12|6,5|6,5|4,2|63,0|20,3|63,0|20,3|
|6|2d6|7,0|7,0|4,6|67,8|21,9|67,8|21,9|
|7|2d8|9,0|9,0|5,9|87,2|28,1|87,2|28,1|
|8|2d10|11,0|11,0|7,2|106,6|34,4|106,6|34,4|
|9|2d12|13,0|13,0|8,5|126,0|40,6|126,0|40,6|
|10|3d10|16,5|16,5|10,7|159,9|51,6|159,9|51,6|

Observações:

- "PV Temp. (valor máx.)" e "PM Temp. (valor máx.)" são o valor se **todos** os pontos forem usados. Na prática eles expiram, e o valor real depende da duração (§5.3).
- Cura vale 9,7× o Dano do mesmo Grau. Um Grau de cura tem que custar proporcionalmente mais que um Grau de dano.
- Um Grau de **dano** agora é pequeno perto de uma Ação (62,5 pt): o maior, o Grau 10, vale 16,5 pt garantido. Qualquer efeito de dano que só use o dado do Grau vale menos que um Ataque comum com Arma. Isso é um ponto em aberto importante (§8).

## 5. Testes por duração

### 5.1 Como a duração é contada

Todas as durações assumem que o efeito é ativado **no seu Turno** e que uma Rodada "conta a atual" (regra do sistema), então a Rodada em que você ativa vale por meia Rodada, em média (a ordem de Iniciativa decide o resto).

|Duração|O (Turnos seus afetados)|I (ciclos de inimigos que o alvo enfrenta)|Ti (Turnos do inimigo afetados)|O' (Turnos com +1 Ação)|
|---|---|---|---|---|
|1 Rodada|0,5|0,5|0,5|1,0|
|2 Rodadas|1,5|1,5|1,5|2,0|
|3 Rodadas|2,5|2,5|2,5|3,0|
|4 Rodadas|3,5|3,5|3,5|4,0|
|Encontro|4,0|4,0|4,0|4,0|
|Até ini. próx. Turno|0,5|1,0|1,0|1,0|
|Fim próx. Turno do alvo (você)|1,5|1,5|1,5|2,0|
|Fim próx. Turno do alvo (aliado)|1,0|1,5|1,5|1,0|

- **O** conta seus Turnos (o Turno de ativação conta 0,5, pois a ativação já gastou parte dele). **I** é a exposição a ataques: vale para CA, Resistência e PV Temporários. **Ti** conta quantos Turnos do inimigo passam sob o efeito, e vale para debuffs e dano contínuo.
- **1 Encontro** é tratado como 4 Rodadas cheias, porque efeitos de Encontro costumam ser ativados antes ou no início do combate.
- Para o **aliado**, o "fim do próximo Turno do alvo" dá 1,0 Turno de benefício ofensivo (o Turno dele), mas ainda 1,5 de exposição.
- **+1 Ação** usa O' (não O): a Ação extra vale inteira no Turno em que for concedida, independentemente de ter sido ativada no meio dele.

### 5.2 Efeitos de bônus × duração (pontos totais)

|Efeito|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|+1 BA em Ataques|7,2|21,6|36,1|50,5|57,7|7,2|21,6|14,4|
|+1 BA em Salvaguardas|3,6|10,8|18,0|25,2|28,8|7,2|10,8|10,8|
|+1 BA em Perícias|1,6|4,7|7,8|10,9|12,5|1,6|4,7|3,1|
|**+1 BA geral**|12,4|37,1|61,9|86,7|99,0|16,0|37,1|28,4|
|+1 CA|7,2|21,6|36,1|50,5|57,7|14,4|21,6|21,6|
|+1 BD|1,0|2,9|4,9|6,8|7,8|1,0|2,9|2,0|
|+1 de cura (0,5 inst./Rodada)|2,4|7,3|12,1|17,0|19,4|4,8|7,3|7,3|
|+1 Resistência|2,4|7,1|11,8|16,5|18,9|4,7|7,1|7,1|
|+1,5 m Deslocamento|2,6|7,8|13,0|18,2|20,8|2,6|7,8|5,2|
|+1,5 m alcance corpo a corpo|3,1|9,4|15,6|21,9|25,0|3,1|9,4|6,3|
|+1,5 m alcance Ataque Mágico|0,8|2,3|3,9|5,5|6,3|0,8|2,3|1,6|
|+1,5 m alcance de área|0,8|2,3|3,9|5,5|6,3|0,8|2,3|1,6|
|+1,5 m raio de área|6,3|18,8|31,3|43,8|50,0|6,3|18,8|12,5|
|**+1 Ação no Turno**|62,5|125,0|187,5|250,0|250,0|62,5|125,0|62,5|
|+1 Ação Bônus extra por Turno|21,9|43,8|65,6|87,5|87,5|21,9|43,8|21,9|
|+1 Reação extra por Rodada|7,5|22,5|37,5|52,5|60,0|15,0|22,5|22,5|

### 5.3 Graus como PV Temporários, PM Temporários e Resistência × duração (pontos totais)

PV e PM Temporários são **gastos conforme o dano ou o custo aparecem**, e o que sobrar ao fim da duração se perde. Para refletir isso, o valor é "o que você realmente usa": `μ · (1 − e^(−X/μ))`, com X o valor do Grau e μ a média do que seria consumido na janela (μ = I × 19,35 PVs para PV; μ = O × 12 PMs para PM). O resultado de PV é multiplicado por 9,7 e o de PM por 3,125.

**PV Temporários**

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|21,3|23,2|23,6|23,8|23,8|22,7|23,2|23,2|
|Grau 2 (1d6)|28,5|31,9|32,7|33,1|33,2|31,0|31,9|31,9|
|Grau 3 (1d8)|34,9|40,4|41,6|42,2|42,4|38,9|40,4|40,4|
|Grau 4 (1d10)|40,7|48,5|50,4|51,2|51,4|46,4|48,5|48,5|
|Grau 5 (1d12)|45,9|56,4|58,9|60,1|60,4|53,5|56,4|56,4|
|Grau 6 (2d6)|48,3|60,3|63,2|64,4|64,9|56,9|60,3|60,3|
|Grau 7 (2d8)|56,8|75,0|79,6|81,7|82,3|69,7|75,0|75,0|
|Grau 8 (2d10)|63,7|88,7|95,3|98,4|99,4|81,3|88,7|88,7|
|Grau 9 (2d12)|69,3|101,5|110,5|114,6|116,0|91,7|101,5|101,5|
|Grau 10 (3d10)|76,7|122,0|135,5|141,9|144,0|107,6|122,0|122,0|

**PM Temporários**

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|6,4|7,3|7,5|7,6|7,6|6,4|7,3|7,1|
|Grau 2 (1d6)|8,3|9,9|10,3|10,5|10,5|8,3|9,9|9,5|
|Grau 3 (1d8)|9,9|12,4|13,1|13,3|13,4|9,9|12,4|11,7|
|Grau 4 (1d10)|11,3|14,8|15,7|16,1|16,2|11,3|14,8|13,8|
|Grau 5 (1d12)|12,4|17,0|18,3|18,8|19,0|12,4|17,0|15,7|
|Grau 6 (2d6)|12,9|18,1|19,5|20,1|20,4|12,9|18,1|16,6|
|Grau 7 (2d8)|14,6|22,1|24,3|25,3|25,6|14,6|22,1|19,8|
|Grau 8 (2d10)|15,8|25,7|28,8|30,2|30,7|15,8|25,7|22,5|
|Grau 9 (2d12)|16,6|28,9|33,0|34,9|35,6|16,6|28,9|24,8|
|Grau 10 (3d10)|17,6|33,8|39,7|42,6|43,6|17,6|33,8|28,0|

**Resistência** (cada Grau vale a média do dado por instância de dano, e o mínimo de 1 de dano por instância continua valendo)

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo (você)|Fim próx. Turno do alvo (aliado)|
|---|---|---|---|---|---|---|---|---|
|Grau 1 (1d4)|5,9|17,7|29,5|41,3|47,2|11,8|17,7|17,7|
|Grau 2 (1d6)|8,3|24,8|41,3|57,9|66,1|16,5|24,8|24,8|
|Grau 3 (1d8)|10,6|31,9|53,1|74,4|85,0|21,3|31,9|31,9|
|Grau 4 (1d10)|13,0|39,0|65,0|90,9|103,9|26,0|39,0|39,0|
|Grau 5 (1d12)|15,4|46,1|76,8|107,5|122,8|30,7|46,1|46,1|
|Grau 6 (2d6)|16,5|49,6|82,7|115,7|132,3|33,1|49,6|49,6|
|Grau 7 (2d8)|21,3|63,8|106,3|148,8|170,1|42,5|63,8|63,8|
|Grau 8 (2d10)|26,0|77,9|129,9|181,9|207,8|52,0|77,9|77,9|
|Grau 9 (2d12)|30,7|92,1|153,5|214,9|245,6|61,4|92,1|92,1|
|Grau 10 (3d10)|39,0|116,9|194,9|272,8|311,8|77,9|116,9|116,9|

Leitura:

- O PV Temporário perde pouco valor com a duração, porque cada acerto inimigo (≈ 40 PVs) é bem maior que o Grau. Por exemplo, o Grau 3 vale 34,9 em 1 Rodada e 42,4 em 1 Encontro, contra 43,6 da cura (≈ 80% e ≈ 97%). Isso muda se os PV Temporários forem grandes ou se o inimigo causar dano pequeno e frequente.
- O **PM Temporário** perde mais valor que o PV Temporário em durações curtas (Grau 3: ≈ 70% em 1 Rodada), porque você gasta ≈ 12 PMs por Turno e pouco desse gasto cabe na janela.
- A **Resistência** cresce de forma quase linear com a duração e passa o PV Temporário do mesmo Grau a partir de ≈ 1,5 Rodada (Grau 3: 31,9 contra 40,4).

### 5.4 Debuffs e dano contínuo (alvo inimigo)

**Dano contínuo** causa uma instância imediata e uma no início de cada Turno do alvo. Então 1 de dano contínuo por uma duração vale **1 + Ti** instâncias. Assume-se que cada instância rola novamente o dado do Grau. O dano contínuo não faz teste de acerto, então vale o valor "garantido", e o mínimo de 1 de dano por instância o protege de Resistência.

|Grau|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo|
|---|---|---|---|---|---|---|---|
|1 de dano contínuo|1,5|2,5|3,5|4,5|5,0|2,0|2,0|
|Grau 1 (1d4)|3,8|6,3|8,8|11,3|12,5|5,0|5,0|
|Grau 2 (1d6)|5,3|8,8|12,3|15,8|17,5|7,0|7,0|
|Grau 3 (1d8)|6,8|11,3|15,8|20,3|22,5|9,0|9,0|
|Grau 4 (1d10)|8,3|13,8|19,3|24,8|27,5|11,0|11,0|
|Grau 5 (1d12)|9,8|16,3|22,8|29,3|32,5|13,0|13,0|
|Grau 6 (2d6)|10,5|17,5|24,5|31,5|35,0|14,0|14,0|
|Grau 7 (2d8)|13,5|22,5|31,5|40,5|45,0|18,0|18,0|
|Grau 8 (2d10)|16,5|27,5|38,5|49,5|55,0|22,0|22,0|
|Grau 9 (2d12)|19,5|32,5|45,5|58,5|65,0|26,0|26,0|
|Grau 10 (3d10)|24,8|41,3|57,8|74,3|82,5|33,0|33,0|

**Debuffs de posição**

|Efeito (alvo inimigo)|1 Rod.|2 Rod.|3 Rod.|4 Rod.|Encontro|Até ini. próx. Turno|Fim próx. Turno do alvo|
|---|---|---|---|---|---|---|---|
|−1,5 m Deslocamento|2,1|6,3|10,4|14,6|16,7|4,2|4,2|
|Terreno Difícil (raio 1,5 m)|3,1|9,4|15,6|21,9|25,0|6,3|6,3|

### 5.5 Ação Bônus e Reação extras

- **+1 Ação Bônus** (além da gratuita): uma Ação Bônus não causa dano nem controle, então vale ≈ 70% de uma Ação (43,8 pt) quando há o que fazer com ela, e a chance de haver uma segunda opção útil no mesmo Turno é de ≈ 50%. Valor: 62,5 × 0,7 × 0,5 = **21,9 pt por Turno**. "No próximo Turno do alvo" é um Turno só, logo **21,9 pt**. É um efeito barato porque hoje há poucas opções de Ação Bônus: se o Capítulo 5 criar muitas, esse valor sobe para até 43,8 pt.
- **+1 Reação**: uma Reação usada vale ≈ 60% de uma Ação (37,5 pt; mistura de Ataque de Oportunidade, ≈ 1 Ação, e reações defensivas, menores). Como a Reação base já cobre o gatilho mais comum, a segunda só é usada em ≈ 40% das Rodadas: **15,0 pt por Rodada cheia**. "Nessa Rodada" (o resto dela, ≈ 0,5 Rodada) vale **7,5 pt**, que é exatamente a coluna "1 Rod." da tabela de §5.2. Se o alvo ainda não gastou a Reação base, a extra vale quase nada. Se já gastou, vale o valor cheio.

## 6. Como os valores mudam com o Nível

Efeitos **proporcionais** (BA, CA, Salvaguarda) escalam com o dano e a vida da época. Para isso, usei o dano por Nível e os PVs de monstro de `Balanceamento.md` (BD de Escalas ≈ 3,75 por Nível, PVs do monstro Médio = 150 por Nível). Efeitos **fixos** (BD, +1 de cura por instância e +1 de Resistência por instância) não mudam em PVs, mas o fator de cura muda um pouco com o Nível, porque a razão entre PVs do monstro e dano dele varia.

|Nível|+1 BA (Ataque)|+1 CA|+1 BA Salv.|+1 BD|+1 cura|+1 Resist.|
|---|---|---|---|---|---|---|
|1|1,6|0,7|0,4|2,0|10,4|5,1|
|5|4,0|3,6|1,8|2,0|13,0|6,3|
|10|7,3|7,2|3,6|2,0|10,6|5,2|
|15|10,6|10,8|5,4|2,0|9,6|4,7|
|20|14,4|14,4|7,2|2,0|9,7|4,7|

Isso mostra um problema a decidir: **no Nível 1, +1 de BD vale ≈ 1,2× o +1 de BA** (no Nível 20, vale ≈ 0,14×). Duas saídas: (a) cobrar o BD e a Resistência fixos em PMs mais altos nos Níveis baixos, ou (b) aceitar que bônus fixos são fortes no começo e marcá-los como "poder de início". Os valores do Nível 1 dependem do modelo grosseiro de BD por Nível, então são só uma indicação.

## 7. Observações e alertas de design

1. **+1 Ação é o efeito mais caro.** 62,5 pt por Turno só no valor médio, e um 4º Ataque com a Penalidade de −5 cumulativa vale bem menos que uma Ação "comum" (≈ 25% do valor), mas ainda há opções melhores (conjurar, usar Habilidade, mover-se). Sugestão: custar 62,5 pt por Turno e/ou restringir a Ação a Habilidades e Movimentação, não a Ataques.
2. **Cura vale 9,7× dano por PV.** Essa é a decisão que o sistema precisa confirmar. Se for 1:1, o Grau de cura custa o mesmo que o Grau de dano, e o PV Temporário e a Resistência ficam ≈ 10× mais baratos. Se for 10:1, cura é cara e dano é barato. O valor subiu de 3:1 para ≈ 9,7:1 porque o grupo agora causa muito mais dano que o monstro. Um meio-termo (por exemplo, 5:1) pode ser mais confortável. Mantive o valor derivado dos números do Balanceamento.
3. **PV Temporário e PM Temporário** nunca valem o valor máximo. Cobrar pelo valor máximo faz com que eles sejam ruins em durações curtas. Sugiro cobrar pelo valor das tabelas de §5.3.
4. **Dano contínuo** é um bom "dano por PM": rende o valor integral sem teste de acerto e ignora Resistência pequena. Em durações de Encontro, 1 de dano contínuo vale 5 pt, quase um Grau 4 de dano direto. O Grau 10 de dano contínuo por um Encontro vale 82,5 pt. Talvez valha um desconto de ≈ 15% no custo (porque o alvo pode morrer ou ser curado antes do fim).
5. **+1 BA geral ≈ 24,8 pt/Rodada** vs **+1 BA em Ataques ≈ 14,4**. O "geral" só deve ser cobrado como geral se realmente cobrir os três usos.
6. **Cura contínua / Regeneração** (cura por Turno) ainda não existe na lista, mas segue a mesma lógica do dano contínuo: valor do Grau × 9,7 × (1 + Turnos).
7. **Dano de Grau perde para o Ataque com Arma.** Um Ataque com Arma vale ≈ 62,5 pt por Ação (96,2 de dano × 65%). Um Ataque Mágico de Grau 10 vale ≈ 10,7 pt, e mesmo em 3 alvos só 32,2. Magias e Habilidades de dano baseadas só em Grau, mais um Modificador (Capítulo 1.6), nunca superam atacar. Para competirem, precisam de um BD próprio que escale com Nível ou Atributo (por exemplo, Escalas em Cajados ou Focos).

## 8. Pontos em aberto

- Confirmar a **razão cura:dano** (≈ 9,7:1 derivada, ou 5:1, 3:1, 1:1).
- Confirmar que o **dano contínuo rola o dado do Grau a cada instância** (ou se o valor é fixo na aplicação).
- Confirmar o que significa **"alcance de magias de área"**: distância até o ponto de origem (como assumi) ou raio (valor extra em §3).
- Confirmar o gasto médio de PMs por Turno (usei 12) quando houver uma tabela de PMs por Nível.
- Definir a **conversão de pontos em PMs**. Provisoriamente, 1 PM = 3,125 pt (§1).
- Definir como **magias de dano** acompanham o BD de Armas (observação 7).
- Estes efeitos ainda não estão na lista e entram quando você quiser: −1 de BA/CA no inimigo, Vantagem/Desvantagem, Condições (Atordoado, Caído, Agarrado etc.), cura contínua, teletransporte, invisibilidade, aumentar/diminuir Margem de Ameaça.
- O custo em PHs de Habilidades usa estes pontos e está em `Custo de PHs.md`. Os preços de equipamentos estão em `Custo de Moedas.md`.

## 9. Requisitos de Atributo e o custo de PM

**Resposta curta: os requisitos de Atributo não devem diminuir o custo de PM.** Eles devem **aumentar o poder permitido da Habilidade** (ver `Custo de PHs.md`). Quatro razões:

1. **Pagamentos diferentes.** O requisito é pago uma vez, ao adquirir a Habilidade (em PAs). O PM é pago a cada uso. Um desconto por uso pagaria uma restrição permanente de forma desigual: quem usa mais vezes recebe mais desconto.
2. **Dupla contagem.** A maioria das magias já escala com o Modificador do Atributo exigido (BA, BD, CD). Quem tem o Atributo alto já ganha uma magia mais forte. Baixar o custo também seria pagar duas vezes.
3. **O requisito é, antes de tudo, um portão de Nível.** Com LA = Nível/2 + 3, um requisito de valor R só pode ser cumprido a partir do Nível 2 × (R − 3) (por exemplo, 6 no Nível 6 e 10 no Nível 14). Isso já tira da frente as Habilidades fortes nos Níveis baixos sem custo nenhum de PM.
4. **O custo real é de oportunidade, e é pequeno.** Um requisito só custa o que o personagem **não** teria investido de qualquer forma. Considerei: build típico no Nível 20 com 30 PAs (10, 8, 6, 4, 2, 0, 0). Metade dos jogadores escolhe a Habilidade já alinhada ao seu build (custo 0 se o requisito é ≤ 10 no Atributo principal), e metade acaba exigindo um Atributo que não seria prioridade. Cada PA forçado fora do plano custa ≈ 19,6 pt por Encontro: metade de um passo de Escala D (+1 de BA e +1 de BD a cada 2 pontos de Atributo, ou seja, 16,4 pt por Rodada para o passo inteiro), com 60% de perda efetiva, em 4 Rodadas. No rascunho anterior era 7,9 pt, com o Modificador no lugar da Escala.

**Compensação por um requisito** (1 PH = 57,7 pt/Encontro):

|Requisito (valor)|Nível mínimo (LA)|PAs forçados (alinhado)|PAs forçados (aleatório)|PAs forçados (efetivo)|Compensação (pt/Encontro)|Compensação (PHs)|
|---|---|---|---|---|---|---|
|1|1|0,0|0,29|0,14|2,8|0,05|
|2|1|0,0|0,57|0,29|5,6|0,10|
|3|1|0,0|1,00|0,50|9,8|0,17|
|4|2|0,0|1,43|0,71|14,0|0,24|
|5|4|0,0|2,00|1,00|19,6|0,34|
|6|6|0,0|2,57|1,29|25,3|0,44|
|7|8|0,0|3,29|1,64|32,3|0,56|
|8|10|0,0|4,00|2,00|39,3|0,68|
|9|12|0,0|4,86|2,43|47,7|0,83|
|10|14|0,0|5,71|2,86|56,1|0,97|

**Compensação por vários requisitos** (cada Atributo exigido é um Atributo diferente):

|Requisitos (valores)|Nível mínimo (LA)|PAs forçados (alinhado)|PAs forçados (aleatório)|PAs forçados (efetivo)|Compensação (pt/Encontro)|Compensação (PHs)|
|---|---|---|---|---|---|---|
|4 + 4|2|0,0|2,86|1,43|28,1|0,49|
|5 + 5|4|0,0|4,00|2,00|39,3|0,68|
|6 + 6|6|0,0|5,14|2,57|50,5|0,88|
|8 + 8|10|0,0|8,00|4,00|78,6|1,36|
|10 + 10|14|2,0|11,43|6,71|131,9|2,29|
|5 + 5 + 5|4|0,0|6,00|3,00|58,9|1,02|
|8 + 6 + 4|10|0,0|8,00|4,00|78,6|1,36|
|10 + 8 + 6|14|0,0|12,29|6,14|120,7|2,09|
|8 + 8 + 8|10|2,0|12,00|7,00|137,5|2,38|
|10 + 10 + 10|14|6,0|17,14|11,57|227,4|3,94|
|6 + 6 + 6 + 6|6|2,0|10,29|6,14|120,7|2,09|

Se, mesmo assim, você quiser um desconto de PM em vez de mais poder, divida a compensação (em pt/Encontro) pelos usos por Encontro da magia (≈ 3). Por exemplo, um requisito de 10 em um Atributo equivale a ≈ 18,7 pt de desconto por uso. Mas eu não recomendo.