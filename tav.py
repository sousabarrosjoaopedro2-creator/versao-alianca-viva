#!/usr/bin/env python3

from pathlib import Path
import re
import sys


# Diretório onde estão os arquivos USFM
TEXTOS_DIR = Path("textos")


# Códigos dos livros bíblicos
LIVROS = {
    "mt": "Mateus",
    "mc": "Marcos",
    "lc": "Lucas",
    "jo": "João",
    "atos": "Atos",
    "rm": "Romanos",
    "1co": "1 Coríntios",
    "2co": "2 Coríntios",
    "gl": "Gálatas",
    "ef": "Efésios",
    "fp": "Filipenses",
    "cl": "Colossenses",
    "1ts": "1 Tessalonicenses",
    "2ts": "2 Tessalonicenses",
    "1tm": "1 Timóteo",
    "2tm": "2 Timóteo",
    "tt": "Tito",
    "fm": "Filemom",
    "hb": "Hebreus",
    "tg": "Tiago",
    "1pe": "1 Pedro",
    "2pe": "2 Pedro",
    "1jo": "1 João",
    "2jo": "2 João",
    "3jo": "3 João",
    "jd": "Judas",
    "ap": "Apocalipse",
}


def limpar_texto(texto):
    """Remove marcadores USFM que não devem aparecer na leitura."""
    texto = re.sub(r"\\[a-zA-Z0-9]+\*?", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def carregar_versiculos(codigo, capitulo):
    """Carrega os versículos de um capítulo a partir do arquivo USFM."""
    arquivo = TEXTOS_DIR / codigo / f"{capitulo:02d}.usfm"

    if not arquivo.exists():
        # Também permite arquivos no formato capítulo.usfm
        arquivo = TEXTOS_DIR / codigo / f"{capitulo}.usfm"

    if not arquivo.exists():
        return None

    versiculos = {}
    versiculo_atual = None
    texto_atual = []

    with arquivo.open("r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            if not linha:
                continue

            # Início de um novo versículo
            match = re.match(r"\\v\s+(\d+)\s*(.*)", linha)

            if match:
                if versiculo_atual is not None:
                    versiculos[versiculo_atual] = limpar_texto(
                        " ".join(texto_atual)
                    )

                versiculo_atual = int(match.group(1))
                texto_atual = [match.group(2)]
            else:
                if versiculo_atual is not None:
                    texto_atual.append(linha)

    if versiculo_atual is not None:
        versiculos[versiculo_atual] = limpar_texto(
            " ".join(texto_atual)
        )

    return versiculos


def exibir_capitulo(codigo, capitulo, versiculo=None):
    """Exibe um capítulo inteiro ou um versículo específico."""

    if codigo not in LIVROS:
        print(f"Livro não encontrado: {codigo}")
        return

    nome = LIVROS[codigo]
    versiculos = carregar_versiculos(codigo, capitulo)

    if versiculos is None:
        print(f"Texto não encontrado: {nome} {capitulo}")
        return

    print()
    print("TRADUÇÃO ALIANÇA VIVA")
    print(f"{nome} {capitulo}")
    print("─" * 40)
    print()

    if versiculo is not None:
        if versiculo not in versiculos:
            print(f"Versículo não encontrado: {nome} {capitulo}:{versiculo}")
            return

        print(f"{versiculo}  {versiculos[versiculo]}")
        return

    for numero, texto in versiculos.items():
        print(f"{numero}  {texto}")


def ajuda():
    print("""
TRADUÇÃO ALIANÇA VIVA — LEITOR

Uso:

    python tav.py <livro> <capítulo>
    python tav.py <livro> <capítulo> <versículo>

Exemplos:

    python tav.py mt 7
    python tav.py mt 7 21
    python tav.py jo 3 16

Livros:

    mt   Mateus
    mc   Marcos
    lc   Lucas
    jo   João
    atos Atos
    rm   Romanos
    1co  1 Coríntios
    2co  2 Coríntios
    gl   Gálatas
    ef   Efésios
    fp   Filipenses
    cl   Colossenses
    1ts  1 Tessalonicenses
    2ts  2 Tessalonicenses
    1tm  1 Timóteo
    2tm  2 Timóteo
    tt   Tito
    fm   Filemom
    hb   Hebreus
    tg   Tiago
    1pe  1 Pedro
    2pe  2 Pedro
    1jo  1 João
    2jo  2 João
    3jo  3 João
    jd   Judas
    ap   Apocalipse
""")


def main():
    if len(sys.argv) < 3:
        ajuda()
        return

    codigo = sys.argv[1].lower()

    try:
        capitulo = int(sys.argv[2])
    except ValueError:
        print("O capítulo deve ser um número.")
        return

    versiculo = None

    if len(sys.argv) >= 4:
        try:
            versiculo = int(sys.argv[3])
        except ValueError:
            print("O versículo deve ser um número.")
            return

    exibir_capitulo(codigo, capitulo, versiculo)


if __name__ == "__main__":
    main()