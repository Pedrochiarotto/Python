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

palavra_secret = 'cinema'
palavra = 0
tentativa = 0
letracorreta = ''
letra_ja_foi = ''

for i in range(1000):
    letra =input('Digite uma letra ')
    if len(letra) > 2:
        print("Digite apenas uma letra!")
        continue
        
    if letra in palavra_secret:
        palavra+=1
        letracorreta = letracorreta + letra

    for letra in palavra_secret:
        if letra in letracorreta:
            print(letra)
        else:
            print('*')
            letra_ja_foi += letra
    print(f'Letras que ja foram: {letra_ja_foi}')
            

    if palavra == len(palavra_secret):
        print ("Voce descobriu todas as letras da Palavra!") 
        break
    tentativa+=1
    print("Números de tentativas: " f'{tentativa}')
    

for i in range (100):
    correta = input("Qual eh a palavra correta? ")
    if correta == palavra_secret:
         print("Resposta correta!")
         break
    else:
        print("Resposta incorreta!")
        
    
    

