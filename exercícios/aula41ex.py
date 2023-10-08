frase = 'O Python e uma linguagem de programacao'\
        'multiparadigma.'\

i = 0
apareceu_mais_vezes = ""
qnt_apareceu_mais_vezes = 0
while i < len(frase):
        letra_atual = frase[i]
        letraap_atual = frase.count(letra_atual)

        if letra_atual== " ":
                i+=1
                continue

        if qnt_apareceu_mais_vezes < letraap_atual:
                qnt_apareceu_mais_vezes = letraap_atual
                apareceu_mais_vezes = letra_atual
        i+=1


print(
        "A letra que apareceu mais vezes foi "f"({apareceu_mais_vezes})" ' que apareceu ' f'{qnt_apareceu_mais_vezes}'
        "x")
        