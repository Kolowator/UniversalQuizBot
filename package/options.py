from aiogram import  Dispatcher, types
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from package import dbase
from package import commands
import json


dp = Dispatcher()

with open('quiz_data.json', 'r', encoding='utf-8') as file:
   quiz_data = json.load(file)



def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for index, option in enumerate(answer_options):
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data=f"right_answer_{index}" if option == right_answer else f"wrong_answer_{index}")
        )

    builder.adjust(1)
    return builder.as_markup()



@dp.callback_query(F.data.startswith("right_"))
async def right_answer(callback: types.CallbackQuery):
    
    index = callback.data.split("_")[2]
    index = int(index)

    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    current_question_index = await dbase.get_quiz_index(callback.from_user.id)
    await callback.message.answer(f"Ваш ответ: {quiz_data[current_question_index]['options'][index]}")
    
    await callback.message.answer("Верно!")
    
    current_question_index = await dbase.get_quiz_index(callback.from_user.id)

    current_score = await dbase.get_score(callback.from_user.id)

    # Обновление номера текущего вопроса в базе данных
    current_question_index += 1
    current_score +=1
    await dbase.update_quiz_index(callback.from_user.id, callback.from_user.first_name, current_question_index, current_score)


    if current_question_index < len(quiz_data):
        await commands.get_question(callback.message, callback.from_user.id)
    else:
        await callback.message.answer(f"Это был последний вопрос. Квиз завершен! Ваш результат {current_score}/10")


@dp.callback_query(F.data.startswith("wrong_"))
async def wrong_answer(callback: types.CallbackQuery):

    index = callback.data.split("_")[2]
    index = int(index)

    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )

    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await dbase.get_quiz_index(callback.from_user.id)
    correct_option = quiz_data[current_question_index]['correct_option']
    await callback.message.answer(f"Ваш ответ: {quiz_data[current_question_index]['options'][index]}")
    await callback.message.answer(f"Неправильно. Правильный ответ: {quiz_data[current_question_index]['options'][correct_option]}")

    current_score = await dbase.get_score(callback.from_user.id)
    # Обновление номера текущего вопроса в базе данных
    current_question_index += 1
    
    await dbase.update_quiz_index(callback.from_user.id, callback.from_user.first_name, current_question_index, current_score)


    if current_question_index < len(quiz_data):
        await commands.get_question(callback.message, callback.from_user.id)
    else:
        await callback.message.answer(f"Это был последний вопрос. Квиз завершен! Ваш результат {current_score}/10")