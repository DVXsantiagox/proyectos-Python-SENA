#programa de datos 
#Deleloper: osaa 
#date: 21-08-26

print()
print("="*50)
print("---Promocion social---")
print("="*50)

nombre = input("cual es tu nombre:?")
nota = int (input("\n cual es tu nota:?"))

if nota >= 100:
    print(" la nota ",nota," es invalida")
elif nota >= 90:
    print("Exelente nivel")
elif nota >= 70:
    print("Aprobado, buen desempeño")    
else:
    print("Debes repasar los conceptos, tu puedes")
