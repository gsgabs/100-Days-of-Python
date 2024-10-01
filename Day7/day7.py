# hangman!

import random

lista_de_palavras = [
    # Astronomia e Espaço
    "planeta", "galaxia", "meteoro", "satellite", "nebulosa",
    "astronauta", "cometa", "orbita", "eclipse", "gravidade",

    # Pedras e Joias
    "diamante", "esmeralda", "safira", "rubi", "ametista", "topazio",
    "quartzo", "jade", "turquesa",

    # Fazenda
    "cevada", "milho", "foice",
    "colheita", "celeiro", "espantalho", "ovelha", "arado", "trigo",

    # Mar
    "oceano", "coral", "golfinho", "onda",
    "marisco", "peixe", "mar",

    # random
    "poder", "biblioteca", "relampago", "girassol", "montanha",
    "pirata", "camuflagem", "engenheiro", "lareira",
    "maratona", "esfinge",

    # Padaria e Doces
    "bolo", "biscoito", "brigadeiro", "sonho", "pudim",

    # Personalidades e Sentimentos
    "alegria", "tristeza", "odio", "amor", "coragem", "celebridade",

    # Medieval e Mitologia
    "cavaleiro", "cavalheiro", "castelo", "magia", "espada", "heroi", "deus", "olimpo",

    # Lendas e Musica
    "excalibur", "piano", "sinfonia", "partitura"
]

list_of_words = [
    # Astronomy and Space
    "planet", "galaxy", "meteor", "satellite", "nebula",
    "astronaut", "comet", "orbit", "eclipse", "gravity",

    # Stones and Jewelry
    "diamond", "emerald", "sapphire", "ruby", "amethyst", "topaz",
    "quartz", "jade", "turquoise",

    # Farm
    "corn", "scyther", "barn", "scarecrow", "sheep", "pilow", "wheat",

    # Sea
    "ocean", "coral", "dolphin", "wave",
    "shellfish", "fish", "sea",

    # random
    "power", "library", "lightning", "sunflower", "mountain", "chemistry",
    "pirate", "camouflage", "engineer", "fireplace",
    "marathon", "sphinx",

    # Bakery and Sweets
    "cake", "cookie", "dream", "pudding",

    # Personalities and Feelings
    "joy", "sadness", "love", "courage", "celebrity",

    # Medieval and Mythology
    "knight", "gentleman", "castle", "magic", "sword", "hero", "god", "olympus",

    # Legends and Music
    "excalibur", "piano", "symphony", "score"
]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def generate_random_word(word_collection):
    return word_collection[random.randint(0, (len(word_collection)-1))]


def generate_blank_word(word):
    new_word = '_' * len(word)
    new_list = ['_'] * len(word)
    return new_word, new_list


def new_guess(guess_letter):
    for each_guess in list_of_guesses:
        if each_guess.lower() == guess_letter:
            return False
    if len(guess_letter) > 1:
        return False
    return True


language = ''
while language != 'en' and language != 'pt':
    language = input("Type 'en' to play english or 'pt' to play portuguese: ").lower()

# english game
if language == "en":
    print("\nWelcome to Hangman game!")
    en_word = generate_random_word(list_of_words)
    blank_word, blank_word_list = generate_blank_word(en_word)
    life = 6
    game_over = False
    list_of_guesses = []

    # game loop
    while life > 0 and not game_over:
        # start
        print(stages[life])
        print(blank_word)

        # user makes a guess
        guess = input("Try to guess a letter: ").lower()
        while not new_guess(guess):
            guess = input("Try to guess a letter: ").lower()
        list_of_guesses.append(guess.upper())

        # checking user guesses
        guess_wrong = True
        for index, letter in enumerate(en_word):
            if guess == letter:
                blank_word_list[index] = letter
                guess_wrong = False

        # wrong guess
        if guess_wrong:
            print(f"The letter {guess.upper()}, isn't in the word.")
            print(f"\nYour previous guesses: {list_of_guesses}")
            life -= 1
            if life == 0:
                print(f"\n\nYou lose! What a shame, the word was {en_word.upper()}")
                print("But don't feel bad, you can try again.")

        # right guess
        elif not guess_wrong:
            print(f"Well done, {guess.upper()} is in the word.")
            print(f"\nYour previous guesses: {list_of_guesses}")
            if life < 6:
                life += 1  # bonus life cause game hard
            blank_word = ''.join(blank_word_list)
            if blank_word == en_word:
                print(f"\n\nCongratulations! You won the game, the word was {en_word.upper()}")
                game_over = True

elif language == 'pt':
    print("\nBem vindo ao jogo da forca!")
    pt_word = generate_random_word(lista_de_palavras)
    blank_word, blank_word_list = generate_blank_word(pt_word)
    life = 6
    game_over = False
    list_of_guesses = []

    # game loop
    while life > 0 and not game_over:
        # start
        print(stages[life])
        print(blank_word)

        # user makes a guess
        guess = input("Tente acertar uma letra: ").lower()
        while not new_guess(guess):
            guess = input("Tente acertar uma letra: ").lower()
        list_of_guesses.append(guess.upper())

        # checking user guesses
        guess_wrong = True
        for index, letter in enumerate(pt_word):
            if guess == letter:
                blank_word_list[index] = letter
                guess_wrong = False

        # wrong guess
        if guess_wrong:
            print(f"A letra {guess.upper()} não pertence à palavra.")
            print(f"\nSuas tentativas anteriores: {list_of_guesses}")
            life -= 1
            if life == 0:
                print(f"\n\nVocê perdeu! A palavra era {pt_word.upper()}")
                print("Mas não fica triste, você pode tantar de novo.")

        # right guess
        elif not guess_wrong:
            print(f"Muito bem, {guess.upper()} é uma letra correta.")
            print(f"\nSuas tentativas anteriores {list_of_guesses}")
            if life < 6:
                life += 1  # bonus life cause game hard
            blank_word = ''.join(blank_word_list)
            if blank_word == pt_word:
                print(f"\n\nParabéns você venceu! A palavra era {pt_word.upper()}")
                game_over = True
