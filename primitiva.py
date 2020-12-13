#!/usr/bin/python
# -*- coding: utf-8 -*-


##############################################
## PRIMITIVA - Version 2.0                  ##
## - Envio mensajes por telegram            ##
## - Calculo probabilidades números con TXT ##
##         @cgasper79                       ## 
##############################################

#Importamos la librería para hacer Random y enviar a Telegram
import random
import enviarTelegram

#Definicion probabilidades numeros y reintegro mediante matrices

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
prob_numeros = []  # --> La probabilidad la establecemos en el archivo /.Primi/Prob_Numeros.txt
matriz_numeros = []
#Matriz para los 6 numeros
resultado_num = []
rep_num = []


complementario = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
prob_complem = [] # --> La probabilidad la establecemos en el archivo /.Primi/Prob_Complem.txt
matriz_complem = []
#Matriz para el complementario
resultado_complem = []
rep_complem = []

 
reintegro = [0,1,2,3,4,5,6,7,8,9]
prob_reint = [] # --> La probabilidad la establecemos en el archivo /.Primi/Prob_Reintegro.txt
matriz_reint = []
#Matriz para el reintegro
resultado_reint = []

#FUNCIONES

#Leemos probabilidad del txt (números, complementario y reintegro) y lo ponemos en una matriz
def leer_proba():
    with open('/home/pi/Apuestas/Primi/Prob_Numeros.txt', 'r') as f:
       lines = f.readlines()

    for line in lines:
       prob_numeros.append(float(line.rstrip()))

    with open('/home/pi/Apuestas/Primi/Prob_Complem.txt', 'r') as f:
       lines = f.readlines()

    for line in lines:
       prob_complem.append(float(line.rstrip()))
    
    with open('/home/pi/Apuestas/Primi/Prob_Reintegro.txt', 'r') as f:
       lines = f.readlines()

    for line in lines:
       prob_reint.append(float(line.rstrip()))



#Duplicamos lista con numeros mas probables
def prepara_num():
    global matriz_numeros
    global matriz_complem
    global matriz_reint
    for n, p in zip(numeros, prob_numeros):
        # se almacenan repetidos los numeros según la probabilidad elegida
        # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
        matriz_numeros += [n] * int(p * 100)

    for n, p in zip(complementario, prob_complem):
        # se almacenan repetidos los numeros según la probabilidad elegida
        # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
        matriz_complem += [n] * int(p * 100)

    for e, p in zip(reintegro, prob_reint):
        # se almacenan repetidos los numeros según la probabilidad elegida
        # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
        matriz_reint += [e] * int(p * 100)


#Calculamos lo 6 Numeros sin valores repetidos

def calcula_num():
    num = 1
    while num == 1:
        for i in range(6):
            resultado_num.append(random.choice(matriz_numeros))
        for x in resultado_num:
            if x not in rep_num:
	               rep_num.append(x)
            else:
                resultado_num.append(random.choice(matriz_numeros))
                
        num = 0


#Calculamos el complementario sin valores repetidos
def calcula_compl():
    num = 1
    while num == 1:
        for i in range(1):
            resultado_complem.append(random.choice(matriz_complem))

        for x in resultado_complem:
            if x not in rep_num:
                rep_complem.append(x)
            else:
                print('valor repetido')
                resultado_complem.append(random.choice(matriz_numeros))

        num = 0


#Calculamos Reintegro y ordenamos
def combinacion(): 
    resultado_reint.append(random.choice(matriz_reint))
    rep_num.sort()

#Borramos listas
def borrar_listas():
    del resultado_num[:]
    del rep_num[:]
    del resultado_complem[:]
    del rep_complem[:]
    del matriz_reint[:]
    del resultado_reint[:]
    
    

#Enviamos números y estrellas por Telegram
def enviar_telegram():
    mensaje = '🍀 Primitiva 🍀  \n '+'Números:' + str(rep_num) + '\nC: ' + str(rep_complem) + '\nR: ' + str(resultado_reint)
    enviarTelegram.enviarMensaje (mensaje)


# Generamos combinaciones
def generar():
    leer_proba()
    prepara_num()
    calcula_num()
    calcula_compl()
    combinacion()
    enviar_telegram()
    print('Numeros:',rep_num)
    print('C:',rep_complem)
    print('R:',resultado_reint)
    borrar_listas()

#FIN
