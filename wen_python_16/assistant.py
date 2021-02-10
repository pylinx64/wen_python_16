import pyttsx3

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
	
	else:							# Работает если False (Привет нету в command)
		say_bot('Я тебя не понимаю')
	
