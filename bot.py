import time
from threading import Thread
import vk_api   
import json # помоему эта библиотека вообще лишняя, похуй оставлю пока
import requests
#from config import token 
# можно через конфиг, но мне лень
import asyncio
import logging
import telebot
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# токены токены токены токеын тоыкеокын_______________________________________

TOOKEN = '5486302592:AAEaZGA6bJ2e5t4TyTtOBYBC_X9uL0tXe9U'

bot = Bot(token=TOOKEN)
dp = Dispatcher(bot)

vk_session = vk_api.VkApi(token='vk1.a.U4WrZvqX1H5OwA-F_0ArkiHCQPEhKquPzpOPAIvkZT4ODeS4SSezl4KVl5MfBYZpAewo4PkoUYbLHkb-mzjeu3a8BilMiFXdX0z2TW_uUT1VlFAhCtEqz2kLBo-PnxKZEF5_R7OQFw4c58ZWN2NxNO_t4kghxboRq0mPFu8URh3FpG9u-7lEBgWtVlvlAdon')

vk = vk_session.get_api() 

tme = telebot.TeleBot(TOOKEN)

#важные переменные______________________________________________________

offst = 1 #оффсет - отступ в поиске поста. в данном случае я скипаю отступом в 1 штучку пост с закрепом

idshka0 = '-198130632' # id группы из которой воруются посты.

idshka1 = '-185529179' # id группы из которой воруются посты.

idshka2 = '-187540358' # id группы из которой воруются посты.

grp = 1  # количество груп, с которых будут вороваться посты  (максимум можно 3, но можно дописать до скольки хочешь в коде)

cont = 1 # количество получаемых постов за 1 присест. можно сделать до 100 штук, но мне удобней чтобы разобраться, получать 1 пост за 1 запрос

spemr = 0   # хз че это, но без неё программа не работает

albom = 283616455  # id альбома, в котором будет сохраняться фотка НАДО ПОМЕНЯТЬ НА GETUPLOADSERVER  ___________________

group = 212562082  # id группы в которой находится альбом  НАДО ПОМЕНЯТЬ НА GETUPLOADSERVER ________________________

owner = -212562082  # id группы, в которую будет идти пост 

# забей ____________________________

vremya = time.strftime(" %H:%M ") 

vremya_cicl = 2

mes1 = 0

mes2 = 0

mes3 = 0

mes4 = 0

mes5 = 0

# timer1 = 'None'

# timer2 = 'None'

# timer3 = 'None'

tim1 = 0

tim = 0


#______________________________________________________

# keyboard = types.InlineKeyboardMarkup(row_width=2) 
# keyboard.add(types.InlineKeyboardButton(text="Погнали", callback_data="pizdi"), types.InlineKeyboardButton(text="Потом", callback_data="potom"))


# уведомления_______________
def remind():
    global keyboard, button_1
    while vremya_cicl == 2:
        time.sleep(50)

        vremya = time.strftime("%H:%M")
        print(vremya)
        if vremya == '05:45' or vremya == '05:50' or  vremya == '05:55' or vremya == '11:45' or vremya == '11:50' or  vremya == '11:55':       # тут ставить уведомления
            print('ащворщвыазпыл')
            tme.send_message(1958637050, 'На часах {} \nвремя воровать пост'.format(vremya))
            tme.send_message(783914894, 'На часах {} \nвремя воровать пост'.format(vremya))            


#запуск этой штуки в ассинхроне
th = Thread(target=remind, args=())
th.start()

#_______________________________________

@dp.callback_query_handler(text="potom")
async def call_main_menu(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.message_handler(commands="margramloh")
@dp.message_handler(Text(equals='Меню'))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='Пизди мемы')
    keyboard.add(button_1)
    # button_2 = types.KeyboardButton(text='⚙️')
    # keyboard.add(button_2)
    await message.answer('Пиздить - кнопака " Пизди мемы"', reply_markup=keyboard)


print('\n \n \n Время запуска программы: {} \n \n \n'.format(vremya))

# # настройки времени


# @dp.message_handler(Text(equals='⚙️'))
# @dp.message_handler(Text(equals='Назад'))
# async def call_main_menu(message: types.Message):
#     global tim, tim1
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     keyboard.add(types.InlineKeyboardButton(text=timer1, callback_data="time1"), types.InlineKeyboardButton(text=timer2, callback_data="time2"), types.InlineKeyboardButton(text=timer3, callback_data="time3"))  
#     tim = await message.answer('Настройка времени',  reply_markup=keyboard)        
#     tim1 = tim.message_id


# @dp.callback_query_handler(text="time1")
# async def call_main_menu(call: types.CallbackQuery):  
#     await bot.edit_message_text(
#         chat_id=call.from_user.id,
#         message_id=tim1,
#         text="Для установки первого таймера напиши \n /stime1 и время в формате HH:MM \n \nпример /stime1 04:20")


# @dp.callback_query_handler(text="time2")
# async def call_main_menu(call: types.CallbackQuery): 
#     await bot.edit_message_text(
#         chat_id=call.from_user.id,
#         message_id=tim1,
#         text='Для установки второго таймера напиши \n /stime2 и время в формате HH:MM \n \nпример /stime2 04:20')

# @dp.callback_query_handler(text="time3")
# async def call_main_menu(call: types.CallbackQuery): 
#     await bot.edit_message_text(
#         chat_id=call.from_user.id,
#         message_id=tim1,
#         text="Для установки третьего таймера напиши \n /stime3 и время в формате HH:MM \n \nпример /stime3 04:20")

# @dp.message_handler(Text(equals="/stime3 <v3>"))
# async def call_main_menu(message: types.Message, v3):
#     print('dfgjsdflgksdf', v3)

msg = 0  # так надо


@dp.message_handler(Text(equals='''Пизди мемы'''))

async def with_puree(message: types.Message):
    global idshka0, idshka2, idshka2, idd, vk_session, grp, mes1, mes2, mes3, mes4, mes5,  mes6, mes7, mes8, mes9, mes10, mes11, mes12, mes13, mes14, mes15


    


    photo_nom = 1

    idshka = idshka0
    
    # прога чето выёбывалась, поэтому я продублировал переменные сюда
    # все важные переменные я перенёс наверх

    vk = vk_session.get_api()


    
    offst = 1 #оффсет - отступ. в данном случае я скипаю отступом в 1 штучку пост с закрепом

    # idshka = '-182035619' # id группы с которой будут вороваться посты.  в данном случае @wemew

    cont = 1 

    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1

                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1



    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print(' \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print(' \n', 'РЕЗУЛЬТ', result, ' \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1

    print('Было найдено {} постов'.format(photo_nom))
                  
    ChatId = message.chat.id
    phot = open('photochka 1.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg1 = await bot.send_photo(ChatId, photo = phot, reply_markup=keyboard )
    mes1 = msg1.message_id

    ChatId = message.chat.id
    phot1 = open('photochka 2.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti1"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg2 = await bot.send_photo(ChatId, photo = phot1, reply_markup=keyboard )
    mes2 = msg2.message_id

    ChatId = message.chat.id
    phot2 = open('photochka 3.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti2"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg3 = await bot.send_photo(ChatId, photo = phot2, reply_markup=keyboard )
    mes3 = msg3.message_id

    ChatId = message.chat.id
    phot3 = open('photochka 4.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti3"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg4 = await bot.send_photo(ChatId, photo = phot3, reply_markup=keyboard )
    mes4 = msg4.message_id

    ChatId = message.chat.id
    phot = open('photochka 5.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti4"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg5 = await bot.send_photo(ChatId, photo = phot, reply_markup=keyboard )
    mes5 = msg5.message_id



    yved = 0

    photo_nom = photo_nom

    if photo_nom <= 10 and photo_nom >4:
        yved = 'постов'

    if photo_nom > 1 and photo_nom < 5:
        yved = 'поста' 

    if photo_nom == 1:
        yved = 'пост' 

    yved1 = photo_nom

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Спасибо", callback_data="spasibo"), types.InlineKeyboardButton(text="Отмена", callback_data="delet"))
    #await bot.send_message(message.from_user.id, 'Были отправлены последние {} {}, за исключением закрепа и текстовых постов'.format(yved1, yved),  reply_markup=keyboard)




    idshka = idshka1
    

    
    offst = 1 #оффсет - отступ. в данном случае я скипаю отступом в 1 штучку пост с закрепом

    # idshka = '-182035619' # id группы с которой будут вороваться посты.  в данном случае @wemew

    cont = 1 

    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1

                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1



    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print(' \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print(' \n', 'РЕЗУЛЬТ', result, ' \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1

    print('Было найдено {} постов'.format(photo_nom))
                  
    ChatId = message.chat.id
    phot = open('photochka 6.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti5"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg1 = await bot.send_photo(ChatId, photo = phot, reply_markup=keyboard )
    mes6 = msg1.message_id

    ChatId = message.chat.id
    phot1 = open('photochka 7.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti6"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg2 = await bot.send_photo(ChatId, photo = phot1, reply_markup=keyboard )
    mes7 = msg2.message_id

    ChatId = message.chat.id
    phot2 = open('photochka 8.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti7"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg3 = await bot.send_photo(ChatId, photo = phot2, reply_markup=keyboard )
    mes8 = msg3.message_id

    ChatId = message.chat.id
    phot3 = open('photochka 9.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti8"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg4 = await bot.send_photo(ChatId, photo = phot3, reply_markup=keyboard )
    mes9 = msg4.message_id

    ChatId = message.chat.id
    phot = open('photochka 10.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti9"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg5 = await bot.send_photo(ChatId, photo = phot, reply_markup=keyboard )
    mes10 = msg5.message_id



    yved = 0

    photo_nom = photo_nom

    if photo_nom <= 10 and photo_nom >4:
        yved = 'постов'

    if photo_nom > 1 and photo_nom < 5:
        yved = 'поста' 

    if photo_nom == 1:
        yved = 'пост' 

    yved1 = photo_nom

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Спасибо", callback_data="spasibo"), types.InlineKeyboardButton(text="Отмена", callback_data="delet"))
    #await bot.send_message(message.from_user.id, 'Были отправлены последние {} {}, за исключением закрепа и текстовых постов'.format(yved1, yved),  reply_markup=keyboard)
        
    idshka = idshka2
    
    # прога чето выёбывалась, поэтому я продублировал переменные сюда
    # все важные переменные я перенёс наверх

    vk = vk_session.get_api()


    
    offst = 1 #оффсет - отступ. в данном случае я скипаю отступом в 1 штучку пост с закрепом

    # idshka = '-182035619' # id группы с которой будут вороваться посты.  в данном случае @wemew

    cont = 1 

    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1

                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1



    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1


    posting = vk.wall.get(owner_id=idshka,offset=offst,count=cont)   # запрос на сервер для получения поста со стенки

    #print(posting, '  \n')  # можно убрать. я для себя делал вывод после каждого действия

    try:
        result = posting['items'][0]['attachments'][0]['photo']['sizes'][8]['url']

        r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

        photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

        open(photka, 'wb').write(r.content)         # закачка фотки на комп

        print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

        offst = offst+1
        photo_nom = photo_nom+1

    except KeyError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][1]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except KeyError:
          print(' \nпост текстовый, скипаем \n')

          offst = offst+1

    except IndexError:

        try:
         result = posting['items'][0]['attachments'][0]['photo']['sizes'][6]['url']

         r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

         photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

         open(photka, 'wb').write(r.content)         # закачка фотки на комп

         print('  \n', 'РЕЗУЛЬТ', result, '  \n')          

         offst = offst+1
         photo_nom = photo_nom+1

        except IndexError:
          try:
             result = posting['items'][0]['attachments'][0]['photo']['sizes'][5]['url']

             r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

             photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

             open(photka, 'wb').write(r.content)         # закачка фотки на комп

             print(' \n', 'РЕЗУЛЬТ', result, '  \n')          

             offst = offst+1
             photo_nom = photo_nom+1

          except IndexError:
                try:
                  result = posting['items'][0]['attachments'][0]['photo']['sizes'][4]['url']

                  r = requests.get(result, allow_redirects=True)   #получение результа для закачки фото на комп

                  photka = 'photochka {}.jpg'.format(photo_nom)      # закачка фотки на комп

                  open(photka, 'wb').write(r.content)         # закачка фотки на комп

                  print(' \n', 'РЕЗУЛЬТ', result, ' \n')          

                  offst = offst+1
                  photo_nom = photo_nom+1
                  
                except IndexError:
                  print('там фотка шакальная, скипаем')

                  offst = offst+1

    print('Было найдено {} постов'.format(photo_nom))
                  
    ChatId = message.chat.id
    phot = open('photochka 11.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti10"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg1 = await bot.send_photo(ChatId, photo = phot, reply_markup=keyboard )
    mes11 = msg1.message_id

    ChatId = message.chat.id
    phot1 = open('photochka 12.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti11"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg2 = await bot.send_photo(ChatId, photo = phot1, reply_markup=keyboard )
    mes12 = msg2.message_id

    ChatId = message.chat.id
    phot2 = open('photochka 13.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti12"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg3 = await bot.send_photo(ChatId, photo = phot2, reply_markup=keyboard )
    mes13 = msg3.message_id

    ChatId = message.chat.id
    phot3 = open('photochka 14.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti13"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg4 = await bot.send_photo(ChatId, photo = phot3, reply_markup=keyboard )
    mes14 = msg4.message_id

    ChatId = message.chat.id
    phot = open('photochka 15.jpg', 'rb') 
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Пости ✅", callback_data="posti14"), types.InlineKeyboardButton(text="Нахуй ❌", callback_data="ne_posti"))
    msg5 = await bot.send_photo(ChatId, photo = phot, reply_markup=keyboard )
    mes15 = msg5.message_id



    # yved = 0

    # photo_nom = photo_nom

    # if photo_nom <= 10 and photo_nom >4:
    #     yved = 'постов'

    # if photo_nom > 1 and photo_nom < 5:
    #     yved = 'поста' 

    # if photo_nom == 1:
    #     yved = 'пост' 

    yved1 = photo_nom

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add( types.InlineKeyboardButton(text="Очистка", callback_data="delet"))
    await bot.send_message(message.from_user.id, 'Готово',  reply_markup=keyboard)

    


@dp.callback_query_handler(text="posti")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 1.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti1")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 2.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)
 

@dp.callback_query_handler(text="posti2")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 3.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti3")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 4.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti4")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 5.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)
 



@dp.callback_query_handler(text="posti5")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 6.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti6")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 7.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)
 

@dp.callback_query_handler(text="posti7")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 8.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti8")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 9.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti9")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 10.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)
 



@dp.callback_query_handler(text="posti10")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 11.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti11")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 12.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)
 

@dp.callback_query_handler(text="posti12")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 13.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti13")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 14.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)

@dp.callback_query_handler(text="posti14")
async def send_random_value(call: types.CallbackQuery):
    

    with open('photochka 15.jpg', 'rb') as photo:
        await bot.send_photo(-1001604641351, photo)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Ок", callback_data="spasibo"))  
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Картинка опубликована',  reply_markup=keyboard)
 



@dp.callback_query_handler(text="ne_posti")
async def call_main_menu(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
@dp.callback_query_handler(text="spasibo")
async def call_main_menu(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="delet")
async def call_main_menu(call: types.CallbackQuery):
    global mes1
    print(mes1, mes2, mes3, mes4, mes5)
    try:
         await bot.delete_message(chat_id=call.from_user.id, message_id=mes1)
    except:   
        print('сообщения нет') 
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes2)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes3)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes4)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes5)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes6)
    except:   
        print('сообщения нет') 
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes7)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes8)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes9)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes10)
    except:
        print('сообщения нет') 
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes11)
    except:   
        print('сообщения нет') 
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes12)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes13)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes14)
    except:
        print('сообщения нет')
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes15)
    except:
        print('сообщения нет')        
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    except:
        print('сообщения нет')
    mes1 = mes1-1
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=mes1)
    except:
        print('сообщения нет')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
