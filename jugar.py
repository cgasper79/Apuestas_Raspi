#!/usr/bin/python
# -*- coding: utf-8 -*-


#######################################################################
##                PRIMITIVA y EUROMILLONES                           ##
## Programa Principal para enviar por Telegram las combinaciones     ##
## y resultados.                                                     ##
##                                                                   ##
## - Resultados Euromillones: se envía URL el Miércoles y Sábado     ##
##  (Día después del sorteo)                                         ##
##                                                                   ##   
## - Resultados Primitiva: se envía URL el Viernes y Domingo         ##
##  (Día después del sorteo)                                         ##
##                                                                   ##
## - Combinaciones de Euromillones: se envían 5 combinaciones        ##
##   todos los Lunes y Jueves para el sorteo del Martes y Viernes    ##
##                                                                   ##
## - Combinaciones de Primitiva: se envían 5 combinaciones           ##
##   todos los Miércoles y Viernes para el sorte del Jueves y Sábado ##
##                                                                   ##
## Realizado por: @cgasper79                                         ##
## Visita Telegram: https://t.me/raspiapuestas                       ##
## Versión: 2.0 
#######################################################################


#Importamos librerías necesarias
from datetime import datetime, date, time, timedelta
import calendar
import primitiva
import euromillones
import enviarTelegram

#Variables y Constantes
urlPrimi = 'https://www.loteriasyapuestas.es/es/resultados/primitiva'
urlEuro = 'https://www.loteriasyapuestas.es/es/resultados/euromillones'
numCombinaciones = 5


#FUNCIONES

#Enviar mensaje a través de Telegram
def enviarMensaje(msj):
    enviarTelegram.enviarMensaje(msj)


#Enviamos URL con resultado del día anterior
def enviarURL():
    #Euromillones se envia Miércoles y Sábado 
    if (diaSemana == '3') or (diaSemana == '6'):
        mensaje = '🍀  Resultado Euromillones de ayer ' + ayer + '\n' + urlEuro
        enviarMensaje(mensaje)
        print(mensaje)
    
    #Primitiva se envía Viernes y Domingo
    if (diaSemana == '5') or (diaSemana == '0'):
        mensaje = '🍀  Resultado Primitiva de ayer ' + ayer + '\n' + urlPrimi
        enviarMensaje(mensaje)
        print(mensaje)

#Generamos 5 combinaciones según el día
def combinaciones():

    #Lunes y Jueves para sorteo Euromillones Martes y Viernes
    if (diaSemana == '1') or (diaSemana == '4'):
        mensaje = '🍀  Euromillones 🍀  - Combinaciones para mañana  ' + manana 
        print(mensaje)
        enviarMensaje(mensaje)
        i = 1
        while i <= numCombinaciones:
            print ('Combinación Euromillones')
            euromillones.generar()
            i += 1

    #Miércoles y Viernes para el sorteo Primitiva del Jueves y sábado
    if (diaSemana == '3') or (diaSemana == '5'):
        mensaje = '🍀  Primitiva 🍀  - Combinaciones para mañana  ' + manana 
        print(mensaje)
        enviarMensaje(mensaje)
        i = 1
        while i <= numCombinaciones:
            print ('Combinación Primitiva')
            primitiva.generar()
            i += 1


#Verificar fecha
def fechas():
    global diaSemana
    global diaMes
    global ayer
    global manana

    #Miramos la fecha actual y la descomponemos
    fecha = datetime.today()
    formato = ('%d-%m-%Y')
    
    #Calculamos ayer y mañana
    ayer = fecha+timedelta(days=-1)
    manana = fecha+timedelta(days=1)
    
    #Damos formato a las fechas
    hoy = fecha.strftime(formato)
    ayer = ayer.strftime(formato)
    manana = manana.strftime(formato)
  
    #Descomponemos la fecha
    diaSemana = fecha.strftime('%w')
    diaMes = fecha.strftime('%d')
   

#Principal
def main():
    fechas()
    enviarURL()
    combinaciones()
    


#INICIO PROGRAMA

if __name__ == "__main__":
    main()

#FIN PROGRAMA
