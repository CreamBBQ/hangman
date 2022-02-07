import random
from termcolor import colored
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
        string = string.replace(x, y).upper()
    return string


def getWord():
    words = []
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for word in f:
            word = normalize(word)
            words.append(word.strip())
    mainWord = words[random.randint(0, len(words))]
    return mainWord


def clear(): 
    os.system("clear")


def run():
    mainWord = getWord()
    lettersMW = [i for i in mainWord]
    hiddenLetters = ["_ " for i in mainWord]
    wrongLetters = set()
    attempts = 5
    print(*hiddenLetters)
    
    while attempts > 0:
        win = False
        userLetter = input("Ingrese una letra: ")
        clear()
        userLetter = userLetter.upper()
        for count, i in enumerate(lettersMW):
            if i == userLetter:
                hiddenLetters[count] = i
                win = True
        if win == False: 
                attempts = attempts - 1
                wrongLetters.add("❌" + userLetter)
                print(colored("Fallaste", "red") + ". Vidas restantes: " + str(attempts) + "\n" + " ".join(wrongLetters) + "\n")
        else: 
            print(colored("Acertaste", "green") + ". Te quedan " + str(attempts) + " Vidas" + "\n" + " ".join(wrongLetters) + "\n")
        print(*hiddenLetters)
        if hiddenLetters == lettersMW: 
            print("\nFelicidades! Ganaste")
            break
    print("\nPerdiste, vuelve a intentarlo. La palabra correcta era: " + mainWord)


if __name__ == "__main__":
    run()