import random
import os


def normalize(string):
    repl = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for x, y in repl:
        string = string.replace(x, y)
    return string


def read():
    words = []
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word.strip())
    return words 


def game():
    words = read()
    mainWord = words[random.randint(0, len(words))]
    mainWord = normalize(mainWord) #No lo pongo en read() porque pretendo hacer un nivel solo con tildes.
    lettersMW = [i for i in mainWord]
    hiddenLetters = ["_ " for i in mainWord]
    print(*hiddenLetters)
    vidas = 5

    while vidas > 0:
        win = False
        cont = 0
        userLetter = input("Ingrese una letra: ")
        os.system("clear")
        userLetter = userLetter.lower()
        for i in lettersMW:
            if i == userLetter:
                hiddenLetters[cont] = i
                win = True
            cont = cont + 1
        if win == False: 
                vidas = vidas - 1
                print("Fallaste. vidas restantes: " + str(vidas) + "\n")
        print(*hiddenLetters)
        if hiddenLetters == lettersMW: 
            print("\nFelicidades! Ganaste")
            break
        if vidas == 0:
            print("\nPerdiste, vuelve a intentarlo. La palabra correcta era: " + mainWord)
        

def run(): 
    game()


if __name__ == "__main__":
    run()