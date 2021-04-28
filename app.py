import asyncio

from aiogram import Bot, Dispatcher, executor
# Bot - класс бота, Dispatcher - достващик, Executor - будет начинать работу  бота

from config import BOT_TOKEN

# поток в котором будут обрабатываться все события, обязательно для работы с аснхронным ботом
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
#Обработчик и доставщик
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
  from handlers import dp, send_to_admin
  executor.start_polling(dp, on_startup=send_to_admin)