from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import Dispatcher, types
from package import options
from package import dbase
from aiogram import F
import json

dp = Dispatcher()

with open('quiz_data.json', 'r', encoding='utf-8') as file:
   quiz_data = json.load(file)





# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))


async def get_question(message, user_id):

    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await dbase.get_quiz_index(user_id)
    correct_index = quiz_data[current_question_index]['correct_option']
    opts = quiz_data[current_question_index]['options']
    kb = options.generate_options_keyboard(opts, opts[correct_index])
    await message.answer(f"{quiz_data[current_question_index]['question']}", reply_markup=kb)


async def new_quiz(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    current_question_index = 0
    score = 0
    await dbase.update_quiz_index(user_id, user_name, current_question_index, score)
    
    await get_question(message, user_id)

# Хэндлер на команду /quiz
@dp.message(F.text=="Начать игру")
@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):

    await message.answer(f"Давайте начнем квиз!")
    await new_quiz(message)

# Хэндлер команды /stats
@dp.message(Command("stats"))
async def cmd_stats(message: types.Message):
    current_score = await dbase.get_score(message.from_user.id)
    await message.answer(f"Ваш последний результат: {current_score}/10")
