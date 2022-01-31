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
    print(mainWord)
    lettersMW = [i for i in mainWord]
    hiddenLetters = ["_ " for i in mainWord]
    print(*hiddenLetters)
    vidas = 5

    while vidas > 0:
        win = False
        cont = 0
        userLetter = input("Ingrese una letra: ")
        userLetter = userLetter.lower()
        for i in lettersMW:
            if i == userLetter:
                hiddenLetters[cont] = i
                win = True
            cont = cont + 1
        if win == False: 
                vidas = vidas - 1
        print(*hiddenLetters)
        if hiddenLetters == lettersMW: 
            print("Felicidades! Ganaste")
            break
        if vidas == 0:
            print("Perdiste. Vuelve a intentarlo")
        

def run(): 
    game()
    

if __name__ == "__main__":
    run()