#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################
## EUROMILLONES - Version 2.0               ##
## - Envio mensajes por telegram            ##
## - Calculo probabilidades números con TXT ##
##         @cgasper79                       ## 
##############################################

#Importamos la librería para hacer Random y enviar a Telegram
import random
import enviarTelegram

#Definicion probabilidades numeros y estrellas mediante listas
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
prob_numeros = [] # --> La probabilidad la establecemos en el archivo ./Euro/Prob_Numeros.txt
#listas para los 5 numeros
resultado_num = []
rep_num = []
matriz_numeros = []

estrellas = [1,2,3,4,5,6,7,8,9,10,11,12]
prob_est = [] # --> La probabilidad la establecemos en el archivo ./Euro/Prob_Reintegro.txt
#Listas para las 2 estrellas
resultado_est = []
rep_est = []
matriz_est = []


#Leemos probabilidad del txt (números y Estrellas) y lo ponemos en una matriz
def leer_proba():

    with open('/home/pi/Apuestas/Euro/Prob_Numeros.txt', 'r') as f:
       lines = f.readlines()

    for line in lines:
       prob_numeros.append(float(line.rstrip()))
    
    with open('/home/pi/Apuestas/Euro/Prob_Estrellas.txt', 'r') as f:
       lines = f.readlines()

    for line in lines:
       prob_est.append(float(line.rstrip()))


#Duplicamos lista con numeros mas probables
def prepara_num():
    global matriz_numeros 
    global matriz_est

    for n, p in zip(numeros, prob_numeros):
        # se almacenan repetidos los numeros según la probabilidad elegida
        # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
        matriz_numeros += [n] * int(p * 100)

    for e, p in zip(estrellas, prob_est):
        # se almacenan repetidos los numeros según la probabilidad elegida
        # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
        matriz_est += [e] * int(p * 100)


#Calculamos Numeros sin valores repetidos
def calcula_num():

    num = 1
    while num == 1:
        for i in range(5):
            resultado_num.append(random.choice(matriz_numeros))
        for x in resultado_num:
            if x not in rep_num:
	               rep_num.append(x)
            else:
                resultado_num.append(random.choice(matriz_numeros))
        num = 0


#Calculamos Estrellas sin valores repetidos
def calcula_est():
    est = 1

    while est == 1:

        for i in range(2):
            resultado_est.append(random.choice(matriz_est))

        for x in resultado_est:
            if x not in rep_est:
                rep_est.append(x)
            else:
                resultado_est.append(random.choice(matriz_est))
        est = 0

#Combinamos números y Estrellas, ordenamos
def combinacion():
    rep_num.sort()
    rep_est.sort()
    


#Borramos listas
def borrar_listas():
    del resultado_num[:]
    del rep_num[:]
    del resultado_est[:]
    del rep_est[:]
    del matriz_numeros[:]
    del matriz_est[:]
    

    

#Enviamos números y estrellas por Telegram
def enviar_telegram():
    mensaje = '🍀 Euromillones 🍀  \n '+'Números:' + str(rep_num) + '\nEstrellas: ' + str(rep_est) 
    enviarTelegram.enviarMensaje (mensaje)


# Generamos combinaciones
def generar():
    leer_proba()
    prepara_num()
    calcula_num()
    calcula_est()
    combinacion()
    enviar_telegram()
    print('Numeros:',rep_num)
    print('Estrellas:',rep_est)
    borrar_listas()

#FIN
