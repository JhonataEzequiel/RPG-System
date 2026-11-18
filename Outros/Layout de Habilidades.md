Este documento define como toda Habilidade é escrita, tanto as adquiridas com PHs (Capítulo 5) quanto as Habilidades de Raça (Capítulo 3). A estrutura tem dois níveis: o cabeçalho, com os dados da Habilidade inteira, e os efeitos, cada um com os seus próprios dados. Toda Habilidade usa este mesmo layout, ainda que tenha apenas um efeito.

## Layout

```
### Nome da Habilidade

**Custo de PHs**: X | **Requisitos de Atributos**: Y | **Requisitos de Habilidades**: Z | **Outros Requisitos**: W

Descrição geral: regras que valem para todos os efeitos da Habilidade.

- **Nome do Efeito 1** (Ativa | Custo de Ações: X | Custo de Mana: Y | Alcance: Z | Alvo: W | Duração: V | Limite de Usos: U | Requisitos de Uso: R): descrição do efeito.
  - **Aprimoramento** (Custo de Mana adicional: Y): descrição do aprimoramento.
- **Nome do Efeito 2** (Ativa | Custo de Ações: X | Alcance: Z): descrição do efeito.
- **Nome do Efeito 3** (Passiva | Alvo: W | Duração: V | Requisitos de Uso: R): descrição do efeito.
```

## Cabeçalho

O cabeçalho reúne apenas o que vale para a Habilidade inteira. Os requisitos do cabeçalho são os de aquisição: valem apenas no momento em que a Habilidade é adquirida. Os requisitos para usar um efeito são outra coisa e ficam no próprio efeito, no campo Requisitos de Uso.

|Campo|Preenchimento|
|---|---|
|Custo de PHs|De 1 a 3.|
|Requisitos de Atributos|O nome de cada Atributo exigido e o valor mínimo, como em "3 de Arcano, Vínculo ou Carisma". As siglas não são usadas aqui, pois denotam Modificadores. Omitido se não houver requisitos.|
|Requisitos de Habilidades|Cada Habilidade que precisa ser adquirida antes, com o nome entre aspas e o custo dela, no formato "Nome da Habilidade Requerida" de Custo X. Quando a Habilidade requerida pertence a outro Arquétipo, o Arquétipo também é indicado, no formato "Nome da Habilidade Requerida" de Custo X do Arquétipo Y. Havendo mais de uma, são separadas por vírgulas. Omitido se não houver requisitos.|
|Outros Requisitos|Todo requisito de aquisição que não seja de Atributos nem de Habilidades, como um Nível mínimo, ser Perito em uma Perícia, ser Proficiente em um tipo de Arma, ter um item ou não ter adquirido determinada Habilidade. Cada requisito é escrito no infinitivo, como em "ser Perito em Erudição". Havendo mais de um, são separados por ponto e vírgula. Omitido se não houver requisitos.|

## Outros Requisitos

Este campo é sempre o último do cabeçalho e reúne os requisitos de aquisição que não aparecem na maioria das Habilidades. Assim como os demais requisitos do cabeçalho, eles só são cobrados no momento da aquisição. Por exemplo:

```
### Memória Perfeita

**Custo de PHs**: 1 | **Outros Requisitos**: ser Perito em Erudição
```

```
### Arte Nobre

**Custo de PHs**: 1 | **Requisitos de Atributos**: 10 de Constituição, Sabedoria, Força, Destreza, Arcano, Vínculo ou Carisma | **Outros Requisitos**: estar no Nível 14; não ter outro Atributo com valor 10
```

Não confunda com os Requisitos de Uso. Um item que você só precisa ter no momento de adquirir a Habilidade, como um Grimório, vai em Outros Requisitos. Um item que você precisa ter para que o efeito funcione vai em Requisitos de Uso, no próprio efeito.

## Efeitos

Cada efeito é um item da lista, com a sua própria linha de parênteses. Os campos são sempre escritos na ordem da tabela.

|Campo|Aplica-se a|Preenchimento|
|---|---|---|
|Ativa ou Passiva|Todo efeito|Sempre o primeiro item. Efeitos ativos custam uma Ação, uma Ação Livre, uma Ação Bônus ou uma Reação, e os passivos não custam nada.|
|Custo de Ações|Ativa|Uma Ação, Duas Ações, Três Ações, Ação Livre, Ação Bônus ou Reação.|
|Custo de Mana|Ativa|A quantidade de PMs.|
|Alcance|Todo efeito|Apenas a distância até a qual o efeito pode ser usado: Toque, uma distância em metros, Deslocamento ou Ilimitado.|
|Alvo|Todo efeito|Apenas quem ou o que é afetado: você, uma criatura, múltiplas criaturas, um Objeto, uma Área (formato e tamanho) etc. Não indica distância.|
|Duração|Todo efeito|Instantânea, uma quantidade de Rodadas, um Encontro, uma quantidade de horas ou de dias etc.|
|Limite de Usos|Todo efeito|Quantas vezes o efeito pode ser usado e a cada quanto tempo, como uma vez por Encontro, por Descanso, por Descanso Curto ou por Descanso Longo.|
|Requisitos de Uso|Todo efeito|As condições que precisam estar cumpridas para usar o efeito ou, se ele for passivo, para que ele tenha efeito: itens, estado do personagem ou circunstância. Escrito no infinitivo, como em "estar com uma Arma que cause Dano Perfurante equipada". Havendo mais de uma condição, são separadas por "e" ou por ponto e vírgula. Omitido se não houver.|

## Requisitos de Uso

O Requisito de Uso pertence ao efeito, e não à Habilidade. Uma Habilidade com dois efeitos pode ter um Requisito de Uso em apenas um deles, ou um diferente em cada. Por exemplo:

```
### Linha de Frente

**Custo de PHs**: 1 | **Requisitos de Atributos**: 2 de Força e 1 de Constituição

- **Linha de Frente** (Ativa | Custo de Ações: Ação Bônus | Alcance: 18 metros | Alvo: você | Requisitos de Uso: estar usando uma Armadura com Peso superior a 6): descrição do efeito.
- **Desativar Linha de Frente** (Ativa | Custo de Ações: Ação Bônus): descrição do efeito.
```

Itens, equipamentos, estados do personagem e circunstâncias exigidos para usar um efeito sempre vão em Requisitos de Uso, e nunca no cabeçalho nem na descrição geral.

## Regras de Escrita

- Campos que não se aplicam a um efeito são omitidos.
- Quando mais de um efeito da mesma Habilidade tem o mesmo Requisito de Uso, ele é repetido em cada um deles. Efeitos sem o requisito não o recebem.
- Requisitos de aquisição que não sejam de Atributos nem de Habilidades, como um Nível mínimo ou ser Perito em uma Perícia, ficam no campo Outros Requisitos do cabeçalho, e não na descrição geral.
- Alcance e Alvo são campos separados. O Alcance traz apenas a distância, e o Alvo traz apenas quem ou o que é afetado, sem mencionar o alcance. Por exemplo, "Alcance: 9 metros | Alvo: múltiplas criaturas", e não "Alvo: criaturas no alcance".
- Quando o alcance for o Deslocamento, escreve-se apenas "Deslocamento", e não "igual ao seu Deslocamento". A definição está no Capítulo 5 - Habilidades.
- A descrição geral é omitida quando não há regras que valham para todos os efeitos.
- Uma Habilidade com um único efeito também usa a lista, com um só item. Esse efeito tem o mesmo nome da Habilidade, a não ser que ele tenha um nome próprio.
- Efeitos com custos, alcances ou durações diferentes são itens separados da lista, cada um com a sua linha de parênteses.
- Um Aprimoramento é uma modificação opcional de um efeito ativo, paga com Mana adicional. Ele fica recuado dentro do efeito que modifica.
- Parágrafos adicionais que pertencem a um efeito ficam recuados dentro dele.
- Tabelas nunca ficam dentro de um item da lista, pois o Obsidian não as renderiza ali. Quando pertencem ao último efeito, vêm logo depois da lista. Caso contrário, ficam na descrição geral, e o efeito faz referência a elas.
- Salvaguardas, tipos de dano, Graus, Condições e demais detalhes vão na descrição de cada efeito.
- O texto é escrito em segunda pessoa, e "você" é quem possui a Habilidade.
- Habilidades de Raça não têm os campos do cabeçalho, pois são gratuitas e não possuem requisitos de aquisição. Os efeitos delas podem ter Requisitos de Uso normalmente. Todas têm título "####" dentro de "### Habilidades de Raça".

## Tabela-Índice de Arquétipo

Opcionalmente, cada Arquétipo pode começar com uma tabela para consulta rápida. Ela segue os mesmos formatos do cabeçalho: os Atributos escritos por extenso, as Habilidades requeridas com o custo e, quando for o caso, o Arquétipo, e os Outros Requisitos escritos como no cabeçalho, separados por ponto e vírgula. Campos sem requisitos recebem "-".

|Habilidade|Custo de PHs|Requisitos de Atributos|Requisitos de Habilidades|Outros Requisitos|
|---|---|---|---|---|
|Nome da Habilidade|X|3 de Arcano|"Nome da Habilidade Requerida" de Custo X|-|
|Nome da Habilidade|X|-|"Nome da Habilidade Requerida" de Custo X do Arquétipo Y|ser Perito em Erudição|