#funcion con argumentos

def saludar_persona(nombre):
    print(f"hola {nombre}")
    
#llamamos la funcion 
saludar_persona("carlos")
saludar_persona("mathias")

#otro ejemplo-------------------------
#utilizamos return
def suma (a,b):
    resultado=a+b
    return resultado

print (suma(5,8))


#otro ejemplo
def despedida (nombre="amigo"):
    print(f"adios {nombre}")

despedida()

