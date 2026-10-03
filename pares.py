#combinamos for e if 

def obtener_pares(lista_numeros):
    pares = [] #lista vacia
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares 

#------------------------------
#
numeros = [1,2,3,4,5,6,7,8,9,10]
print(obtener_pares(numeros))



        
            