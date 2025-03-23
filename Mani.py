from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("TOKEN")  # Koyeb uchun TOKEN ni olish

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Salom! Men Koyeb yordamida doimiy ishlaydigan Telegram botman!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    
