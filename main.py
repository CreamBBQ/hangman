def read():
    palabras = []
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            palabras.append(palabra)

def run(): 
    pass
    
if __name__ == "__main__":
    run()