from  aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Obuna bo'lishni  tekshirosh",callback_data="check_subs")
    ]]
)