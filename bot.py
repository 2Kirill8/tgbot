import telebot
import types
token='8264047223:AAEmWAWulxVxmPKTxcp96RDjZdWL0kLyLos'
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
  bot.send_message(message.chat.id,"Привет, я бот который поможет тебе с формулами ", reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
  if call.data == "math":
     markup = telebot.types.InlineKeyboardMarkup()
     btn1 = telebot.types.InlineKeyboardButton('ОГЭ',callback_data='oge_math')
     btn2 = telebot.types.InlineKeyboardButton('ЕГЭ',callback_data='ege_math')
     markup.add(btn1)
     markup.add(btn2)
     bot.send_message(call.message.chat.id,"Выберите тип экзамена", reply_markup=markup)



  if call.data == "oge_math":
      markup1 = telebot.types.InlineKeyboardMarkup()
      btn11 = telebot.types.InlineKeyboardButton('Алгебра',callback_data='oge_algeb')
      btn21 = telebot.types.InlineKeyboardButton('Геометрия',callback_data='oge_geom')
      markup1.add(btn11)
      markup1.add(btn21)
      bot.send_message(call.message.chat.id,"Выберите предмет", reply_markup=markup1)


  if call.data == "ege_math":
      markup2 = telebot.types.InlineKeyboardMarkup()
      btn12= telebot.types.InlineKeyboardButton('Алгебра', callback_data='ege_algeb')
      btn22 = telebot.types.InlineKeyboardButton('Геометрия',callback_data='ege_geom')
      markup2.add(btn12)
      markup2.add(btn22)
      bot.send_message(call.message.chat.id,"Выберите предмет", reply_markup=markup2)




     
  if call.data == "physics":
     markup = telebot.types.InlineKeyboardMarkup()
     btn1 = telebot.types.InlineKeyboardButton('ОГЭ',callback_data='oge_physics')
     btn2 = telebot.types.InlineKeyboardButton('ЕГЭ',callback_data='ege_physics')
     markup.add(btn1)
     markup.add(btn2)
     bot.send_message(call.message.chat.id,"Выберите тип экзамена", reply_markup=markup)





  if call.data == "inf":
     markup = telebot.types.InlineKeyboardMarkup()
     btn1 = telebot.types.InlineKeyboardButton('ОГЭ',callback_data='oge_inf')
     btn2 = telebot.types.InlineKeyboardButton('ЕГЭ',callback_data='ege_inf')
     markup.add(btn1)
     markup.add(btn2)
     bot.send_message(call.message.chat.id,"Выберите тип экзамена", reply_markup=markup)




bot.polling()

