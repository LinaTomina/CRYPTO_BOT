import telebot


TOKEN = '1421482627:AAFk8dcgCuVGn4GJV6pL5HMvk3siVL2pnGc'


bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>'
    bot.reply_to(message, text)


 bot.polling() 