# Load Library
from RvLProMaster.Secret.secret import GetSecret
from RvLProMaster.Polling.clear_log import clear_log
from RvLProMaster.bot import bot
from httpx import AsyncClient
import asyncio

# Endpoint
endpoint = GetSecret.endpoint

@staticmethod
async def polling():
    await clear_log()
    offset = None
    while True:
        up = await bot.getUpdates(offset)
        for obtain in up['result']: # type: ignore
            offset = obtain['update_id'] + 1
            return obtain
        await asyncio.sleep(1)