


lista = [] 
while(True):
    r = str(input("Selecione uma opção: \n [i]-Inserir [a]-Apagar [l]-Listar"))
    if r == 'i': 
        valor = input("Valor: ")
        lista.append(valor)
    elif r == 'a':
        valor = input("Qual valor deseja apagar?") 
        if valor in lista:
            lista.remove(valor)
        else:
            print("Insira um valor existente")
    elif r == 'l':
        if len(lista) == 0:
            print("Lista vazia")
        else: 
            print(lista)
    else:
        print("Escolha alguma das opções (i, a ou l)")
    

    