#!/usr/bin/python
import requests

# Definimos variables Token, Chat ID y mensaje
token = 'TU_TOKEN'
chatId= 'TU_CHAT_ID'



def enviarMensaje (text):
	requests.post('https://api.telegram.org/bot' + token +'/sendMessage',
			data={'chat_id': chatId, 'text': text})



