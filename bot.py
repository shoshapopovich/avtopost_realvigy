import asyncio
import requests
import random
import json
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
from bs4 import BeautifulSoup

# Переменные
group_id = '182035619'
secret = '4efd20464d780d238e61568222678b9beea0d8c25f6bba1d386567a45937202dca5133a8fa08fabd43d71'
ya = 'doc381260583_611979108'
ya2 = 'photo381260583_457378962'
ya4 = 'audio-2001213818_80213818'
bot_token = secret
bot_group_id = group_id
vk = Bot(bot_token, bot_group_id)

#анеки

async def get_joke():
    joke_html = requests.get('https://nekdo.ru/random/').text
    joke_text = BeautifulSoup(joke_html, 'lxml').find('div', class_='text').get_text()

    return joke_text

@vk.on.private_message(text='ещё')
async def joke(message: Message):
    text = await get_joke()
    await message.answer(message= text)

@vk.on.private_message(text=('анекдот','Анекдот','анек','Анек','шутка','Шутка',''))
async def joke(message: Message):
    text = await get_joke()
    await message.answer(message= text,
keyboard = (
            Keyboard(one_time = True, inline = False)
            .add(Text('еще', payload={'cmd': 'esheanek'}), color=KeyboardButtonColor.POSITIVE)
          
  .row()
       
            .add(Text('хватит', payload={'cmd': 'komandi'}))
            )
    )


@vk.on.private_message(payload={'cmd':'esheanek'})
async def esheanek(message: Message):
    text = await get_joke()
    await message.answer(message= text,
      keyboard = (
            Keyboard(one_time = True, inline = False)
            .add(Text('еще', payload={'cmd': 'esheanek'}), color=KeyboardButtonColor.POSITIVE)
          
  .row()
            .add(Text('хватит', payload={'cmd': 'komandi'}))
            ))


@vk.on.private_message(payload={'cmd': 'aneki'})
async def joke(message: Message):
    text = await get_joke()
    await message.answer(message= text,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('ещё'), color=KeyboardButtonColor.POSITIVE)
          
  .row()
            .add(Text('ой в пизду', payload={'cmd': 'prikol'}))
            )
    )



@vk.on.private_message(text=('хватит'))
async def file(message: Message):
	await message.answer(' ')



@vk.on.private_message(text=('/бред'))
async def file(message: Message):
	await message.answer('пока что не работает :(')
#Меня можно добавить в беседу и я буду отправлять сообщения, сгенерированные на основе написаных в чате это будет просто набор слов, но должно получиться прикольно \nЧтобы включить эту функцию не надо прописывать команды, достаточно добавить бота в беседу и выдать админку \nбред включится сам и его нельзя будет выключить (пока что) \nбред будет генерироваться с шансом в 10% \n \n ВНИМАНИЕ: в личке эта функция не работает, только в беседе')
			     

# Приветствие

# Есть 3 типа - private_message - ожидание\ответ только в личные сообщения группы!
# chat_message - ожидание\ответ только в беседе!
# message - ожидание\ответ и в беседе и в личные сообщения!

@vk.on.private_message(text=['Начать', 'Ку', 'Привет','начать', 'ку', 'привет','Ку','здарова','Здарова','прив','Прив','здаров','Здаров',])
# Сама функция:
async def privet(message: Message):
	# Ответ на сообщение
	await message.answer(
message = '    здарова шелуха 😎 \nНапиши "команды" чтоб узнать что я могу'
)

@vk.on.private_message(text=['команды','Команды','комы','rjvfyls','Rjvfyls','Комы'])
@vk.on.private_message(payload={'cmd': 'komandi'})
# Сама функция:
async def privet(message: Message):
	# Ответ на сообщение
	await message.answer(
message = 'Че я могу \n \n💦Напиши "хентай" и я пришлю тебе аниме тяночку \n🥵Напиши "анекдот" и я расскажу тебе анекдот \n😈Напиши "авка", чтобы получить аватарочку  \n🌏Напиши "музыка", чтобы получить рандомную песню \n🔥Напиши "видео" и я отправлю тебе смешной видосик \n🤡Напиши "меню", чтобы переключиться с текстовой версии бота на кнопочки  '
)

#\n💦Напиши "демотиватор" чтобы я сделал тебе демотиватор \n💅Добавь меня в беседу и я буду отправлять демотиваторы и писать всякий бред \n(подробнее: /дембеседа /бред) \n демотиваторы пока что не работают :(
	
#😍🥶🥸💅🥵😈🌏🔥💦🧐🤡

# ХЕНТААААААААААААААААААААААААААА

hentai1 = 'photo-212149787_457239097'
hentai2 = 'photo-212149787_457239098'
hentai3 = 'photo-212149787_457239099'
hentai4 = 'photo-212149787_457239100'
hentai5 = 'photo-212149787_457239101'
hentai6 = 'photo-212149787_457239102'
hentai7 = 'photo-212149787_457239103'
hentai8 = 'photo-212149787_457239104'
hentai9 = 'photo-212149787_457239105'
hentai10 = 'photo-212149787_457239106'
hentai11 = 'photo-212149787_457239107'
hentai12 = 'photo-212149787_457239108'
hentai13 = 'photo-212149787_457239109'
hentai14 = 'photo-212149787_457239110'
hentai15 = 'photo-212149787_457239111'
hentai16 = 'photo-212149787_457239112'
hentai17 = 'photo-212149787_457239113'
hentai18 = 'photo-212149787_457239114'
hentai19 = 'photo-212149787_457239115'
hentai20 = 'photo-212149787_457239116'



hent = [hentai1, hentai2, hentai3, hentai4, hentai5, hentai6, hentai7, hentai8, hentai9, hentai10, hentai11, hentai12, hentai13, hentai14, hentai15, hentai16, hentai17, hentai18, hentai19, hentai20 ]



@vk.on.private_message(text=['хентай','хент','порнр','ХЕНТАЙ','[tynfq','Хентай','порнуха','хентыч'])
async def video(message: Message):
    
    await message.answer(attachment = random.choice(hent), state = random.getstate())
    #await message.answer(message = 'это всё хуйня ещё \nу нас появилась телега, где таких тонна 0_0 \nvigyviger наберите в тележечке')


# Дембеседа
@vk.on.private_message(text=('/дембеседа'))
async def file(message: Message):
	await message.answer('демотиваторы пока что не работают :(')


# Видео 
vid1='video-182035619_456239750'
vid2='video-182035619_456239499'
vid3='video-182035619_456239771'
vid4='video-182035619_456239770'
vid5='video-182035619_456239752'
vid6='video-182035619_456239749'
vid7='video-182035619_456239748'
vid=[vid1,vid2,vid3,vid4,vid5,vid6,vid7,]
@vk.on.private_message(text=('видео','Видео','видос','видосы','Видос','Видосы'))
async def video(message: Message):
	await message.answer('Держи епто', random.choice(vid), state = random.getstate())

# Музыка
mus1='audio-2001213818_80213818'
mus2='audio-419524347_456242574'
mus3='audio-2001419757_54419757'
mus4='audio-2001510307_56510307'
mus5='audio-2001512024_80512024'
mus6='audio-2001071494_63071494'
mus=[mus1,mus2,mus3,mus4,mus5]
@vk.on.private_message(text=('музыка','Музыка','Музло','музло','Музон','музон'))
async def video(message: Message):
	await message.answer('Держи епто', random.choice(mus), state = random.getstate())
# Файл 
@vk.on.private_message(text=('файл','Файл','Файлы','файлы'))
async def file(message: Message):
	await message.answer('Вот твой файл ', attachment=ya)


# ГЛАВНОЕ МЕНЮ

@vk.on.private_message(text=['/mm', 'menu', 'меню','Меню'])
@vk.on.private_message(payload={'cmd': 'menu'})
async def menu(message: Message):
	await message.answer(
		# Сообщение при отправлении клавиатуры 
		message = 'меню хуеню:',
		# Клавиатура
        keyboard = (
        	# one_time - True - одноразовая клавиатура, False - постоянная клавиатура
        	# inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
        	# .add - добавить кнопку
        	# .row - отступ
        	# Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
        	# PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time = False, inline = False)
            .add(Text('приколы'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('не приколы (серьёзка)'), color=KeyboardButtonColor.NEGATIVE)
            .row()
            .add(Text('закрыть меню', payload={'cmd': 'closemenu'}))
            )
    )

@vk.on.private_message(payload={'cmd': 'closemenu'})
async def menu(message: Message):
	await message.answer(
		message = 'хочешь вернуться к тексту?',
        keyboard = (
            Keyboard(one_time = True, inline = False)
            .add(Text('да', payload={'cmd': 'komandi'}),color=KeyboardButtonColor.POSITIVE)     
            .row()
            .add(Text('нет', payload={'cmd': 'menu'}),color=KeyboardButtonColor.NEGATIVE)
            )
    )


# Меню c приколами
@vk.on.private_message(text='приколы')
@vk.on.private_message(payload={'cmd': 'prikol'})
async def menu(message: Message):
	await message.answer(
		message = 'приколы приколюхи приколдесы ржакич',
		# Клавиатура
        keyboard = (
        	# one_time - True - одноразовая клавиатура, False - постоянная клавиатура
        	# inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
        	# .add - добавить кнопку
        	# .row - отступ
        	# Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
        	# PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time = False, inline = False)
	    .add(Text('хентай'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('ЕБЛААААН'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('анекдот'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('авка'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('???'), color=KeyboardButtonColor.NEGATIVE)
            .row()
            .add(Text('демотиватор'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('ой в пизду', payload={'cmd': 'menu'}))
            )
    )

# меню без приколов
@vk.on.private_message(text='не приколы (серьёзка)')
@vk.on.private_message(payload={'cmd': 'noprikol'})
async def menu(message: Message):
	await message.answer(
		message = 'прям серьёзная серьёзность',
		# Клавиатура
        keyboard = (
        	# one_time - True - одноразовая клавиатура, False - постоянная клавиатура
        	# inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
        	# .add - добавить кнопку
        	# .row - отступ
        	# Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
        	# PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time = False, inline = False)
            .add(Text('реклама'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('???'), color=KeyboardButtonColor.NEGATIVE)
 .row()
 .add(Text('ой в пизду', payload={'cmd': 'menu'}))
            )
    )

#???
@vk.on.private_message(text='???')
async def magaz(message: Message):
	await message.answer( 
		message = 'пока что тут ничего нет, но скоро может появится',
        keyboard = (
            Keyboard(one_time = False, inline = False)

            .add(Text('ой в пизду', payload={'cmd': 'menu'}))
            )
    )


# перевод в демотиватор
@vk.on.private_message(text='демотиватор')
async def deem(message: Message):
	await message.answer( 
		message = 'пока что не работает ://',
       
            )
#чтоб сделать демотиватор напиши \n/дем \n и нужный текст, а еще фотку не забудь прикрепить
	
# ответ на дем

@vk.on.private_message(text=['/дем','дем'])
async def deem(message: Message):
	await message.answer( 
		message = ' ',
       
            )


# авки

av = 'photo-212149787_457239017'
av3 = 'photo-212149787_457239018'
av4 = 'photo-212149787_457239019'
av5 = 'photo-212149787_457239020'
av6 = 'photo-212149787_457239021'
av7 = 'photo-212149787_457239022'
av8 = 'photo-212149787_457239023'
av9 = 'photo-212149787_457239024'
av10 = 'photo-212149787_457239025'
av11 = 'photo-212149787_457239026'
av12 = 'photo-212149787_457239027'
av13 = 'photo-212149787_457239028'
av14 = 'photo-212149787_457239029'
av15 = 'photo-212149787_457239030'
av16 = 'photo-212149787_457239031'
av17 = 'photo-212149787_457239032'
av18 = 'photo-212149787_457239033'
av19 = 'photo-212149787_457239034'
av20 = 'photo-212149787_457239035'
av21 = 'photo-212149787_457239036'
av22 = 'photo-212149787_457239037'
av23 = 'photo-212149787_457239038'

avki= [av, av3, av4, av5, av6, av7, av8, av9, av10, av11, av12, av13, av14, av15, av16, av17, av18, av19, av20, av21, av22, av23,]

@vk.on.private_message(text=('авка','авы','Авы','Авка','Авки','авки','аву','Аву','ава','Ава'))
async def photo(message: Message):
	await message.answer('Вот твоя авка ', random.choice(avki), state = random.getstate())

@vk.on.private_message(text='реклама')
async def magaz(message: Message):
	await message.answer( 
		message = 'реклама?',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Купить рекламу'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Продать рекламу'), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text('ой в пизду', payload={'cmd': 'noprikol'}))
            )
    )

@vk.on.private_message(text='Купить рекламу')
async def main(message):
 await message.answer(
message = 'хочешь заказать рекламу? тебе сюда',
keyboard = (
Keyboard(inline = True)
.add(OpenLink('https://vk.com/@wemew-ad', 'выгувыг реклама'))
)
)
@vk.on.private_message(text='Продать рекламу')
async def blasthk(message: Message):
    await message.answer(
message = 'напиши админам (желательно марку, но можно и илье)',
keyboard = (
Keyboard(inline = True)
.add(OpenLink('https://vk.com/nesquick.s.pivom', 'мар грамыч'))
.add(OpenLink('https://vk.com/k0ronav1rus', 'иля прасолв'))
)
)
@vk.on.private_message(text='ЕБЛААААН')
async def main(message):
    await message.answer('сам еблан')

@vk.on.private_message(text='ссылка')
async def blasthk(message: Message):
	await message.answer(
		message = 'тут будет рандомный аник',
		keyboard = (
			Keyboard(inline = True)
			.add(OpenLink('https://vk.com/wemew', 'а тут можно ссылочку'))

		)
	)
# нада сделать

@vk.on.private_message()
async def main(message):
    await message.answer('')
#че, не понял :/ \nнапиши "команды" ёпта  

# Толик видиорегистратор система мене
vk.run_forever()
