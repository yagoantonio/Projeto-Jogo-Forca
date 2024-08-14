# Projeto jogo Forca
# Curso Python DSA
# Yago Antonio Maciel
#

#Imports
import random
from os import system, name

def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def display(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():
    limpa_tela()

    print('\n----- Jogo da Forca -----')
    print('Advinhe a Palavra abaixo:')

    ## Definição de lista de palavras possíveis
    lista_palavaras = [
        "abelha", "abacaxi", "abismo", "abrigo", "acorde", "adivinha", "afeto", "água", "alegria", "alface",
        "almofada", "amendoim", "amor", "aniversário", "antílope", "apito", "árvore", "asfalto", "azul", "bailarina",
        "banana", "bandeira", "barco", "batata", "beija-flor", "biblioteca", "biscoito", "bola", "borboleta", "brincadeira",
        "cachorro", "caderno", "caixa", "calendário", "camiseta", "caneta", "canguru", "canto", "capa", "carro",
        "castelo", "celular", "chave", "chuva", "coração", "coruja", "criança", "diamante", "dinossauro", "doce",
        "elefante", "energia", "enigma", "escada", "escola", "estrela", "fada", "família", "fantasia", "foguete",
        "futebol", "gato", "girassol", "globo", "guitarra", "herói", "história", "hortelã", "igreja", "imã",
        "inseto", "internet", "jardim", "janela", "jornal", "lagarto", "lâmpada", "leão", "livro", "lua",
        "macaco", "mamão", "mar", "medalha", "melancia", "mesa", "moeda", "montanha", "navio", "nuvem",
        "oceano", "olho", "ônibus", "ovo", "pássaro", "pérola", "piano", "pinguim", "pirulito", "planeta"
    ]

    #Escolher uma palavra aleatória da lista
    palavra_aleatoria = random.choice(lista_palavaras)

    #Criar uma lista vazia para armazenar as letras adivinhadas e erradas
    letras_certas = ['_' for letra in palavra_aleatoria]
    letras_erradas = []

    #Definir o número máximo de tentativas permitidas
    tentativas = 6

    #Enquanto o número de tentativas não atingir o limite máximo
    while tentativas > 0:
        # Mostrar a palavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos
        print(display(tentativas))
        print(" ".join(letras_certas))
        print('\nTentativas Restantes:', tentativas)
        print('Letras erradas:', ''.join(letras_erradas))

        # Pedir ao jogador que adivinhe uma letra
        letra = input("\nDigite uma Letra: ").lower()

        # Verificar se a letra adivinhada está na palavra
        # Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
        # Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]"
        if letra in palavra_aleatoria:
            index = 0
            for l in palavra_aleatoria:
                if letra == l:
                    letras_certas[index] = letra
                index += 1
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print('Letra incorreta. Tentativas restantes: ', tentativas,'\n')

        # Verificar se todas as letras da palavra foram adivinhadas
        # Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"
        if "_" not in letras_certas:
            print("\nVocê venceu, a palavra era:", palavra_aleatoria)
            break

    # Se o número de tentativas restantes chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.
    if "_" in letras_certas:
        print("\nVocê perdeu, a palavra era:", palavra_aleatoria)


if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")