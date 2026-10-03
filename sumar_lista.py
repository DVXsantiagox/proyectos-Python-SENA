#Bucles for para sumar una lista 

def sumar_lista(numeros):
    total = 0
    for num in numeros:
        total += num 
        total = total + num
        return total 
    
    
#------------------------------------+
#llamamos la funcion
notas = [10, 25, 5, 40] #Esto es una lista
sumar_lista(notas)
   
print