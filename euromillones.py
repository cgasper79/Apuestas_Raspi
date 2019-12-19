#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importamos la librería necesaria para hacer una consulta HTTP y utilizar JSON
import requests
#Importamos la librería para hacer Random
import random

#Definicion probabilidades numeros y estrellas mediante matrices

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
prob_numeros = [0.11,0.09,0.1,0.11,0.12,0.1,0.1,0.09,0.09,0.11,0.1,0.1,0.1,0.1,0.11,0.11,0.09,0.11,0.09,0.11,0.1,0.1,0.08,0.12,0.1,0.11,0.11,0.11,0.1,0.11,0.11,0.09,0.08,0.09,0.1,0.1,0.11,0.11,0.1,0.09,0.08,0.11,0.1,0.12,0.1,0.08,0.08,0.09,0.1,0.12]
matriz_numeros = []
#Matriz para los 5 numeros
resultado_num = []
rep_num = []
 
estrellas = [1,2,3,4,5,6,7,8,9,10,11,12]
prob_est = [0.18,0.2,0.2,0.17,0.19,0.18,0.19,0.2,0.19,0.13,0.12,0.04]
matriz_est = []
#Matriz para las 2 estrellas
resultado_est = []
rep_est = []

#Duplicamos lista con numeros mas probables
for n, p in zip(numeros, prob_numeros):
    # se almacenan repetidos los numeros según la probabilidad elegida
    # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
    matriz_numeros += [n] * int(p * 100)

for e, p in zip(estrellas, prob_est):
    # se almacenan repetidos los numeros según la probabilidad elegida
    # por ejemplo el 1 estará 50 veces en la lista y el 8, 40 veces repetido
    matriz_est += [e] * int(p * 100)

#Calculamos Numeros sin valores repetidos
num = 1

while num == 1:

 for i in range(5):
    resultado_num.append(random.choice(matriz_numeros))

 for x in resultado_num:
    if x not in rep_num:
	rep_num.append(x) 
    else:
	print('valor repetido')
        resultado_num.append(random.choice(matriz_numeros))
 num = 0

#Calculamos Estrellas sin valores repetidos

est = 1
while est == 1:

 for i in range(2):
    resultado_est.append(random.choice(matriz_est))

 for x in resultado_est: 
    if x not in rep_est:
        rep_est.append(x)
    else:
        print('valor repetido estrella')
        resultado_est.append(random.choice(matriz_est))   
 est = 0

rep_num.sort()
rep_est.sort()
print('Numeros:',rep_num)
print('Estrellas:',rep_est)


 #Enviamos POST a WebHook con los números y las estrellas de la EUROMILLONES
url = "https://maker.ifttt.com/trigger/apuestas/with/key/dhF38W2gCVDFXS-3iP6Lwr"
post_fields = { "value1" :rep_num, "value2" :rep_est, "value3" : "" }
request = requests.post(url,json=post_fields)
