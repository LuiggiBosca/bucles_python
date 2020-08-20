#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


valor_maximo = 6


def bucle_while():
    # Ejercicios con bucles "while"
    x = 0

    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración
    while x < valor_maximo:
        if x == 5:
            print('Bucle interrumpido en x =', x)
            break

        x_prima = x     #guardamos la variable en un x_prima
        x += 1          #incrementamos la variable
        if(x_prima) == 0:
            continue
            print(x_prima, 'es menor a', valor_maximo)


    while True:    # reemplace "condicion" por lo que crea necesario
        print("ingrese un valor para x =", valor_x)
        valor_x = int(input())

        x_prima2 = valor_x
        valor_x += 1

        if valor_x == 5:
            print('Se termino. x={}'.format(valor_x))
            break
        print('x ingresada={}'.format(valor_x))
        
    # Coloque la línea de código para que "X" incremente "1"
    x = 5

    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    while True:    # reemplace "condicion" por lo que crea necesario
        print("ingrese un valor para x >= 0", x)
        x = int(input())

        # Coloque la línea de código para que "X" decremente "1"
        x_prima = x
        x -= -1

        if(x_prima) == 4:
            print('Se termino en x_prima = {}'.format(x_prima))
            break
            print(x_prima, 'es menor a', valor_maximo)



def bucle_for ():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']
    colores_len = len(colores)
    
    for i in range(colores_len):
        if i == 0:
            lista_color = colores[i]        
            print('el color es:', lista_color)


    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...
    
    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ... (**no me quedo claro que quiere)

    for i in range(ageda_len):
        if i == 0:
            lista_color = colores[i]
            numero_color = colores_len[i]
            print('para el color:', lista_color, 'el numero:', numero_color)

def bucle_sumatoria():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    sumatoria = 0   # Variable ya inicializada, la suma arranca en cero

    for numero in numeros:
        sumatoria += numero
        print('numero =', numero, 'sumatoria =', sumatoria)


def bucle_while():
    # Ejercicios con bucles "while"
    
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    valor_maximo = 9
    contador = 1
    numero_valido = True
    print('ingrese un numero mayor a 0 y menor a 10')
    print('ingrese el numero 6 para terminar')

    while numero_valido:
        x = int(int())
    
    if ((x >= 0 and x < 10 and x >= 0) and x != 6):
            print('el numero de x =', x)
    else:
        if x == 6:
            print('bucle interrumpido en x =', x)
            break

        x_aux = x
        x += 2

        if x_aux == 0:
            continue
            print('el valor de x incrementada es:'. x_aux,)

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    valor_maximo = 9
    contador = 1
    numero_valido = True
    print('ingrese un numero mayor a 0 y menor a 10')
    print('ingrese el numero 6 para terminar')

    while numero_valido:
        x = int(int())
    
    if (x >= 0 and x < 10 and x >= 0):
            print('el numero de x =', x)
    elif x == 6:
            print('bucle interrumpido en x =', x)
            break

    x_aux = x
    x += 2

    if x_aux == 0:
            continue
            print('el valor de x incrementada es:'. x_aux,)

def bucle_for():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # fin....
    numero_minimo = None
    numero_maximo = (None - 1)

    print('para esta secuencia, ingrese el numero inicial')
    numero_minimo = input(int())
    print('para esta secuencia, ingrese el numero final')
    numero_maximo = input(int())

    numeros = []
    sumatoria = 0

    # for ... in range(....)
    for numero in numeros:
        sumatoria += numero
    
    # Imprimir el valor de la sumatoria
        print('sumatoria =', sumatoria)


def ej6():
    # Ejercicio de secuencias numéricas

    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # fin....
    # Inicializo el contador en 0
    # cantidad_numeros_negativos
    # for ... in range(....)
    # Imprimir el valor de la cantidad de números positivos y negativos

    minimo = None
    maximo = (None - 1)

    print('para esta secuencia, ingrese el numero inicial')
    minimo = input(int())
    print('para esta secuencia, ingrese el numero final')
    maximo = input(int())

    numeros = [minimo, maximo]
    numeros_len = len(numeros)

    for numero in range(numeros_len):
        if numero >= 0:
            positivos = numeros_len
            print('numero positivos o cero:', positivos)
        else:
            negativos = numeros_len
            print('numeros negativos:', negativos)
    
        


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #bucle_while()
    #bucle_for()
    #bucle_sumatoria()
    #bucle_while()
    #bucle_for()
    #ej6()
