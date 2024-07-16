


lista = [] 
while(True):
    r = str(input("Selecione uma opção: \n [i]-Inserir [a]-Apagar [l]-Listar\n"))
    if r == 'i': 
        valor = input("Valor: ")
        lista.append(valor)
    elif r == 'l':
        if len(lista) == 0:
            print("Lista vazia")
        else: 
            for indice, valor in enumerate(lista):
                print(indice,valor)
    elif r == 'a':
        indice_str = input("Qual Item da lista deseja apagar?") 
        try: 
            indice = int(indice_str)
            del lista[indice]
        except ValueError:#O que ira printar na tela caso o valor digitado nao seja um numero inteiro 
            print("Digite um número inteiro")
        except IndexError: #O que ira printar na tela caso o número digitado nao esteja na lista
            print("Indice nao existe na lista")
    else:
        print("Escolha alguma das opções (i, a ou l)")
    

    