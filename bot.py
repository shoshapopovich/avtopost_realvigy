import requests #_______________________ ПОКА НЕ НУЖНО
import time 
import vk_api
import sqlite3 #________________________ ПОКА НЕ НУЖНО
import asyncio
import logging
import telebot
import aiogram

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from vkbottle import Callback, GroupEventType, GroupTypes, Keyboard, ShowSnackbarEvent, TemplateElement, template_gen, Text, KeyboardButtonColor
from vkbottle.bot import Bot as Boot
from vkbottle.bot import Message
from vkbottle.modules import json #_____________________ ПОКА НЕ НУЖНО

bot = Boot(token="vk1.a.Eit-xI-wnoFpRdB0PyDeknTX7q97IDhAJxiYjhLm5kXSJp_Q4cgP6ut5kVmY5KPa0BBKUT3tDOzGI_BSlWbQkPw20quI5h5Re96Kycrl5cerVqVRDnxBHPfUMBulzQHS3YlgB69y4I-LStowV1qOVu1ZpDKTNGr4V_mbOh9wgRzGNqkR7ou01GHzCuil3pyI")
vk_session = vk_api.VkApi(token='vk1.a.Eit-xI-wnoFpRdB0PyDeknTX7q97IDhAJxiYjhLm5kXSJp_Q4cgP6ut5kVmY5KPa0BBKUT3tDOzGI_BSlWbQkPw20quI5h5Re96Kycrl5cerVqVRDnxBHPfUMBulzQHS3YlgB69y4I-LStowV1qOVu1ZpDKTNGr4V_mbOh9wgRzGNqkR7ou01GHzCuil3pyI') 
vk = vk_session.get_api() 

TOOKEN = '5486302592:AAEaZGA6bJ2e5t4TyTtOBYBC_X9uL0tXe9U'

bot1 = Bot(token=TOOKEN)
dp = Dispatcher(bot1) 

tme = telebot.TeleBot(TOOKEN)


@bot.on.raw_event(GroupEventType.WALL_POST_NEW, dataclass=GroupTypes.WallPostNew)
async def handle_message_event(event: GroupTypes.WallReplyNew):
    global bot1

    post_id=event.object.id
    post_text=event.object.text
    post_istok=event.object.copyright
    post_donut=event.object.donut.is_donut
    print(post_istok, post_donut)

    
    if post_istok == None:
        if post_donut == False:
            try: 
                try: 
                    s1 = event.object. attachments[0].photo.sizes[1].height
                except:
                    print('такого размера нет')   
                    s1 = 0 

                try: 
                    s2 = event.object.attachments[0].photo.sizes[2].height
                except:
                    print('такого размера нет')    
                    s2 = 0
                try: 
                    s3 = event.object.attachments[0].photo.sizes[3].height
                except:
                    print('такого размера нет')    
                    s3 = 0
                try: 
                    s4 = event.object.attachments[0].photo.sizes[4].height
                except:
                    print('такого размера нет')    
                    s4 = 0        
                try: 
                    s5 = event.object.attachments[0].photo.sizes[5].height
                except:
                    print('такого размера нет')    
                    s5 = 0
                try: 
                    s6 = event.object.attachments[0].photo.sizes[6].height
                except:
                    print('такого размера нет') 
                    s6 = 0           
                try: 
                    s7 = event.object.attachments[0].photo.sizes[7].height
                except:
                    print('такого размера нет')    
                    s7 = 0
                sizes = {"1":s1, "2":s2, "3":s3, "4":s4, "5":s5, "6":s6, "7":s7}

                good_size=max(sizes, key=sizes.get)
                print(good_size)

                if good_size == '1':
                    photo=event.object.attachments[0].photo.sizes[1].url
                else: 
                    print('не то1')
                if good_size == '2':
                    photo=event.object.attachments[0].photo.sizes[2].url
                else: 
                    print('не то2')
             
                if good_size == '3':
                    photo=event.object.attachments[0].photo.sizes[3].url
                else: 
                    print('не то3')
             
                if good_size == '4':
                    photo=event.object.attachments[0].photo.sizes[4].url
                else: 
                    print('не то4')
             
                if good_size == '5':
                    photo=event.object.attachments[0].photo.sizes[5].url
                else: 
                    print('не то5')
             
                if good_size == '6':
                    photo=event.object.attachments[0].photo.sizes[6].url
                else: 
                    print('не то6')
             
                if good_size == '7':
                    photo=event.object.attachments[0].photo.sizes[7].url
                else: 
                    print('не то7')
             

                print(photo)

                r = requests.get(photo, allow_redirects=True)   #получение результа для закачки фото на комп

                photka = 'post_{}.jpg'.format(post_id)      # закачка фотки на комп

                open(photka, 'wb').write(r.content) 


                with open('post_{}.jpg'.format(post_id), 'rb') as photo:
                    await bot1.send_photo(-1001604641351, photo, caption = post_text) # ЗАМЕСТО -1001604641351 ПОСТАВЬ ID СВОЕГО КАНАЛА И СДЕЛАЙ БОТА АДМИНОМ В КАНАЛЕ
            except: 
                await bot1.send_message(-1001604641351, post_text)        # ЗАМЕСТО -1001604641351 ПОСТАВЬ ID СВОЕГО КАНАЛА И СДЕЛАЙ БОТА АДМИНОМ В КАНАЛЕ
    else:
        print('Пост рекламный или какая то другая ошибка')





bot.run_forever()
