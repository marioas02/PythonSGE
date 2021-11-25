import random

# Ejercicio 1: 1. Introducir tres numeros y mostrarlos ordenados de mayor a menor.
print("#Ejercicio 1: 1. Introducir tres numeros y mostrarlos ordenados de mayor a menor.");
numeros = [0, 0, 0]

print("Numero 1:", end=" ")
numeros[0] = int(input())
print("Numero 2:", end=" ")
numeros[1] = int(input())
print("Numero 3:", end=" ")
numeros[2] = int(input())

numeros.sort(reverse=True)
print("\nOrdenados de mayor a menor son: ", end=" ")
print(numeros)

# 2. Crear un array con los siguientes datos "perro", "gato", 1, 100
print("\n2. Crear un array con los siguientes datos ""perro"", ""gato"", 1, 100")
array = ["perro", "gato", 1, 100]
print("He creado el array y queda asi:", end=" ")
print(array)

# 3. Mostrar de la segunda a la cuarta letra de la primera palabra del array anterior.
print("\n3. Mostrar de la segunda a la cuarta letra de la primera palabra del array anterior.")
print("Si ponemos: array[0][1:4] en un print sale:", end=" ")
print(array[0][1:4])
print("Porque nos dicen de la primera palabra, pos 0 y la letra de la 2 a la 4 que seria de la 1 a la 4 sin incluir")

# 4. Mostrar la penultima letra de la segunda palabra
print("\n4. Mostrar la penultima letra de la segunda palabra")
print(array[1][-2])

# 5. En la tercera posicion del array guardar el siguiente texto con este formato:
print("\n5. En la tercera posici�n del array guardar el siguiente texto con este formato:")
array[2] = """En un
        lugar de
    la mancha..."""
print("Has de poner entre tres comillas.")
print(array[2])

# 6. sumar al contenido de la cuarta posici�n la primera cifra de esta misma posicion
print("\n6. sumar al contenido de la cuarta posici�n la primera cifra de esta misma posicion")
numero = str(array[3])
mostrar = array[3] + int(numero[0])
print(mostrar)

# ejercicio 7
array.append(["tortuga", 200])
print(array[4])

# ejercicio 2.2
numero = 5
contador = 0
while contador < 10:
    contador = contador + 1
    print("5 * " + str(contador) + " = " + str(numero * contador))

# ejercicio 3.2
print("introduce un numero")
numero = input()
print("tiene " + str(len(numero)) + " cifras")

# ejercicio 4.2
print("introduce un numero")
numero = input()
salir = True
contador = [0, (len(numero) - 1)]
acierto = 0
while salir:
    if numero[contador[0]] != numero[contador[1]]:
        salir = False
    else:
        acierto = acierto + 1
    contador[0] = contador[0] + 1
    contador[1] = contador[1] - 1
    if contador[0] == len(numero):
        salir = False
if acierto == len(numero):
    print("es capicua")
else:
    print("no es capicua")

# ejercicio 11
print("introduce el importe de la compra")
pago = int(input())
print("paga con tarjeta")
tarjeta = input()
importe = pago
if importe >= 200:
    pago = pago - (importe * 0.2)
else:
    if importe >= 100:
        pago = pago - (importe * 0.1)
if tarjeta == "si":
    pago = pago - (importe * 0.5)
print("el cliente paga " + str(pago))

# ejercicio 12
print("introduce el numero de horas trabajadas")
hora = int(input())
sueldo = 0
if hora > 40:
    horaextras = hora - 40
    sueldo = 40 * 16
    sueldo = sueldo + (horaextras * 20)
else:
    sueldo = hora * 16
print("tu sueldo es " + str(sueldo))

# ejercicio 13
print("escribe el numero de * que quieres que tenga tu cuadrado")
lado = int(input())
for i in range(lado):
    for j in range(lado):
        print("* ", end="")
    print()

# ejercicio 14
print("escribe el numero de * que quieres que tenga tu cuadrado")
lado = int(input())
for i in range(lado):
    pinta = ""
    for j in range(lado):
        if i == 0 or i == lado - 1:
            pinta = pinta + "* "
        else:
            if j == 0 or j == lado - 1:
                pinta = pinta + "* "
            else:
                pinta = pinta + "  "
    print(pinta)

# ejercicio 15
mayor = 0
media = 0
menor = 0
contador = 0
for i in range(5):
    print("escribe " + str(i + 1) + " numero")
    numero = int(input())
    if i == 0:
        menor = numero
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    media = media + numero
    contador = contador + 1;
print("el mayor es: " + str(mayor))
print("el menor es: " + str(menor))
print("y la media es: " + str(media / contador))

# ejercicio 16
numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(numero)):
    print("escribe " + str(i + 1) + " numero")
    numero[i] = input()
print(numero[0] + ", " + numero[9] + ", " + numero[1] + ", " + numero[8] + ", " + numero[2] + ", " + numero[7] + ", " +
      numero[3] + ", " + numero[6] + ", " + numero[4] + ", " + numero[5])

# ejercicio 17
numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cre = 0
des = 0
for i in range(len(numero)):
    print("escribe " + str(i + 1) + " numero")
    numero[i] = input()
for i in range(len(numero) - 1):
    if numero[i] < numero[i + 1]:
        cre = cre + 1
if cre == 8:
    print("es creciente")
else:
    for i in range(len(numero) - 1):
        if numero[i] > numero[i + 1]:
            des = des + 1
    if des == 8:
        print("es descreciente")
    else:
        print("esta desordenado")

# ejercicio 18
print("escribe el numero de * que quieres que tenga tu triangulo")
numero = int(input())
for i in range(numero):
    pinta = ""
    for j in range(numero):
        if j <= i:
            pinta = pinta + "* "
    print(pinta)
for i in range(numero):
    pinta = ""
    for j in range(numero):
        if j > i:
            pinta = pinta + "* "
    print(pinta)

# ejercicio 19
numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
repeticiones = 0
for i in range(len(numero)):
    print("escribe " + str(i + 1) + " numero")
    numero[i] = input()
for i in range(len(numero)):
    for j in range(len(numero)):
        if i != j:
            if numero[i] == numero[j]:
                repeticiones += 1
if repeticiones == 0:
    print("no se repite ningun numero")
else:
    print("se repite algunos numeros")

# ejercicio 20
print("escribe el numero de * que quieres que tenga tu rombo")
numero = int(input())
limite = 0
for i in range(numero):
    pinta = ""
    for j in range(numero + limite):
        if j < limite:
            pinta = pinta + "  "
        else:
            pinta = pinta + "* "
    limite = limite + 1
    print(pinta)

# ejercicio 21
numeros1 = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
            random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
            random.randint(1, 50), random.randint(1, 50)]
numeros2 = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
            random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
            random.randint(1, 50), random.randint(1, 50)]
repeticiones = 0
for i in range(len(numeros1)):
    for j in range(len(numeros2)):
        if numeros1[i] == numeros2[j]:
            repeticiones += 1
if repeticiones > 0:
    print("los numeros se repiten")
else:
    print("los numeros no se repiten")

# ejercicio 22
numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(8):
    print("escribe " + str(i + 1) + " numero")
    numero[i] = int(input())
print(numero)
print("escribe un numero")
mete = int(input())
print("escribe una posicion")
posicion = int(input())
numero.insert(posicion, mete)
numero.pop(10)
print(numero)

# ejercicio 23aa
alumno = 0
print("escribe el numero de alumnos")
alumno = int(input())
asignatura1 = []
asignatura2 = []
asignatura3 = []
for i in range(alumno):
    print("introduce la nota del alumno " + (i + 1) + " y la asignatura 1")
    asignatura1.append(int(input()))
    print("introduce la nota del alumno " + (i + 1) + " y la asignatura 2")
    asignatura2.append(int(input()))
    print("introduce la nota del alumno " + (i + 1) + " y la asignatura 3")
    asignatura3.append(int(input()))
for i in range(alumno):
    print("Alumno " + (i + 1) + ": la asignatura 1 " + asignatura1[i] + ", la asignatura 2 " + asignatura2[
        i] + ", la asignatura 3 " + asignatura3[i])
    print("media ")
