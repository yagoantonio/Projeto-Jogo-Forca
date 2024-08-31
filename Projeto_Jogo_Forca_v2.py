# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system, name

def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>> Forca <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

>>>>>>>>>> Forca <<<<<<<<<<
+---+
|   |
O   |
    |
    |
    |
=========''', '''

>>>>>>>>>> Forca <<<<<<<<<<
+---+
|   |
O   |
|   |
    |
    |
=========''', '''

>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

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

# Classe
class Forca:

# Metodo Construtor
    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_certas = []
        self.letras_erradas = []

#Metodo para adivinhar a letra
    def checar_letra(self,letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            pass
# Metodo para verificar se o jogo terminou
    def gameOver(self):
        return self.gameWon() or (len(self.letras_erradas)==6)

# Metodo para verificar se o jogador venceu
    def gameWon(self):
        if "_" not in self.esconde_palavra():
            return True
        else:
            return False

# Metodo para não mostrar a letra no board
    def esconde_palavra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                rtn += '_'
            else:
                rtn += letra

        return rtn

# Metodo para checar o status do game e imprimir o board na tela
    def printStatusGame(self):
        print(board[len(self.letras_erradas)])
        print(self.esconde_palavra())
        #print('\nTentativas Restantes:', 6-len(self.letras_erradas))
        print('\nLetras erradas:', ' - '.join(self.letras_erradas))

if __name__ == "__main__":
    limpa_tela()

    game = Forca(random.choice(lista_palavaras))

    # Enquanto o número de tentativas não atingir o limite máximo
    while not game.gameOver():
        #Status do game
        game.printStatusGame()

        # Pedir ao jogador que adivinhe uma letra
        letra = input("\nDigite uma Letra: ").lower()

        #Verifica se a letra está na palavra
        game.checar_letra(letra)

    game.printStatusGame()

    if game.gameWon():
        print('Parabéns, você venceu a palavra era: ', game.palavra)
    else:
        print("\nVocê perdeu, a palavra era:", game.palavra)

    print("\nFim de Jogo!\n")