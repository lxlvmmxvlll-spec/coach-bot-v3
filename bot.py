import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN
from ai_engine import ask_ai
from prompts import day_prompt, simulate_prompt

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    text = ask_ai(day_prompt())
    await message.answer(text)

@dp.message(Command("day"))
async def day(message: types.Message):
    text = ask_ai(day_prompt())
    await message.answer(text)

@dp.message(Command("simulate"))
async def simulate(message: types.Message):
    text = ask_ai(simulate_prompt())
    await message.answer(text)

@dp.message()
async def fallback(message: types.Message):
    text = ask_ai(f"Improve this communication:\n{message.text}")
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
