import asyncio
from aiogram import Bot, Dispatcher, types
import logging
from package import dbase
from package import commands
from aiogram.filters.command import Command
from package import options
from aiogram import F
from package.options import right_answer
from package.options import wrong_answer

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7574181279:AAECIRkRxxAUUrTQVEgZ3lTj1oj8TDQ7cZA'


# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()


dp.message.register(commands.cmd_start, Command(commands=['start']))

dp.message.register(commands.cmd_quiz, F.text=="Начать игру")
dp.message.register(commands.cmd_quiz, Command(commands=['quiz']))

dp.message.register(commands.cmd_stats, Command(commands=['stats']))

@dp.callback_query(F.data.startswith("right_"))
async def handle_right_answer(callback: types.CallbackQuery):
    await right_answer(callback)

@dp.callback_query(F.data.startswith("wrong_"))
async def handle_wrong_answer(callback: types.CallbackQuery):
    await wrong_answer(callback)





# Запуск процесса поллинга новых апдейтов
async def main():

    # Запускаем создание таблицы базы данных
    await dbase.create_table()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())