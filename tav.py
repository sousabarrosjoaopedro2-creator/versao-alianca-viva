#!/usr/bin/env python3

from pathlib import Path
import re
import sys


# ============================================================
# TRADUÇÃO ALIANÇA VIVA
# Leitor de textos bíblicos em USFM
# ============================================================

NOME_TRADUCAO = "Tradução Aliança Viva"
SIGLA = "TAV"

DIRETORIO_TEXTOS = Path("textos")


# Código do livro -> nome do livro
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


def limpar_usfm(texto):
    """Remove marcadores USFM e normaliza espaços."""

    # Remove marcadores como \add, \wj, \f etc.
    texto = re.sub(r"\\[a-zA-Z0-9]+\*?", "", texto)

    # Remove caracteres de notas restantes
    texto = re.sub(r"\|.*?\|", "", texto)

    # Normaliza espaços
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()


def localizar_arquivo(codigo, capitulo):
    """Localiza o arquivo USFM correspondente ao capítulo."""

    pasta = DIRETORIO_TEXTOS / codigo

    possibilidades = [
        pasta / f"{capitulo:02d}.usfm",
        pasta / f"{capitulo}.usfm",
    ]

    for arquivo in possibilidades:
        if arquivo.exists():
            return arquivo

    return None


def carregar_capitulo(codigo, capitulo):
    """Lê todos os versículos de um capítulo USFM."""

    arquivo = localizar_arquivo(codigo, capitulo)

    if arquivo is None:
        return None

    versiculos = {}
    versiculo_atual = None
    texto_atual = []

    with arquivo.open("r", encoding="utf-8") as f:

        for linha in f:
            linha = linha.rstrip()

            # Novo versículo
            correspondencia = re.match(
                r"^\s*\\v\s+(\d+)\s*(.*)$",
                linha
            )

            if correspondencia:

                if versiculo_atual is not None:
                    versiculos[versiculo_atual] = limpar_usfm(
                        " ".join(texto_atual)
                    )

                versiculo_atual = int(correspondencia.group(1))
                texto_atual = [correspondencia.group(2)]

            else:

                if versiculo_atual is not None:
                    texto_atual.append(linha)

    # Salva o último versículo
    if versiculo_atual is not None:
        versiculos[versiculo_atual] = limpar_usfm(
            " ".join(texto_atual)
        )

    return versiculos


def exibir_cabecalho(livro, capitulo):
    """Exibe o cabeçalho da passagem."""

    print()
    print(NOME_TRADUCAO.upper())
    print(f"{livro} {capitulo}")
    print("=" * 50)
    print()


def exibir_capitulo(codigo, capitulo):
    """Exibe um capítulo completo."""

    if codigo not in LIVROS:
        print(f"Livro não encontrado: {codigo}")
        return

    livro = LIVROS[codigo]
    versiculos = carregar_capitulo(codigo, capitulo)

    if versiculos is None:
        print(f"Texto não encontrado: {livro} {capitulo}")
        return

    exibir_cabecalho(livro, capitulo)

    for numero, texto in versiculos.items():
        print(f"{numero}  {texto}")


def exibir_versiculo(codigo, capitulo, versiculo):
    """Exibe um único versículo."""

    if codigo not in LIVROS:
        print(f"Livro não encontrado: {codigo}")
        return

    livro = LIVROS[codigo]
    versiculos = carregar_capitulo(codigo, capitulo)

    if versiculos is None:
        print(f"Texto não encontrado: {livro} {capitulo}")
        return

    if versiculo not in versiculos:
        print(
            f"Versículo não encontrado: "
            f"{livro} {capitulo}:{versiculo}"
        )
        return

    exibir_cabecalho(livro, capitulo)

    print(f"{versiculo}  {versiculos[versiculo]}")


def listar_livros():
    """Lista os livros disponíveis."""

    print()
    print(NOME_TRADUCAO.upper())
    print("=" * 50)
    print()

    for codigo, nome in LIVROS.items():
        print(f"{codigo:<6} {nome}")


def mostrar_ajuda():
    """Exibe as instruções de uso."""

    print(f"""
{NOME_TRADUCAO} ({SIGLA})

Leitor bíblico baseado em arquivos USFM.

Uso:

    python tav.py <livro> <capítulo>

Exemplo:

    python tav.py mt 7

Para exibir um versículo específico:

    python tav.py 2tm 3 16

Para listar os livros:

    python tav.py livros
""")


def main():

    if len(sys.argv) < 2:
        mostrar_ajuda()
        return

    comando = sys.argv[1].lower()

    # Lista de livros
    if comando == "livros":
        listar_livros()
        return

    # Leitura de capítulo
    if len(sys.argv) < 3:
        mostrar_ajuda()
        return

    codigo = comando

    try:
        capitulo = int(sys.argv[2])
    except ValueError:
        print("O capítulo deve ser um número.")
        return

    # Versículo específico
    if len(sys.argv) >= 4:

        try:
            versiculo = int(sys.argv[3])
        except ValueError:
            print("O versículo deve ser um número.")
            return

        exibir_versiculo(
            codigo,
            capitulo,
            versiculo
        )

    else:

        exibir_capitulo(
            codigo,
            capitulo
        )


if __name__ == "__main__":
    main()