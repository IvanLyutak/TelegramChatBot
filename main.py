import telebot

bot = telebot.TeleBot()

@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы стать лучшим!".format(message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(content_types=["text"])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
