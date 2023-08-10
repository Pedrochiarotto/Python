#Formatação de strings com método format

a = 'A'
b = 'B'
c = 1.1
formato = 'a= {nome1} b= {nome2} c= {nome3:.2f} {nome1}' .format(nome1= a, nome2=b, nome3=c)

print(formato)