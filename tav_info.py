"""
Tradução Aliança Viva (TAV)
===========================

Informações oficiais da tradução.

Nome: Tradução Aliança Viva
Sigla: TAV
Idioma: Português
Testamento: Antigo e Novo Testamento
Tipo: Tradução bíblica contemporânea

Descrição:
A Tradução Aliança Viva (TAV) é uma tradução contemporânea da Bíblia
em português, desenvolvida para comunicar fielmente o sentido das
Escrituras em linguagem clara, natural e acessível.

Princípios:
- Fidelidade ao sentido das Escrituras
- Linguagem contemporânea e natural
- Clareza e precisão
- Consistência terminológica
- Respeito ao contexto literário e histórico
- Preservação da mensagem teológica

Objetivo:
Comunicar a mensagem das Escrituras com fidelidade, clareza e
naturalidade, tornando o texto bíblico acessível ao leitor
contemporâneo.

Formato:
USFM

Licença:
Creative Commons Zero v1.0 Universal (CC0 1.0)

Projeto:
Tradução Aliança Viva

Copyright:
CC0 1.0 Universal
"""


TRANSLACAO = {
    "nome": "Tradução Aliança Viva",
    "sigla": "TAV",
    "idioma": "Português",
    "tipo": "Tradução bíblica contemporânea",
    "formato": "USFM",
    "licenca": "CC0 1.0 Universal",
    "descricao": (
        "Tradução contemporânea da Bíblia em português, "
        "desenvolvida para comunicar fielmente o sentido das "
        "Escrituras em linguagem clara, natural e acessível."
    ),
    "objetivo": (
        "Comunicar a mensagem das Escrituras com fidelidade, "
        "clareza e naturalidade."
    ),
}


def mostrar_informacoes():
    print("TRADUÇÃO ALIANÇA VIVA")
    print("=" * 30)
    print(f"Nome: {TRANSLACAO['nome']}")
    print(f"Sigla: {TRANSLACAO['sigla']}")
    print(f"Idioma: {TRANSLACAO['idioma']}")
    print(f"Tipo: {TRANSLACAO['tipo']}")
    print(f"Formato: {TRANSLACAO['formato']}")
    print(f"Licença: {TRANSLACAO['licenca']}")
    print()
    print("Descrição:")
    print(TRANSLACAO["descricao"])
    print()
    print("Objetivo:")
    print(TRANSLACAO["objetivo"])


if __name__ == "__main__":
    mostrar_informacoes()