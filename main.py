import telebot
from telebot import types
from jproperties import Properties
configs = Properties()

with open('token.properties', 'rb') as config_file: configs.load(config_file)

bot = telebot.TeleBot(configs.get("TOKEN"))

@bot.message_handler(commands = ['start'])

def send_welcome(message):
#    if message.text.lower() == '/start':
        begin = types.InlineKeyboardMarkup(row_width=8)
        start = types.InlineKeyboardButton('Начать', callback_data='start')
        begin.add(start)

        bot.send_message(message.chat.id, 'Женщину невозможно понять с двух слов. Поэтому, если вы хотите угадать с подарком для нее, придется немного потрудиться!) Чтобы ответить на вопросы теста, вам понадобиться около 10 минут.', reply_markup=begin)

#         bot.send_message(message.chat.id, 'Предлагаю перейти к делу!)')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'start':
            question1(call.message)
        if call.data == 'girlfriiend' or call.data == 'wife' or call.data == 'sister' or call.data == 'mum' or call.data == 'friend':
            question2(call.message)
        if call.data == 'small' or call.data == 'classic' or call.data == 'great':
            question3(call.message)


def question1(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    girlfriend = types.InlineKeyboardButton('Девушка', callback_data='girlfriiend')
    wife = types.InlineKeyboardButton('Жена', callback_data='wife')
    sister = types.InlineKeyboardButton('Сестра', callback_data='sister')
    mum = types.InlineKeyboardButton('Мама', callback_data='mum')
    friend = types.InlineKeyboardButton('Коллега', callback_data='friend')
    markup.add(girlfriend, wife, sister, mum, friend)

    bot.send_message(message.chat.id, '1. Ее статус', reply_markup=markup)

def question2(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    birthday = types.InlineKeyboardButton('День рождения', callback_data='birthday')
    march = types.InlineKeyboardButton('8 Марта', callback_data='march')
    stValentine = types.InlineKeyboardButton('День Святого Валентина', callback_data='stValentine')
    newYear = types.InlineKeyboardButton('Новый год', callback_data='newYear')
    anniversary = types.InlineKeyboardButton('Годовщина свадьбы', callback_data='anniversary')
    markup.add(birthday, march, stValentine, newYear, anniversary)

    bot.send_message(message.chat.id, '2. Повод', reply_markup=markup)

def question3(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    birthday = types.InlineKeyboardButton('А. День рождения', callback_data='birthday')
    march = types.InlineKeyboardButton('Б. 8 Марта', callback_data='march')
    stValentine = types.InlineKeyboardButton('В. День Святого Валентина', callback_data='stValentine')
    newYear = types.InlineKeyboardButton('Г. Новый год', callback_data='newYear')
    anniversary = types.InlineKeyboardButton('Д. Годовщина свадьбы', callback_data='anniversary')
    markup.add(birthday, march, stValentine, newYear, anniversary)

    bot.send_message(message.chat.id, '2. Повод', reply_markup=markup)

def question3(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    small = types.InlineKeyboardButton('Менее 50$', callback_data='small')
    classic = types.InlineKeyboardButton('50$ - 200$', callback_data='classic')
    great = types.InlineKeyboardButton('Более 200$', callback_data='great')
    markup.add(small, classic, great)

    bot.send_message(message.chat.id, '3. Бюджет подарка', reply_markup=markup)



bot.polling(none_stop= True, interval= 0)
