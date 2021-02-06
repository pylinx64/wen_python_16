import pyttsx3
from datetime import date, datetime, time
import webbrowser

tts = pyttsx3.init()			# включение голосового движка
def say_bot(msg):
	print(msg)
	tts.say(msg)				# собираем фразы
	tts.runAndWait()			# включает голос


say_bot('Привет я ассистент версия 2.0')
while True:
	command = input('Введите команду: ')
	if command == 'Привет':			# Работает если True (Привет есть в command)
		say_bot('Ну привет')
	elif command == 'Как дела':			
		say_bot('Норм')
	elif command == 'время':
		time_checker=datetime.now()
		h=time_checker.hour
		m=time_checker.minute
		say_bot(str(h)+':'+str(m))
	elif command == 'дата':
		time_checker=datetime.now()
		h=time_checker.day
		m=time_checker.month
		say_bot(str(h)+'.'+str(m))
	else:							# Работает если False (Привет нету в command)
		say_bot('Я тебя не понимаю')
	
