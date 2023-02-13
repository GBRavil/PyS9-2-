from aiogram import types
from loader import dp
import random

total = 150
new_game = False
player1 = ''
player2 = ''
player1_id = 0
player2_id = 0
flag = random.randint(1, 3)

@dp.message_handler(commands=['start']) #text=['help'] без /
async def mes_start(message: types.Message):
    await message.answer(f'/new_game - начать новую игру\n'
                         f'/set и число - указать количество конфет на столе\n')
    global player1
    global player2
    global player1_id
    global player2_id
    if player1 == '':
        player1 = message.from_user.first_name
        player1_id = message.from_user.id
        await message.answer(f'{player1}, здравствуй игрок № 1\n'
                             f'Игрок № 2 отсутствует')
    else:
        player2 = message.from_user.first_name 
        player2_id = message.from_user.id
        await message.answer(f'{player2}, здравствуй игрок № 2')
        await dp.bot.send_message(player1_id, f'Игроки {player1} и {player2} готовы к игре!')
        await dp.bot.send_message(player2_id, f'Игроки {player1} и {player2} готовы к игре!')


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global flag
    new_game = True
    await dp.bot.send_message(player1_id, f'Игра началась! Всего {total} конфет.')
    await dp.bot.send_message(player2_id, f'Игра началась! Всего {total} конфет.')
    if flag:
        await dp.bot.send_message(player1_id, f'Первым ходит {player1}')
        await dp.bot.send_message(player2_id, f'Первым ходит {player1}')
    else:
        await dp.bot.send_message(player1_id, f'Первым ходит {player2}')
        await dp.bot.send_message(player2_id, f'Первым ходит {player2}')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    global new_game
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            total = int(count)
            await message.answer(f'Конфет теперь будет {total} ')
        else:
            await message.answer(f'{message.from_user.first_name}, напишите число цифрами')
    else:
        await message.answer(f'{message.from_user.first_name}, нельзя менять правила во время игры')


@dp.message_handler()
async def mes_num(message: types.Message):
    global total
    global new_game
    global player1
    global player2
    global player1_id
    global player2_id
    player = ''
    if new_game:
        if message.text.isdigit():
            candy =int(message.text)
            total -= candy
            if message.from_user.first_name == player1:
                player = player2
            elif message.from_user.first_name == player2:
                player = player1
            if total <= 0:
                await dp.bot.send_message(player1_id, f'Победил {message.from_user.first_name}!')
                await dp.bot.send_message(player2_id, f'Победил {message.from_user.first_name}!')
                new_game = False
                total = 150
                player1 = ''
                player2 = ''
                player1_id = 0
                player2_id = 0
            else: 
                await dp.bot.send_message(player1_id, f'{message.from_user.first_name} взял {candy} конфет.'
                                                      f'На столе осталось {total}, теперь берет конфеты {player}')
                await dp.bot.send_message(player2_id, f'{message.from_user.first_name} взял {candy} конфет.'
                                                      f'На столе осталось {total},, теперь берет конфеты {player}')
