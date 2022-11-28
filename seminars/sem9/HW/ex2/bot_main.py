import time
import logging

from aiogram import *

TOKEN = ''
GREETINGS = 'Приветствую, {}'

# достаём токен
path = r'C:\Users\МSI\Desktop\tg tokens\token.txt'
file = open(path, mode='r')
key= file.read()
TOKEN=key
file.close()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
logFile=open(r'C:\Users\МSI\Desktop\Python for n00bz\seminars\sem9\HW\ex2\logs.txt', 'a')
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    log = f'{user_id} {user_fullname} {time.asctime()} '
    logging.basicConfig(level=logging.INFO, filename='logs.txt', format= "%(message)s %(levelname)s")
    await message.reply(GREETINGS.format(user_name))

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    log = f'{user_id} {user_fullname}: '
    logging.basicConfig(level=logging.info(log), filename='logs.txt', format= "%(asctime)s %(levelname)s %(message)s",
                        filemode='a')
    await message.reply(\
        '/start\n'+
        '/help\n'+
        '/sum <выражение которое надо подсчитать> - сложить числа\n'+
        '/sub <выражение которое надо подсчитать> - вычесть числа\n' +
        '/mpl <выражение которое надо подсчитать> - перемножить числа\n' +
        '/div <выражение которое надо подсчитать> - поделить числа\n'
        )

@dp.message_handler(commands=['sum'])
async def help_handler(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    log = f'{user_id} {user_fullname}: '
    logging.basicConfig(level=logging.info(log), filename='logs.txt', format="%(asctime)s %(levelname)s %(message)s",
                        filemode='a')
    msg = message.text[4:]
    digits = list(map(int, msg.split('+')))
    await message.reply(f'Сумма чисел: {digits} равна {sum(digits)}.')

@dp.message_handler(commands=['sub'])
async def help_handler(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    log = f'{user_id} {user_fullname}: '
    logging.basicConfig(level=logging.info(log), filename='logs.txt', format="%(asctime)s %(levelname)s %(message)s",
                        filemode='a')
    msg = message.text[4:]
    digits = list(map(int, msg.split('-')))
    for i in range(1,len(digits)):
        digits[i]*=-1
    await message.reply(f'Разность чисел: {digits} равна {sum(digits)}.')

@dp.message_handler(commands=['mpl'])
async def help_handler(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    log = f'{user_id} {user_fullname}: '
    logging.basicConfig(level=logging.info(log), filename='logs.txt', format="%(asctime)s %(levelname)s %(message)s",
                        filemode='a')
    msg = message.text[4:]
    digits = list(map(int, msg.split('*')))
    pr=1
    for i in digits:
        pr*=i
    await message.reply(f'Произведение чисел: {digits} равна {pr}.')

@dp.message_handler(commands=['div'])
async def help_handler(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    log = f'{user_id} {user_fullname}: '
    logging.basicConfig(level=logging.info(log), filename='logs.txt', format="%(asctime)s %(levelname)s %(message)s",
                        filemode='a')
    msg = message.text[4:]
    digits = list(map(int, msg.split('/')))
    d=digits[0]
    for i in range(1,len(digits)):
        d/=digits[i]
    await message.reply(f'Частное чисел: {digits} равна {(d)}.')



if __name__ == '__main__':
    executor.start_polling(dp)
