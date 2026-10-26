# Nirvana RPG — Relatório de Problemas e Inconsistências

Cada item aponta o **arquivo exato**, a **seção** e o **problema**. Os caminhos são relativos à pasta `Nirvana RPG/`, e usei atalhos para as pastas mais repetidas:

| Atalho | Pasta |
|---|---|
| **[F]** | `Capítulo 1 - Fundamentos/` |
| **[C2]** | `Capítulo 2 - Criação de Personagens/` |
| **[R]** | `Capítulo 3 - Raças/Capítulo 3.2 - Lista de Raças/` |
| **[E]** | `Capítulo 4 - Equipamentos/` |
| **[H]** | `Capítulo 5 - Habilidades/Capítulo 5.1 - Lista de Habilidades/` |
| **[M]** | `Capítulo 6 - Magias/` |
| **[L]** | `Capítulo 6 - Magias/Capítulo 6.1 - Lista de Magias Por Atributo/` |

Tipos: **Contradição** (dois trechos se negam), **Lacuna** (falta regra ou arquivo), **Ambiguidade** (mais de uma leitura possível), **Exploit** (brecha de regras) e **Balanceamento** (subjetivo).

Observação: só analisei os arquivos enviados. A lista de magias por Sabedoria, se existir, não estava entre eles.

---

## A. Contradições diretas

**A1 — Dado de Vida com Con 1** · Contradição
- `[F]Capítulo 1.11 - Descansos.md`, seção *Descanso Curto*: diz que com 1 de Constituição o Dado de Vida é 1d8.
- `[C2]Capítulo 2 - Criação de Personagens.md`, seção *Pontos de Vida* (tabela): Con 1 dá 1d6, e 1d8 só começa em Con 2.

**A2 — Limite máximo de Atributo** · Contradição
- `[F]Capítulo 1.3 - Atributos.md`, logo após a tabela: a fórmula "metade do seu Nível de Personagem acrescido de 3" dá 11 no Nível 16 e 13 no Nível 20.
- A tabela do mesmo arquivo trava o limite em 10 a partir do Nível 14.

**A3 — CA do esqueleto/zumbi** · Contradição
- `[M]Sortilégios/Custo 2.md`, magia *Animar os Mortos*: o texto diz "CA 12" e, duas frases depois, "13 de CA".

**A4 — Bônus de Amado Coiote** · Contradição
- `[H]Bardo.md`, habilidade *Amado Coiote*: concede "+5", mas o fim da descrição fala em "bônus padrão de +4".

**A5 — Transformações "independentes" do Nível e dos Atributos** · Contradição
- `Capítulo 7 - Transformações/Capítulo 7 - Transformações.md`: diz que elas "não levam em consideração o Nível do seu personagem, seus Atributos".
- `Capítulo 7 - Transformações/Capítulo 7.1 - Vampirismo.md`: *Mordida Demoníaca* usa "CD é 10 + metade do seu Nível", e *Nobreza* concede Pontos de Atributo extras.
- `Capítulo 7 - Transformações/Capítulo 7.2 - Licantropia.md`: usa CDs com For + Car (*Intimidar* e *Sangue Puro*), *Salto Bestial* usa "12 + Força" e *Mordida* soma o Modificador de Constituição.

**A6 — Custo de Habilidade fora de 1 a 3** · Contradição
- `Capítulo 5 - Habilidades/Capítulo 5 - Habilidades.md`: diz que o custo "pode variar entre 1 e 3".
- `[H]Guerreiro (Arcano).md`, *Sol* e *Lua*: custam 6 se você já tem a outra.
- `[H]Especialista.md`, *Polivalente* (parte *Elementar*): o custo vira o dobro do natural (ex.: 6).

**A7 — Custo de Margem de Ameaça Reversa** · Possível erro
- `[H]Mundano.md`, *Margem de Ameaça Reversa* (Custo 2): "na terceira vez ela custará 1 Ponto de Habilidade", ou seja, menos que o Custo 2 original. Provável erro de digitação.

**A8 — Exemplo de Pontos Retroativos** · Contradição
- `[C2]Capítulo 2.2 - Níveis.md`, seção *Pontos Retroativos*: o exemplo fala em "1 Ponto de Vida adicional para cada Nível **além do** 20" e conclui "19 Pontos de Vida". O texto não bate com a conta (provavelmente deveria ser "até o 20").

**A9 — Pré-requisito de Habilidade inexistente** · Contradição
- `[H]Alquimista.md`, *Alquimista Mágico*: exige "Artesão de Itens Arremessáveis". A habilidade se chama **Artesão de Bombas** (no mesmo arquivo).

**A10 — Gnomo da Natureza: PV do escudo e vulnerabilidade a Fogo** · Contradição
- `[R]Gnomo.md`, *Espíritos da Floresta* (Primeira Forma): fala em "Pontos de Vida Máximos garantidos pelo Escudo", mas as regras de Escudo (`[E]Capítulo 4 - Equipamentos.md`) não dão PV.
- `[H]Parágono.md`, *Floresta Interior*: cita uma "vulnerabilidade a Dano de Fogo na primeira forma" que não existe em `Gnomo.md`.

**A11 — Autômato é "objeto" mas age sozinho** · Contradição
- `[H]Artífice.md`, *Autômatos Menores, Medianos e Maiores*: "Autômatos criados por você são considerados objetos", mas os Medianos "lutam ou agem por conta própria".
- `[F]Capítulo 1.9 - Elementos do Cenário.md`, seção *Objetos*: objeto não "realiza ações por conta própria".
- `[R]Fjer.md`, *Troca de Corpo*: só pode possuir objetos, então a classificação muda o que o Fjer pode possuir.

**A12 — Mana com Sabedoria 1** · Contradição
- `[C2]Capítulo 2 - Criação de Personagens.md`, seção *Pontos de Mana*, e `[C2]Capítulo 2.2 - Níveis.md`, seção *Pontos de Mana*: Sab 0 ou menos dá 1 de Mana, mas Sab 1 (Modificador 0) dá 0.
- A mesma tabela dá 3 Magias conhecidas com Sab 1: o personagem conhece Magias e não consegue conjurar.
- `[F]Capítulo 1.11 - Descansos.md`: o Descanso Curto recupera "Modificador de Sabedoria" de Mana, então Sab 1 recupera zero.

**A13 — Faixas de peso do Tamanho se sobrepõem** · Contradição
- `[F]Capítulo 1.13 - Tamanho.md`, tabela: Médio vai até 200 kg, Grande começa em 100 kg, Enorme em 200 kg e Colossal em 300 kg.

**A14 — Queda livre** · Contradição
- `[F]Capítulo 1.5 - Movimentação.md`, seção *Queda e Queda Livre*: o texto diz "velocidade", mas a fórmula calcula **distância** (`Turnos*10`). Não há aceleração, unidade nem arredondamento. A fórmula do dano não respeita o limiar de "até 5m não causam dano".

**A15 — CD de Revelação usa Sabedoria** · Contradição
- `[M]Sagradas/Custo 9.md`, *Revelação*: o requisito é só Fé 9, mas a CD é "12 + Car + Sab". Nenhuma outra Magia usa Sabedoria na CD.

**A16 — Quando o Dano Contínuo ocorre** · Contradição
- `[F]Capítulo 1.7 - Dano e Resistências.md`, seção *Dano Contínuo*: ocorre "no início de cada Turno" de quem sofreu.
- `[M]Sangue/Custo 1.md`, *Dreno Vital*: "no final de cada um de seus Turnos".
- `[M]Elementais/Custo 10.md`, *Caos Cromático*: "ao final de cada um dos Turnos do alvo".

**A17 — Dano Verdadeiro "não pode ser resistido"** · Contradição
- `[F]Capítulo 1.7 - Dano e Resistências.md`, seção *Dano Verdadeiro*: "Não é possível resistir a Dano Verdadeiro", e não existe Imunidade a ele.
- `[M]Sangue/Custo 6.md`, *Cicatrizar*: ignora dano ≤ 6, "até mesmo Dano Verdadeiro".
- `[M]Ilusão/Custo 10.md`, *Espaço Branco*: "imunidade total […] a Dano Verdadeiro de qualquer fonte".
- `[M]Imaculadas/Custo 10.md`, *Apaziguar*: invulnerável a qualquer dano, "incluindo Dano Verdadeiro".
- `[M]Sagradas/Custo 7.md`, *Beira do Mundo*: "Imune a todo e qualquer tipo de dano".
- Pode ser exceção intencional, mas a regra geral não prevê exceções.

---

## B. Listas do Cap. 6.1 × descrições das Magias

Magias com descrição que **faltam** nas listas ou estão **inconsistentes** entre elas.

| #   | Magia                    | Arquivo da descrição                              | Requisito na descrição | Situação nas listas                                                                                                                                                          |
| --- | ------------------------ | ------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| B1  | Jato D'água              | `[M]Elementais/Custo 1.md`                        | Int 1                  | Ausente de `[L]Inteligência.md`                                                                                                                                              |
| B2  | Mãos Flamejantes         | `[M]Elementais/Custo 1.md`                        | Int 1                  | Ausente de `[L]Inteligência.md`                                                                                                                                              |
| B3  | Lâmina Corrosiva         | `[M]Elementais/Custo 3.md`                        | Int 3 **e** Car 3      | `[L]Inteligência.md` mostra só "3 de Inteligência"; não aparece em `[L]Carisma.md`                                                                                           |
| B4  | Gaiola                   | `[M]Elementais/Custo 7.md`                        | Int 7                  | Ausente de `[L]Inteligência.md`                                                                                                                                              |
| B5  | Pássaro Trovão           | `[M]Elementais/Custo 9.md`                        | Int 9                  | Ausente de `[L]Inteligência.md`                                                                                                                                              |
| B6  | Iéti                     | `[M]Elementais/Custo 9.md`                        | Int 9                  | Ausente de `[L]Inteligência.md`                                                                                                                                              |
| B7  | Devorar Pesadelos        | `[M]Ilusão/Custo 2.md`                            | Int 2, Car 1           | Ausente de `[L]Inteligência.md` e de `[L]Carisma.md`                                                                                                                         |
| B8  | Controle Mental Completo | `[M]Ilusão/Custo 10.md`                           | Car ou Int 10          | Ausente de `[L]Inteligência.md` e de `[L]Carisma.md`                                                                                                                         |
| B9  | Preservar                | `[M]Imaculadas/Custo 2.md`                        | Int 2                  | Ausente de `[L]Inteligência.md`                                                                                                                                              |
| B10 | Línguas                  | `[M]Imaculadas/Custo 2.md`                        | Int ou Car 2           | Ausente de `[L]Inteligência.md` e de `[L]Carisma.md`                                                                                                                         |
| B11 | Armadura de Sangue       | `[M]Sangue/Custo 4.md`                            | Int 4, Fé 4            | Ausente de `[L]Inteligência.md` e de `[L]Fé.md`                                                                                                                              |
| B12 | Destino de Sangue        | `[M]Sangue/Custo 8.md`                            | Int 8, Fé 8            | Ausente de `[L]Inteligência.md` e de `[L]Fé.md`                                                                                                                              |
| B13 | Ferver Sangue            | `[M]Sangue/Custo 8.md`                            | Int 8, Fé 8            | Ausente de `[L]Inteligência.md` e de `[L]Fé.md`                                                                                                                              |
| B14 | Raio de Enfraquecimento  | `[M]Sortilégios/Custo 1.md`                       | Int 1, Fé 1            | Ausente de `[L]Inteligência.md` e de `[L]Fé.md`                                                                                                                              |
| B15 | Dose Letal               | `[M]Sortilégios/Custo 1.md`                       | Int 1, Fé 1            | Ausente de `[L]Inteligência.md` e de `[L]Fé.md`                                                                                                                              |
| B16 | Cria das Trevas          | `[M]Sortilégios/Custo 1.md`                       | Int 1, Fé 1            | Está em `[L]Fé.md`, mas falta em `[L]Inteligência.md`                                                                                                                        |
| B17 | Novo Corpo               | `[M]Sortilégios/Custo 6.md`                       | Int 6, Fé 6            | Ausente de `[L]Inteligência.md` e de `[L]Fé.md`                                                                                                                              |
| B18 | Espada de Ossos          | `[M]Sortilégios/Custo 8.md`                       | Int 8, Fé 8            | Está em `[L]Fé.md`, mas falta em `[L]Inteligência.md`                                                                                                                        |
| B19 | Escuridão Eterna         | `[M]Sortilégios/Custo 10.md`                      | Int 10, Fé 10          | Está em `[L]Fé.md`, mas falta em `[L]Inteligência.md`                                                                                                                        |
| B20 | Buraco Negro             | **sem descrição** em `[M]Sortilégios/Custo 10.md` | —                      | Listado só em `[L]Inteligência.md` (Custo 10); sem entrada em `[L]Fé.md`                                                                                                     |
| B21 | Neutralizar Magia        | **sem descrição**                                 | —                      | Listada em `[L]Carisma.md` (Custo 3). Provável troca por **Neutralizar Veneno** (`[M]Sagradas/Custo 3.md`, Fé ou Car 3), que está em `[L]Fé.md` mas falta em `[L]Carisma.md` |
| B22 | Horrípilo                | `[M]Ilusão/Custo 7.md`                            | Int 7, Car 7           | Erro de digitação em `[L]Carisma.md` (Custo 7): "7 e Carisma"                                                                                                                |

---

## C. Termos e regras não definidos ou ambíguos

**C1 — Terreno Difícil** · Lacuna
- Usado em `[F]Capítulo 1.5 - Movimentação.md` (*Pular* diz que "impede que você pule"), `[H]Velocista.md` (*Escalador*), `[M]Elementais/Custo 4.md` (*Congelamento*), `[M]Elementais/Custo 6.md` (*Chuva de Magma*, *Caminho de Gelo*) e outros.
- Nenhum arquivo enviado define o que ele faz com o Deslocamento.

**C2 — Pontos de Vida e Mana Temporários** · Lacuna
- Aparecem em dezenas de Habilidades e Magias.
- `[F]Capítulo 1.1 - Vida.md` e `[F]Capítulo 1.2 - Mana.md` não definem como acumulam, em que ordem absorvem dano nem se contam para o máximo.
- A única regra solta está em `[M]Capítulo 6 - Magias.md`, categoria *Sangue*.

**C3 — Tipos de visão** · Lacuna
- `[R]Elfo.md` (Elfo da Floresta): "Visão Noturna".
- `[H]Polímata.md` (*Habitante das Cavernas*): "Visão na Penumbra" e "Visão no Escuro".
- `[F]Capítulo 1.9 - Elementos do Cenário.md` só define Escuridão e Penumbra como ambientes. Nenhum arquivo define as visões nem se "Visão Noturna" equivale a alguma delas.

**C4 — Vocabulário de resistências** · Ambiguidade
- `[F]Capítulo 1.7 - Dano e Resistências.md` define **Imunidade** e usa **Fraqueza** e **Vulnerabilidade** juntas.
- Outros arquivos usam **Invulnerabilidade** sem definição: `[M]Elementais/Custo 9.md`, `[M]Imaculadas/Custo 3.md` (*Arma Incorpórea*), `[M]Sangue/Custo 4.md` (*Lâmina de Sangue*) e `[H]Guerreiro (Arcano).md` (*Memória Perfeita*).

**C5 — Dobrar o Bônus de Proficiência** · Ambiguidade
- `[H]Especialista.md` (*Arte Nobre*, *Esperteza*), `[E]Capítulo 4.11 - Itens Mágicos e Únicos.md` (*Anel da Soberania*) e `[R]Siderium.md` (*Foco Aprimorado*) dobram a proficiência.
- `Capítulo 5 - Habilidades/Capítulo 5 - Habilidades.md` diz que efeitos iguais valem só uma vez, sem esclarecer se dobros empilham.

**C6 — Sigla (Modificador) × nome por extenso (Atributo)** · Ambiguidade
- A regra de `[F]Capítulo 1.3 - Atributos.md`, seção *Modificadores*, é: sigla = Modificador, nome por extenso = Atributo inteiro. Vários trechos misturam as duas formas no mesmo item, e parece descuido:
  - `[H]Bárbaro.md`, *Berserk*: a tabela alterna "Con" e "Constituição+3".
  - `[E]Capítulo 4.8 - Lista de Poções e Venenos.md`: *Cura Maior* usa "Constituição", *Cura Menor* usa "Con"; *Mana Maior* usa "Sabedoria", *Mana Menor* usa "Sab".
  - `[M]Imaculadas/Custo 1.md`, *Armadura Arcana*: "9 + Inteligência" (a CA seria 19 com Int 10; se fosse Modificador, seria 14).
  - `[M]Elementais/Custo 10.md`, *Tsunami*: "12d12 + Inteligência".
  - `[H]Guerreiro (Tanque).md`, *Respirar Fundo*: "1d10 + Constituição".

**C7 — Salvaguardas ao ser Nocauteado** · Ambiguidade
- `[F]Capítulo 1.12 - Condições.md`, *Nocauteado*: "Será uma melhor de 5" não diz se são 5 rolagens, se é a melhor de 5 ou o quê. O limiar de sucesso (10) e o de morte (3 falhas) estão claros.

**C8 — Condição "Encantamento"** · Terminologia
- `[H]Ilusionista.md`, *Si-Mesmo*: "Imune à Condição Encantamento". A Condição se chama **Encantado** (`[F]Capítulo 1.12 - Condições.md`).

**C9 — Infusão acima da escala S** · Lacuna
- `[E]Capítulo 4.10 - Infusões.md`: diz que a infusão sobe a Escala em 1 grau, mas não diz o que acontece se o item já está em S.
- A seção *Infusões Mágicas* ordena trocar o tipo de dano da Arma, mas não cobre itens sem dano (varinhas, armaduras).

**C10 — Mana das varinhas e cajados** · Ambiguidade
- `[E]Capítulo 4.11 - Itens Mágicos e Únicos.md`, seção *Varinhas e Cajados Mágicos*, não diz:
  - se o Mana extra aumenta o máximo ou é uma reserva separada;
  - se a "soma dos Bônus de Escala ativos" inclui as duas varinhas equipadas;
  - se infusões em varinhas são permitidas, já que `[E]Capítulo 4.10 - Infusões.md` fala só em Armas e Armaduras.

**C11 — Armadura Arcana × Roupas** · Ambiguidade
- `[M]Imaculadas/Custo 1.md`, *Armadura Arcana*: exige "O alvo não pode estar usando armadura".
- `[E]Capítulo 4.1 - Lista de Armaduras.md` e `[E]Capítulo 4 - Equipamentos.md` (*Classificação*) tratam Roupas como uma classe de armadura, mas "Nenhuma Armadura" também é Roupa. Não fica claro se Roupas, Mantos e Túnicas bloqueiam a magia.
- Também não diz se a CA substituída soma o Modificador de Destreza.

**C12 — Pergaminhos de Magia sem regra** · Lacuna
- `[M]Imaculadas/Custo 10.md`, *Alterar Realidade*: fala em "forma de pergaminho".
- `[E]Capítulo 4.12 - Outros Itens.md`, *Pergaminho*: "pergaminhos de Magia".
- Nenhum arquivo enviado define como funciona um pergaminho de Magia.

**C13 — Soma das linhas das escalas** · Decisão do autor registrada
- `[E]Capítulo 4 - Equipamentos.md`, tabelas de Escala: "os bônus são cumulativos". A decisão do autor é que a regra vale a **soma das linhas**. Convém escrever isso no texto, pois a tabela por si só pode ser lida como valor atual e não como incremento.

---

## D. Economia e brechas

**D1 — Peso das moedas × Carga** · Exploit
- `[E]Capítulo 4.9 - Moedas.md`: 3 kg a cada 100 moedas, com 5000 moedas como máximo sugerido (150 kg).
- `Capítulo 3 - Raças/Capítulo 3.1 - Carga de Peso.md`: Carga Base de 35 a 50 kg.

**D2 — Exaustão curada por consumíveis baratos** · Exploit
- `[E]Capítulo 4.12 - Outros Itens.md`: *Ração de Viagem* e *Cantil* removem 1 Nível de Exaustão por uso (1 Ação).
- Isso desfaz `[E]Capítulo 4.8 - Lista de Poções e Venenos.md` (*Amatoxina*, Exaustão crescente até a morte) e `[M]Sortilégios/Custo 5.md` (*Raio da Morte*).
- O vampirismo (`Capítulo 7 - Transformações/Capítulo 7.1 - Vampirismo.md`) é protegido explicitamente ("não se recupera com Descansos, apenas com sangue").

**D3 — Armadura Melhorada é barata demais** · Exploit
- `[E]Capítulo 4.11 - Itens Mágicos e Únicos.md`, seção *Armadura Melhorada*: +3 de CA custa só 4× o preço (ex.: Couro +3 por 4po, Armadura Completa +3 por 120po), enquanto os *Braceletes de Gladiador* (+4 CA) custam 750pl.

**D4 — Preço de Grau 1 por Infusão × por criação** · Contradição de preços
- `[E]Capítulo 4.10 - Infusões.md`: um item infundido vira Grau 1 e custa 200po (pedra) + 80po (infundir), ou seja, 280po.
- `[H]Ferreiro.md` (*Ferraria Mágica*) e `[H]Alquimista.md` (*Alquimista Mágico*): materiais de um Grau 1 custam 150pl (1500po).
- `[E]Capítulo 4.11 - Itens Mágicos e Únicos.md`: *Joia de Resistência* (Grau 1) custa em média 35pl (350po).

**D5 — Nível Médio sempre ÷ 4** · Ambiguidade
- `[C2]Capítulo 2.2 - Níveis.md`, seção *Calculando Pontos de Experiência*: divide a soma dos Níveis por 4, independentemente do tamanho do grupo (3, 5 ou mais jogadores).

**D6 — Habilidade Nirvana provavelmente inalcançável** · A verificar
- `[H]Mundano.md`, *Nirvana*: exige nenhum Atributo abaixo de 7 (49 pontos).
- O orçamento padrão até o Nível 20 é 30 pontos (7 + 23). Somando os extras que encontrei (*Equilíbrio* +2, *Equilíbrio Aprimorado* +1, *Equilíbrio Supremo* +2, *Pau Para Toda Obra* +1 e *Bom Início* +1 em `[H]Polímata.md`, e *Escola da Tartaruga* +3 em `[R]Tártaro.md`), o máximo é cerca de 40.
- A única saída aparente seria *Polivalente* → *Elementar* (`[H]Especialista.md`), que dispensa requisitos de Atributo. Confirme se é a intenção.

---

## E. Balanceamento (subjetivo)

**E1 — Canção do Perecimento** · `[H]Bardo.md`
- Custo 1 e 5 de Mana: mata todos que ouvirem em 3 Rodadas, sem Salvaguarda. As únicas defesas são Surdez ou Resistência a Dano Sombrio.

**E2 — Relâmpago forte demais para o Custo 3** · `[M]Elementais/Custo 3.md`
- 8d8 + Int, linha de 12m, sem Salvaguarda. Compare com `[M]Elementais/Custo 5.md` (*Esmagamento de Rochas*, 10d6 com Salvaguarda) e `[M]Elementais/Custo 6.md` (*Chuva de Magma*).

**E3 — Golem de Custo 1 × Golem de Custo 3** · `[M]Elementais/Custo 1.md` × `[M]Sortilégios/Custo 3.md`
- *Conjurar Golem Menor* (Custo 1) tem os mesmos 30 PV do *Golem Zumbi* (Custo 3).

**E4 — Espada Larga domina as Armas Comuns** · `[E]Capítulo 4.2 - Lista de Armas.md`
- 1d12 + For por 2po, superior à *Espada Longa*, ao *Machado de Batalha* e à *Espada Bastarda*.

**E5 — Besta Pesada sem requisitos** · `[E]Capítulo 4.2 - Lista de Armas.md`
- 2d10 por 5po, sem requisitos, só com Escala 0. Quase iguala armas que exigem Atributos e investimento.

**E6 — Gibão de Peles × Camisão de Malha** · `[E]Capítulo 4.1 - Lista de Armaduras.md`
- O Gibão (+3 CA, 2 For, 8 kg) supera o Camisão de Malha (+2 CA, 3 For, 10 kg) com preço quase igual.

---

## Correções às análises anteriores

Ao localizar cada item corrigi dois pontos da minha resposta inicial:
- **Novo Corpo** é uma Magia de **Sortilégio** (`[M]Sortilégios/Custo 6.md`), não de Sangue. Está no item B17.
- **Margem de Ameaça Reversa** na terceira vez **custa menos**, não mais. Está no item A7.
