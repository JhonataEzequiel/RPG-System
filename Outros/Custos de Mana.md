Este documento calcula o preço, em PMs, de certos efeitos. O principal intuito dele não é providenciar um balanceamento 100% correto, sempre sendo seguido à risca, mas sim uma ideia de como cada efeito contribui para o todo.

## 1. Custo Base

Para simplificar, do Grau 1 ao 5 de dano é 1 PM. Esse será o parâmetro base da análise. Alguns custos podem ser maiores ou menores que o esperado, sendo arbitrários com alguma lógica por trás. Outros podem ter valores fracionados, mas o custo final será dado como inteiro, arredondando de acordo com a matemática (0,5 vira 1).

### 1.1. Custo de Graus

A tabela a seguir mostra quanto que cada Grau de dano e cura se converte em PMs. A cura custa 2x o preço do dano. Os preços são diferentes dos presentes nos equipamentos devido ao fato de que o dano aqui calculado é instantâneo, ou seja, uma instância de dano por PMs, ao invés de uma quantidade de dano sempre possível de ser causada através de Ataques. Os preços não são lineares.

| Grau | Média | Custo do Dano | Custo da Cura |
| ---- | ----- | ------------- | ------------- |
| 1    | 2,5   | 1 PM          | 2 PM          |
| 2    | 3,5   | 1 PM          | 2 PM          |
| 3    | 4,5   | 1 PM          | 2 PM          |
| 4    | 5,5   | 1 PM          | 4 PM          |
| 5    | 6,5   | 1 PM          | 4 PM          |
| 6    | 7,0   | 5 PM          | 10 PM         |
| 7    | 9,0   | 5 PM          | 10 PM         |
| 8    | 11,0  | 8 PM          | 16 PM         |
| 9    | 13,0  | 8 PM          | 16 PM         |
| 10   | 16,5  | 10 PM         | 20 PM         |

### 1.2 Estatísticas da Magia

As Estatísticas da Magia contribuem para o custo. O custo mínimo é 1. Quanto maior o dano causado; cura gerada; área de efeito; Alcance da Magia (alvo único); Quantidade de Ações; Requisitos; ou tempo de duração, maior o custo.

Magias que tem um requisito adicional não tem o custo diminuído, pois fazem parte da fantasia.

| Efeito                              | Custo   |
| ----------------------------------- | ------- |
| +1,5 metros de área                 | 2 PM    |
| +1,5 metros de Alcance (alvo único) | 1 PM    |
| Requer uma Ação Bônus               | -0,1 PM |
| Requer uma Ação                     | -0,3 PM |
| Requer duas Ações                   | -0,4 PM |
| Requer três Ações                   | -0,5 PM |
| 1 Requisito                         | -0,1 PM |

| Tempo de Duração | Peso no Custo final |
| ---------------- | ------------------- |
| 1 Rodada         | 1x                  |
| 2 Rodadas        | 1.1x                |
| 3 Rodadas        | 1.2x                |
| 4 Rodadas        | 1.25x               |
| 1 Encontro       | 1.5x                |
| 1 Hora           | Entre 1 e 1.5x      |
| mais de 1 hora   | Entre 1 e 1.5x      |

Os Efeitos que durarem mais que um Encontro terão rendimento menor na maioria dos casos, ou serão efeitos que tem como objetivo ter impacto duradouro para questões de balanceamento. Portanto, o custo desses efeitos será arbitrário, baseando-se apenas levemente nos custos de Mana já existentes neste arquivo, podendo ou não ter justificativa.

## 2. Efeitos Benéficos

A Metamagia permitirá modificar Magias. Os efeitos variam entre instantâneos e temporários

### 2.1 Custo da Metamagia

| Efeito                                      | Custo |
| ------------------------------------------- | ----- |
| +1 de BD                                    | 1 PM  |
| +1 de Resistência Concedida                 | 1 PM  |
| +1,5 metros de Alcance Corpo-a-Corpo        | 5 PM  |
| +1,5 metros de Alcance de Ataques Mágicos   | 2 PM  |
| +1,5 metros de Deslocamento                 | 1 PM  |
| +1 em Teste de Perícia                      | 1 PM  |
| 1 de Regeneração de PV                      | 2 PM  |
| +1,5 metros de aumento de área de uma Magia | 1 PM  |
| 1 PV Temporário                             | 1 PM  |
| +5 PV Máximo para um servo invocado         | 1 PM  |

### 2.2 Efeitos Benéficos Temporários

| Efeito                                      | Custo por 1 Rodada | Custo por 2 Rodadas | Custo por 3 Rodadas | Custo por 4 Rodadas | Custo por 1 Encontro | Observações                                               |
| ------------------------------------------- | ------------------ | ------------------- | ------------------- | ------------------- | -------------------- | --------------------------------------------------------- |
| +1 de BD                                    | 1 PM               | 1 PM                | 1 PM                | 1 PM                | 2 PM                 | O preço aumenta de maneira não linear, ver a sessão 2.2.1 |
| +1 de Resistência                           | 1 PM               | 1 PM                | 1 PM                | 1 PM                | 2 PM                 | O preço aumenta de maneira não linear, ver a sessão 2.2.1 |
| +1,5 metros de Alcance Corpo-a-Corpo        | 5 PM               | 5 PM                | 5 PM                | 5 PM                | 5 PM                 |                                                           |
| +1,5 metros de Alcance de Ataques Mágicos   | 2 PM               | 2 PM                | 2 PM                | 2 PM                | 2 PM                 |                                                           |
| +1,5 metros de Deslocamento                 | 1 PM               | 2 PM                | 2 PM                | 3 PM                | 4 PM                 |                                                           |
| +1 em Teste de Perícia                      | 1 PM               | 1 PM                | 1 PM                | 1 PM                | 1 PM                 |                                                           |
| 1 de Regeneração de PV                      | 2 PM               | 3 PM                | 4 PM                | 5 PM                | 6 PM                 |                                                           |
| +1,5 metros de aumento de área de uma Magia | 1 PM               | 2 PM                | 2 PM                | 3 PM                | 3 PM                 |                                                           |
| 1 PV Temporário                             | 1 PM               | 1 PM                | 1 PM                | 1 PM                | 1 PM                 |                                                           |
| +5 PV Máximo para um servo invocado         | 1 PM               | 1 PM                | 1 PM                | 1 PM                | 1 PM                 |                                                           |
