Este documento atribui uma **pontuação** a cada efeito que uma Habilidade pode ter, para que o custo de Mana de cada Habilidade possa ser calculado depois, somando os pontos dos seus efeitos. Aqui ainda **não há conversão para PMs**: a primeira etapa é só garantir que os efeitos estejam proporcionais entre si e testar como os valores se comportam com cada duração.

Todos os números foram derivados do Balanceamento (cenário típico no Nível 20, Rodada de 3 Ações, Encontro de 4 Rodadas). Eles estão no fim, em §2, como premissas explícitas. Se uma premissa mudar, os valores mudam com ela.

## 1. A unidade: o ponto (pt)

- **1 pt = 1 PV de dano causado** a um inimigo (≈ 1 PM de custo, quando a conversão for feita).
- **1 PV curado, absorvido ou evitado vale 3 pt.** Motivo: um monstro Médio de Nível 20 tem 980 PVs e causa ≈ 309 de dano por Encontro (77,4 × 4 Rodadas), ou seja, ≈ 3,2× mais PVs do que dano. Cada PV de dano que você causa remove ≈ 0,31 PV de dano futuro que ele causaria; logo, para valer o mesmo, 1 PV de dano evitado precisa ser contado como ≈ 3 PVs de dano causado.
- Esse fator (3) é o **botão principal** do sistema. Ele afeta: Cura, PV Temporários, Resistência, +1 de CA, +1 de BA em Salvaguardas e +1 de cura. Ele **não** afeta: Dano, BA em Ataques, BD, Ação, Deslocamento e PMs. Se você preferir que 1 PV curado valha o mesmo que 1 PV de dano, basta dividir essas seis linhas por 3 (ver §7).

## 2. Premissas (Nível 20)

| Premissa | Valor | Origem |
|---|---|---|
| Dano-alvo do PDJ por Rodada | 60 | Balanceamento |
| Ataques por Rodada / chance média de acerto | 3 / 65% (≈ 1,95 acertos) | Balanceamento (cenário típico) |
| Dano por acerto | ≈ 30,8 | 60 ÷ 1,95 |
| Dano recebido por PDJ por Rodada | 19,35 | 10% do total do grupo (77,4) ÷ 4 PDJs |
| Instâncias de dano recebidas por Rodada | ≈ 0,63 | 19,35 ÷ 30,8 |
| Variação de +1 de BA ou CA | +5 pp (≈ +7,7% do valor relativo) | d20, chance base de 65% |
| Valor de 1 Ação | 20 pt | 60 ÷ 3 Ações |
| PM gastos por Turno | ≈ 12 | suposição (ajustar quando a tabela de PMs existir) |
| Duração de um Encontro | 4 Rodadas | Balanceamento |

## 3. Valores base

| Efeito | Pontos | Unidade de contagem | Confiança |
|---|---|---|---|
| +1 de BA em Ataques | 4,6 | por Turno próprio | Alta |
| +1 de BA em Salvaguardas (todas) | 2,2 | por ciclo de inimigos (Rodada) | Média |
| +1 de BA em Testes de Perícia | 1,0 | por Turno próprio (em combate) | Baixa |
| **+1 de BA geral** (Ataques + Salvaguardas + Perícias) | 7,8 | Rodada (soma das três linhas acima) | Média |
| +1 de CA | 4,5 | por ciclo de inimigos (Rodada) | Alta |
| +1 de BD (dano por instância) | 2,0 (1,0 por instância) | por Turno próprio (≈1,95 acertos) | Alta |
| +1 de cura (por instância de cura) | 3,0 | por instância de cura recebida | Alta |
| +1 de Resistência (por instância de dano) | 1,9 por Rodada | por ciclo de inimigos (≈0,63 instâncias/Rodada) | Média |
| +1,5 m de Deslocamento | 1,7 | por Turno próprio | Baixa |
| −1,5 m de Deslocamento (debuff no inimigo) | 1,3 | por Turno do inimigo | Baixa |
| +1,5 m de alcance em Ataques corpo a corpo | 2,0 | por Turno próprio | Baixa |
| +1,5 m de alcance em Ataques Mágicos | 0,5 | por Turno próprio | Baixa |
| +1,5 m de alcance em magias de área (distância até o ponto) | 0,5 | por Turno próprio | Baixa |
| *(extra)* +1,5 m no raio de uma magia de área | 4,0 | por Turno próprio, se você usa área com frequência | Muito baixa |
| Terreno Difícil em área circular de raio 1,5 m | 2,0 | por Turno de inimigo (≈1,5 criaturas atravessando) | Baixa |
| **+1 Ação no Turno** | 20,0 | por Turno próprio (Ação não-Ataque) | Alta (como teto) |
| +1 Ação Bônus extra (no próximo Turno do alvo) | 7,0 | por Turno do alvo | Baixa |
| +1 Reação extra (nessa Rodada, resto dela) | 2,4 (4,8 por Rodada cheia) | uma vez | Baixa |
| 1 de dano contínuo | 1,0 por instância | ver §5.4: 1 + Turnos do alvo afetados | Alta |

Leitura rápida:
- **+1 de BA em Ataques (4,6) e +1 de CA (4,5) saem praticamente iguais.** Isso não foi forçado: sai da razão entre PVs do monstro e dano que ele causa (o fator 3). É um bom sinal de que o sistema de BA/CA está coerente.
- **+1 Ação (20 pt) vale ≈ 2,6× o +1 de BA geral e ≈ 4× o +1 de BA em Ataques.** É de longe o efeito mais forte da lista e deve ser o mais caro (ver §7).
- Os efeitos de **posicionamento** (Deslocamento, alcances, Terreno Difícil) são os de menor confiança: o valor depende de mapa e de tática, não de números.

## 4. Valor de cada Grau

Os valores são do **dado do Grau** (média), sem modificadores. "Garantido" assume que não há teste. Efeitos com Ataque devem usar a coluna de ×0,65; efeitos com Salvaguarda ficam entre as duas colunas, dependendo do dano em caso de sucesso.

| Grau | Dado | Média | Dano (garantido) | Dano (com Ataque, ×0,65) | Cura (PV) | PM restaurados | PV Temp. (valor máx.) | PM Temp. (valor máx.) |
|---|---|---|---|---|---|---|---|---|
| 1 | 1d4 | 2,5 | 2,5 | 1,6 | 7,5 | 2,5 | 7,5 | 2,5 |
| 2 | 1d6 | 3,5 | 3,5 | 2,3 | 10,5 | 3,5 | 10,5 | 3,5 |
| 3 | 1d8 | 4,5 | 4,5 | 2,9 | 13,5 | 4,5 | 13,5 | 4,5 |
| 4 | 1d10 | 5,5 | 5,5 | 3,6 | 16,5 | 5,5 | 16,5 | 5,5 |
| 5 | 1d12 | 6,5 | 6,5 | 4,2 | 19,5 | 6,5 | 19,5 | 6,5 |
| 6 | 2d6 | 7,0 | 7,0 | 4,5 | 21,0 | 7,0 | 21,0 | 7,0 |
| 7 | 2d8 | 9,0 | 9,0 | 5,9 | 27,0 | 9,0 | 27,0 | 9,0 |
| 8 | 2d10 | 11,0 | 11,0 | 7,2 | 33,0 | 11,0 | 33,0 | 11,0 |
| 9 | 2d12 | 13,0 | 13,0 | 8,5 | 39,0 | 13,0 | 39,0 | 13,0 |
| 10 | 3d10 | 16,5 | 16,5 | 10,7 | 49,5 | 16,5 | 49,5 | 16,5 |

Observações:
- "PV Temp. (valor máx.)" e "PM Temp. (valor máx.)" são o valor se **todos** os pontos forem usados. Na prática eles expiram, e o valor real depende da duração (§5.3).
- Cura vale 3× o Dano do mesmo Grau. Um Grau de cura tem que custar proporcionalmente mais que um Grau de dano.
- PMs restaurados valem 1 pt cada, pois essa é a definição da unidade, e (Descanso à parte) são o único efeito 1:1 com o custo.

## 5. Testes por duração

### 5.1 Como a duração é contada

Todas as durações assumem que o efeito é ativado **no seu Turno** e que uma Rodada "conta a atual" (regra do sistema), então a Rodada em que você ativa vale por meia Rodada, em média (a ordem de Iniciativa decide o resto).

| Duração | O (Turnos seus afetados) | I (ciclos de inimigos que o alvo enfrenta) | Ti (Turnos do inimigo afetados) | O' (Turnos com +1 Ação) |
|---|---|---|---|---|
| 1 Rodada | 0,5 | 0,5 | 0,5 | 1,0 |
| 2 Rodadas | 1,5 | 1,5 | 1,5 | 2,0 |
| 3 Rodadas | 2,5 | 2,5 | 2,5 | 3,0 |
| 4 Rodadas | 3,5 | 3,5 | 3,5 | 4,0 |
| 1 Encontro | 4,0 | 4,0 | 4,0 | 4,0 |
| Até o início do seu próx. Turno | 0,5 | 1,0 | 1,0 | 1,0 |
| Até o fim do próx. Turno do alvo (você) | 1,5 | 1,5 | 1,5 | 2,0 |
| Até o fim do próx. Turno do alvo (aliado) | 1,0 | 1,5 | 1,5 | 1,0 |

- **O** conta seus Turnos (o Turno de ativação conta 0,5, pois a ativação já gastou parte dele). **I** é a exposição a ataques: vale para CA, Resistência e PV Temporários. **Ti** conta quantos Turnos do inimigo passam sob o efeito, e vale para debuffs e dano contínuo.
- **1 Encontro** é tratado como 4 Rodadas cheias, porque efeitos de Encontro costumam ser ativados antes ou no início do combate.
- Para o **aliado**, o "fim do próximo Turno do alvo" dá 1,0 Turno de benefício ofensivo (o Turno dele), mas ainda 1,5 de exposição.
- **+1 Ação** usa O' (não O): a Ação extra vale inteira no Turno em que for concedida, independentemente de ter sido ativada no meio dele.

### 5.2 Efeitos de bônus × duração (pontos totais)

| Efeito | 1 Rod. | 2 Rod. | 3 Rod. | 4 Rod. | Encontro | Até ini. próx. Turno | Fim próx. Turno do alvo (você) | Fim próx. Turno do alvo (aliado) |
|---|---|---|---|---|---|---|---|---|
| +1 BA em Ataques | 2,3 | 6,9 | 11,5 | 16,2 | 18,5 | 2,3 | 6,9 | 4,6 |
| +1 BA em Salvaguardas | 1,1 | 3,3 | 5,6 | 7,8 | 8,9 | 2,2 | 3,3 | 3,3 |
| +1 BA em Perícias | 0,5 | 1,5 | 2,5 | 3,5 | 4,0 | 0,5 | 1,5 | 1,0 |
| **+1 BA geral** | 3,9 | 11,8 | 19,6 | 27,5 | 31,4 | 5,0 | 11,8 | 9,0 |
| +1 CA | 2,2 | 6,7 | 11,2 | 15,6 | 17,9 | 4,5 | 6,7 | 6,7 |
| +1 BD | 1,0 | 2,9 | 4,9 | 6,8 | 7,8 | 1,0 | 2,9 | 2,0 |
| +1 de cura (0,5 inst./Rodada) | 0,8 | 2,2 | 3,8 | 5,2 | 6,0 | 1,5 | 2,2 | 2,2 |
| +1 Resistência | 0,9 | 2,8 | 4,7 | 6,6 | 7,5 | 1,9 | 2,8 | 2,8 |
| +1,5 m Deslocamento | 0,8 | 2,5 | 4,2 | 5,8 | 6,7 | 0,8 | 2,5 | 1,7 |
| +1,5 m alcance corpo a corpo | 1,0 | 3,0 | 5,0 | 7,0 | 8,0 | 1,0 | 3,0 | 2,0 |
| +1,5 m alcance Ataque Mágico | 0,2 | 0,8 | 1,2 | 1,8 | 2,0 | 0,2 | 0,8 | 0,5 |
| +1,5 m alcance de área | 0,2 | 0,8 | 1,2 | 1,8 | 2,0 | 0,2 | 0,8 | 0,5 |
| +1,5 m raio de área | 2,0 | 6,0 | 10,0 | 14,0 | 16,0 | 2,0 | 6,0 | 4,0 |
| **+1 Ação no Turno** | 20,0 | 40,0 | 60,0 | 80,0 | 80,0 | 20,0 | 40,0 | 20,0 |
| +1 Ação Bônus extra por Turno | 7,0 | 14,0 | 21,0 | 28,0 | 28,0 | 7,0 | 14,0 | 7,0 |
| +1 Reação extra por Rodada | 2,4 | 7,2 | 12,0 | 16,8 | 19,2 | 4,8 | 7,2 | 7,2 |

### 5.3 Graus como PV Temporários, PM Temporários e Resistência × duração (pontos totais)

PV e PM Temporários são **gastos conforme o dano ou o custo aparecem**, e o que sobrar ao fim da duração se perde. Para refletir isso, o valor é "o que você realmente usa": `μ · (1 − e^(−X/μ))`, com X o valor do Grau e μ a média do que seria consumido na janela (μ = I × 19,35 PVs para PV; μ = O × 12 PMs para PM). O resultado de PV é multiplicado por 3 e o de PM por 1.

**PV Temporários**

| Grau | 1 Rod. | 2 Rod. | 3 Rod. | 4 Rod. | Encontro | Até ini. próx. Turno | Fim próx. Turno do alvo (você) | Fim próx. Turno do alvo (aliado) |
|---|---|---|---|---|---|---|---|---|
| Grau 1 (1d4) | 6,6 | 7,2 | 7,3 | 7,4 | 7,4 | 7,0 | 7,2 | 7,2 |
| Grau 2 (1d6) | 8,8 | 9,9 | 10,1 | 10,2 | 10,3 | 9,6 | 9,9 | 9,9 |
| Grau 3 (1d8) | 10,8 | 12,5 | 12,9 | 13,1 | 13,1 | 12,0 | 12,5 | 12,5 |
| Grau 4 (1d10) | 12,6 | 15,0 | 15,6 | 15,8 | 15,9 | 14,4 | 15,0 | 15,0 |
| Grau 5 (1d12) | 14,2 | 17,5 | 18,2 | 18,6 | 18,7 | 16,6 | 17,5 | 17,5 |
| Grau 6 (2d6) | 14,9 | 18,7 | 19,6 | 20,0 | 20,1 | 17,6 | 18,7 | 18,7 |
| Grau 7 (2d8) | 17,6 | 23,2 | 24,6 | 25,3 | 25,5 | 21,6 | 23,2 | 23,2 |
| Grau 8 (2d10) | 19,7 | 27,5 | 29,5 | 30,5 | 30,8 | 25,2 | 27,5 | 27,5 |
| Grau 9 (2d12) | 21,5 | 31,4 | 34,2 | 35,5 | 35,9 | 28,4 | 31,4 | 31,4 |
| Grau 10 (3d10) | 23,8 | 37,8 | 41,9 | 43,9 | 44,6 | 33,3 | 37,8 | 37,8 |

**PM Temporários**

| Grau | 1 Rod. | 2 Rod. | 3 Rod. | 4 Rod. | Encontro | Até ini. próx. Turno | Fim próx. Turno do alvo (você) | Fim próx. Turno do alvo (aliado) |
|---|---|---|---|---|---|---|---|---|
| Grau 1 (1d4) | 2,0 | 2,3 | 2,4 | 2,4 | 2,4 | 2,0 | 2,3 | 2,3 |
| Grau 2 (1d6) | 2,7 | 3,2 | 3,3 | 3,4 | 3,4 | 2,7 | 3,2 | 3,0 |
| Grau 3 (1d8) | 3,2 | 4,0 | 4,2 | 4,3 | 4,3 | 3,2 | 4,0 | 3,8 |
| Grau 4 (1d10) | 3,6 | 4,7 | 5,0 | 5,2 | 5,2 | 3,6 | 4,7 | 4,4 |
| Grau 5 (1d12) | 4,0 | 5,5 | 5,8 | 6,0 | 6,1 | 4,0 | 5,5 | 5,0 |
| Grau 6 (2d6) | 4,1 | 5,8 | 6,2 | 6,4 | 6,5 | 4,1 | 5,8 | 5,3 |
| Grau 7 (2d8) | 4,7 | 7,1 | 7,8 | 8,1 | 8,2 | 4,7 | 7,1 | 6,3 |
| Grau 8 (2d10) | 5,0 | 8,2 | 9,2 | 9,7 | 9,8 | 5,0 | 8,2 | 7,2 |
| Grau 9 (2d12) | 5,3 | 9,3 | 10,5 | 11,2 | 11,4 | 5,3 | 9,3 | 7,9 |
| Grau 10 (3d10) | 5,6 | 10,8 | 12,7 | 13,6 | 14,0 | 5,6 | 10,8 | 9,0 |

**Resistência** (cada Grau vale a média do dado por instância de dano; mínimo de 1 de dano por instância continua valendo)

| Grau | 1 Rod. | 2 Rod. | 3 Rod. | 4 Rod. | Encontro | Até ini. próx. Turno | Fim próx. Turno do alvo (você) | Fim próx. Turno do alvo (aliado) |
|---|---|---|---|---|---|---|---|---|
| Grau 1 (1d4) | 2,4 | 7,1 | 11,8 | 16,5 | 18,9 | 4,7 | 7,1 | 7,1 |
| Grau 2 (1d6) | 3,3 | 9,9 | 16,5 | 23,1 | 26,4 | 6,6 | 9,9 | 9,9 |
| Grau 3 (1d8) | 4,2 | 12,7 | 21,2 | 29,7 | 34,0 | 8,5 | 12,7 | 12,7 |
| Grau 4 (1d10) | 5,2 | 15,6 | 25,9 | 36,3 | 41,5 | 10,4 | 15,6 | 15,6 |
| Grau 5 (1d12) | 6,1 | 18,4 | 30,7 | 42,9 | 49,1 | 12,3 | 18,4 | 18,4 |
| Grau 6 (2d6) | 6,6 | 19,8 | 33,0 | 46,2 | 52,8 | 13,2 | 19,8 | 19,8 |
| Grau 7 (2d8) | 8,5 | 25,5 | 42,4 | 59,4 | 67,9 | 17,0 | 25,5 | 25,5 |
| Grau 8 (2d10) | 10,4 | 31,1 | 51,9 | 72,6 | 83,0 | 20,8 | 31,1 | 31,1 |
| Grau 9 (2d12) | 12,3 | 36,8 | 61,3 | 85,8 | 98,1 | 24,5 | 36,8 | 36,8 |
| Grau 10 (3d10) | 15,6 | 46,7 | 77,8 | 109,0 | 124,5 | 31,1 | 46,7 | 46,7 |

Leitura:
- O PV Temporário perde pouco valor com a duração, porque cada acerto inimigo (≈ 31 PVs) é bem maior que o Grau: ex.: Grau 3 vale 10,8 em 1 Rodada e 13,1 em 1 Encontro, contra 13,5 da cura (≈ 80% e ≈ 97%). Isso muda se os PV Temporários forem grandes ou se o inimigo causar dano pequeno e frequente.
- O **PM Temporário** perde mais valor que o PV Temporário em durações curtas (Grau 3: ≈ 70% em 1 Rodada), porque você gasta ≈ 12 PMs por Turno e pouco desse gasto cabe na janela.
- A **Resistência** cresce de forma quase linear com a duração e passa o PV Temporário do mesmo Grau a partir de ≈ 1,5 Rodada (ex.: Grau 3: 12,7 contra 12,5).

### 5.4 Debuffs e dano contínuo (alvo inimigo)

**Dano contínuo** causa uma instância imediata e uma no início de cada Turno do alvo. Então 1 de dano contínuo por uma duração vale **1 + Ti** instâncias. Assume-se que cada instância rola novamente o dado do Grau. O dano contínuo não faz teste de acerto, então vale o valor "garantido", e o mínimo de 1 de dano por instância o protege de Resistência.

| Efeito | 1 Rod. | 2 Rod. | 3 Rod. | 4 Rod. | Encontro | Até ini. próx. Turno | Fim próx. Turno do alvo |
|---|---|---|---|---|---|---|---|
| 1 de dano contínuo | 1,5 | 2,5 | 3,5 | 4,5 | 5,0 | 2,0 | 2,0 |
| Grau 1 (1d4) | 3,8 | 6,2 | 8,8 | 11,2 | 12,5 | 5,0 | 5,0 |
| Grau 2 (1d6) | 5,2 | 8,8 | 12,2 | 15,8 | 17,5 | 7,0 | 7,0 |
| Grau 3 (1d8) | 6,8 | 11,2 | 15,8 | 20,2 | 22,5 | 9,0 | 9,0 |
| Grau 4 (1d10) | 8,2 | 13,8 | 19,2 | 24,8 | 27,5 | 11,0 | 11,0 |
| Grau 5 (1d12) | 9,8 | 16,2 | 22,8 | 29,2 | 32,5 | 13,0 | 13,0 |
| Grau 6 (2d6) | 10,5 | 17,5 | 24,5 | 31,5 | 35,0 | 14,0 | 14,0 |
| Grau 7 (2d8) | 13,5 | 22,5 | 31,5 | 40,5 | 45,0 | 18,0 | 18,0 |
| Grau 8 (2d10) | 16,5 | 27,5 | 38,5 | 49,5 | 55,0 | 22,0 | 22,0 |
| Grau 9 (2d12) | 19,5 | 32,5 | 45,5 | 58,5 | 65,0 | 26,0 | 26,0 |
| Grau 10 (3d10) | 24,8 | 41,2 | 57,8 | 74,2 | 82,5 | 33,0 | 33,0 |

**Debuffs de posição**

| Efeito (alvo inimigo) | 1 Rod. | 2 Rod. | 3 Rod. | 4 Rod. | Encontro | Até ini. próx. Turno | Fim próx. Turno do alvo |
|---|---|---|---|---|---|---|---|
| −1,5 m Deslocamento | 0,7 | 2,0 | 3,3 | 4,7 | 5,3 | 1,3 | 1,3 |
| Terreno Difícil (raio 1,5 m) | 1,0 | 3,0 | 5,0 | 7,0 | 8,0 | 2,0 | 2,0 |

### 5.5 Ação Bônus e Reação extras

- **+1 Ação Bônus** (além da gratuita): uma Ação Bônus não causa dano nem controle, então vale ≈ 70% de uma Ação (14,0 pt) quando há o que fazer com ela, e a chance de haver uma segunda opção útil no mesmo Turno é de ≈ 50%. Valor: 20 × 0,7 × 0,5 = **7,0 pt por Turno**. "No próximo Turno do alvo" é um Turno só, logo **7,0 pt**. É um efeito barato porque hoje há poucas opções de Ação Bônus: se o Capítulo 5 criar muitas, esse valor sobe para até 14 pt.
- **+1 Reação**: uma Reação usada vale ≈ 12 pt (mistura de Ataque de Oportunidade, ≈ 20 pt, e reações defensivas, menores). Como a Reação base já cobre o gatilho mais comum, a segunda só é usada em ≈ 40% das Rodadas: **4,8 pt por Rodada cheia**. "Nessa Rodada" (o resto dela, ≈ 0,5 Rodada) vale **2,4 pt**, que é exatamente a coluna "1 Rod." da tabela de §5.2. Se o alvo ainda não gastou a Reação base, a extra vale quase nada; se já gastou, vale o valor cheio.

## 6. Como os valores mudam com o Nível

Efeitos **proporcionais** (BA, CA, Salvaguarda) escalam com o dano e a vida da época, então foram escalados linearmente por Nível/20 (aproximação grosseira, melhor substituída pela tabela de dano por Nível quando ela existir). Efeitos **fixos** (BD, +1 de cura, +1 de Resistência) não mudam em pontos, porque 1 PV é 1 PV em qualquer Nível.

| Nível | +1 BA (Ataque) | +1 CA | +1 BA Salv. | +1 BD | +1 cura | +1 Resist. |
|---|---|---|---|---|---|---|
| 1 | 0,2 | 0,2 | 0,1 | 2,0 | 3,0 | 1,9 |
| 5 | 1,2 | 1,1 | 0,6 | 2,0 | 3,0 | 1,9 |
| 10 | 2,3 | 2,2 | 1,1 | 2,0 | 3,0 | 1,9 |
| 15 | 3,5 | 3,3 | 1,7 | 2,0 | 3,0 | 1,9 |
| 20 | 4,6 | 4,5 | 2,2 | 2,0 | 3,0 | 1,9 |

Isso mostra um problema a decidir: **em Nível 1, +1 de BD vale ≈ 8× mais que +1 de BA** e +1 de BA vale bem menos do que um Grau 1 de dano. Duas saídas: (a) cobrar o BD e a Resistência fixos em PMs mais altos nos níveis baixos; ou (b) aceitar que bônus fixos são fortes no começo e marcá-los como "poder de início".

## 7. Observações e alertas de design

1. **+1 Ação é o efeito mais caro.** 20 pt por Turno só no valor médio, e um 4º Ataque com a Penalidade de −5 cumulativa vale bem menos que uma Ação "comum" (≈ 25% do valor), mas ainda há opções melhores (conjurar, usar Habilidade, mover-se). Sugestão: custar 20 pt por Turno e/ou restringir a Ação a Habilidades e Movimentação, não a Ataques.
2. **Cura vale 3× dano por PV.** Essa é a decisão que o sistema precisa confirmar. Se for 1:1, o Grau de cura custa o mesmo que o Grau de dano, e o PV Temporário e a Resistência ficam ≈ 3× mais baratos. Se for 3:1, cura é cara e dano é barato. Meu palpite é que 2:1 (um meio-termo) pode ser mais confortável, mas eu preferi manter o 3:1 por ser o único valor derivado dos números do Balanceamento.
3. **PV Temporário e PM Temporário** nunca valem o valor máximo. Cobrar pelo valor máximo faz com que eles sejam ruins em durações curtas. Sugiro cobrar pelo valor das tabelas de §5.3.
4. **Dano contínuo** é um bom "dano por PM": rende o valor integral sem teste de acerto e ignora Resistência pequena. Em durações de Encontro, 1 de dano contínuo vale 5 pt, quase um Grau 4 de dano direto. Talvez valha um desconto de ≈ 15% no custo (porque o alvo pode morrer ou ser curado antes do fim).
5. **+1 BA geral ≈ 7,8 pt/Rodada** vs **+1 BA em Ataques ≈ 4,6**. O "geral" só deve ser cobrado como geral se realmente cobrir os três usos.
6. **Cura contínua / Regeneração** (cura por Turno) ainda não existe na lista, mas segue a mesma lógica do dano contínuo: valor do Grau × 3 × (1 + Turnos).

## 8. Pontos em aberto

- Confirmar a **razão cura:dano** (3:1, 2:1 ou 1:1).
- Confirmar que o **dano contínuo rola o dado do Grau a cada instância** (ou se o valor é fixo na aplicação).
- Confirmar o que significa **"alcance de magias de área"**: distância até o ponto de origem (como assumi) ou raio (valor extra em §3).
- Confirmar o gasto médio de PMs por Turno (usei 12) quando houver uma tabela de PMs por Nível.
- Estes efeitos ainda não estão na lista e entram quando você quiser: −1 de BA/CA no inimigo, Vantagem/Desvantagem, Condições (Atordoado, Caído, Agarrado etc.), cura contínua, teletransporte, invisibilidade, aumentar/diminuir Margem de Ameaça.
- Conversão de pontos em PMs: próximo passo, depois que os pontos estiverem aprovados.
- O custo em PHs de Habilidades usa estes pontos e está em `Custo de PHs.md`.

## 9. Requisitos de Atributo e o custo de PM

**Resposta curta: os requisitos de Atributo não devem diminuir o custo de PM.** Eles devem **aumentar o poder permitido da Habilidade** (ver `Custo de PHs.md`). Quatro razões:

1. **Pagamentos diferentes.** O requisito é pago uma vez, ao adquirir a Habilidade (em PAs). O PM é pago a cada uso. Um desconto por uso pagaria uma restrição permanente de forma desigual: quem usa mais vezes recebe mais desconto.
2. **Dupla contagem.** A maioria das magias já escala com o Modificador do Atributo exigido (BA, BD, CD). Quem tem o Atributo alto já ganha uma magia mais forte; baixar o custo também seria pagar duas vezes.
3. **O requisito é, antes de tudo, um portão de Nível.** Com LA = Nível/2 + 3, um requisito de valor R só pode ser cumprido a partir do Nível 2 × (R − 3) (ex.: 6 no Nível 6, 10 no Nível 14). Isso já tira da frente as Habilidades fortes nos níveis baixos sem custo nenhum de PM.
4. **O custo real é de oportunidade, e é pequeno.** Um requisito só custa o que o personagem **não** teria investido de qualquer forma. Considerei: build típico no Nível 20 com 30 PAs (10, 8, 6, 4, 2, 0, 0); metade dos jogadores escolhe a Habilidade já alinhada ao seu build (custo 0 se o requisito é ≤ 10 no atributo principal) e metade acaba exigindo um Atributo que não seria prioridade. Cada PA forçado fora do plano custa ≈ 7,9 pt por Encontro (metade de um Modificador de ataque, com 60% de perda efetiva, em 4 Rodadas).

**Compensação por um requisito** (1 PH = 18 pt/Encontro):

| Requisito (valor) | Nível mínimo (LA) | PAs forçados (build alinhado) | PAs forçados (atributo aleatório) | PAs forçados (efetivo) | Compensação (pt/Encontro) | Compensação (PHs) |
|---|---|---|---|---|---|---|
| 1 | 1 | 0,0 | 0,29 | 0,14 | 1,1 | 0,06 |
| 2 | 1 | 0,0 | 0,57 | 0,29 | 2,3 | 0,13 |
| 3 | 1 | 0,0 | 1,00 | 0,50 | 3,9 | 0,22 |
| 4 | 2 | 0,0 | 1,43 | 0,71 | 5,6 | 0,31 |
| 5 | 4 | 0,0 | 2,00 | 1,00 | 7,9 | 0,44 |
| 6 | 6 | 0,0 | 2,57 | 1,29 | 10,1 | 0,56 |
| 7 | 8 | 0,0 | 3,29 | 1,64 | 12,9 | 0,72 |
| 8 | 10 | 0,0 | 4,00 | 2,00 | 15,8 | 0,88 |
| 9 | 12 | 0,0 | 4,86 | 2,43 | 19,1 | 1,06 |
| 10 | 14 | 0,0 | 5,71 | 2,86 | 22,5 | 1,25 |

**Compensação por vários requisitos** (cada Atributo exigido é um Atributo diferente):

| Requisitos (valores) | Nível mínimo (LA) | PAs forçados (alinhado) | PAs forçados (aleatório) | PAs forçados (efetivo) | Compensação (pt/Encontro) | Compensação (PHs) |
|---|---|---|---|---|---|---|
| 4 + 4 | 2 | 0,0 | 2,86 | 1,43 | 11,3 | 0,63 |
| 5 + 5 | 4 | 0,0 | 4,00 | 2,00 | 15,8 | 0,88 |
| 6 + 6 | 6 | 0,0 | 5,14 | 2,57 | 20,3 | 1,13 |
| 8 + 8 | 10 | 0,0 | 8,00 | 4,00 | 31,5 | 1,75 |
| 10 + 10 | 14 | 2,0 | 11,43 | 6,71 | 52,9 | 2,94 |
| 5 + 5 + 5 | 4 | 0,0 | 6,00 | 3,00 | 23,6 | 1,31 |
| 8 + 6 + 4 | 10 | 0,0 | 8,00 | 4,00 | 31,5 | 1,75 |
| 10 + 8 + 6 | 14 | 0,0 | 12,29 | 6,14 | 48,4 | 2,69 |
| 8 + 8 + 8 | 10 | 2,0 | 12,00 | 7,00 | 55,1 | 3,06 |
| 10 + 10 + 10 | 14 | 6,0 | 17,14 | 11,57 | 91,2 | 5,06 |
| 6 + 6 + 6 + 6 | 6 | 2,0 | 10,29 | 6,14 | 48,4 | 2,69 |

Se, mesmo assim, você quiser um desconto de PM em vez de mais poder, divida a compensação (em pt/Encontro) pelos usos por Encontro da magia (≈ 3). Por exemplo, um requisito de 10 em um Atributo equivale a ≈ 7,5 pt de desconto por uso. Mas eu não recomendo.
