from aiogram import executor
from handlers import dp

async def on_start(_):
    print('Бот запущен')

executor.start_polling(dp, skip_updates=True, on_startup=on_start) 
# True - все сообщение, которые будут приходить пока бот выключен, будут проходить мимо, 
# False - все сообщение, которые будут приходить пока бот выключен, будут складироваться.