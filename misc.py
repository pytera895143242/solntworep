import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '5609831909:AAGwaBYtmOhqf3Wm6cCf6JFhTqv24MWjDtM'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN,parse_mode='html',disable_web_page_preview=True)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)