import telebot
import types
import os 
token=os.getenv("BOT_TOKEN")
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  markup =   telebot.types.InlineKeyboardMarkup()
  btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
  btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
  btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
  markup.add(btn1)
  markup.add(btn2)
  markup.add(btn3)
  bot.send_message(message.chat.id,"Здравствуйте! Я бот-помощник для работы с формулами. Чем могу помочь? ", reply_markup=markup)
  bot.send_message(message.chat.id,"Инструкция: /help")

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
  if call.data == "math":
     markup = telebot.types.InlineKeyboardMarkup()
     btn1 = telebot.types.InlineKeyboardButton('ОГЭ',callback_data='oge_math')
     btn2 = telebot.types.InlineKeyboardButton('ЕГЭ',callback_data='ege_math')
     markup.add(btn1)
     markup.add(btn2)
     bot.send_message(call.message.chat.id,"Чтобы я мог помочь вам с подготовкой, уточните ваш экзамен ОГЭ (9 класс) | ЕГЭ (11 класс)", reply_markup=markup)



  if call.data == "oge_math":
      markup1 = telebot.types.InlineKeyboardMarkup()
      btn11 = telebot.types.InlineKeyboardButton('Алгебра',callback_data='oge_algeb')
      btn21 = telebot.types.InlineKeyboardButton('Геометрия',callback_data='oge_geom')
      markup1.add(btn11)
      markup1.add(btn21)
      bot.send_message(call.message.chat.id,"Выберите предмет", reply_markup=markup1)

  if call.data == "oge_algeb":
     photo = open("algeb.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()


     photo1 = open("algeb32.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo1)
     photo1.close()


     photo2 = open("algeb33.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo2)
     photo2.close()


     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)




  if call.data == "oge_geom":
     photo = open("geom.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()
     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)



     

  if call.data == "ege_math":
      markup2 = telebot.types.InlineKeyboardMarkup()
      btn12= telebot.types.InlineKeyboardButton('Алгебра', callback_data='ege_algeb')
      btn22 = telebot.types.InlineKeyboardButton('Геометрия',callback_data='ege_geom')
      markup2.add(btn12)
      markup2.add(btn22)
      bot.send_message(call.message.chat.id,"Выберите предмет", reply_markup=markup2)



  if call.data == "ege_algeb":
     photo = open("algeb22.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()

     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)



  if call.data == "ege_geom":
     photo = open("geom22.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()


     photo1 = open("geom23.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo1)
     photo1.close()

     photo2 = open("geom24.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo2)
     photo2.close()

     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)




     
  if call.data == "physics":
     markup = telebot.types.InlineKeyboardMarkup()
     btn1 = telebot.types.InlineKeyboardButton('ОГЭ',callback_data='oge_physics')
     btn2 = telebot.types.InlineKeyboardButton('ЕГЭ',callback_data='ege_physics')
     markup.add(btn1)
     markup.add(btn2)
     bot.send_message(call.message.chat.id,"Выберите тип экзамена", reply_markup=markup)

  if call.data == "oge_physics":
     photo = open("phyz.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()
     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)






     
  if call.data == "ege_physics":
     photo = open("phyz2.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()


     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)










  if call.data == "inf":
     markup = telebot.types.InlineKeyboardMarkup()
     btn1 = telebot.types.InlineKeyboardButton('ОГЭ',callback_data='oge_inf')
     btn2 = telebot.types.InlineKeyboardButton('ЕГЭ',callback_data='ege_inf')
     markup.add(btn1)
     markup.add(btn2)
     bot.send_message(call.message.chat.id,"Выберите тип экзамена", reply_markup=markup)


  if call.data == "ege_inf":
     photo = open("inf.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()

     photo1 = open("inf22.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo1)
     photo1.close()

     photo2 = open("inf23.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo2)
     photo2.close()


     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)




  if call.data == "oge_inf":
     photo = open("inf1.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo)
     photo.close()
     photo2 = open("inf2.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo2)
     photo2.close()
     photo3 = open("inf3.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo3)
     photo3.close()
     photo4 = open("inf4.jpeg", "rb")
     bot.send_photo(call.message.chat.id, photo4)
     photo4.close()

     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)



  if call.data == "help":
     text = (f"Как пользоваться ботом:\n"
     f"1.Выберите предмет: математику, физику или информтику\n"
     f"2.Выберите экзамен:огэ или егэ\n"
     f"3.Для возвращения инструкции нажмите /help")
     bot.send_message(call.message.chat.id,text)


     markup =   telebot.types.InlineKeyboardMarkup()
     btn1 =   telebot.types.InlineKeyboardButton('формулы по математике', callback_data="math")
     btn2 =   telebot.types.InlineKeyboardButton('формулы по физике', callback_data="physics")
     btn3 =   telebot.types.InlineKeyboardButton('формулы по информатике', callback_data="inf")
     markup.add(btn1)
     markup.add(btn2)
     markup.add(btn3)
     bot.send_message(call.message.chat.id," Может я могу помочь чем-то еще? ", reply_markup=markup)




@bot.message_handler(commands=['help'])
def start_message(message):
    markup =   telebot.types.InlineKeyboardMarkup()
    btn1 =   telebot.types.InlineKeyboardButton('если вам нужна помощь жмите сюда', callback_data="help")
    markup.add(btn1)
    bot.send_message(message.chat.id,"Инструкция ", reply_markup=markup)

bot.polling()

