edad = int(input("ingrese la edad del asisitente: "))
tiene_identificacion = True

# Nivel 1: if/ else basico
if edad >= 18:
    print("Acesso permitido al area general.")
else:
    print("Acesso denegado. es menor de edad.")    

# Nivel 2 Agregado elif y operadores logicos (and) 
if edad >= 18 and tiene_identificacion:
    print("Acceso completo autorizado.")
elif edad >= 18 and not tiene_identificacion:
    print(" Ve a la taquilla para verificar tu identidad.")
elif  edad >= 13:
    print("Acceso permitido solo a la zona familiar.")
else:
    print("Acceso denegado.")

    




