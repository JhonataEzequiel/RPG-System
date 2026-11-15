Este documento define como toda Habilidade é escrita, tanto as adquiridas com PHs (Capítulo 5) quanto as Habilidades de Raça (Capítulo 3). A estrutura tem dois níveis: o cabeçalho, com os dados da Habilidade inteira, e os efeitos, cada um com os seus próprios dados. Toda Habilidade usa este mesmo layout, ainda que tenha apenas um efeito.

## Layout

```
### Nome da Habilidade

**Custo de PHs**: X | **Requisitos de Atributos**: Y | **Requisitos de Habilidades**: Z

Descrição geral: regras que valem para todos os efeitos da Habilidade.

- **Nome do Efeito 1** (Ativa | Custo de Ações: X | Custo de Mana: Y | Alcance: Z | Alvo: W | Duração: V | Limite de Usos: U): descrição do efeito.
  - **Aprimoramento** (Custo de Mana adicional: Y): descrição do aprimoramento.
- **Nome do Efeito 2** (Ativa | Custo de Ações: X | Alcance: Z): descrição do efeito.
- **Nome do Efeito 3** (Passiva | Alvo: W | Duração: V): descrição do efeito.
```

## Cabeçalho

O cabeçalho reúne apenas o que vale para a Habilidade inteira.

|Campo|Preenchimento|
|---|---|
|Custo de PHs|De 1 a 3.|
|Requisitos de Atributos|O nome de cada Atributo exigido e o valor mínimo, como em "3 de Arcano, Vínculo ou Carisma". As siglas não são usadas aqui, pois denotam Modificadores. Omitido se não houver requisitos.|
|Requisitos de Habilidades|Cada Habilidade que precisa ser adquirida antes, com o nome entre aspas e o custo dela, no formato "Nome da Habilidade Requerida" de Custo X. Quando a Habilidade requerida pertence a outro Arquétipo, o Arquétipo também é indicado, no formato "Nome da Habilidade Requerida" de Custo X do Arquétipo Y. Havendo mais de uma, são separadas por vírgulas. Omitido se não houver requisitos.|

## Efeitos

Cada efeito é um item da lista, com a sua própria linha de parênteses. Os campos são sempre escritos na ordem da tabela.

|Campo|Aplica-se a|Preenchimento|
|---|---|---|
|Ativa ou Passiva|Todo efeito|Sempre o primeiro item. Efeitos ativos custam uma Ação, uma Ação Livre, uma Ação Bônus ou uma Reação, e os passivos não custam nada.|
|Custo de Ações|Ativa|Uma Ação, Duas Ações, Três Ações, Ação Livre, Ação Bônus ou Reação.|
|Custo de Mana|Ativa|A quantidade de PMs.|
|Alcance|Todo efeito|Toque, uma distância em metros ou Ilimitado.|
|Alvo|Todo efeito|Quem ou o que é afetado: você, uma criatura, um Objeto, uma Área (formato e tamanho) etc.|
|Duração|Todo efeito|Instantânea, uma quantidade de Rodadas, um Encontro, uma quantidade de horas ou de dias etc.|
|Limite de Usos|Todo efeito|Quantas vezes o efeito pode ser usado e a cada quanto tempo, como uma vez por Encontro, por Descanso, por Descanso Curto ou por Descanso Longo.|

## Regras de Escrita

- Campos que não se aplicam a um efeito são omitidos.
- A descrição geral é omitida quando não há regras que valham para todos os efeitos.
- Uma Habilidade com um único efeito também usa a lista, com um só item. Esse efeito tem o mesmo nome da Habilidade, a não ser que ele tenha um nome próprio.
- Efeitos com custos, alcances ou durações diferentes são itens separados da lista, cada um com a sua linha de parênteses.
- Um Aprimoramento é uma modificação opcional de um efeito ativo, paga com Mana adicional. Ele fica recuado dentro do efeito que modifica.
- Parágrafos adicionais que pertencem a um efeito ficam recuados dentro dele.
- Tabelas nunca ficam dentro de um item da lista, pois o Obsidian não as renderiza ali. Quando pertencem ao último efeito, vêm logo depois da lista. Caso contrário, ficam na descrição geral, e o efeito faz referência a elas.
- Salvaguardas, tipos de dano, Graus, Condições e demais detalhes vão na descrição de cada efeito.
- O texto é escrito em segunda pessoa, e "você" é quem possui a Habilidade.
- Habilidades de Raça não têm os campos do cabeçalho, pois são gratuitas e não possuem requisitos. Todas têm título "####" dentro de "### Habilidades de Raça".

## Tabela-Índice de Arquétipo

Opcionalmente, cada Arquétipo pode começar com uma tabela para consulta rápida. Ela segue os mesmos formatos do cabeçalho: os Atributos escritos por extenso e as Habilidades requeridas com o custo e, quando for o caso, o Arquétipo.

| Habilidade         | Custo de PHs | Requisitos de Atributos | Requisitos de Habilidades                                |
| ------------------ | ------------ | ----------------------- | -------------------------------------------------------- |
| Nome da Habilidade | X            | 3 de Arcano             | "Nome da Habilidade Requerida" de Custo X                |
| Nome da Habilidade | X            | -                       | "Nome da Habilidade Requerida" de Custo X do Arquétipo Y |