"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secret = 'pedro'
palavra = 0
tentativa = 0

for i in range(1000):
    letra =input('Digite uma letra ')
    if len(letra) >= 2:
        print("Digite apenas uma letra!")
        continue
        
    if letra in palavra_secret:
        print(letra)
        palavra+=1
    else:
        print('*')
    if palavra == 5:
        print ("Voce descobriu todas as letras da Palavra!") 
        break
    tentativa+=1
    print("Números de tentativas: " f'{tentativa}')
    

for i in range (100):
    correta = input("Qual eh a palavra correta? ")
    if correta == "pedro":
         print("Resposta correta!")
         break
    else:
        print("Resposta incorreta!")
        
    
        

