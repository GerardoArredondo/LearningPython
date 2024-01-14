weight = float(input("Hola, qué tal?\n\nPor favor introduce tu peso ---> "))
kilosOLibras = str(input("(K)g o (L)bs --> "))

if kilosOLibras.upper() == "K":
    kilosFinales = str(weight*2.205)
    print("Pesas " + kilosFinales + " Lbs")
elif kilosOLibras.upper() == "L":
    kilosFinales = str(weight//2.205)
    print("Pesas " + kilosFinales + " Kg")
else:
    print("No ingresas ninguna opción correcta")
