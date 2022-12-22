import logging
import asyncio
import datetime
from aiogram import Bot, Dispatcher, executor, types
from Sources import gazeta_image, gazeta_news_text,gazeta_news_header,ria_news_text,ria_news_header,ria_news_image

API_TOKEN = 'BOT TOKEN HERE'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
time_now_hour = datetime.datetime.now().hour
truefalse = True

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    """Эта функция используется в качестве обработчика сообщений в боте, который реагирует на команду /start.
    При получении этой команды от пользователя, бот отправляет сообщение с информацией
     о пользователе на указанный в коде ID (admin_id). Если сообщение пришло от пользователя с указанным ID,
     то бот также отправляет сообщение "Слушаюсь, сер"."""

    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    if user_id == "ADMIN_ID":
        truefalse = True
        await bot.send_message("ADMIN_ID",  "Слушаюсь, сер")
    else:
        bot.send_message("ADMIN_ID", "У вас новый пользователь, сер! Вот его данные: \n" + "ФИО: " + str(full_name) + '\nID: ' + str(user_id) + '\nUsername: ' + str(username))

@dp.message_handler(commands=['bot_send_news_to_channel_from_Gazeta_ru'])
async def src1(msg: types.Message):

    """ 1. Выполняет бесконечный цикл с помощью инструкции while truefalse.
        2. Внутри цикла инициализирует пустую строку text.
        3. Добавляет результат функции gazeta_news_header(), заключенный в теги <b>, к text, за которым следует символ новой строки."""

    while truefalse:
        text = ""
        text += ("<b>" + gazeta_news_header() + "</b>") + '\n'
        text += gazeta_news_text()
        if len(text) <= 1024:
            await bot.send_photo(chat_id="@tactics_ru", photo=gazeta_image(), caption=text)
        elif len(text) <= 3900:
            await bot.send_photo(chat_id="@tactics_ru", photo=gazeta_image(), caption="<b>" + gazeta_news_header() + "</b>")
            await bot.send_message(chat_id="@tactics_ru", text=gazeta_news_text())
        if time_now_hour >= 8:
            await asyncio.sleep(900)
        else:
            await asyncio.sleep(2400)

@dp.message_handler(commands=['bot_send_news_to_channel_from_RIA_ru'])
async def src2(msg: types.Message):
    """ 1. Выполняет бесконечный цикл с помощью инструкции while truefalse.
        2. Внутри цикла инициализирует пустую строку text.
        3. Добавляет результат функции ria_news_header(), заключенный в теги <b>, к text, за которым следует символ новой строки."""

    while truefalse:
        text = ""
        text += ("<b>" + ria_news_header() + "</b>") + '\n'
        text += ria_news_text()
        if len(text) <= 1024:
            await bot.send_photo(chat_id="@tactics_ru", photo=ria_news_image(), caption=text)
        elif len(text) <= 3900:
            await bot.send_photo(chat_id="@tactics_ru", photo=ria_news_image(), caption="<b>" + ria_news_header() + "</b>")
            await bot.send_message(chat_id="@tactics_ru", text=ria_news_text())
        await asyncio.sleep(7200)

@dp.message_handler(commands=['stopnews'])
async def start(message: types.Message):

    """Функция сначала проверяет, равен ли id пользователя, который отправил команду,
    912930887. Если это так, функция устанавливает переменную truefalse в False
     и отправляет сообщение пользователю с id admin_id, содержащее сообщение "Слушаюсь, сер" """

    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    if user_id == "ADMIN_ID":
        truefalse = False
        await bot.send_message("ADMIN_ID",  "Слушаюсь, сер")
    else:
        bot.send_message("ADMIN_ID", "Кто-то хотел остановить бота, сер! Вот его данные: \n" + "ФИО: " + str(full_name) + '\nID: ' + str(user_id) + '\nUsername: ' + str(username))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



