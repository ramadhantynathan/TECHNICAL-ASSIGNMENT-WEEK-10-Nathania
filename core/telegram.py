from datetime import datetime
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from database import DB
import os


class Telegram:

    bot : Bot
    db: DB
    token : str

    def __init__(self, db: DB) -> None:
        self.token = os.getenv("BOT_TOKEN")
        self.bot = Bot(self.token)
        self.db = DB()
    
    def send_notification(self, message: str) :
        chats = self.db.get_chat()
        for chat in chats:
            self.bot.send_message(chat_id=chat["chat_id"], text=message)