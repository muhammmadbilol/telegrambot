from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 chop etish",callback_data=post_callback.new("post")),
        InlineKeyboardButton(text="❌ Rad etish",callback_data=post_callback.new("cancel"))
    ]]
)
