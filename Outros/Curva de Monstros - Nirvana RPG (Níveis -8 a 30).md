
Fórmulas de PV, Mana e Dano para monstros de Nível -8 a 30, com CA e CD de apoio. **Versão 2:** os atributos dos monstros são independentes do Nível, e as fórmulas de PV e Mana aceitam qualquer valor de Constituição e Sabedoria.

---

## 1. Premissas

- **Equivalência de poder:** Nível $-8 =$ meio jogador de Nível 1; Nível $-4 = 1$ jogador de Nível 1; Nível $1 = 4$ jogadores de Nível 1. Do Nível 1 em diante, um monstro de Nível $L$ equivale a 4 jogadores de Nível $L$.
- **Poder ($n$):** É o valor em jogadores de Nível 1 para monstros de Nível $< 1$:
    - $n = 2^{(L+4)/4}$ de -8 a -4
    - $n = 4^{(L+4)/5}$ de -4 a 1
- **Encontro Moderado:** O monstro dura cerca de 3,5 rodadas contra o grupo e causa cerca de 20% dos PV totais do grupo por rodada.
- **Atributos independentes do Nível:** Os atributos de um monstro vão de **-10 a 20** (modificadores de -5 a +10) e **não dependem do Nível**. Um Nível 3 pode ter Con 18, e um Nível 20 pode ter For -3. O Nível mede o poder total, e os atributos dizem _de onde_ esse poder vem.
- **Em todas as fórmulas, "Con" e "Sab" são os modificadores** (atributo $\div 2$, arredondado para baixo), como no resto do livro.
- **Referência:** Con 12 (mod +6) é o "Padrão". A tabela de PV com Con 12 da versão anterior continua valendo, porque o Con +6 da fórmula nova reproduz os mesmos números.
- **Arredondamento:** Sempre para baixo, como no livro.

---

## 2. Poder ($n$) nos Níveis -8 a 1

|Nível|-8|-7|-6|-5|-4|-3|-2|-1|0|1|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**$n$ (jogadores de Nível 1)**|0,50|0,59|0,71|0,84|1,00|1,32|1,74|2,30|3,03|4,00|
|**Contribuição ao Nível do Encontro ($n \div 4$)**|0,12|0,15|0,18|0,21|0,25|0,33|0,44|0,57|0,76|1,00|

A soma de Níveis do Capítulo 2.2 funciona bem a partir do Nível 1, porque a curva é quase linear. Abaixo do Nível 1, some as contribuições da tabela (quatro monstros de Nível -4 valem um de Nível 1).

---

## 3. Pontos de Vida

$$PV = Xd20 + (\text{Con} \times K)$$

- **Nível $\ge 1$:** $K = 10 \times \text{Nível}$ e $X = \lfloor(49 + 3 \times \text{Nível}) \div 10{,}5\rfloor$.
- **Nível $< 1$:** dados menores (d6 a d12) e $K$ inteiro entre 2 e 10 (tabela abaixo). Com Con +6 o resultado fica a poucos PV da versão anterior.
- **Con negativo:** cada ponto negativo tira apenas $\max(\text{Nível}, 1)$ PV, em vez de $K$, e o PV nunca fica abaixo da metade dos dados. Assim um monstro frágil (fantasma, enxame) continua vivo e utilizável.
- **Média:** Dados $\times$ média do dado + bônus. Para ir mais rápido, use a média.

### Efeito da Constituição

Cada ponto de Con soma ou subtrai $K$ de PV, ou seja, cerca de **14% a 15% do PV Padrão** (Con +6) por ponto, nos níveis altos. A tabela abaixo mostra o PV médio resultante.

|Atributo|-5|0|4|8|12|16|20|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**Con (modificador)**|-3|0|+2|+4|**+6**|+8|+10|
|**PV no Nível 10 (média)**|54|84|284|484|684|884|1084|
|**% do Padrão (Nível 10)**|8%|12%|42%|71%|100%|129%|158%|

### Perfis de Constituição

Os perfis são só pontos de partida. Qualquer Con de -10 a 20 funciona.

|Perfil|Con (atributo)|Mod|Efeito no PV (nível alto)|
|:--|:-:|:-:|:--|
|**Espectro / Enxame**|-10 a 0|-5 a 0|só os dados, cerca de 10% do Padrão|
|**Frágil**|1 a 5|0 a +2|cerca de 12% a 42% do Padrão|
|**Conjurador**|6 a 9|+3 a +4|cerca de 55% a 70% do Padrão|
|**Padrão**|10 a 13|+5 a +6|85% a 100% (tabela do Con 12)|
|**Bruto**|14 a 17|+7 a +8|115% a 130%|
|**Tanque**|18 a 20|+9 a +10|145% a 160%|

Para um monstro que não é nenhum desses perfis, rolar Con e Sab separadamente também vale (por exemplo, um golem com Con 20 e Sab -4).

### Tabela de PV (PV médio por Constituição)

Fórmula por Nível e PV médio para cada modificador de Con.

|Nível|PV (dados + bônus)|Con -3|Con 0|Con +2|Con +4|Con +6|Con +8|Con +10|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**-8**|$1d8 + \text{Con} \times 2$|2|4|8|12|16|20|24|
|**-7**|$1d10 + \text{Con} \times 2$|2|5|9|13|17|21|25|
|**-6**|$1d10 + \text{Con} \times 2$|2|5|9|13|17|21|25|
|**-5**|$1d12 + \text{Con} \times 3$|3|6|12|18|24|30|36|
|**-4**|$2d6 + \text{Con} \times 3$|4|7|13|19|25|31|37|
|**-3**|$3d6 + \text{Con} \times 4$|7|10|18|26|34|42|50|
|**-2**|$4d6 + \text{Con} \times 6$|11|14|26|38|50|62|74|
|**-1**|$5d6 + \text{Con} \times 8$|14|17|33|49|65|81|97|
|**0**|$7d6 + \text{Con} \times 10$|21|24|44|64|84|104|124|
|**1**|$5d20 + \text{Con} \times 10$|49|52|72|92|112|132|152|
|**2**|$5d20 + \text{Con} \times 20$|46|52|92|132|172|212|252|
|**3**|$6d20 + \text{Con} \times 30$|54|63|123|183|243|303|363|
|**4**|$6d20 + \text{Con} \times 40$|51|63|143|223|303|383|463|
|**5**|$6d20 + \text{Con} \times 50$|48|63|163|263|363|463|563|
|**6**|$6d20 + \text{Con} \times 60$|45|63|183|303|423|543|663|
|**7**|$7d20 + \text{Con} \times 70$|52|73|213|353|493|633|773|
|**8**|$7d20 + \text{Con} \times 80$|49|73|233|393|553|713|873|
|**9**|$7d20 + \text{Con} \times 90$|46|73|253|433|613|793|973|
|**10**|$8d20 + \text{Con} \times 100$|54|84|284|484|684|884|1084|
|**11**|$8d20 + \text{Con} \times 110$|51|84|304|524|744|964|1184|
|**12**|$8d20 + \text{Con} \times 120$|48|84|324|564|804|1044|1284|
|**13**|$8d20 + \text{Con} \times 130$|45|84|344|604|864|1124|1384|
|**14**|$9d20 + \text{Con} \times 140$|52|94|374|654|934|1214|1494|
|**15**|$9d20 + \text{Con} \times 150$|49|94|394|694|994|1294|1594|
|**16**|$9d20 + \text{Con} \times 160$|47|94|414|734|1054|1374|1694|
|**17**|$10d20 + \text{Con} \times 170$|54|105|445|785|1125|1465|1805|
|**18**|$10d20 + \text{Con} \times 180$|52|105|465|825|1185|1545|1905|
|**19**|$10d20 + \text{Con} \times 190$|52|105|485|865|1245|1625|2005|
|**20**|$10d20 + \text{Con} \times 200$|52|105|505|905|1305|1705|2105|
|**21**|$11d20 + \text{Con} \times 210$|57|115|535|955|1375|1795|2215|
|**22**|$11d20 + \text{Con} \times 220$|57|115|555|995|1435|1875|2315|
|**23**|$11d20 + \text{Con} \times 230$|57|115|575|1035|1495|1955|2415|
|**24**|$12d20 + \text{Con} \times 240$|63|126|606|1086|1566|2046|2526|
|**25**|$12d20 + \text{Con} \times 250$|63|126|626|1126|1626|2126|2626|
|**26**|$12d20 + \text{Con} \times 260$|63|126|646|1166|1686|2206|2726|
|**27**|$12d20 + \text{Con} \times 270$|63|126|666|1206|1746|2286|2826|
|**28**|$13d20 + \text{Con} \times 280$|68|136|696|1256|1816|2376|2936|
|**29**|$13d20 + \text{Con} \times 290$|68|136|716|1296|1876|2456|3036|
|**30**|$13d20 + \text{Con} \times 300$|68|136|736|1336|1936|2536|3136|

_Os Níveis 21 a 30 são extrapolação: os jogadores param no Nível 20, então use-os para chefes lendários com Ações Lendárias e Resistências Lendárias._

_Os atributos também entram nas Salvaguardas. Um Con alto ou baixo, por exemplo, muda a Salvaguarda de Constituição do monstro, então a escolha do atributo tem efeito além do PV._

---

## 4. Mana

$$\text{Mana} = \text{Sab}\ d8 + (\text{Sab} \times \text{Nível})$$

- **Leitura:** role um d8 para cada ponto de Sab e some Sab $\times$ Nível. **Use no máximo Sab 5** (teto herdado da fórmula anterior). Nos Níveis $\le 0$, o segundo termo é zero e fica só $\text{Sab}\ d8$.
- **Exemplo:** Nível 10 com Sab +3 rola $3d8 + 30$ (média 43). Na fórmula anterior eram 42.
- É a regra dos jogadores ($\text{mod de Sabedoria} \times \text{Nível}$) acrescida do dado, que dá o bônus para o monstro conseguir conjurar e a variação entre dois monstros do mesmo Nível. A Sabedoria acima de 10 (dragões, liches) continua valendo para Salvaguardas, Percepção e Testes, mas não rende mais Mana nem mais dados.
- **Marcial (só Habilidades):** Sab +1, cerca de um terço da Mana de conjurador.
- **Conjurador:** Sab +3.
- **Chefe ou arquimago:** Sab +5 ou mais.
- **Sem Mana:** Sab 0 ou menos. Ignore o mínimo de 1 por Nível dos jogadores.
- **Magias Conhecidas:** Seguem a tabela dos jogadores (Sab 6 ou 7 dá 12 ou 13 Magias; Sab 10 dá 20 Magias e 10 Arcanos Menores). Acima de Sab 10, o Mestre escolhe a lista.
- **Custo máximo de Magia:**
    - Nível $\le -4 \rightarrow 1$
    - $-3 \text{ a } -1 \rightarrow 2$
    - $0 \text{ e } 1 \rightarrow 3$
    - $\ge 2 \rightarrow 3 + \lfloor \text{Nível} \div 2 \rfloor$, com teto 10.

### Perfis de Sabedoria

|Perfil|Sab (atributo)|Mod usado na Mana|
|:--|:-:|:-:|
|**Sem Mana**|-10 a 1|0|
|**Marcial**|2 a 3|+1|
|**Aprendiz**|4 a 5|+2|
|**Conjurador**|6 a 7|+3|
|**Mago veterano**|8 a 9|+4|
|**Arquimago / Chefe**|10 a 20|+5 (teto)|

### Tabela de Mana (média)

A média usa $4{,}5$ por d8, arredondada para baixo. A Mana real varia com os dados.

|Nível|Custo máx. de Magia|Sab +1|Sab +2|Sab +3|Sab +4|Sab +5|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**-8**|1|4|9|13|18|22|
|**-7**|1|4|9|13|18|22|
|**-6**|1|4|9|13|18|22|
|**-5**|1|4|9|13|18|22|
|**-4**|1|4|9|13|18|22|
|**-3**|2|4|9|13|18|22|
|**-2**|2|4|9|13|18|22|
|**-1**|2|4|9|13|18|22|
|**0**|3|4|9|13|18|22|
|**1**|3|5|11|16|22|27|
|**2**|4|6|13|19|26|32|
|**3**|4|7|15|22|30|37|
|**4**|5|8|17|25|34|42|
|**5**|5|9|19|28|38|47|
|**6**|6|10|21|31|42|52|
|**7**|6|11|23|34|46|57|
|**8**|7|12|25|37|50|62|
|**9**|7|13|27|40|54|67|
|**10**|8|14|29|43|58|72|
|**11**|8|15|31|46|62|77|
|**12**|9|16|33|49|66|82|
|**13**|9|17|35|52|70|87|
|**14**|10|18|37|55|74|92|
|**15**|10|19|39|58|78|97|
|**16**|10|20|41|61|82|102|
|**17**|10|21|43|64|86|107|
|**18**|10|22|45|67|90|112|
|**19**|10|23|47|70|94|117|
|**20**|10|24|49|73|98|122|
|**21**|10|25|51|76|102|127|
|**22**|10|26|53|79|106|132|
|**23**|10|27|55|82|110|137|
|**24**|10|28|57|85|114|142|
|**25**|10|29|59|88|118|147|
|**26**|10|30|61|91|122|152|
|**27**|10|31|63|94|126|157|
|**28**|10|32|65|97|130|162|
|**29**|10|33|67|100|134|167|
|**30**|10|34|69|103|138|172|

_Em relação à versão anterior, a média sobe cerca de 0,5 por ponto de Sab (e cai um pouco nos Níveis $\le 0$), o que não muda o equilíbrio._

---

## 5. Dano

Dano por rodada do monstro $\approx 20%$ da soma dos PV do grupo. Use 15% (Fácil) ou 25% (Difícil). Assim a regra se adapta ao grupo que você tem na mesa.

### PV dos jogadores em cada cenário

Segue as regras do livro: Nível 1 usa o dado no máximo, os demais níveis usam a média ($\text{máximo} \div 2$), e os Pontos Retroativos de Constituição contam.

- **Frágil (mago, Con 3 fixa):** $4 + 5 \times \text{Nível}$
- **Tanque (Con 10 fixa):** $15 + 20 \times \text{Nível}$
- **Crescente (Con acompanha o limite de atributo, de 3 no Nível 1 a 10 no Nível 14):** Tabela abaixo; do Nível 14 em diante, $20 \times \text{Nível} - 95$.

|Perfil|Nível 1|Nível 3|Nível 5|Nível 8|Nível 10|Nível 14|Nível 20|Nível 30|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**Frágil**|9|19|29|44|54|74|104|154|
|**Crescente**|9|24|38|76|110|185|305|505|
|**Tanque**|35|75|115|175|215|295|415|615|

### Dano por rodada para um grupo de 4

|Perfil de Grupo|Nível 1|Nível 3|Nível 5|Nível 8|Nível 10|Nível 14|Nível 20|Nível 30|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**Grupo de Frágeis**|7|15|23|35|43|59|83|123|
|**Grupo Crescente**|7|19|30|61|88|148|244|404|
|**Grupo de Tanques**|28|60|92|140|172|236|332|492|
|**Grupo Misto**|12|28|44|74|98|148|226|356|

_O grupo misto é 1 Frágil + 2 Crescentes + 1 Tanque, e é o usado na tabela completa abaixo._

### Tabela completa (grupo misto)

_Nos Níveis $< 1$, o dano moderado é $3{,}1 \times n$._

|Nível|Fácil (15%)|Moderado (20%)|Difícil (25%)|
|:-:|:-:|:-:|:-:|
|**-8**|1|2|2|
|**-7**|1|2|2|
|**-6**|2|2|3|
|**-5**|2|3|3|
|**-4**|2|3|4|
|**-3**|3|4|5|
|**-2**|4|5|7|
|**-1**|5|7|9|
|**0**|7|9|12|
|**1**|9|12|16|
|**2**|15|21|26|
|**3**|21|28|36|
|**4**|27|36|45|
|**5**|33|44|55|
|**6**|42|55|69|
|**7**|49|65|81|
|**8**|56|74|93|
|**9**|63|84|105|
|**10**|73|98|122|
|**11**|81|108|136|
|**12**|89|119|149|
|**13**|97|130|162|
|**14**|111|148|185|
|**15**|121|161|201|
|**16**|130|174|217|
|**17**|140|187|234|
|**18**|150|200|250|
|**19**|160|213|266|
|**20**|169|226|282|
|**21**|179|239|299|
|**22**|189|252|315|
|**23**|199|265|331|
|**24**|208|278|347|
|**25**|218|291|364|
|**26**|228|304|380|
|**27**|238|317|396|
|**28**|247|330|412|
|**29**|257|343|429|
|**30**|267|356|445|

### Dano por ação

- **Uma Ação:** cerca de 35% do dano por rodada.
- **Duas Ações:** cerca de 65%.
- **Três Ações:** cerca de 100%.
- **Em área:** reduza em cerca de 25%.
- **Crítico** dobra o dano, e o dano mínimo é 1.

---

## 6. Cuidados e ajustes

### Morte instantânea

Com a regra de morte instantânea (dano em uma instância $=$ dobro dos PV Máximos), o dano do grupo misto passa do limite de um Frágil a partir de certo nível.

|Nível|Dobro dos PV do mago (Frágil)|Dano/rodada do grupo misto|
|:-:|:-:|:-:|
|**1**|18|12|
|**10**|108|98|
|**14**|148|148|
|**20**|208|226|
|**30**|308|356|

Do Nível 14 em diante, um golpe de três Ações com todo o dano de uma rodada em um alvo só pode matar um mago de uma vez. Mantenha a maior instância de dano abaixo de ~90% do valor da tabela, ou assuma o risco como característica de um monstro assassino.

### Monstros comuns versus chefes

A curva de PV foi calibrada para lutas de ~3,5 rodadas com Con +6 (Padrão), o que combina mais com chefes. Para monstros comuns, multiplique o PV por ~0,7 (cerca de 2,5 rodadas) e o dano por ~1,3.

### Atributos fora do Padrão

Um monstro com Con alto ou baixo muda a duração da luta. Se quiser manter a luta em ~3,5 rodadas, compense: monstro de Con baixo pode causar um pouco mais de dano, e de Con alto, um pouco menos (cerca de $\pm 10%$ por perfil).

---

## 7. Anexo: CA e CD

- **CA:**
    - Nível $\ge 1$: $13 + 0{,}6 \times (\text{Nível} - 1)$
    - Nível $< 1$: $11 + 0{,}4 \times (\text{Nível} + 4)$, com mínimo 10.
- **Bônus de Ataque:** $\text{CA} - 8$, o que dá cerca de 65% de acerto contra um jogador do mesmo nível.
- **CD de Salvaguarda:** (depende só do Nível, não dos atributos do monstro)
    - Nível $\ge 1$: $11 + \text{Nível} \div 2$ (arredondando 0,5 para cima).
    - Nível $< -4$: 10.
    - Níveis -3 a 0: 11.

|Nível|CA|CD|Nível|CA|CD|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**-8**|10|10|**11**|19|17|
|**-7**|10|10|**12**|20|17|
|**-6**|10|10|**13**|20|18|
|**-5**|11|10|**14**|21|18|
|**-4**|11|10|**15**|21|19|
|**-3**|11|11|**16**|22|19|
|**-2**|12|11|**17**|23|20|
|**-1**|12|11|**18**|23|20|
|**0**|13|11|**19**|24|21|
|**1**|13|12|**20**|24|21|
|**2**|14|12|**21**|25|22|
|**3**|14|13|**22**|26|22|
|**4**|15|13|**23**|26|23|
|**5**|15|14|**24**|27|23|
|**6**|16|14|**25**|27|24|
|**7**|17|15|**26**|28|24|
|**8**|17|15|**27**|29|25|
|**9**|18|16|**28**|29|25|
|**10**|18|16|**29**|30|26|
|—|—|—|**30**|30|26|