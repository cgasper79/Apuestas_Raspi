#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importamos la librería necesaria para hacer una consulta HTTP y utilizar JSON
import requests

import random

#Definicion probabilidades numeros y reintegro mediante matrices

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
prob_numeros = [0.150862068965517,	0.137931034482759,	0.147988505747126,	0.150862068965517,	0.107758620689655,	0.145114942528736,	0.145114942528736,	0.139367816091954,	0.137931034482759,	0.137931034482759,	0.152298850574713,	0.156609195402299,	0.113505747126437,	0.132183908045977,	0.150862068965517,	0.142241379310345,	0.135057471264368,	0.140804597701149,	0.133620689655172,	0.137931034482759,	0.153735632183908,	0.145114942528736,	0.137931034482759,	0.156609195402299,	0.125,	0.149425287356322,	0.129310344827586,	0.150862068965517,	0.139367816091954,	0.153735632183908,	0.132183908045977,	0.150862068965517,	0.122126436781609,	0.139367816091954,	0.152298850574713,	0.147988505747126,	0.150862068965517,	0.149425287356322,	0.130747126436782,	0.155172413793103,	0.139367816091954,	0.123563218390805,	0.140804597701149,	0.130747126436782,	0.158045977011494,	0.135057471264368,	0.132183908045977,	0.117816091954023,	0.15948275862069]
matriz_numeros = []
#Matriz para los 6 numeros
resultado_num = []
rep_num = []


complementario = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
prob_complem = [0.0201149425287356,0.0158045977011494,0.0172413793103448,0.0316091954022989,0.00718390804597701,0.0316091954022989,0.014367816091954,0.021551724137931,0.00574712643678161,0.0229885057471264,0.0172413793103448,0.0129310344827586,0.00862068965517241,0.0172413793103448,0.0244252873563218,0.0272988505747126,0.0186781609195402,0.0272988505747126,0.0158045977011494,0.021551724137931,0.0229885057471264,0.0114942528735632,0.0172413793103448,0.0301724137931034,0.0244252873563218,0.021551724137931,0.021551724137931,0.0158045977011494,0.0229885057471264,0.0129310344827586,0.0158045977011494,0.021551724137931,0.0201149425287356,0.0201149425287356,0.0158045977011494,0.0186781609195402,0.014367816091954,0.0114942528735632,0.0129310344827586,0.021551724137931,0.0172413793103448,0.0201149425287356,0.014367816091954,0.0201149425287356,0.0201149425287356,0.0229885057471264,0.0129310344827586,0.00718390804597701,0.0172413793103448]
matriz_complem = []
#Matriz para el complementario
resultado_complem = []
rep_complem = []

 
reintegro = [0,1,2,3,4,5,6,7,8,9]
prob_reint = [0.09,0.09,0.1,0.09,0.1,0.08,0.09,0.09,0.11,0.09]
matriz_reint = []
#Matriz para el reintegro
resultado_reint = []


#Duplicamos lista con numeros mas probables

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
num = 1
while num == 1:
 for i in range(6):
    resultado_num.append(random.choice(matriz_numeros))

 for x in resultado_num:
    if x not in rep_num:
	rep_num.append(x) 
    else:
	print('valor repetido')
        resultado_num.append(random.choice(matriz_numeros))
 num = 0


#Calculamos el complementario sin valores repetidos
num = 1
while num == 1:
 resultado_complem.append(random.choice(matriz_complem))

 for x in resultado_complem:
    if x not in rep_num:
        rep_complem.append(x)
    else:
        print('valor repetido')
        #resultado_num.append(random.choice(matriz_numeros))
 num = 0


#Calculamos Reintegro
resultado_reint.append(random.choice(matriz_reint))

rep_num.sort()
print('Numeros:',rep_num)
print('Reintegro:',resultado_reint)


 #Enviamos POST a WebHook con los números y las estrellas de la EUROMILLONES
url = "https://maker.ifttt.com/trigger/apuestas_primi/with/key/dhF38W2gCVDFXS-3iP6Lwr"
post_fields = { "value1" :rep_num, "value2" :resultado_reint, "value3" :""}
request = requests.post(url,json=post_fields)
