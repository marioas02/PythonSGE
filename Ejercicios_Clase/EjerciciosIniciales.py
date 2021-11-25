
import random


# 2. Crear un array con los siguientes datos "perro", "gato", 1, 100.:--------------------------

arraycosas = ["perro", "gato", 1, 00]


# 3. Mostrar de la segunda a la cuarta letra de la primera palabra del array anterior:----------

print(arraycosas[0][1:4])


# 4. Mostrar la pen�ltima letra de la segunda palabra:-----------------------------------------

print(arraycosas[1][-2])


# 5. En la tercera posici�n del array guardar el siguiente texto con este formato:-------------
# "En un
# 	lugar de
#     la mancha..."
arraycosas[2] = """En un
        lugar de
    la mancha..."""
print(arraycosas[2])


# 6. Sumar al contenido de la cuarta posici�n la primera cifra de esta misma posici�n:---------
numero = str(arraycosas[3])
mostrar = arraycosas[3]+int(numero[0])
print(mostrar)


# 7. Agregar al final del array otro array: "tortuga", 200:--------------------------------------
arraycosas.append(["tortuga", 200])
print(arraycosas[4])


# 8. Mostrar por pantalla la tabla de multiplicar del 5 usando un while:-------------------------
numero = 5
contador = 0
while contador < 10:
    contador = contador + 1
    print("5 * "+str(contador)+" = "+str(numero * contador))


# 9. Introducir un número en una variable y decir cuántas cifras tiene:--------------------------
print("introduce un numero")
numero = input()
print("tiene "+str(len(numero))+" cifras")


# 10. Introducir un número en una variable y decir si es capicúa:--------------------------------
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


# 11. En MegaPlaza se hacen los siguientes descuentos:
# 10% a los clientes cuya compra supere los 100�
# 20% a los clientes cuya compra supere los 200�
# si el cliente paga con tarjeta se haga un 5% de descuento adicional
# ¿Cual será la cantidad que pagara una persona por su compra?
# ej: Introduce el importe de tu compra: 100
# Pagará con tarjeta? S/N : S
# El cliente deberá pagar 85€:
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
print("el cliente paga "+str(pago))


# 12. Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
# Si trabaja 40 horas o menos se le paga $16 por hora
# Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
# Calcular su salario semanal a partir de sus horas de trabajo.
print("introduce el numero de horas trabajadas")
hora = int(input())
sueldo = 0
if hora > 40:
    horaextras = hora - 40
    sueldo = 40 * 16
    sueldo = sueldo + (horaextras * 20)
else:
    sueldo = hora * 16
print("tu sueldo es "+str(sueldo))


# 13. Dibuja un cuadrado de n elementos de lado utilizando *. Pedir n al usuario.
# ej:
# Introduce un numero : 5
# *****
# *****
# *****
# *****
print("escribe el numero de * que quieres que tenga tu cuadrado")
lado = int(input())
for i in range(lado):
    for j in range(lado):
        print("* ", end="")
    print()


# 14. Dibuja un cuadrado hueco de n elementos de lado utilizando *. Pedir n al usuario.
# ej:
# Introduce un numero : 5
# *****
# *   *
# *   *
# *   *
# *****
print("escribe el numero de * que quieres que tenga tu cuadrado")
lado = int(input())
for i in range(lado):
    pinta = ""
    for j in range(lado):
        if i == 0 or i == lado-1:
            pinta = pinta + "* "
        else:
            if j == 0 or j == lado-1:
                pinta = pinta + "* "
            else:
                pinta = pinta + "  "
    print(pinta)


# 15. Leer 5 numeros y mostrar el m�nimo introducido, el m�ximo introducido y la media.
mayor = 0
media = 0
menor = 0
contador = 0
for i in range(5):
    print("escribe "+str(i+1)+" numero")
    numero = int(input())
    if i == 0:
        menor = numero
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    media = media + numero
    contador = contador + 1;
print("el mayor es: "+str(mayor))
print("el menor es: "+str(menor))
print("y la media es: "+str(media/contador))


# 16. Leer 10 n�meros enteros. Debemos mostrarlos en el siguiente orden:
# el primero, el �ltimo, el segundo, el pen�ltimo, el tercero, etc.
numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(numero)):
    print("escribe " + str(i + 1) + " numero")
    numero[i] = input()
print(numero[0]+", "+numero[9]+", "+numero[1]+", "+numero[8]+", "+numero[2]+", "+numero[7]+", "+numero[3]+", "+numero[6]+", "+numero[4]+", "+numero[5])


# 17. Leer por teclado una serie de 10 n�meros enteros. La aplicaci�n
# debe indicarnos si los n�meros est�n ordenados de forma creciente, decreciente, o si est�n desordenados.
numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cre = 0
des = 0
for i in range(len(numero)):
    print("escribe " + str(i + 1) + " numero")
    numero[i] = input()
for i in range(len(numero)-1):
    if numero[i] < numero[i+1]:
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


# 18. Dibujar esta figura con el numero de asteriscos que diga el usuario:
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


# 19. Cargar un array con 10 numeros que introduzca el usuario
# y comprobar si alguno de esos numeros se repite.
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


# 20. Dibujar un rombo con el numero de asteriscos en su fila centralque diga el usuario.
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


# 21. Con 2 arrays que se rellenan con 10 numeros aleatorios del 1 al 50 comprobar si alguno
# de los numeros del array A se repile en el array B.
numeros1 = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)]
numeros2 = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)]
repeticiones = 0
for i in range(len(numeros1)):
    for j in range(len(numeros2)):
        if numeros1[i] == numeros2[j]:
            repeticiones += 1
if repeticiones > 0:
    print("los numeros se repiten")
else:
    print("los numeros no se repiten")


# 22. Dise�ar una aplicaci�n que declare una tabla de 10 elementos enteros. Leer mediante el teclado 8 n�meros.
# Despu�s se debe pedir un n�mero y una posici�n, insertarlo en la posici�n indicada, desplazando los que est�n detr�s.
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


# 23. Introducir las notas de 3 asignaturas y n alumnos.
# 	1- Pedir por teclado el numero de alumnos. (N)
# 	2- Habra 3 asignaturas.
# 	Crear 3 arrays de N posiciones e introducir los datos:
# ej: introduce la nota del alumno 2 y la asignatura 1: 8
# 	introduce la nota del alumno 2 y la asignatura 2: 7
# Al finalizar se mostrar�n todos los datos, adem�s de la media por alumno, la media por asignatura,
# el numero de suspensos por asignatura y el numero de suspensos por alumnos.
alumno = 0
print("escribe el numero de alumnos")
alumno = int(input())
asignatura1 = []
asignatura2 = []
asignatura3 = []
for i in range(alumno):
    print("introduce la nota del alumno "+(i + 1)+" y la asignatura 1")
    asignatura1.append(int(input()))
    print("introduce la nota del alumno " + (i + 1) + " y la asignatura 2")
    asignatura2.append(int(input()))
    print("introduce la nota del alumno " + (i + 1) + " y la asignatura 3")
    asignatura3.append(int(input()))
for i in range(alumno):
    print("Alumno "+(i + 1)+": la asignatura 1 "+asignatura1[i]+", la asignatura 2 "+asignatura2[i]+", la asignatura 3 "+asignatura3[i])
    print("media ")
