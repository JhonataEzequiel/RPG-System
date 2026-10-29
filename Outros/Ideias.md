
### 1. Ataque e dano

**Bônus de Ataque (BA)**: como você propôs. Isso absorve Modificador de Atributo, Proficiência, Escala (Nível 10), Arma +X, Munição +X, Mira Acoplada e habilidades como Foco de Ataque.

**Dano = XdY + Z**: sugiro ir além e separar o dano em **componentes tipados**:

- **Dados base** (da arma/magia)
- **Bônus Fixo de Dano (BFD)**: Modificador + Escala + bônus de habilidades
- **Dados Adicionais**: cada um com tipo próprio (hoje aparece como “+1d6 de um dos tipos que a Arma causa, à sua escolha” em dezenas de habilidades)

Hoje existe a frase “adicione Xd6 de dano de um dos tipos possíveis” repetida em Ataque Furtivo, Dança Combatente, Risco e Recompensa, Show do Imperador, Nébula e outras. Criar a regra única **“Dano Adicional (herda tipo da fonte)”** e depois só escrever “+2d6 Dano Adicional” elimina esse texto todo.

**Penalidade de Ataque**: hoje é -5/-10 aplicado ao teste. Poderia ser uma estatística própria (**Redutor de Múltiplos Ataques**), que habilidades como Ataque Extra, Dualidade Militar e Maestria em Armas Comuns modificam, em vez de cada uma reescrever a regra com exceções.

### 2. Defesa

- **CA**: hoje é 10 + For + Dex + Armadura, mais bônus de Escala, mais habilidades. Mantenha como estatística única e padronize: “Sua CA aumenta em X”.
- **Redução de Dano** unificando “Resistência (pontos)” e “Resistência a tipo X”. Hoje o livro usa “Pontos de Resistência”, “Resistência”, “Vulnerabilidade” e “Fraqueza” de formas quase intercambiáveis. Sugiro um glossário fechado: **Redução [tipo] X** e **Vulnerabilidade [tipo] X**, ambas numéricas, e **Imunidade** como caso especial.
- **Vantagem e Desvantagem** numéricas: você já tem “Desvantagem substituída por -3” em Maestria em Armas Comuns. Talvez definir que Vantagem/Desvantagem equivalem a ±X no BA (ou continuar como d20 duplo, mas com regra explícita de empilhamento).

### 3. CD e Salvaguardas

Hoje as CDs aparecem como “CD 11 + Int + Fth”, “CD 13 + Int”, “CD 10 + For + Dex”, “CD 8 + Fth + Int”, “CD 5 + Con + For + Sab + Prof”. Isso é o ponto mais caótico para balancear.

Sugestão: **CD de Efeito (CDE)** como estatística do personagem, calculada uma vez:  
`CDE = 8 + Bônus de Proficiência + Modificador do Atributo de conjuração`  
Cada magia/habilidade diz apenas “CDE” ou “CDE +2”. Habilidades como Foco Arcano, Arcano Aprimorado e Agente Punitivo passam a dizer “Sua CDE aumenta em 1”.

Em paralelo, o **Bônus de Salvaguarda** por atributo (Modificador + Proficiência + extras), o que já é quase o caso.

### 4. Dano de magia e escalonamento

As magias usam dados muito diferentes para o mesmo custo (Custo 3: Bola de Fogo 7d6, Relâmpago 8d8, Frio Noturno 5d6+6d6; Custo 5: Esmagamento 10d6, Corpo Elemental 10d6; Custo 8: Lança de Raio 10d8+2d12, Perseguidores 8d6). Sugestões:

- **Tabela de Dano Alvo por Custo**: define um orçamento (ex.: dano médio esperado por Custo) e cada magia “gasta” esse orçamento em dano, área, condições, duração. Facilita muito o balanceamento.
- **Dano de Magia = XdY + Modificador**: padronizar que o modificador sempre é “Atributo de Conjuração” (hoje é Int, Fth, Int+Fth, Car, “Int ou Fth”…). Magias de dois atributos (Sangue/Sortilégio) usam a soma, o que dobra o bônus; talvez uma regra única para multi-atributo.
- **Custo extra de Mana** com fórmula única: “+1 Mana = +1 dado base” (hoje varia entre +1d8, +2d6, +2d8, +1d6, +2d4, +5 de PV temporário…).

### 5. Economia de ação e recursos

- **Ações Bônus**: ter só uma por turno e a segunda virar Ação é ótimo, mas várias habilidades dão “Ação Bônus extra” (Domo de Gelo, Sombra Agente, Poção de Velocidade). Definir **Pool de Ações Bônus** como estatística.
- **Reações**: igual, com estatística **Reações por Rodada** (Supremo Protetor, Fusão, etc. já modificam isso).
- **Recursos com recarga**: hoje há “uma vez por Descanso Curto/Longo”, “X vezes igual ao Bônus de Proficiência”, “uma vez por Encontro”, “uma vez ao dia”. Padronizar em **Cargas** com tipo de recarga (Curto, Longo, Encontro) e notação única, ex.: `[Cargas: Prof / Longo]`.

### 6. Vida, Mana e progressão

- **PV Máximo** e **Mana Máxima** como estatísticas únicas, onde cada habilidade só diz “+X” (hoje há “adicione 1d4 permanentemente”, “adicione o Modificador a cada Nível”, “dobre”, “converta Mana em PV”…). Separar bônus **por Nível**, **flat** e **multiplicador**.
- **Pontos Temporários**: já existe regra, mas padronizar a notação (PV Temp. / Mana Temp.).
- **Dados de Vida**: a tabela por Constituição (1d4 a 3d10) é um ponto de curva que merece revisão no mesmo passe.

### 7. Movimento e utilidade

- **Deslocamento** já é estatística; padronizar como “+X m” e definir ordem de operações (soma antes de multiplicar, penalidades por último). Guepardo, Sonido, Corrida de Besta, Correr, etc. cada um define sua ordem.
- **Testes de Perícia**: unificar em **Bônus de Perícia = Modificador + Proficiência (+ extras)**, e habilidades dizem só “seu Bônus de [Perícia] aumenta em X”.
- **Iniciativa**: estatística própria com modificadores.

### 8. Ordem de operações e empilhamento

Isso importa mais do que parece, porque o livro já tem regras ad hoc: “multiplicadores se multiplicam entre si”, “habilidades que dão o mesmo efeito não acumulam”, “Vantagem e Desvantagem se anulam”. Sugiro uma seção única de **Ordem de Cálculo** (por exemplo: base → bônus fixos → bônus percentuais/multiplicadores → mínimos/máximos → resistências) e uma regra de **empilhamento por fonte** (mesma fonte não soma, fontes diferentes somam).

### 9. Organização do texto

- **Glossário de termos fechado**: “Condição” vs. “Efeito”, “Encontro” vs. “Combate”, “Rodada” vs. “Turno”, “Salvaguarda” vs. “Teste de Resistência” (você usa os dois), “Ataque” vs. “Habilidade de Ataque”.
- **Bloco padrão de habilidade/magia**: Custo, Ação, Alcance, Duração, Gatilho, Teste (quem rola o quê contra o quê), Efeito, Escalonamento. Hoje há campos faltando ou fora de ordem (ex.: “Custo” às vezes vem junto de Ações, às vezes separado).
- **Palavras-chave reutilizáveis** (como “Dano Adicional”, “Dano Contínuo”, “Concentração”) com definição única no capítulo 1.

### 10. Descansos e Mana Como Recurso Único

### Ordem sugerida de trabalho

1. Definir o **vocabulário de estatísticas** (BA, BFD, CA, CDE, Redução, etc.) e a ordem de cálculo.
2. Fazer o **orçamento por Custo** (magias) e por Custo de Habilidade (1/2/3 pontos).
3. Só depois reescrever os textos das habilidades, magias e itens.