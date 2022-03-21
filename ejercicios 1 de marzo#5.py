edad = int(input("Introducetuedad: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
        precio = 10
print("Elpreciodelaentradaes$ ",precio)