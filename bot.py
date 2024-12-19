import aiogram 
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()
####### Feader

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Вітаю, {message.from_user.username}! Це Бот, який допоможе тобі стати кращою версією тебе)')
    await message.answer('Згодом тут буде меню де можна вибрати основні функції бота. Зокрема, інформація про можливості бота, майбутні зміни і далі головні команди.')











######### Footer
async def main():
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stoped')