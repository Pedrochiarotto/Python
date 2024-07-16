


lista = []
continuar = True 
while(continuar == True):
    r = str(input("Selecione uma opção: \n [i]-Inserir [a]-Apagar [l]-Listar [f]-Finalizar"))
    if r == 'i': 
        valor = input("Valor: ")
        lista.append(valor)
    elif r == 'a':
        valor = input("Qual valor deseja apagar?") 
        if valor in lista:
            lista.remove(valor)
        else:
            print("Insira um valor valido")
    elif r == 'l':
        if range(len(lista)) != 0:
            print(lista)
        else: 
            print("Lista vazia")
    elif r == 'f':
        continuar == False
    

    