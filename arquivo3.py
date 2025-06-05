while True:
    print("\n1. Cadastrar produto")
    print("2. Listar produtos") 
    print("3. Buscar produto pelo nome") 
    print("4. Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        preco = input("Preço: ")
        with open("produtos.txt", "a") as f:
            f.write(nome + ";" + preco + "\n") 
            
    elif op == "2":
           for linha in open("produtos.txt", "r"): 
            print(linha.strip()) 
            
    elif op == "3": 
        nome = input("Nome para buscar: ") 
        for linha in open("produtos.txt", "r"):
             if nome.lower() in linha.lower():
                 print(linha.strip()) 
                

    elif op == "4":
         break
    
    else:
        print("Opção inválida.")