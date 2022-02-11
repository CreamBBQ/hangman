import random
from termcolor import colored
import os

title = """██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    """

five = """         ========================================
         ||                               ||
         ||                               ||
         ||                             (ಥ﹏ಥ)                 
         ||                               /|\              
         ||                              / | \\
         ||                                |
         ||                               / \\
         ||      (ง ͠° ͟ل͜ ͡°)ง          /   \\
         ||           |                                               
         ||          / \\                   
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
                     ༼ ºل͟º ༽ ºل͟º ༽ \n"""

four = """         ========================================
         ||                               ||
         ||                               ||
         ||                             (ಥ﹏ಥ)                 
         ||                               /|\              
         ||                              / | \\
         ||                                |
         ||                               / 
         ||      (ง ͠° ͟ل͜ ͡°)ง          /   
         ||           |                                               
         ||          / \\                   
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
               ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽ \n"""

three = """         ========================================
         ||                               ||
         ||                               ||
         ||                             (ಥ﹏ಥ)                 
         ||                               /|\              
         ||                              / | \\
         ||                                |
         ||                                
         ||      (ง ͠° ͟ل͜ ͡°)ง             
         ||           |                                               
         ||          / \\                   
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
         ºل͟º ༽༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽ºل͟º ༽\n"""

two = """         ========================================
         ||                               ||
         ||                               ||
         ||                             (ಥ﹏ಥ)                 
         ||                               /|            
         ||                              / | 
         ||                                |
         ||                                
         ||      (ง ͠° ͟ل͜ ͡°)ง             
         ||           |                                               
         ||          / \\                   
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
         ºل͟º ༽༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽ºل͟º ༽
              ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)\n"""

one = """         ========================================
         ||                               ||
         ||                               ||
         ||                             (ಥ﹏ಥ)                 
         ||                                |            
         ||                                | 
         ||                                |
         ||                                
         ||      (ง ͠° ͟ل͜ ͡°)ง             
         ||           |                                               
         ||          / \\                   
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
         ºل͟º ༽༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽ºل͟º ༽
         ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) (▀̿Ĺ̯▀̿ ̿) \n"""

zero = """         ========================================
         ||                               ||
         ||                               ||
         ||                                              
         ||                                            
         ||                                 
         ||                                
         ||                                
         ||       ヽ༼ຈل͜ຈ༽ﾉ           
         ||           |                                               
         ||          / \\                (ಥ﹏ಥ)                
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
         \n"""

win = """         ========================================
         ||                               ||
         ||                               ||
         ||                                              
         ||                                            
         ||                 (ﾉ◕ヮ◕)ﾉ            
         ||                   /|\\    
         ||                  / | \\             
         ||                    |
         ||                   / \\                                   
         ||                  /   \\   
         ========================================          
         ||                                    || 
         ||                                    || 
         ||                                    ||
         \n"""


def art(vidas):
    if vidas == 10:
        print(win)
    elif vidas ==5:
        print(five)
    elif vidas == 4:
        print(four)
    elif vidas == 3:
        print(three)
    elif vidas == 2:
        print(two)
    elif vidas == 1:
        print(one)
    else: 
        print(zero)


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
    return string.upper()


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
    print(title)
    
    while attempts > 0:
        win = False
        art(attempts)
        print(*hiddenLetters)
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
        if hiddenLetters == lettersMW: 
            art(10)
            print("\nFelicidades! Ganaste")
            break
        if attempts == 0: 
            art(zero)
            print("\nPerdiste, vuelve a intentarlo. La palabra correcta era: " + mainWord)


if __name__ == "__main__":
    run()