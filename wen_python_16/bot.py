import telebot
import random

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
	
	
@bot.message_handler(content_types=['sticker'])
def sticker_bot(message):
	'''Принимает стикер и отвечает на него'''
	#print(message.sticker.file_id)
	stickers = ['CAACAgIAAxkBAAMNYFtYqsmr0aW9xg3RtBR4Y6fBNQgAAh8AA8A2TxPkODP3hFKZkh4E',
	'CAACAgIAAxkBAAMNYFtYqsmr0aW9xg3RtBR4Y6fBNQgAAh8AA8A2TxPkODP3hFKZkh4E', ]
	
	one_sticker = random.choice(stickers)
	
	bot.send_sticker(message.chat.id, one_sticker)
	

print('# start bot ...')	
bot.polling()
print('# stop bot ...')
