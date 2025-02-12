from RvLProMaster import bot, run
from json import dumps
import asyncio

async def main():
    while True:
        out_polling, user_id, first_name, last_name, username, chat_id, group_title, group_username, text, reply, channel_title = await run()
        if text == "/start":
            await bot.Methods.sendMessage(chat_id, "*Hi I'm From Start*", "MarkdownV2")
asyncio.run(main())