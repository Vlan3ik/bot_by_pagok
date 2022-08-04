from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text, OpenLink
from vkbottle.api import API
import random


bot = Bot("946ce0b0b141eeba369f8e4ba4518ce52d15a99233364c519fc3a84a8b8a3740d6cc5ab165964e4167253")
group_id = 151288842
api = API("7b622eca46d0e42d92c46a9ee64dd8e030c930ecad3c9153d0347bbf2ea425d0e243bf69a40863deb0bc9")


@bot.on.private_message(text=['Мультфильм'])
async def mult(message: Message):
    l = await keyb()
    wall = await film(message=message)
    if 'Ошибка' in wall:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')
    else:
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)


@bot.on.private_message(text=['Комедия'])
async def rofl(message: Message):
    l = await keyb()
    wall = await film(message=message)
    if 'Ошибка' in wall:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')
    else:
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)

@bot.on.private_message(text=['Боевик'])
async def boev(message: Message):
    l = await keyb()
    wall = await film(message=message)
    if 'Ошибка' in wall:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')
    else:
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)


@bot.on.private_message(text=['Драма'])
async def grust(message: Message):
    l = await keyb()
    wall = await film(message=message)
    if 'Ошибка' in wall:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')
    else:
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)


@bot.on.private_message(text=['Фантастика'])
async def fantasy(message: Message):
    l = await keyb()
    wall = await film(message=message)
    if 'Ошибка' in wall:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')
    else:
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)

@bot.on.private_message(text=['Ужасы'])
async def triller(message: Message):
    l = await keyb()
    wall = await film(message=message)
    if 'Ошибка' in wall:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')
    else:
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)

@bot.on.private_message(text=['Новинки'])
async def news(message: Message):
    l = await keyb()
    try:
        req = await api.request("wall.search", {"owner_id": f"-{group_id}", "query": f"новинки 2022", "count": 100})
        tox = req['response']['items']
        choice = random.choice(tox)
        wall = f"wall{choice['owner_id']}_{choice['id']}"
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)
    except Exception as error:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')


async def linker():
    grouplink = await bot.api.request("groups.getById", {"group_id": group_id})
    name = grouplink['response'][0]['screen_name']
    return name

async def keyb():
    link = await linker()

    linkkb = Keyboard(inline=True)
    linkkb.row()
    linkkb.add(OpenLink(label='Помощь', link='https://vk.com/odun04ka'))
    linkkb.add(OpenLink(link=f'https://vk.com/{link}', label='Подпишись'))
    return linkkb

async def film(message):
    try:
        req = await api.request("wall.search", {"owner_id": f"-{group_id}", "query": f"жанр {message.text.lower()}", "count": 100})
        tox = req['response']['items']
        choice = random.choice(tox)
        wall = f"wall{choice['owner_id']}_{choice['id']}"
        return wall
    except Exception as error:
        return 'Ошибка {}'.format(error)

@bot.on.private_message(text=['начать', 'привет'])
async def start(message: Message):
    keyboard = Keyboard(one_time=False)
    keyboard.row()
    keyboard.add(Text(label="Мультфильм"))
    keyboard.add(Text(label="Комедия"))
    keyboard.add(Text(label="Боевик"))
    keyboard.row()
    keyboard.add(Text(label="Драма"))
    keyboard.add(Text(label="Фантастика"))
    keyboard.add(Text(label="Ужасы"))
    keyboard.row()
    keyboard.add(Text(label="Новинки"))
    await message.answer('Привет! Выбери жанр и я отправлю тебе фильм.', keyboard=keyboard)

@bot.on.private_message()
async def handling(message: Message):
    l = await keyb()
    try:
        req = await api.request("wall.search", {"owner_id": f"-{group_id}", "query": f"{message.text.lower()}", "count": 100, "owners_only": 1, "offset": 0})
        tox = req['response']['items']
        choice = random.choice(tox)
        wall = f"wall{choice['owner_id']}_{choice['id']}"
        await message.answer('Держи свой фильм! Желаем приятного просмотра.', keyboard=l, attachment=wall)
    except Exception as error:
        await message.answer('Таких фильмов в группе нет, выбери что-нибудь другое.')


bot.run_forever()