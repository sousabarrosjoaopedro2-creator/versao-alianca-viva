#!/usr/bin/env python3

from pathlib import Path
import re


# ============================================================
# TRADUÇÃO ALIANÇA VIVA
# Validador dos arquivos USFM
# ============================================================

TEXTOS_DIR = Path("textos")

LIVROS = {
    "mt": ("Mateus", 28),
    "mc": ("Marcos", 16),
    "lc": ("Lucas", 24),
    "jo": ("João", 21),
    "atos": ("Atos", 28),
    "rm": ("Romanos", 16),
    "1co": ("1 Coríntios", 16),
    "2co": ("2 Coríntios", 13),
    "gl": ("Gálatas", 6),
    "ef": ("Efésios", 6),
    "fp": ("Filipenses", 4),
    "cl": ("Colossenses", 4),
    "1ts": ("1 Tessalonicenses", 5),
    "2ts": ("2 Tessalonicenses", 3),
    "1tm": ("1 Timóteo", 6),
    "2tm": ("2 Timóteo", 4),
    "tt": ("Tito", 3),
    "fm": ("Filemom", 1),
    "hb": ("Hebreus", 13),
    "tg": ("Tiago", 5),
    "1pe": ("1 Pedro", 5),
    "2pe": ("2 Pedro", 3),
    "1jo": ("1 João", 5),
    "2jo": ("2 João", 1),
    "3jo": ("3 João", 1),
    "jd": ("Judas", 1),
    "ap": ("Apocalipse", 22),
}


def validar_arquivo(arquivo):
    """Valida a estrutura básica de um arquivo USFM."""

    erros = []

    texto = arquivo.read_text(encoding="utf-8")

    if "\\c " not in texto:
        erros.append("Marcador de capítulo \\c não encontrado.")

    if "\\v " not in texto:
        erros.append("Marcador de versículo \\v não encontrado.")

    versiculos = re.findall(r"\\v\s+(\d+)", texto)

    if not versiculos:
        return erros

    numeros = [int(v) for v in versiculos]

    duplicados = {
        numero for numero in numeros
        if numeros.count(numero) > 1
    }

    if duplicados:
        erros.append(
            f"Versículos duplicados: "
            f"{', '.join(map(str, sorted(duplicados)))}"
        )

    return erros


def validar_livro(codigo, nome, total_capitulos):
    """Valida todos os capítulos de um livro."""

    pasta = TEXTOS_DIR / codigo
    erros = []

    print(f"Verificando {nome}...")

    if not pasta.exists():
        erros.append(f"Pasta ausente: {pasta}")
        return erros

    for capitulo in range(1, total_capitulos + 1):

        arquivo = pasta / f"{capitulo:02d}.usfm"

        if not arquivo.exists():
            arquivo = pasta / f"{capitulo}.usfm"

        if not arquivo.exists():
            erros.append(
                f"Capítulo ausente: {nome} {capitulo}"
            )
            continue

        problemas = validar_arquivo(arquivo)

        for problema in problemas:
            erros.append(
                f"{nome} {capitulo}: {problema}"
            )

    return erros


def main():

    print("=" * 60)
    print("VALIDAÇÃO — TRADUÇÃO ALIANÇA VIVA")
    print("=" * 60)
    print()

    erros_totais = []

    for codigo, (nome, capitulos) in LIVROS.items():

        erros = validar_livro(
            codigo,
            nome,
            capitulos
        )

        erros_totais.extend(erros)

    print()
    print("=" * 60)

    if erros_totais:

        print("VALIDAÇÃO CONCLUÍDA COM ERROS")
        print()

        for erro in erros_totais:
            print(f"[ERRO] {erro}")

        print()
        print(
            f"Total de problemas encontrados: "
            f"{len(erros_totais)}"
        )

        return 1

    print("VALIDAÇÃO CONCLUÍDA COM SUCESSO")
    print()
    print("Nenhum problema estrutural básico foi encontrado.")
    print("Os arquivos USFM estão prontos para a próxima etapa.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())