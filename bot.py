import aiogram 
import asyncio
from models.user import User

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()
####### Feader

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Вітаю, {message.from_user.username}! Це Бот, який допоможе тобі стати кращою версією тебе)')
    await message.answer('Згодом тут буде меню де можна вибрати основні функції бота. Зокрема, інформація про можливості бота, майбутні зміни і далі головні команди.')
    
    usr = message.from_user
    global new_user
    new_user = User(id=usr.id, name=usr.username, goals=None, reminders=None, status="free", diary=None)

@dp.message(Command('user_info'))
async def user_info(message: Message):
    await message.reply(f'ID: {new_user.id}\nName: {new_user.name}\nStatus: {new_user.status}')










######### Footer
async def main():
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stoped')