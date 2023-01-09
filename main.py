import telebot

Aizat = {
    "пн": "1) 5В\n2) 8Б\n3) 5Б\n4) --\n5) 6А\n6) 6В",
    "вт": "1) 5В\n2) 6А\n3) 6Б\n4) 8Б\n5) 5А\n6) 8А",
    "ср": "1) --\n2) --\n3) --\n4) --\n5) --\n6) --",
    "чт": "1) --\n2) --\n3) 5Б\n4) --\n5) 5В\n6) 6В",
    "пт": "1) 5А\n2) 6Б\n3) 6А\n4) --\n5) 6В\n6) 8А",
    "сб": "1) 8А\n2) 5Б\n3) 5А\n4) 6Б\n5) 8Б\n6) --"
}

LK = {
    "пн": "1) 11\n2) 7Б\n3) 10\n4) 9Б\n5) 4В\n6) 9А",
    "вт": "1) --\n2) --\n3) --\n4) --\n5) --\n6) --",
    "ср": "1) 7В\n2) 9Б\n3) 7А\n4) 4В\n5) 11\n6) 10",
    "чт": "1) --\n2) --\n3) --\n4) 11\n5) --\n6) 7Б",
    "пт": "1) 9А\n2) 7В\n3) --\n4) 4В\n5) 7А\n6) --",
    "сб": "1) 10\n2) 7В\n3) 7Б\n4) 7А\n5) 9Б\n6) 9А"
}

bot = telebot.TeleBot("5779038448:AAGoXtQb2B8LLppFsgRmpgOhNZz-Q3OxZPc")

teacher = []

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Лилия Камилевна")
    btn2 = telebot.types.KeyboardButton("Айзат Рифатович")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я могу скинуть расписание учителей".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_message(message):
    global teacher
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_pn = telebot.types.InlineKeyboardButton(text='Понедельник', callback_data='пн')
    keyboard.add(key_pn)
    key_vt = telebot.types.InlineKeyboardButton(text='Вторник', callback_data='вт')
    keyboard.add(key_vt)
    key_sr = telebot.types.InlineKeyboardButton(text='Среда', callback_data='ср')
    keyboard.add(key_sr)
    key_cht = telebot.types.InlineKeyboardButton(text='Четверг', callback_data='чт')
    keyboard.add(key_cht)
    key_pt = telebot.types.InlineKeyboardButton(text='Пятница', callback_data='пт')
    keyboard.add(key_pt)
    key_sb = telebot.types.InlineKeyboardButton(text='Суббота', callback_data='сб')
    keyboard.add(key_sb)
    if message.text == "Лилия Камилевна":
        teacher = LK
        bot.send_message(message.from_user.id, text="Выбери день недели:", reply_markup=keyboard)
    elif message.text == "Айзат Рифатович":
        teacher = Aizat
        bot.send_message(message.from_user.id, text="Выбери день недели:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    for i in teacher:
        if call.data == i:
            bot.send_message(call.from_user.id, teacher[i])

bot.polling(none_stop=True, interval=0)