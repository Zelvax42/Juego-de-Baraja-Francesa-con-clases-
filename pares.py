#!/usr/bin/python3
# Equipo: Mustafar
# Fecha: 27 de marzo de 2020
# Integrantes:
#
#   Félix López Juan Pablo
#   López Velásquez Octavio
#   Serna Navarro Ángel Emilio
''' Juego de Baraja Francesa con Clases '''
import argparse
import tarjetas


def genera_lista_cartas():
    ''' 
        genera una lista de todas las cartas de la baraja (52 cartas)
        y regresa una lista de estas
    '''
    lista_cartas = list()
    for i in range(0, 4):
        if i == 0:
            figura = "♥"  # Corazones
        elif i == 1:
            figura = "♠"  # Picas
        elif i == 2:
            figura = "♣"  # Trébol
        elif i == 3:
            figura = "♦"  # Diamante
        for valor in range(2, 15):  # los valores de las cartas empiezan en 2
            if valor == 14:
                valor = 20  # As vale 20
            carta_nueva = tarjetas.Carta(valor, figura)
            lista_cartas.append(carta_nueva)

    return lista_cartas


def genera_jugadores(lista_jugadores, baraja):
    '''
        genera los jugadores en un objeto baraja
        recibe: una lista de jugadores (string)
        recibe: un objeto baraja
    '''
    for nombre in lista_jugadores:
        nombre = tarjetas.Jugador(nombre, baraja)


def desplegar_cartas(lista_cartas):
    '''
        imprime cada carta de una lista de cartas
        POSIBLEMENTE QUEDE EN DESHUSO
    '''
    for carta in lista_cartas:
        print(carta)


def despliega_lista_manos(baraja, mano):
    '''
        imprime las cartas de todos los jugadores
        recibe: objeto baraja
    '''
    lista_puntajes = []
    i = 0
    dic = {}
    lista_diccionarios = []
    lista_jugadores = []
    for jugador in baraja.lista_jugadores:
        lista_valores = []
        cartas_mano = jugador.despliega_mano(baraja)
        nombre_jugador = (baraja.lista_jugadores[i].nombre)

        for index in range(0, mano):
            valores = (baraja.lista_jugadores[i].mano[index].valor)

            lista_valores.append(valores)

        i += 1
        dic = {i: lista_valores.count(i) for i in lista_valores}

        lista_puntaje = []
        for key, value in dic.items():
            temp = [key, value]
            lista_puntaje.append(temp)

        lista_diccionarios.append(lista_puntaje)
        #print(lista_puntaje[1])
        puntuacion = (puntaje(lista_puntaje)[0])
        pares = (puntaje(lista_puntaje)[1])
        trios = (puntaje(lista_puntaje)[2])

        print("\nCantidad de pares: " + str(pares))
        print("Cantidad de trios: " + str(trios))

        tupla_jugadores = []
        tupla_jugadores.append(nombre_jugador)
        tupla_jugadores.append(puntuacion)
        tupla_jugadores.append(pares)
        tupla_jugadores.append(trios)

        lista_puntajes.append(tuple(tupla_jugadores))

        print("\nPuntuación: " + str(puntuacion) + " puntos")

    jugador_ganador = ganador(lista_puntajes)

    if(len(jugador_ganador) != 0):
        print("\nGanador: " + str(jugador_ganador[0][0]) + ", con " + str(jugador_ganador[0][1]) + " puntos, " + str(
            jugador_ganador[0][2]) + " pare(s) y " + str(jugador_ganador[0][3]) + " trios.")
    else:
        print("\nEmpate.")

    return lista_diccionarios, lista_puntajes

# OctavioLovesLists


def puntaje(lista_diccionarios):
    '''
        Calcula el puntaje
        recibe: lista de diccionarios
        regresa una lista: puntaje, cantidad de pares, cantidad de tercias
    '''

    lista_puntaje = []
    puntaje = 0
    cantidad_pares = 0
    cantidad_trios = 0
    index = -1

    for elemento in lista_diccionarios:
        valor = elemento[1]
        if valor >= 2:
            lista_puntaje.append(elemento)
            if valor == 2:
                cantidad_pares += 1
            if valor == 3:
                cantidad_trios += 1
            index += 1

            for carta in range(len(lista_puntaje)-index):
                cartas = lista_puntaje[index]
                puntaje += cartas[0]*cartas[1]

    return puntaje, cantidad_pares, cantidad_trios


def ganador(lista_puntajes):
    ganador = []

    for jugador in lista_puntajes:
        if (len(ganador) == 0):
            if(jugador[1] != 0):
                ganador.append(jugador)
        elif(jugador[1] > 0):
            if (jugador[2] == ganador[0][2] or jugador[3] == ganador[0][3]) and (jugador[1] > ganador[0][1]):
                ganador = jugador

            if(jugador[2] == 2) and (ganador[0][3] == 1):
                ganador = jugador

            if(jugador[3] == 1) and (ganador[0][2] == 1):
                ganador = ganador

            if(jugador[2] == 1) and (ganador[0][3] == 1):
                ganador = jugador

            if(jugador[2] == 2) and (ganador[0][2] == 1):
                ganador = jugador

    return ganador


def calcula_pares_trios(baraja):
    '''
        calcula el numero de pares y tercias que tienen los jugadores
        recibe: objeto baraja
        regresa: una lista = nombre del jugador, numero de pares, numero de tercias
    '''
    lista_jugadores = baraja.lista_jugadores
    lista_pares_trios = list()
    for jugador in lista_jugadores:  # se iteran todos los jugadores
        nombre = jugador.nombre
        mano = jugador.mano
        mano_formato_limpio = list() # esta mano solo tiene valores, sin figuras

        for valores in mano:
            mano_formato_limpio.append(valores.valor)

        dicc = dict.fromkeys(mano_formato_limpio, 0) # diccionario a partir de la mano

        pares = 0
        trios = 0
        for carta in mano:          # se iteran las cartas de la mano de un jugador
            valor = carta.valor
            if dicc.get(valor) == 0:  # no existe
                dicc[valor] = 1
            elif dicc.get(valor) > 0:  # ya existe
                dicc[valor] += 1

        for key in dicc:     # calcular pares y trios
            valor = dicc.get(key)   # valor del diccionario
            if valor % 2 == 0:      # es par
                pares += 1
            elif valor % 3 == 0:    # es trio
                trios += 1
        lista = [nombre, pares, trios]
        lista_pares_trios.append(lista)
        del(dicc)

    return lista_pares_trios


def main(jugadores, mano):
    lista_cartas = genera_lista_cartas()

    if (len(jugadores) >= 2 and (
            len(jugadores)) * mano <= 52):  # Tienen que más de dos jugadores y la mano menor a 52
        print("\n== JUEGO DE BARAJA FRANCESA ==\n")
        baraja = tarjetas.Baraja(lista_cartas)
        genera_jugadores(jugadores, baraja)
        baraja.genera_mano(mano)
        despliega_lista_manos(baraja, mano)
        print(calcula_pares_trios(baraja))

    else:
        print(
            "\nLa cantidad de cartas repartidas por jugador debe de ser acorde al número de cartas disponible en la baraja.\n")
        print("Cantidad solicitada: " + str(mano * len(jugadores)))
        print("Total de cartas disponibles: " + str(len(lista_cartas)) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--jugadores', dest='jugadores',
                        help="Nombre del jugador.", required=True, action="append")
    parser.add_argument('-m', '--mano', dest='mano',
                        help="Tamaño de mano", type=int, required=False, default=5)
    args = parser.parse_args()
    jugadores = args.jugadores
    mano = args.mano

    main(jugadores, mano)
