#!/usr/bin/env python3
"""Consulta rápida de monstros do Nirvana RPG (níveis -8 a 30).

Digite o nível e veja PV médio, Mana, dano por rodada, CA e CD.
Enter em branco (ou 'q') para sair.
"""


def r(x):
    """Arredonda 0,5 para cima."""
    return int(x + 0.5)


# PV de um jogador "Crescente" (Con acompanha o limite de atributo), níveis 1 a 13.
# A partir do nível 14 a fórmula é 20 * nível - 95.
CRESCENTE = {1: 9, 2: 17, 3: 24, 4: 31, 5: 38, 6: 54, 7: 65,
             8: 76, 9: 87, 10: 110, 11: 124, 12: 138, 13: 152}

# PV dos monstros nos níveis -8 a 0: (quantidade de dados, lados, bônus), Con 12
PV_BAIXO = {-8: (1, 8, 10), -7: (1, 10, 12), -6: (1, 10, 14), -5: (1, 12, 17),
            -4: (2, 6, 20), -3: (3, 6, 26), -2: (4, 6, 35), -1: (5, 6, 46),
            0: (7, 6, 61)}


def poder(nivel):
    """Poder em jogadores de nível 1 (só para níveis abaixo de 1)."""
    if nivel <= -4:
        return 2 ** ((nivel + 4) / 4)
    if nivel < 1:
        return 4 ** ((nivel + 4) / 5)
    return 4


def pv(nivel):
    if nivel < 1:
        dados, lados, bonus = PV_BAIXO[nivel]
        media = int(dados * (lados + 1) / 2 + bonus)
        return f"{dados}d{lados} + {bonus}", media
    x = r((49 + 3 * nivel) / 10.5)
    bonus = 60 * nivel
    return f"{x}d20 + {bonus}", int(10.5 * x + bonus)


def mana(nivel):
    """Retorna (Sab, custo máximo de Magia, Mana conjurador, Mana máxima)."""
    if nivel <= -4:
        sab, mod, custo = 2, 1, 1
    elif nivel < 0:
        sab, mod, custo = 4, 2, 2
    else:
        sab, mod = 6, 3
        custo = 3 if nivel <= 1 else min(10, 3 + nivel // 2)
    base = max(5, nivel + 4)
    return sab, custo, mod * base, 5 * base


def dano(nivel):
    """Retorna (fácil, moderado, difícil) para um grupo misto."""
    if nivel < 1:
        grupo = 15.5 * poder(nivel)
    else:
        fragil = 4 + 5 * nivel
        tanque = 15 + 20 * nivel
        crescente = CRESCENTE.get(nivel, 20 * nivel - 95)
        grupo = fragil + tanque + 2 * crescente
    return r(grupo * 0.15), r(grupo * 0.20), r(grupo * 0.25)


def ca(nivel):
    if nivel < 1:
        return max(10, r(11 + 0.4 * (nivel + 4)))
    return r(13 + 0.6 * (nivel - 1))


def cd(nivel):
    if nivel <= -4:
        return 10
    if nivel <= 0:
        return 11
    return r(11 + nivel / 2)


def consulta(nivel):
    dados, media = pv(nivel)
    sab, custo, mana_conj, mana_max = mana(nivel)
    facil, moderado, dificil = dano(nivel)
    c = ca(nivel)
    print(f"\n=== Monstro de Nível {nivel} ===")
    print(f"PV médio:     {media}   ({dados})")
    print(f"Dano/rodada:  {moderado}   (Fácil {facil} | Difícil {dificil})")
    print(f"Mana:         {mana_conj}   (Sab {sab}; com mod +5: {mana_max}; "
          f"Magia até custo {custo})")
    print(f"CA:           {c}   (bônus de ataque +{c - 8})")
    print(f"CD:           {cd(nivel)}")
    if nivel > 20:
        print("(Nível acima de 20: extrapolação, use para chefes lendários.)")


def main():
    print("Monstros do Nirvana RPG - digite o nível (-8 a 30). Enter para sair.")
    while True:
        texto = input("\nNível: ").strip().lower()
        if texto in ("", "q", "sair"):
            break
        try:
            nivel = int(texto)
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if not -8 <= nivel <= 30:
            print("O nível precisa estar entre -8 e 30.")
            continue
        consulta(nivel)


if __name__ == "__main__":
    main()
