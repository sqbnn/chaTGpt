#pip install aiogram
#pip install python_dotenv
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

import os
import openai

openai.api_key = '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'
openai.Model.list()

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Что стало с первым ботом?').add('Че там по It, когда 300к в секунду?')


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.id}')
    await message.answer(f'{message.from_user.first_name}, ',
                         reply_markup=main)

@dp.message_handler()
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=1,
        max_tokens=2048,
        top_p=0.7,
        frequency_penalty=0
    )
    await message.reply(response['choices'][0]['text'])

if __name__ == '__main__':
    executor.start_polling(dp)
