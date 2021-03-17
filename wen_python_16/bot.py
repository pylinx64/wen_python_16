import telebot

bot = telebot.TeleBot('1619506853:AAG29EDn_qKFkdHQSKCNw0gWnkYC_anS-HQ')	# сюда токен

@bot.message_handler(commands=['start'])
def text_start(message):
	'''Принимает команду старт и отвечает на нее'''
	bot.send_message(message.chat.id, 'Привет! Я ретро бот с ретро картинками')
	print(message.chat.first_name, message.text)
	
	
@bot.message_handler(content_types=['text'])
def text_bot(message):	
	'''Принимает текстовые сообщения и отправляет ответ'''
	if message.text == 'привет':
		bot.send_message(message.chat.id, 'привет!')
	elif message.text == 'как дела':
		bot.send_message(message.chat.id, 'нормально')
	else:
		bot.send_message(message.chat.id, 'я не распознаю такой команды')
	

print('# start bot ...')	
bot.polling()
print('# stop bot ...')
