#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de custos do Shattered Veil.

Modos:
  1. Moedas (Custo de Moedas.md)  -> resultado em PO / PL / PP / PC
  2. Mana   (Custos de Mana.md)   -> resultado em PMs
  3. PH     (Custo de PHs.md)     -> resultado em PHs

Uso: python3 calculadora_custos.py
Durante a escolha de efeitos:
  <número>  adiciona o efeito       m  mostra o menu       v  mostra o que foi escolhido
  d         desfaz o último         c  calcula             s  volta ao menu de modos
"""

import math
from fractions import Fraction


# ----------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------
def arred(x):
    """Arredondamento matematico: 0,5 sobe."""
    return int(math.floor(x + 0.5))


def fmt(x):
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")


def ler(msg):
    return input(msg).strip()


def ler_int(msg, mínimo=None, máximo=None, padrao=None):
    while True:
        sufixo = f" [{padrao}]" if padrao is not None else ""
        txt = ler(f"{msg}{sufixo}: ")
        if txt == "" and padrao is not None:
            return padrao
        try:
            v = int(txt)
        except ValueError:
            print("  Digite um número inteiro.")
            continue
        if (mínimo is not None and v < mínimo) or (máximo is not None and v > máximo):
            print(f"  Valor fora do intervalo ({mínimo} a {máximo}).")
            continue
        return v


def ler_float(msg, mínimo=None, padrao=None):
    while True:
        sufixo = f" [{fmt(padrao)}]" if padrao is not None else ""
        txt = ler(f"{msg}{sufixo}: ")
        if txt == "" and padrao is not None:
            return padrao
        try:
            v = float(txt.replace(",", "."))
        except ValueError:
            print("  Digite um número.")
            continue
        if mínimo is not None and v < mínimo:
            print(f"  O valor mínimo é {fmt(mínimo)}.")
            continue
        return v


def escolher(titulo, opcoes, padrao=None):
    """Mostra opcoes numeradas e devolve o indice (0-based)."""
    print(f"\n{titulo}")
    for i, o in enumerate(opcoes, 1):
        print(f"  {i}. {o}")
    while True:
        sufixo = f" [{padrao + 1}]" if padrao is not None else ""
        txt = ler(f"Escolha{sufixo}: ")
        if txt == "" and padrao is not None:
            return padrao
        if txt.isdigit() and 1 <= int(txt) <= len(opcoes):
            return int(txt) - 1
        print("  Opção inválida.")


def escolher_varias(titulo, opcoes):
    """Devolve uma lista de indices (0-based). Enter = nenhuma."""
    print(f"\n{titulo}")
    for i, o in enumerate(opcoes, 1):
        print(f"  {i}. {o}")
    while True:
        txt = ler("Números separados por virgula (Enter = nenhum): ")
        if txt == "":
            return []
        partes = txt.replace(",", " ").split()
        if all(p.isdigit() and 1 <= int(p) <= len(opcoes) for p in partes):
            return sorted(set(int(p) - 1 for p in partes))
        print("  Entrada inválida.")


def sim_nao(msg, padrao=False):
    sufixo = " [S/n]" if padrao else " [s/N]"
    while True:
        txt = ler(msg + sufixo + ": ").lower()
        if txt == "":
            return padrao
        if txt in ("s", "sim"):
            return True
        if txt in ("n", "não", "não"):
            return False
        print("  Responda s ou n.")


# ----------------------------------------------------------------------
# Estruturas
# ----------------------------------------------------------------------
class Efeito:
    """
    tipos:
      fixo       dados = preço unitario (quantidade multiplica)
      grau       dados = lista com 10 precos (Graus 1 a 10)
      dur        dados = {duracao: preço}
      tabela     dados = {N: preço do bônus +N}
      cubico     preço de +N = (N+1)^3
      triplo     dados = base; preço de N iteracoes = base * 3^(N-1)
      escolha    dados = {opcao: preço}
      perm_fator dados = preço permanente; pergunta se e permanente ou temporário
    """

    def __init__(self, nome, tipo, dados, categoria, tags=()):
        self.nome = nome
        self.tipo = tipo
        self.dados = dados
        self.categoria = categoria
        self.tags = set(tags)


class Item:
    def __init__(self, texto, custo, tags):
        self.texto = texto
        self.custo = custo
        self.tags = set(tags)


class Modo:
    def __init__(self, titulo, unidade, efeitos, calcular, longas=None, ref_longa="1 Encontro", fatores=None):
        self.titulo = titulo
        self.unidade = unidade
        self.efeitos = efeitos
        self.calcular = calcular
        self.longas = longas or {}
        self.ref_longa = ref_longa
        self.fatores = fatores or {}


# ----------------------------------------------------------------------
# Perguntas por efeito
# ----------------------------------------------------------------------
def pedir_efeito(e, modo):
    print(f"\n-> {e.nome}")
    det = []
    qtd = 1
    t = e.tipo

    if t == "fixo":
        qtd = ler_int("Quantas vezes", 1, padrao=1)
        custo = e.dados * qtd

    elif t == "grau":
        grau = ler_int("Grau (1 a 10)", 1, 10)
        qtd = ler_int("Quantas vezes", 1, padrao=1)
        custo = e.dados[grau - 1] * qtd
        det.append(f"Grau {grau}")
        if "area_moedas" in e.tags:
            raio = ler_float("Raio da área em metros (0 = alvo único)", 0, padrao=0)
            if raio > 0:
                passos = math.ceil(raio / 1.5 - 1e-9)
                custo *= 1.5 ** passos
                det.append(f"raio {fmt(raio)} m")

    elif t == "dur":
        rotulos = list(e.dados.keys())
        precos = dict(e.dados)
        if "longa" in e.tags and modo.longas:
            base = e.dados[modo.ref_longa]
            for r, m in modo.longas.items():
                rotulos.append(r)
                precos[r] = base * m
        i = escolher("Duração", [f"{r}  ({fmt(precos[r])})" for r in rotulos])
        qtd = ler_int("Quantas vezes", 1, padrao=1)
        custo = precos[rotulos[i]] * qtd
        det.append(rotulos[i])

    elif t == "tabela":
        n = ler_int(f"Valor do bônus (+N, de {min(e.dados)} a {max(e.dados)})", min(e.dados), max(e.dados))
        custo = e.dados[n]
        det.append(f"+{n}")

    elif t == "cubico":
        n = ler_int("Valor do bônus (+N)", 1)
        custo = (n + 1) ** 3
        det.append(f"+{n}")

    elif t == "triplo":
        n = ler_int("Quantos aumentos de +1,5 m", 1)
        custo = e.dados * 3 ** (n - 1)
        det.append(f"+{fmt(1.5 * n)} m")

    elif t == "escolha":
        rotulos = list(e.dados.keys())
        i = escolher("Opção", [f"{r}  ({fmt(e.dados[r])})" for r in rotulos])
        qtd = ler_int("Quantas vezes", 1, padrao=1)
        custo = e.dados[rotulos[i]] * qtd
        det.append(rotulos[i])

    elif t == "perm_fator":
        rotulos = ["Permanente"] + list(modo.fatores.keys())
        textos = ["Permanente  (x1)"] + [f"{r}  (x{fmt(f)})" for r, f in modo.fatores.items()]
        i = escolher("Permanente ou temporário?", textos, padrao=0)
        fator = 1.0 if i == 0 else modo.fatores[rotulos[i]]
        qtd = ler_int("Quantas vezes", 1, padrao=1)
        custo = e.dados * fator * qtd
        det.append(rotulos[i])

    else:
        raise ValueError(f"tipo desconhecido: {t}")

    texto = e.nome
    if det:
        texto += f" [{', '.join(det)}]"
    if qtd != 1:
        texto += f" x{qtd}"
    return Item(texto, custo, e.tags)


def mostrar_menu(efeitos):
    cat = None
    for i, e in enumerate(efeitos, 1):
        if e.categoria != cat:
            cat = e.categoria
            print(f"\n== {cat} ==")
        print(f"  {i:>3}. {e.nome}")


def listar_itens(itens, unidade):
    if not itens:
        print("  (nenhum efeito escolhido)")
        return
    for i, it in enumerate(itens, 1):
        print(f"  {i}. {it.texto} = {fmt(it.custo)} {unidade}")
    print(f"  Subtotal dos efeitos: {fmt(sum(i.custo for i in itens))} {unidade}")


def coletar(modo):
    itens = []
    mostrar_menu(modo.efeitos)
    print("\nComandos: <número> adiciona | m menu | v ver escolhidos | d desfaz | c calcula | s sair do modo")
    while True:
        cmd = ler("\n> ").lower()
        if cmd == "c":
            if not itens:
                print("  Nenhum efeito escolhido ainda.")
                continue
            return itens
        elif cmd == "m":
            mostrar_menu(modo.efeitos)
        elif cmd == "v":
            listar_itens(itens, modo.unidade)
        elif cmd == "d":
            if itens:
                print(f"  Removido: {itens.pop().texto}")
            else:
                print("  Nada para desfazer.")
        elif cmd == "s":
            return None
        elif cmd.isdigit() and 1 <= int(cmd) <= len(modo.efeitos):
            item = pedir_efeito(modo.efeitos[int(cmd) - 1], modo)
            itens.append(item)
            print(f"  Adicionado: {item.texto} = {fmt(item.custo)} {modo.unidade}")
        else:
            print("  Comando inválido.")


# ----------------------------------------------------------------------
# Área, alvos e alcance (Mana e PH usam as mesmas regras)
# ----------------------------------------------------------------------
def passos_de_area():
    formas = ["Esfera ou Cilindro (raio)", "Cone (comprimento)", "Cubo (lado)", "Linha (comprimento)"]
    f = escolher("Formato da Área", formas)
    tam = ler_float("Tamanho em metros", 0.1)
    if f == 0:
        r = tam
    elif f in (1, 2):
        r = tam / 2
    else:
        r = 1.5 * math.ceil(tam / 9 - 1e-9)
        largura = ler_float("Largura da Linha em metros", 0.1, padrao=1.5)
        if largura >= 3:
            r += 1.5
    passos = max(1, math.ceil(r / 1.5 - 1e-9))
    return passos, f"{formas[f].split(' ')[0]} de {fmt(tam)} m (raio equivalente {fmt(passos * 1.5)} m)"


def pedir_alvos_e_alcance(preco_passo_alcance):
    """Devolve (multiplicador, descricao, n_alvos_multiplos, custo_alcance)."""
    modo_alvo = escolher("Alvos da Magia/Habilidade", ["Alvo Único", "Área de Efeito", "Múltiplos Alvos"], padrao=0)
    mult, descr, n = 1.0, "Alvo Único", 1
    if modo_alvo == 1:
        passos, descr = passos_de_area()
        mult = 1.5 + 0.5 * passos
        descr = f"Área: {descr}, multiplicador {fmt(mult)}x"
    elif modo_alvo == 2:
        n = ler_int("Quantidade de alvos", 2)
        mult = float(n)
        descr = f"{n} Múltiplos Alvos, multiplicador {n}x"
    alcance = ler_float("Alcance em metros (0 = Toque; até 9 m é gratuito)", 0, padrao=0)
    custo = 0.0
    if alcance > 9:
        passos = math.ceil((alcance - 9) / 1.5 - 1e-9)
        custo = passos * preco_passo_alcance
        if modo_alvo == 2:
            custo *= n
    return mult, descr, custo


def aplicar_multiplicador(itens, mult):
    com = sum(i.custo for i in itens if "sem_area" not in i.tags)
    sem = sum(i.custo for i in itens if "sem_area" in i.tags)
    return com * mult + sem, com, sem


# ----------------------------------------------------------------------
# MOEDAS
# ----------------------------------------------------------------------
TAB_BA_CA = {1: 1, 2: 5, 3: 10, 4: 25, 5: 50, 6: 75, 7: 100, 8: 150, 9: 300, 10: 750}
DUR7 = ["1 Rodada", "2 Rodadas", "3 Rodadas", "4 Rodadas", "1 Encontro", "1 hora", "Mais de 1 hora"]


def d7(*v):
    return dict(zip(DUR7, v))


def efeitos_moedas():
    E = []

    c = "Efeitos permanentes (Passivas)"
    E.append(Efeito("+1 de BD", "fixo", 2, c))
    E.append(Efeito("+1 de Resistência a um tipo de dano", "fixo", 3, c))
    E.append(Efeito("+1,5 m de alcance corpo a corpo (o preço triplica a cada iteracao)", "triplo", 10, c))
    E.append(Efeito("+1,5 m de alcance de Ataque a distancia", "fixo", 1, c))
    E.append(Efeito("+1,5 m de Deslocamento", "fixo", 250, c))
    E.append(Efeito("Bônus em Teste de Perícia (+N, preço cubico)", "cubico", None, c))
    E.append(Efeito("1 de Regeneração de PV (permanente)", "fixo", 375, c))
    E.append(Efeito("1 de Regeneração de PM (permanente)", "fixo", 938, c))
    E.append(Efeito("BA permanente (+N)", "tabela", TAB_BA_CA, c))
    E.append(Efeito("CA permanente (+N)", "tabela", TAB_BA_CA, c))

    c = "Efeitos instantâneos"
    E.append(Efeito("1 de Cura (alvo único)", "fixo", 2, c))
    E.append(Efeito("1 PM restaurado", "fixo", 5, c))
    E.append(Efeito("1 de Dano causado (alvo único)", "fixo", 1, c))
    E.append(Efeito("1 de Dano causado (por 1,5 m de área)", "fixo", 1.5, c))
    E.append(Efeito("1 de PV Temporário", "fixo", 188, c))
    E.append(Efeito("1 de PM Temporário", "fixo", 470, c))
    E.append(Efeito("Grau de Dano", "grau", [2.5, 3.5, 4.5, 5.5, 6.5, 7, 9, 11, 13, 16.5], c, {"area_moedas"}))
    E.append(Efeito("Grau de Cura", "grau", [5, 7, 9, 11, 13, 14, 18, 22, 26, 33], c, {"area_moedas"}))
    E.append(Efeito("Grau de PMs restaurados", "grau", [12.5, 17.5, 22.5, 27.5, 32.5, 35, 45, 55, 65, 82.5], c, {"area_moedas"}))

    c = "Efeitos duradouros, mas não permanentes"
    temp = [
        ("1 de Dano Contínuo", d7(1, 3, 6, 12, 24, 144, 250)),
        ("1 de Regeneração de PV", d7(1.5, 5, 9, 18, 36, 216, 375)),
        ("1 de Regeneração de PM", d7(3.8, 12.5, 22.5, 45, 90, 540, 938)),
        ("1 de PV Temporário", d7(0.7, 3, 5, 9, 18, 108, 188)),
        ("1 de PM Temporário", d7(1.8, 8, 12.5, 22.5, 45, 270, 470)),
        ("+1 no BD", d7(0.5, 0.7, 0.9, 1.5, 2, 2, 2)),
        ("+1 no BA", d7(5, 10, 20, 25, 40, 240, 500)),
        ("+1 na CA", d7(5, 10, 20, 25, 40, 240, 500)),
        ("+1 de Resistência", d7(0.5, 0.8, 1, 1.5, 3, 3, 3)),
        ("Aumenta em 1 o valor de um Atributo", d7(1, 2, 3, 4, 5, 30, 50)),
        ("+1,5 m de Deslocamento", d7(10, 20, 35, 50, 75, 250, 250)),
        ("Recebe uma Condição positiva", d7(10, 15, 20, 25, 40, 240, 500)),
        ("Outros efeitos menores", d7(0.4, 0.6, 0.8, 1, 1.6, 9.6, 20)),
    ]
    for nome, vals in temp:
        E.append(Efeito(nome + " (temporário)", "dur", vals, c))

    c = "Armas"
    E.append(Efeito("Grau da Arma (preço final)", "grau", [5, 7, 9, 11, 13, 28, 54, 88, 130, 330], c))
    E.append(Efeito("Escala de Arma", "escolha", {"D": 5, "C": 20, "B": 75, "A": 300, "S": 2500}, c))
    E.append(Efeito("Aprimorar Arma até o Grau N (total acumulado)", "tabela",
                    dict(zip(range(1, 11), [0, 20, 40, 60, 100, 140, 180, 240, 300, 400])), c))

    c = "Armaduras"
    E.append(Efeito("Escala de Armadura", "escolha", {"D": 8, "C": 23, "B": 115, "A": 450, "S": 2850}, c))
    E.append(Efeito("Aprimorar Armadura até CA +N (total acumulado)", "tabela",
                    dict(zip(range(1, 11), [0, 40, 80, 120, 200, 280, 360, 480, 600, 800])), c))

    c = "Escudos"
    E.append(Efeito("+1 de Resistência de Escudo (Física e Mágica)", "fixo", 6, c))
    E.append(Efeito("Aprimorar Escudo até Resistência +N (total acumulado)", "tabela",
                    dict(zip(range(1, 11), [0, 15, 30, 45, 75, 105, 135, 180, 225, 300])), c))
    E.append(Efeito("Habilidade de Escudo: Aparar (1 uso por Encontro)", "fixo", 6.3, c))
    E.append(Efeito("Habilidade de Escudo: Golpe de Escudo", "fixo", 9.8, c))
    E.append(Efeito("Habilidade de Escudo: Parede de Escudo", "fixo", 7.9, c))

    c = "Infusões"
    E.append(Efeito("Infusão de Escala - Pedra comum (preço final)", "escolha",
                    {"Grau C": 70, "Grau B": 120, "Grau A": 350, "Grau S": 2450}, c))
    E.append(Efeito("Infusão de Escala - Pedra exclusiva (preço final)", "escolha",
                    {"Grau C": 120, "Grau B": 170, "Grau A": 400, "Grau S": 2500}, c))
    E.append(Efeito("Pedra Bruta (preço para infundir)", "fixo", 150, c))
    E.append(Efeito("Pedra Branca (pedra + remoção)", "fixo", 100, c))
    return E


DESC_MOEDAS = [
    ("Desvantagem em uma Perícia", Fraction(1, 4)),
    ("-1,5 m de Deslocamento", Fraction(1, 8)),
    ("Requer uma Ação e não é Ataque/Arma", Fraction(1, 4)),
    ("Requer uma Reação e não é Ataque/Arma", Fraction(1, 4)),
    ("Requer uma Ação Bônus e não é Ataque/Arma", Fraction(1, 8)),
    ("Requer uma Salvaguarda e não é Ataque/Arma", Fraction(1, 8)),
    ("Uma vez por Descanso Curto / por qualquer Descanso", Fraction(1, 16)),
    ("Uma vez por Descanso Longo", Fraction(1, 8)),
    ("Uma vez por Encontro", Fraction(1, 8)),
    ("Uma vez por Alvo", Fraction(1, 8)),
]


def texto_moedas(po):
    """Aplica a Regra de Ouro de arredondamento dos precos."""
    if po < 1:
        pc_total = arred(po * 100)
        if pc_total >= 100:
            return "1 PO"
        pp, pc = divmod(pc_total, 10)
        partes = []
        if pp:
            partes.append(f"{pp} PP")
        if pc or not partes:
            partes.append(f"{pc} PC")
        return " ".join(partes)
    v = arred(po)
    if v < 100:
        return f"{v} PO"
    pl, resto = divmod(v, 10)
    return f"{pl} PL" + (f" {resto} PO" if resto else "")


def calcular_moedas(itens):
    bruto = sum(i.custo for i in itens)
    print(f"\nPreco bruto: {fmt(bruto)} PO")

    sel = escolher_varias(
        "Descontos percentuais (cada um reduz uma fração do custo total):",
        [f"{n} (reduz {f})" for n, f in DESC_MOEDAS],
    )
    total = Fraction(0)
    for i in sel:
        nome, base = DESC_MOEDAS[i]
        n = ler_int(f"Quantas vezes '{nome}' se aplica (a cada repetição o denominador cai pela metade, até 1/2)", 1, padrao=1)
        total += min(base * 2 ** (n - 1), Fraction(1, 2))
    req = ler_int("Soma dos valores de requisito (cada ponto desconta 1 PO)", 0, padrao=0)
    peso = ler_float("Peso do item (cada unidade desconta 5 PP = 0,5 PO)", 0, padrao=0)

    apos_pct = bruto * (1 - float(total))
    liquido = apos_pct - req - peso * 0.5
    piso = 0.25 * bruto
    final = max(liquido, piso)

    print("\n---------------- RESULTADO (Moedas) ----------------")
    listar_itens(itens, "PO")
    print(f"  Descontos percentuais: {total} -> {fmt(apos_pct)} PO")
    print(f"  Desconto de requisitos: -{req} PO | peso: -{fmt(peso * 0.5)} PO")
    if liquido < piso:
        print(f"  Piso de 25% do preço bruto aplicado ({fmt(piso)} PO)")
    print(f"\n  PRECO FINAL: {fmt(final)} PO  ->  {texto_moedas(final)}")


# ----------------------------------------------------------------------
# MANA
# ----------------------------------------------------------------------
DUR5 = ["1 Rodada", "2 Rodadas", "3 Rodadas", "4 Rodadas", "1 Encontro"]


def d5(*v):
    return dict(zip(DUR5, v))


COND_MANA = {
    "Caído": d5(5, 6, 7, 8, 10),
    "Agarrado": d5(6, 12, 18, 24, 60),
    "Amedrontado": d5(4, 7, 9, 12, 14),
    "Debilitado (visao)": d5(6, 9, 12, 18, 18),
    "Encantado": d5(14, 27, 41, 54, 135),
    "Incapacitado": d5(15, 30, 45, 60, 150),
    "Petrificado": d5(23, 45, 68, 90, 225),
    "Furtivo": d5(2, 3, 4, 5, 6),
    "Invisível": d5(3, 4, 5, 6, 8),
}
NEGATIVAS = ["Caído", "Agarrado", "Amedrontado", "Debilitado (visao)", "Encantado", "Incapacitado", "Petrificado"]
LONGAS_MANA = {"20 minutos": 1.25, "1 hora": 1.5, "8 horas": 2.0, "24 horas": 2.5}


def efeitos_mana():
    E = []
    c = "Graus (por uso)"
    E.append(Efeito("Grau de Dano", "grau", [0, 0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5], c, {"dano_bd"}))
    E.append(Efeito("Grau de Cura", "grau", [0, 0, 2, 3, 4, 5, 6, 7, 8, 10], c))
    E.append(Efeito("Grau de PMs restaurados", "grau", [4, 5, 7, 8, 10, 11, 14, 17, 20, 25], c))

    c = "Efeitos instantâneos"
    E.append(Efeito("1 de dano", "fixo", 0.25, c, {"dano_bd"}))
    E.append(Efeito("1 de cura", "fixo", 0.5, c))
    E.append(Efeito("1 PM restaurado", "fixo", 1.5, c))
    E.append(Efeito("Empurrar ou puxar o alvo (1,5 m)", "fixo", 0.25, c))
    E.append(Efeito("Teletransporte (1,5 m)", "fixo", 0.25, c, {"sem_area"}))
    E.append(Efeito("Remover uma Condição negativa", "escolha",
                    {n: 0.5 * COND_MANA[n]["1 Encontro"] for n in NEGATIVAS}, c))
    E.append(Efeito("Condição Morto aplicada", "fixo", 200, c))
    E.append(Efeito("Reviver uma criatura Morta", "fixo", 100, c, {"sem_area"}))
    E.append(Efeito("1 de PV em um servo invocado", "fixo", 0.1, c, {"sem_area"}))
    E.append(Efeito("1 de CA em um servo invocado", "fixo", 0.25, c, {"sem_area"}))
    E.append(Efeito("1 de dano em um servo invocado", "fixo", 0.1, c, {"sem_area"}))
    E.append(Efeito("1 de BA em um servo invocado", "fixo", 0.25, c, {"sem_area"}))
    E.append(Efeito("1,5 m de Deslocamento em um servo invocado", "fixo", 0.25, c, {"sem_area"}))
    E.append(Efeito("1 Ação de um servo invocado por Rodada (até 3)", "fixo", 3, c, {"sem_area"}))

    c = "Efeitos temporários"
    longa = {"longa"}
    temp_longa = [
        ("+1 de BD", d5(0.1, 0.15, 0.2, 0.25, 0.5)),
        ("+1 de Resistência (por tipo de dano)", d5(0.1, 0.15, 0.2, 0.25, 0.5)),
        ("+1 de Fraqueza aplicada (por tipo de dano)", d5(0.1, 0.15, 0.2, 0.25, 0.5)),
        ("+1,5 m de Alcance Corpo a Corpo", d5(2, 2.5, 3, 4, 5)),
        ("+1,5 m de Alcance de Ataques Mágicos", d5(2, 2.5, 3, 4, 5)),
        ("+1,5 m de Deslocamento / -1,5 m no alvo", d5(1, 2, 2.5, 3, 4)),
        ("Deslocamento do alvo reduzido pela metade", d5(3, 6, 8, 9, 12)),
        ("Deslocamento de Voo (1,5 m)", d5(1, 2.5, 3, 3.5, 5)),
        ("+1 em Teste de Perícia", d5(0.25, 0.3, 0.35, 0.4, 0.5)),
        ("+1 em um Atributo", d5(0.5, 0.9, 1.3, 1.6, 2.5)),
        ("+1 de BA / retirar 1 de BA do alvo", d5(1, 1.5, 2, 3, 3)),
        ("+1 de CA / retirar 1 de CA do alvo", d5(1, 1.5, 2, 3, 3)),
        ("+1 na Margem de Ameaça", d5(0.3, 0.45, 0.6, 0.75, 1.5)),
        ("1 PV Temporário", d5(0.3, 0.35, 0.4, 0.45, 0.5)),
        ("1 PM Temporário", d5(0.75, 0.9, 1, 1.1, 1.25)),
        ("Efeito utilitário menor", d5(0.25, 0.4, 0.5, 0.6, 1)),
    ]
    for nome, vals in temp_longa:
        E.append(Efeito(nome, "dur", vals, c, longa))
    E.append(Efeito("1 de Regeneração de PV", "dur", d5(0.5, 1.1, 1.8, 2.5, 6), c))
    E.append(Efeito("1 de Regeneração de PM", "dur", d5(1.5, 3.3, 5.4, 7.5, 18), c))
    E.append(Efeito("1 de Dano Contínuo", "dur", d5(0.25, 0.55, 0.9, 1.25, 3), c, {"dano_bd"}))
    E.append(Efeito("1 de Dano Persistente em Área", "dur", d5(0.25, 0.5, 0.75, 1, 2), c, {"dano_bd"}))

    c = "Condições aplicadas"
    for nome, vals in COND_MANA.items():
        E.append(Efeito(nome, "dur", vals, c, longa))
    E.append(Efeito("Exausto (até Descanso Longo)", "escolha",
                    {f"Valor {i}": v for i, v in zip(range(1, 7), [30, 50, 100, 150, 200, 200])}, c))
    return E


def calcular_mana(itens):
    # BD: Magia de dano que não soma BD paga metade do custo de dano
    if any("dano_bd" in i.tags for i in itens):
        if not sim_nao("A Magia soma o BD do conjurador ao dano?", True):
            for i in itens:
                if "dano_bd" in i.tags:
                    i.custo *= 0.5
                    i.texto += " (sem BD: metade)"

    mult, descr, custo_alc = pedir_alvos_e_alcance(0.2)
    soma_mult, _, _ = aplicar_multiplicador(itens, mult)
    bruto = soma_mult + custo_alc

    print("\nDescontos percentuais (somam, no máximo 50%):")
    tempo = escolher(
        "Tempo de conjuração",
        ["Ação Livre (0%)", "Ação Bônus (-5%)", "Uma Ação (-10%)", "Reação (-15%)",
         "Duas Ações (-20%)", "Três Ações (-25%)", "Minutos, só fora de combate (-50%)"],
        padrao=2,
    )
    pct = [0, 5, 10, 15, 20, 25, 50][tempo]
    salv = escolher(
        "Salvaguarda",
        ["Nenhuma (0%)", "Reduz o dano à metade em caso de sucesso (-15%)", "Nega o efeito em caso de sucesso (-25%)"],
        padrao=0,
    )
    pct += [0, 15, 25][salv]
    if sim_nao("Afeta somente o conjurador? (-10%)", False):
        pct += 10
    pct = min(pct, 50)
    pv = ler_int("Quantos PVs são sacrificados (cada um desconta 0,5 PM)", 0, padrao=0)

    liquido = bruto * (1 - pct / 100) - 0.5 * pv
    piso = 0.25 * bruto
    final = max(liquido, piso)
    final_int = max(arred(final), 1)

    print("\n---------------- RESULTADO (Mana) ----------------")
    listar_itens(itens, "PM")
    print(f"  {descr}")
    print(f"  Soma com multiplicador: {fmt(soma_mult)} PM | Alcance: {fmt(custo_alc)} PM")
    print(f"  Custo bruto: {fmt(bruto)} PM")
    print(f"  Desconto percentual: -{pct}% | Sacrifício de PV: -{fmt(0.5 * pv)} PM")
    if liquido < piso:
        print(f"  Piso de 25% do custo bruto aplicado ({fmt(piso)} PM)")
    print(f"\n  CUSTO FINAL: {final_int} PM   (valor exato: {fmt(final)})")


# ----------------------------------------------------------------------
# PH
# ----------------------------------------------------------------------
FATORES_PH = {
    "1 Rodada": 0.1, "2 Rodadas": 0.2, "3 Rodadas": 0.3, "4 Rodadas": 0.4,
    "1 Encontro": 0.7, "1 hora": 0.9, "Mais de 1 hora": 1.0,
}
COND_PH = {n: {d: round(p * 0.4, 2) for d, p in v.items()} for n, v in COND_MANA.items()}


def efeitos_ph():
    E = []
    sa = {"sem_area"}

    c = "Valores fixos do sistema"
    E.append(Efeito("Proficiência (Armaduras, Armas CaC, Armas à Distância, Magias ou uma Salvaguarda)", "fixo", 1, c, sa))
    E.append(Efeito("Perito em uma Perícia", "fixo", 1, c, sa))
    E.append(Efeito("Iniciado em Magia", "fixo", 1, c, sa))
    E.append(Efeito("+1 Grau no Dado de Vida ou no Dado de Mana", "fixo", 1, c, sa))
    E.append(Efeito("+1 Ponto de Atributo", "fixo", 1, c, sa))

    c = "Efeitos permanentes (Passivas)"
    lista_bonus = [
        ("+1 de BA em Ataques", 0.8),
        ("+1 de CA", 1),
        ("+1 de BD", 0.1),
        ("+1 na Margem de Ameaça", 0.5),
        ("+1 de CD de Salvaguardas causadas", 0.6),
        ("+1 de BA em Salvaguardas de um Atributo", 0.15),
        ("+1 de Resistência (por tipo de dano)", 0.15),
        ("+1 em Teste de Perícia", 0.12),
        ("+1 em Iniciativa", 0.1),
        ("+1 em um Atributo", 1),
        ("+1,5 m de Deslocamento Terrestre", 0.3),
        ("+1,5 m de alcance corpo a corpo", 0.6),
        ("+1,5 m de alcance de Ataques à Distância", 0.1),
    ]
    for nome, p in lista_bonus:
        E.append(Efeito(nome, "perm_fator", p, c, sa))
    fixos = [
        ("+1 no Limite de um Atributo (acima de 10)", 1),
        ("Eliminar a penalidade do segundo Ataque do Turno (-5 de BA)", 3.5),
        ("Eliminar a penalidade do terceiro Ataque do Turno (-5 de BA adicionais)", 2),
        ("+1 Reação por Rodada", 1),
        ("+1 PV Máximo", 0.15),
        ("+1 PM Máximo", 0.15),
        ("+1 PV Máximo por Nível", 1),
        ("+1 PM Máximo por Nível", 1),
        ("1 de Regeneração de PV (por Turno)", 0.5),
        ("1 de Regeneração de PM (por Turno)", 1.25),
        ("1 PV Temporário por Descanso", 0.03),
        ("1 PM Temporário por Descanso", 0.08),
        ("+1 Idioma", 0.1),
        ("Visão no Escuro (18 m)", 0.4),
        ("Visão na Penumbra (18 m)", 0.2),
        ("+9 m de alcance de Visão no Escuro ou na Penumbra", 0.1),
        ("Deslocamento Aquático igual ao dobro do Terrestre", 0.3),
        ("Deslocamento Vertical igual ao Terrestre", 0.5),
        ("Deslocamento Subterrâneo igual à metade do Terrestre", 1.5),
        ("Deslocamento Aéreo igual ao Terrestre", 2.5),
        ("Imunidade a Dano de Queda", 0.2),
        ("Efeito utilitário menor (permanente)", 0.3),
        ("+1 de Resistência a Dano Fisico (os três tipos)", 0.3),
        ("+1 de Resistência a todos os tipos de dano", 0.75),
        ("Imunidade a um tipo de dano (20 de Resistência)", 3),
    ]
    for nome, p in fixos:
        E.append(Efeito(nome, "fixo", p, c, sa))
    E.append(Efeito("Vantagem permanente (5 pontos do bônus equivalente)", "escolha", {
        "Vantagem em Ataques": 4.0,
        "Vantagem em Salvaguardas de um Atributo": 0.75,
        "Vantagem em Testes de uma Perícia": 0.6,
        "Vantagem em Iniciativa": 0.5,
    }, c, sa))
    E.append(Efeito("Imunidade a uma Condição negativa", "escolha",
                    {n: 0.5 * COND_PH[n]["1 Rodada"] for n in NEGATIVAS}, c, sa))

    c = "Efeitos de Magia"
    magia = [
        ("+1 Magia conhecida", 0.3),
        ("Reduz em 1 PM o custo de todas as suas Magias", 1.8),
        ("Reduz em 1 PM o custo das suas Magias de uma categoria", 0.9),
        ("+1 Grau de dano em todas as suas Magias de dano", 0.3),
        ("+1 Grau de dano nas suas Magias de dano de uma categoria", 0.15),
        ("+1 Grau de cura em todas as suas Magias de cura", 0.5),
        ("Uma Metamagia Básica específica sem custo adicional de PMs", 0.5),
        ("Uma Metamagia Média específica sem custo adicional de PMs", 1),
        ("Uma Metamagia Avançada específica sem custo adicional de PMs", 1.5),
    ]
    for nome, p in magia:
        E.append(Efeito(nome, "fixo", p, c, sa))

    c = "Efeitos instantâneos (por uso)"
    E.append(Efeito("Grau de Dano", "grau", [0.2, 0.3, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 2], c))
    E.append(Efeito("Grau de Cura", "grau", [0.4, 0.6, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 4], c))
    E.append(Efeito("1 de dano", "fixo", 0.1, c))
    E.append(Efeito("1 de cura", "fixo", 0.2, c))
    E.append(Efeito("1 PM restaurado", "fixo", 0.6, c))
    E.append(Efeito("Empurrar ou puxar o alvo à força (1,5 m)", "fixo", 0.1, c))
    E.append(Efeito("Teletransporte (1,5 m)", "fixo", 0.1, c, sa))
    E.append(Efeito("Remover uma Condição negativa", "escolha",
                    {n: 0.5 * COND_PH[n]["1 Encontro"] for n in NEGATIVAS}, c))
    E.append(Efeito("1 de PV em um servo invocado", "fixo", 0.04, c, sa))
    E.append(Efeito("1 de CA em um servo invocado", "fixo", 0.1, c, sa))
    E.append(Efeito("1 de dano em um servo invocado", "fixo", 0.04, c, sa))
    E.append(Efeito("1 de BA em um servo invocado", "fixo", 0.1, c, sa))
    E.append(Efeito("1,5 m de Deslocamento em um servo invocado", "fixo", 0.1, c, sa))
    E.append(Efeito("1 Ação de um servo invocado por Rodada (até 3)", "fixo", 1.2, c, sa))

    c = "Efeitos persistentes"
    persist = [
        ("1 de Dano Contínuo", d5(0.1, 0.22, 0.36, 0.5, 1.2)),
        ("1 de Dano Persistente em Área", d5(0.1, 0.2, 0.3, 0.4, 0.8)),
        ("1 de Regeneração de PV", d5(0.2, 0.44, 0.72, 1, 2.4)),
        ("1 de Regeneração de PM", d5(0.6, 1.32, 2.16, 3, 7.2)),
        ("1 PV Temporário", d5(0.12, 0.14, 0.16, 0.18, 0.2)),
        ("1 PM Temporário", d5(0.3, 0.36, 0.4, 0.44, 0.5)),
    ]
    for nome, vals in persist:
        E.append(Efeito(nome, "dur", vals, c))

    c = "Condições aplicadas"
    for nome, vals in COND_PH.items():
        E.append(Efeito(nome, "dur", vals, c))
    E.append(Efeito("Exausto (até Descanso Longo)", "escolha",
                    {f"Valor {i}": v for i, v in zip(range(1, 6), [12, 20, 40, 60, 80])}, c))
    return E


RESTR_PH = [
    ("Só vale para um tipo de Ataque (CaC, à Distância ou Mágico)", Fraction(1, 4)),
    ("Só vale com Armas de um tipo de dano", Fraction(1, 3)),
    ("Só vale com uma Arma específica", Fraction(1, 2)),
    ("Só vale com um item equipado (Escudo, Armadura etc.)", Fraction(1, 8)),
    ("Só vale contra um tipo de criatura", Fraction(2, 5)),
    ("Só vale fora de combate", Fraction(1, 4)),
    ("Só vale uma vez por Turno", Fraction(1, 4)),
    ("Só vale no primeiro Ataque do Turno", Fraction(1, 2)),
    ("Só vale com Vantagem ou com a Condição Furtivo", Fraction(1, 2)),
    ("Só vale com menos da metade dos seus PVs", Fraction(1, 2)),
]


def calcular_ph(itens):
    mult, descr, custo_alc = pedir_alvos_e_alcance(0.08)
    soma_mult, _, _ = aplicar_multiplicador(itens, mult)
    bruto = soma_mult + custo_alc

    print("\nDescontos percentuais:")
    pct = Fraction(0)
    acao = escolher(
        "Custo de Ações",
        ["Ação Livre (sem desconto)", "Ação Bônus (1/8)", "Uma Ação (1/4)", "Reação (1/4)",
         "Duas Ações (3/8)", "Três Ações (1/2)"],
        padrao=0,
    )
    pct += [Fraction(0), Fraction(1, 8), Fraction(1, 4), Fraction(1, 4), Fraction(3, 8), Fraction(1, 2)][acao]
    mana = ler_int("Custo de Mana em PMs (cada PM reduz 1/20, até 1/2)", 0, padrao=0)
    pct += min(Fraction(mana, 20), Fraction(1, 2))
    uso = escolher(
        "Limite de Usos",
        ["Ilimitado (sem desconto)", "Duas vezes por Encontro (1/4)", "Uma vez por Encontro (2/5)",
         "Uma vez por Descanso Curto ou Longo (1/2)", "Uma vez por Descanso Longo (2/3)"],
        padrao=0,
    )
    pct += [Fraction(0), Fraction(1, 4), Fraction(2, 5), Fraction(1, 2), Fraction(2, 3)][uso]
    if sim_nao("Uma vez por alvo? (1/8)", False):
        pct += Fraction(1, 8)
    salv = escolher(
        "Salvaguarda",
        ["Nenhuma", "Dano cai à metade em caso de sucesso (1/8)", "Efeito negado em caso de sucesso (1/4)"],
        padrao=0,
    )
    pct += [Fraction(0), Fraction(1, 8), Fraction(1, 4)][salv]
    for i in escolher_varias("Restrições:", [f"{n} ({f})" for n, f in RESTR_PH]):
        pct += RESTR_PH[i][1]

    print("\nDescontos fixos:")
    req_attr = ler_int("Soma dos requisitos de Atributos (cada ponto desconta 0,1 PH)", 0, padrao=0)
    req_hab = ler_float("Soma do custo em PHs das Habilidades exigidas (cada PH desconta 0,2 PH)", 0, padrao=0)
    pen = ler_float("Preço do bônus equivalente a uma penalidade imposta a voce (desconta metade; 0 = nenhuma)", 0, padrao=0)
    fixos = req_attr * 0.1 + req_hab * 0.2 + pen * 0.5

    apos_pct = bruto * (1 - float(pct))
    liquido = apos_pct - fixos
    piso = 0.25 * bruto
    final = max(liquido, piso)
    arredondado = arred(final)
    final_int = min(max(arredondado, 1), 3)

    print("\n---------------- RESULTADO (PH) ----------------")
    listar_itens(itens, "PH")
    print(f"  {descr}")
    print(f"  Soma com multiplicador: {fmt(soma_mult)} PH | Alcance: {fmt(custo_alc)} PH")
    print(f"  Preço bruto: {fmt(bruto)} PH")
    print(f"  Descontos percentuais: {pct} -> {fmt(apos_pct)} PH | descontos fixos: -{fmt(fixos)} PH")
    if liquido < piso:
        print(f"  Piso de 25% do preço bruto aplicado ({fmt(piso)} PH)")
    print(f"\n  CUSTO FINAL: {final_int} PH   (valor exato: {fmt(final)})")
    if arredondado > 3:
        print("  AVISO: o resultado passa de 3 PHs. Divida o efeito em mais de uma Habilidade, cada uma exigindo a anterior.")
    elif arredondado < 1:
        print("  Observação: o custo mínimo de uma Habilidade é 1 PH.")


# ----------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------
def montar_modos():
    return [
        Modo("Moedas", "PO", efeitos_moedas(), calcular_moedas),
        Modo("Mana", "PM", efeitos_mana(), calcular_mana, longas=LONGAS_MANA),
        Modo("PH", "PH", efeitos_ph(), calcular_ph, fatores=FATORES_PH),
    ]


def main():
    modos = montar_modos()
    print("=== Calculadora de custos - Shattered Veil ===")
    while True:
        i = escolher("Escolha o modo (ou 0 para sair)", [m.titulo for m in modos] + ["Sair"])
        if i == len(modos):
            print("Até mais!")
            return
        modo = modos[i]
        while True:
            print(f"\n##### Modo {modo.titulo} #####")
            itens = coletar(modo)
            if itens is None:
                break
            modo.calcular(itens)
            if not sim_nao("\nCalcular outro custo neste modo?", True):
                break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrado.")