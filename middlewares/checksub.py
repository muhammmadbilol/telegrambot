import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import CHANNELS
from utils.misc import subscription
from loader import bot


class CheckCancel(BaseMiddleware):
    async def on_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        logging.info(user)
        result = "Botdan  foydalanish  uchun  quydagi  kanallarga  obuna  bo'ling \n"
        final_start = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_start *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"👉 <a href='{invite_link}'> {channel.title} </a>\n\n")



        if not final_start:
            await update.message.answer(result,disable_web_page_preview=True)
            raise CancelHandler()
