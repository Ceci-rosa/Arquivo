with open("frases.txt", "r") as f:
     linhas = f.readlines()
     
with open("contagem.txt", "w") as f_contagem:
    for linha in linhas:
        palavras = linha.split()  
        f_contagem.write(f"{len(palavras)} palavras\n")  
        print(f"{len(palavras)} palavras")  