from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS, CHANNELS
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, Message
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from aiogram.dispatcher.filters import Command
from states.newpost import NewPost


@dp.message_handler(Command("yangi_post"))
async def create_post(message: Message):
    await message.answer("Chop  etish  ucun  post yuboring")
    await NewPost.NewMessage.set()


@dp.message_handler(state=NewPost.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("postni  tastiqlash  uchun  yuboraymi? ",
                         reply_markup=confirmation_keyboard)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("post adminga yuborildi")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quydagi postni  chop etmoqchi")
    await bot.send_message(ADMINS[0], text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("post chop etilmadi")


@dp.message_handler(state=NewPost.Confirm)
async def post_unknow(message: Message):
    await message.answer("chop  etish  yoki  rad etish  tugmalarni  tanlang")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Chop etisga  ruhsat  berdingiz.", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def cancel_post(call: CallbackQuery):
    await call.answer("Chop etishni  bekor qilishga  ruhsat  berdingiz.", show_alert=True)
    await call.message.edit_reply_markup()
