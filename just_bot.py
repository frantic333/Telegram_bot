import telebot

bot = telebot.TeleBot('5336339417:AAEH7GPkGfOBAhIDavBtWJJLWdK7Ae1bN3I')

@bot.message_handler(commands=['start'])
def start(message):
#    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


bot.polling(none_stop=True)