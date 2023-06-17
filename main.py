#pip install aiogram
#pip install python_dotenv
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
import os

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

@dp.message_handler(commands=['qwe'])
async def cmd_start(message: types.Message):
    await message.answer('Привет')

if __name__ == '__main__':
    executor.start_polling(dp)
