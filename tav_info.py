# Tradução Aliança Viva (TAV)
# Informações da tradução

TRANSLATION_NAME = "Tradução Aliança Viva"
ABBREVIATION = "TAV"

LANGUAGE = "Português"
TESTAMENT = "Antigo e Novo Testamento"

DESCRIPTION = (
    "A Tradução Aliança Viva (TAV) é uma tradução contemporânea "
    "da Bíblia em português, desenvolvida para comunicar fielmente "
    "o sentido das Escrituras com linguagem clara, natural e acessível."
)

PRINCIPLES = [
    "Fidelidade ao sentido das Escrituras",
    "Linguagem contemporânea e natural",
    "Clareza e precisão",
    "Consistência terminológica",
    "Respeito ao contexto bíblico",
    "Preservação da mensagem teológica",
]

LICENSE = "CC0 1.0 Universal"

FORMAT = "USFM"

PROJECT = "Tradução Aliança Viva"

SLOGAN = "Fidelidade ao texto. Clareza para o leitor. Vida na Palavra."


def mostrar_informacoes():
    print(TRANSLATION_NAME)
    print(f"Sigla: {ABBREVIATION}")
    print(f"Idioma: {LANGUAGE}")
    print(f"Testamentos: {TESTAMENT}")
    print(f"Licença: {LICENSE}")
    print(f"Formato: {FORMAT}")
    print()
    print("Descrição:")
    print(DESCRIPTION)
    print()
    print("Princípios:")
    for principio in PRINCIPLES:
        print(f"- {principio}")
    print()
    print(SLOGAN)


if __name__ == "__main__":
    mostrar_informacoes()