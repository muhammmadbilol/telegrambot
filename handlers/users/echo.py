from aiogram import types
from loader import dp
import wikipedia
wikipedia.set_lang("uz")
@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Ma'lumot  topilmadi")




