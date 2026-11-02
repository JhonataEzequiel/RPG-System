Este documento define como toda Habilidade é escrita, tanto as adquiridas com PHs (Capítulo 5) quanto as Habilidades de Raça (Capítulo 3). A estrutura tem dois níveis: o cabeçalho, com os dados da Habilidade inteira, e os efeitos, cada um com os seus próprios dados.

## Layout Recomendado: Vários Efeitos

```
### Nome da Habilidade

**Custo de PHs**: X | **Requisitos de Atributos**: Y | **Requisitos de Habilidades**: Z

Descrição geral: regras que valem para todos os efeitos da Habilidade.

- **Nome do Efeito 1** (Ativa | Custo de Ações: X | Custo de Mana: Y | Alcance: Z | Alvo: W | Duração: V | Limite de Usos: U): descrição do efeito.
  - **Aprimoramento** (Custo de Mana adicional: Y): descrição do aprimoramento.
- **Nome do Efeito 2** (Ativa | Custo de Ações: X | Alcance: Z): descrição do efeito.
- **Nome do Efeito 3** (Passiva | Alvo: W | Duração: V): descrição do efeito.
```

## Layout Recomendado: Efeito Único

Uma Habilidade com um único efeito não tem título nem lista. Ela é escrita como um parágrafo, com o nome em negrito e uma só linha de parênteses, que reúne primeiro os campos do cabeçalho e depois os do efeito.

```
**Nome da Habilidade** (Custo de PHs: X | Requisitos de Atributos: Y | Requisitos de Habilidades: Z | Ativa | Custo de Ações: X | Custo de Mana: Y | Alcance: Z | Alvo: W | Duração: V | Limite de Usos: U): descrição do efeito.
```

## Cabeçalho

O cabeçalho reúne apenas o que vale para a Habilidade inteira.

|Campo|Preenchimento|
|---|---|
|Custo de PHs|De 1 a 3.|
|Requisitos de Atributos|A sigla de cada Atributo exigido e o valor mínimo. Omitido se não houver requisitos.|
|Requisitos de Habilidades|As Habilidades que precisam ser adquiridas antes. Omitido se não houver requisitos.|

## Efeitos

Nas Habilidades de vários efeitos, cada efeito é um item da lista, com a sua própria linha de parênteses. Os campos são sempre escritos na ordem da tabela.

|Campo|Aplica-se a|Preenchimento|
|---|---|---|
|Ativa ou Passiva|Todo efeito|Sempre o primeiro item. Efeitos ativos custam uma Ação, uma Ação Livre ou uma Reação, e os passivos não custam nada.|
|Custo de Ações|Ativa|Uma Ação, Duas Ações, Três Ações, Ação Livre ou Reação.|
|Custo de Mana|Ativa|A quantidade de PMs.|
|Alcance|Todo efeito|Toque, uma distância em metros ou Ilimitado.|
|Alvo|Todo efeito|Quem ou o que é afetado: você, uma criatura, um Objeto, uma Área (formato e tamanho) etc.|
|Duração|Todo efeito|Instantânea, uma quantidade de Rodadas, um Encontro, uma quantidade de horas ou de dias etc.|
|Limite de Usos|Todo efeito|Quantas vezes o efeito pode ser usado e a cada quanto tempo, como uma vez por Encontro ou por Descanso.|

## Regras de Escrita

- Campos que não se aplicam a um efeito são omitidos.
- Efeitos com custos, alcances ou durações diferentes são itens separados da lista, cada um com a sua linha de parênteses.
- Um Aprimoramento é uma modificação opcional de um efeito ativo, paga com Mana adicional. Ele fica recuado dentro do efeito que modifica.
- Salvaguardas, tipos de dano, Graus, Condições e demais detalhes vão na descrição de cada efeito.
- O texto é escrito em segunda pessoa, e "você" é quem possui a Habilidade.
- Habilidades de Raça não têm os campos do cabeçalho, pois são gratuitas e não possuem requisitos. As de vários efeitos têm título "####" dentro de "### Habilidades de Raça", e as de efeito único são escritas direto, como parágrafos.

## Tabela-Índice de Arquétipo

Opcionalmente, cada Arquétipo pode começar com uma tabela para consulta rápida.

|Habilidade|Custo de PHs|Requisitos de Atributos|Requisitos de Habilidades|
|---|---|---|---|
|Nome da Habilidade|X|Y|Z|
