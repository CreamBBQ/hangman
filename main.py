import random

def read():
    words = []
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word.strip())
    return words 

def game():

    words = read()
    mainWord = words[random.randint(0, len(words))]
    lettersMW = [i for i in mainWord]
    hiddenLetters = ["_ " for i in mainWord]
    print(*hiddenLetters)

    for number in range(5): 
        cont = 0
        userLetter = input("Ingrese una letra: ")
        userLetter = userLetter.lower()
        for i in lettersMW:
            if i == userLetter:
                hiddenLetters[cont] = i
            cont = cont + 1
        print(*hiddenLetters)

def run(): 
    game()
    

if __name__ == "__main__":
    run()