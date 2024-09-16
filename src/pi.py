#!/usr/bin/env python

#funcion para la evaluacion de los puntos medios


def evaluacion(x):
    return (4/(1+(x**2)))

#funcion para realizar una sumatoria de Riemann

def sumatoriaR(inicio,final,numRec,funcionEvaluar):

    baseRec = (abs(final-inicio))/(numRec)
    Areas = []
    ptoMedio = baseRec/2
    for i in range(0,numRec):
        posicion = ptoMedio + (baseRec*i)
        altura = funcionEvaluar(posicion)
        area = baseRec * altura
        Areas.append(area)

    sum = 0
    for i in range (len(Areas)):
        sum = Areas[i] + sum

    print(sum)

#Bloque principal

limiteInicial = 0
limiteFinal = 1
CantidadRectangulos = 100000

sumatoriaR(limiteInicial,limiteFinal,CantidadRectangulos,evaluacion)
