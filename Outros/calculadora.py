#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora interativa de custos — Moedas, PHs e Mana.
Base de dados: tabelas integrais dos três arquivos Markdown fornecidos.
Execute com: python calculadora_custos.py
"""
import base64, gzip, json, re

DATA_B64 = "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"
DATA = json.loads(gzip.decompress(base64.b64decode(DATA_B64)).decode("utf-8"))

MODOS = {
    "1": ("moedas", "MOEDAS"),
    "2": ("phs", "PONTOS DE HABILIDADE (PHs)"),
    "3": ("mana", "PONTOS DE MANA (PMs)"),
}
MOEDAS = {"PC": 1, "PP": 10, "PO": 100, "PL": 1000}

def numero(txt):
    """Converte números com vírgula decimal; retorna None se não houver número."""
    if txt is None: return None
    s = str(txt).replace("**", "").replace("`", "").strip()
    m = re.search(r"[-+]?\d+(?:[.,]\d+)?", s)
    if not m: return None
    return float(m.group(0).replace(",", "."))

def moeda_em_pc(txt):
    s = str(txt).upper().replace("**", "")
    if not re.search(r"\d", s): return None
    total = 0.0
    achou = False
    for valor, unidade in re.findall(r"(\d+(?:[.,]\d+)?)\s*(PL|PO|PP|PC)\b", s):
        total += float(valor.replace(",", ".")) * MOEDAS[unidade]
        achou = True
    if achou: return total
    # Preços expressos apenas como número podem ser preços em pt, não moedas.
    return None

def limpar(txt):
    return re.sub(r"[*_`]", "", str(txt)).strip()

def cabecalho_candidato(modo, headers):
    hs = [limpar(h).lower() for h in headers]
    if modo == "moedas":
        # Preço final/preço é preferido; evita selecionar descontos se houver preço.
        exatos = [i for i,h in enumerate(hs) if h == "preço"]
        if exatos: return exatos[-1]
        precos = [i for i,h in enumerate(hs) if "preço" in h or "moedas" in h]
        if precos: return precos[-1]
        return next((i for i,h in enumerate(hs) if "pt" in h), None)
    if modo == "phs":
        xs = [i for i,h in enumerate(hs) if "ph" in h]
        if xs: return xs[-1]
        return next((i for i,h in enumerate(hs) if "pt" in h), None)
    return next((i for i,h in enumerate(hs) if "pontos" in h or "pt" in h), None)

def valor_coluna(modo, table, row, col):
    header = limpar(table["headers"][col]).lower()
    raw = limpar(row[col])
    if modo == "moedas":
        pc = moeda_em_pc(raw)
        if pc is not None:
            return pc, "pc", raw
        n = numero(raw)
        if n is None: return None
        # Coluna de pt convertida usando 1 pt = 19 PC.
        if "pt" in header or "ponto" in header:
            return n * 19, "pc", raw
        return None
    n = numero(raw)
    if n is None: return None
    if modo == "phs":
        if "ph" in header: return n, "ph", raw
        if "pt" in header or "ponto" in header: return n / 57.7, "ph", raw
        # Tabelas 3, 4 e 5 do documento de PHs já expressam PHs por duração/uso.
        if any(tag in table["title"] for tag in ("Tabela 3", "Tabela 4", "Tabela 5")) and col > 0:
            return n, "ph", raw
        return None
    # No documento de Mana, 1 PM = 3,125 pt. Nas tabelas de duração,
    # as colunas já são pontos totais, embora o cabeçalho seja a duração.
    if "pt" in header or "ponto" in header: return n / 3.125, "pm", raw
    if any(tag in table["title"] for tag in ("5.2 Efeitos de bônus", "5.3 Graus como", "5.4 Debuffs", "6. Como os valores")) and col > 0:
        return n / 3.125, "pm", raw
    return None

def fmt_num(n, casas=2):
    s = f"{n:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_total(modo, total):
    if modo == "moedas":
        pc = round(total + 1e-8)
        pl, resto = divmod(pc, 1000)
        po, resto = divmod(resto, 100)
        pp, pc = divmod(resto, 10)
        partes = []
        if pl: partes.append(f"{pl} PL")
        if po: partes.append(f"{po} PO")
        if pp: partes.append(f"{pp} PP")
        if pc or not partes: partes.append(f"{pc} PC")
        return " e ".join(partes) + f"  (total: {fmt_num(total/100,2)} PO)"
    unidade = "PH" if modo == "phs" else "PM"
    return f"{fmt_num(total, 3)} {unidade}"

def tabela_tem_custo(modo, table):
    titulo = table["title"]
    if modo == "phs" and "Orçamento e unidade" in titulo:
        return False
    if modo == "mana" and "Requisitos de Atributo" in titulo:
        return False
    return any(
        valor_coluna(modo, table, row, col) is not None
        for row in table["rows"]
        for col in range(len(table["headers"]))
    )

def mostrar_tabelas(modo):
    tabelas = [t for t in DATA[modo] if tabela_tem_custo(modo, t)]
    print("\nCategorias/tabelas disponíveis:")
    for i,t in enumerate(tabelas,1):
        qtd = sum(any(valor_coluna(modo,t,row,c) is not None for c in range(len(t["headers"])) ) for row in t["rows"])
        print(f" {i:2}. {t['title']} — {qtd} opções")
    print("  0. Voltar")
    print("  F. Seleção Finalizada")
    while True:
        s=input("\nEscolha uma categoria/tabela: ").strip()
        if s.lower()=="f": return "FINALIZAR"
        if s=="0": return None
        if s.isdigit() and 1<=int(s)<=len(tabelas):
            return tabelas[int(s)-1]
        print("Opção inválida.")

def selecionar_coluna(modo, table, row):
    possiveis=[]
    for i,h in enumerate(table["headers"]):
        v=valor_coluna(modo,table,row,i)
        if v is not None: possiveis.append((i,h,v))
    if not possiveis:
        print("Esta linha não possui um valor de custo conversível neste modo.")
        return None
    preferida=cabecalho_candidato(modo,table["headers"])
    if len(possiveis)==1:
        return possiveis[0]
    print("\nQual coluna representa o valor que deseja cobrar?")
    for j,(idx,h,v) in enumerate(possiveis,1):
        print(f" {j}. {limpar(h)} = {limpar(row[idx])}")
    padrao=next((j for j,x in enumerate(possiveis,1) if x[0]==preferida),1)
    s=input(f"Escolha [Enter = {padrao}]: ").strip()
    if not s: s=str(padrao)
    if not s.isdigit() or not 1<=int(s)<=len(possiveis):
        print("Escolha inválida; item ignorado.")
        return None
    return possiveis[int(s)-1]

def main():
    print("="*64)
    print(" CALCULADORA DE CUSTOS — MOEDAS / PHs / MANA")
    print("="*64)
    for k,(_,nome) in MODOS.items(): print(f" {k}. {nome}")
    escolha=input("\nSelecione o modo: ").strip()
    if escolha not in MODOS:
        print("Modo inválido."); return
    modo,nome=MODOS[escolha]
    selecoes=[]
    total=0.0
    print(f"\nModo selecionado: {nome}")
    print("Você pode adicionar a mesma opção quantas vezes quiser.")
    while True:
        table=mostrar_tabelas(modo)
        if table == "FINALIZAR":
            print("\n"+"="*64+"\nSELEÇÃO FINALIZADA")
            for i,item in enumerate(selecoes,1):
                print(f" {i}. {item['nome']} ×{item['qtd']} — {item['custo']}")
            print(f"\nCUSTO TOTAL: {formatar_total(modo,total)}")
            print("="*64)
            return
        if table is None: break
        print(f"\n{table['title']}")
        rows_validas = [row for row in table["rows"]
                        if any(valor_coluna(modo,table,row,c) is not None
                               for c in range(len(table["headers"])))]
        for i,row in enumerate(rows_validas,1):
            rotulo=limpar(row[0])
            resumo=" | ".join(f"{limpar(h)}: {limpar(v)}" for h,v in zip(table["headers"][1:],row[1:]))
            print(f" {i:3}. {rotulo} — {resumo}")
        print("  0. Voltar às categorias")
        print("  F. Seleção Finalizada")
        while True:
            s=input("\nNúmero da opção (ou F para finalizar): ").strip().lower()
            if s=="f":
                print("\n"+"="*64)
                print("SELEÇÃO FINALIZADA")
                if not selecoes: print("Nenhum efeito/item foi selecionado.")
                else:
                    print("\nItens selecionados:")
                    for i,item in enumerate(selecoes,1):
                        print(f" {i}. {item['nome']} ×{item['qtd']} — {item['valor_original']} ({item['custo']})")
                    print(f"\nCUSTO TOTAL: {formatar_total(modo,total)}")
                print("="*64)
                return
            if s=="0": break
            if not s.isdigit() or not 1<=int(s)<=len(rows_validas):
                print("Opção inválida."); continue
            row=rows_validas[int(s)-1]
            col=selecionar_coluna(modo,table,row)
            if col is None: continue
            idx,header,(custo,unidade,raw)=col
            q=input("Quantidade/repetições [1]: ").strip()
            q=1 if not q else (int(q) if q.isdigit() and int(q)>0 else 0)
            if not q:
                print("Quantidade inválida."); continue
            # Descontos em modo moedas são subtraídos, nunca somados.
            sinal=-1 if modo=="moedas" and ("desconto" in table["title"].lower() or "desconto" in limpar(header).lower()) else 1
            subtotal=custo*q*sinal
            nome_item=f"{table['title']} — {limpar(row[0])} [{limpar(header)}]"
            selecoes.append({"nome":nome_item,"qtd":q,"valor_original":raw,
                             "custo":formatar_total(modo,abs(subtotal)),
                             "valor":subtotal})
            total+=subtotal
            print(f"Adicionado: {q} × {limpar(row[0])}. Parcial: {formatar_total(modo,total)}")
            print("\n1. Adicionar outro item desta tabela")
            print("2. Voltar às categorias")
            print("F. Seleção Finalizada")
            prox=input("Escolha: ").strip().lower()
            if prox=="f":
                print("\n"+"="*64+"\nSELEÇÃO FINALIZADA")
                for i,item in enumerate(selecoes,1):
                    print(f" {i}. {item['nome']} ×{item['qtd']} — {item['custo']}")
                print(f"\nCUSTO TOTAL: {formatar_total(modo,total)}")
                print("="*64)
                return
            if prox=="2": break
            # qualquer outra resposta retorna à lista de opções para adicionar mais
    print("\nSeleção encerrada.")
    print(f"CUSTO TOTAL: {formatar_total(modo,total)}")

if __name__ == "__main__":
    main()
