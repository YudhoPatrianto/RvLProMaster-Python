from RvLProMaster import bot, Types
import asyncio

async def main():
    while True:
        types = await Types.RunBOT()
        if types.text == "/start":
            await bot.Methods.sendMessage(types.chat_id, "*Hi I'm From `/start`*","MarkdownV2")
asyncio.run(main())