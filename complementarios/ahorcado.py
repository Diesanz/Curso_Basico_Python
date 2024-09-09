import random

words = ["melocoton","patata","local","manzana"]
stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
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

def get_word():
    if len(words) > 1:
        random_word = random.choice(words) 
        words.remove(random_word)
        return random_word
    else:
        return None

def append_general_words(game_letter, word, list):

    for i, w in enumerate(word):
        if w == game_letter:
            list[i] = game_letter

    return list

def play_game(word):
    good_words = list()
    bad_words = list()
    general_words = ['_' for _ in word]
    tries = 6
    print(' '.join(general_words))
    print(stages[tries])
    while tries > 0:
        game_letter = input("Dime una letra: ").lower()
        
        if game_letter not in word:
            if game_letter in bad_words:
                print("Ya dijistes esta letra")
            else:
                bad_words.append(game_letter)
                tries -= 1
                print("No se encuentra en la palabra")
                if tries == 0:
                    print("Se han acabado las oportudidades, ", word," era la palabra buscada")
        else:
            if game_letter in good_words:
                print("Ya dijistes esta letra")
            else:
                good_words.append(game_letter)
                general_words = append_general_words(game_letter, word, general_words)

                print("Letra correcta")

        print(' '.join(general_words))
        print(stages[tries])
        if "_" not in general_words:
            print("Has ganado, felicidades")
            break
        

            

def main():
    while True:
        word = get_word()
        play_game(word)
        print("a")
        new_game = input('¿Quieres volver a jugar? [S/N]: ')
        if new_game.upper() == "N":
            print("Gracias por jugar :)")
            break

if __name__ == "__main__":
    main()
