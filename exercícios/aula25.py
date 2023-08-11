"""
Fatiamento de strings e a função lan
 012345678 <-Indices
 Olá mundo
-987654321 <- Indices
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = "Olá Mundo"
print(variavel[4:7]) # pedir um a mais do que está pedindo, pois nesse caso, colocando no Indice "7", ele para no indice "6"
print(variavel[4:]) #Omitir para ir até o final
print(variavel[0:4])
print(variavel[:6])# é possivel omitir o inicio também, que ele começara do começo.
print(len(variavel)) #Função "len" para contar caracteres 

print(variavel[0:9:2]) #[i:f:p]  -> agora utilizaremos o p(passo) para indicar de quanto em quanto iremos contar. No exemplo acima, pularemos de 2 em 2 caracteres
print(variavel[::-1]) #irá inverter a string