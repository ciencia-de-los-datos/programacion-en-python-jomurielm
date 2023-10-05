"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

data = csv.reader(open("data.csv"),delimiter="\t")

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0

    for row in data:
        suma += int(row[1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras = {}

    for row in data:
        if row[0] in letras.keys():
            letras[row[0]] +=1
        else:
            letras[row[0]] = 1

    return sorted(letras.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letras = {}

    for row in data:
        if row[0] in letras.keys():
            letras[row[0]] += int(row[1])
        else:
            letras[row[0]] = int(row[1])

    return sorted(letras.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    letras = {}

    for row in data:
        month = row[2].split("-")[1]
        if month in letras.keys():
            letras[month] += 1
        else:
            letras[month] = 1

    return sorted(letras.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras = {}

    for row in data:
        number = int(row[1])
        if row[0] in letras.keys():
            if number > letras[row[0]][0]:
                letras[row[0]][0] = number
            if number < letras[row[0]][1]:
                letras[row[0]][1] = number
        else:
            letras[row[0]] = [number,number]

    return [(rw[0],rw[1][0],rw[1][1]) for rw in sorted(letras.items())]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    letras = {}

    for row in data:
        for i in row[4].split(","):
            key = i.split(":")[0]
            number = int(i.split(":")[1])
        
            if key in letras.keys():
                if number < letras[key][0]:
                    letras[key][0] = number
                if number > letras[key][1]:
                    letras[key][1] = number
            else:
                letras[key] = [number,number]

    return [(rw[0],rw[1][0],rw[1][1]) for rw in sorted(letras.items())]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    numbers = {}

    for row in data:
        if int(row[1]) in numbers.keys():
            numbers[int(row[1])][0].append(row[0])
        else:
            numbers[int(row[1])] = [[row[0]]]
    return [(rw[0],rw[1][0]) for rw in sorted(numbers.items())]


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numbers = {}

    for row in data:
        if int(row[1]) in numbers.keys():
            if row[0] in numbers[int(row[1])][0]:
                pass
            else:
                numbers[int(row[1])][0].append(row[0])
        else:
            numbers[int(row[1])] = [[row[0]]]
    return [(rw[0],sorted(rw[1][0])) for rw in sorted(numbers.items())]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    letras = {}

    for row in data:
        for i in row[4].split(","):
            key = i.split(":")[0]
        
            if key in letras.keys():
                letras[key] +=1
            else:
                letras[key] = 1

    return dict(sorted(letras.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    letras = []

    for row in data:
        letras.append((row[0],len(row[3].split(",")),len(row[4].split(","))))
    return letras


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letras = {}

    for row in data:
        values = row[3].split(",")
        for i in values:
            if i in letras.keys():
                letras[i] += int(row[1])
            else:
                letras[i] = int(row[1])

    return dict(sorted(letras.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letras = {}

    for row in data:
        values = row[4].split(",")
        dic_values = dict((rw.split(":")[0],int(rw.split(":")[1])) for rw in values)
        if row[0] in letras.keys():
            letras[row[0]] += sum(dic_values.values())
        else:
            letras[row[0]] = sum(dic_values.values())

    return dict(sorted(letras.items()))
