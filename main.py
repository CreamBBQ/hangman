def read():
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        palabras = [word for word in f]

def run(): 
    pass
    
if __name__ == "__main__":
    run()