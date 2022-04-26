"""Programa para calcular si un numero es par o impar"""


print("-------------------------------")
print("-----NUMERO PAR O IMPAR--------")
print("-------------------------------")

# input 
x=int(input("Digite el valor de el nuemro: "))
r=x % 2 


# processing
if r == 0: 
    msj= "es par"
else:
    msj= "es impar"
# output 
print( "El numero " + msj)
