#pip install aiogram
#pip install python_dotenv
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

import os
import openai

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Точный').add('Сбалансированный').add('Творческий')


load_dotenv()

openai.api_key = 'API_TOKEN'
openai.Model.list()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Привет, ', reply_markup=main)

@dp.message_handler(text='Точный')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.2,
        max_tokens=2048,
        top_p=0.7,
        frequency_penalty=0
    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler(text='Сбалансированный')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.5,
        max_tokens=2048,
        top_p=0.7,
        frequency_penalty=0
    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler(text='Творческий')
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.9,
        max_tokens=2048,
        top_p=0.7,
        frequency_penalty=0
    )
    await message.reply(response['choices'][0]['text'])

@dp.message_handler()
async def cmd_start(message: types.Message):
    await message.reply('Я тебя не понимаю')

if __name__ == '__main__':
    executor.start_polling(dp)
