from bs4 import BeautifulSoup as bs
import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import comtypes.client as ct
import requests as rq
import string
import random
import time
import os
import pyaudio
import subprocess
import sys
import numpy
import cv2
import datetime
import clipboard


#sys.platform
#os.startfile('notepad.exe')
#os.startfile('notepad++.exe')
#os.startfile('Steam.exe')
#subprocess.call('systeminfo')
#subprocess.call('tasklist')
#Informações de desempenho
#subprocess.call('perfmon.msc')
#subprocess.call('sticpl.cpl')
#Informações de sistema
#subprocess.call('MSINFO32')
#subprocess.call('mspaint')

#COMPROMISSOS
#subprocess.call('control schedtasks')

#subprocess.call('"C:\Program Files (x86)\Microsoft\Skype for Desktop\Skype" /callto:danypc94')
#subprocess.call('"C:\Program Files (x86)\Steam\Steam.exe"')

tts = ct.CreateObject("sapi.SPVoice")
r = sr.Recognizer()

def recVoz(r):
	try:
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			speech = r.recognize_google(audio,language='pt-BR')
			return speech
	except sr.UnknownValueError:
		print('Erro de reconhecimento de fala')
		time.sleep(2)
		main()

def pass_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

def ler():
    texto = clipboard.paste()
    print (texto)
    main()

def ativarModVigilante():
 #   tts.Speak('iniciando filmagem')
    data = datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S')
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('Monitorado - ' + data + '_'  + '.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    main()

def pesqGoogle():
	print("Quinta-feira: ...")
	speech = recVoz(r)
	print('Você: ', speech)
	speech = speech.replace(" ", '+')
	url = "https://www.google.com.br/search?q="+speech
	os.system("cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "+url)
	main()



def traduzir():
	print('Fale o que deseja traduzir...')
	speech = recVoz(r)
	print('Você: ', speech)
	texto = speech.replace(" ", '%20')
	origem = 'pt'
	destino = 'en'
	url = "https://translate.google.com.br/?hl=pt-BR#"+origem+"/"+destino+"/"+texto
	os.system(
		"cd C:\\Program Files (x86)\\Google\\Chrome\\Application && .\\chrome.exe "+url)
	main()

bot = ChatBot('Quinta-feira')

dialogo = ['Olá', 'Olá, em que posso te ajudar?', 'Oi', 'Oi Senhor', 'tudo bem?', 'estou bem, e você?',
		   'estou bem', 'que bom','pesquisar','O que deseja pesquisar?','quinta-feira']  
bot.set_trainer(ListTrainer)
bot.train(dialogo)

def treinoExtra(bot):
	print('Treinando Diálogo\n')
	titulo = (u"Treinando Diálogo")
	tts.Speak(titulo)

	print('\Faça uma pergunta: ')
	pergunta = (u"Faça uma pergunta")
	tts.Speak(pergunta)
	print('Aprendendo: ...')
	speech = recVoz(r)
	print('Você: ', speech)
	pergunta = speech

	print('\Fale a resposta: ')
	resposta = (u"Fale a resposta")
	tts.Speak(resposta)
	print('Aprendendo: ...')
	speech = recVoz(r)
	print('\nVocê: ', speech)
	resposta = speech

	extra = [pergunta, resposta]
	bot.set_trainer(ListTrainer)
	bot.train(extra)

def main():
	os.system('cls')
	print('\n\t\t  .:: Assistente Virtual ::. \n\t\t Deu muito trabalho pra fazer! \n\n\n Nome: Danyel \t RA: 317201310 \n Nome: Caio \t RA: 317202472 \n Nome: Giovanna  RA: 315108822 \n Nome: Matheus \t RA: 315110952 \n Nome: Geydson \t RA: 315111590\n Nome: Ricardo \t RA: 315107422\n\n\n\n')
# Danyel-danypc94@outlook.com - Autor	
	try:		
		while True:					
			print('Estou ouvindo...')
			speech = recVoz(r)
			print('Você: ', speech)				
			
			if speech == "pesquisar" or speech == "pesquisar no google" or speech == "pesquisar no Google":
				pesqGoogle()
			elif speech == "traduzir" or speech == "translate" or speech == "Translator":
				traduzir()
			elif speech == "treinar" or speech == "treinar dialogo":
				treinoExtra(bot)
			elif speech == "quinta-feira":
				tts.Speak("Em que posso ajudar?")
				main()
			elif speech == "previsão do tempo para hoje" or speech == "clima":
				time.sleep(2)
				url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp"
				page = rq.get(url=url, timeout=2)
				soup = bs(page.content, 'html.parser')
				content = soup.find(id="tempMin0")
				minima = content.get_text()
				content = soup.find(id="tempMax0")
				maxima = content.get_text()
				content = soup.find(id="content0")
				classe = content.find(class_="small-4 left rain-block")
				prob = classe.get_text()
				content = soup.find(id="content0")
				classe = content.find(class_="left font14 txt")
				descricao = classe.get_text()
				tempo = (u"Minima de "+minima +" e máxima de "+maxima)
				tts.Speak(tempo)
				print(tempo)
				chuva = (u"Probabilidade de "+prob)
				tts.Speak(chuva)
				desc = (u""+descricao)
				tts.Speak(desc)
				print(desc)
				main()
			elif speech == "previsão do tempo para amanhã" or speech == "clima amanhã":
				time.sleep(2)
				url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp"
				page = rq.get(url=url, timeout=2)
				soup = bs(page.content, 'html.parser')
				content = soup.find(id="tempMin1")
				minima = content.get_text()
				content = soup.find(id="tempMax1")
				maxima = content.get_text()
				content = soup.find(id="content1")
				classe = content.find(class_="small-4 left rain-block")
				prob = classe.get_text()
				content = soup.find(id="content1")
				classe = content.find(class_="left font14 txt")
				descricao = classe.get_text()
				tempo = (u"Minima de "+minima +" e máxima de "+maxima)
				tts.Speak(tempo)
				print(tempo)
				chuva = (u"Probabilidade de "+prob)
				tts.Speak(chuva)
				desc = (u""+descricao)
				tts.Speak(desc)
				print(desc)
				main()					
			elif speech == "Ativar modo vigilante":
				ativarModVigilante()
			elif speech == "fechar" or speech == "sair" or speech == "close":					
				print("Encerrando sessão...")
				exit()
			else:
				response = bot.get_response(speech)
				print('Quinta-feira:', response)
				resposta = (u""+str(response))
				tts.Speak(resposta)
				main()		
	except:
		print('Erro de excesão')
		os.system('pause')

if __name__ == "__main__":
	main()
#teste
#teste2
#bugadao
