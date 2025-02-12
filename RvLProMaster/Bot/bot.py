from RvLProMaster import endpoint
from httpx import AsyncClient
from typing import Optional, Union, Literal

class bot:
    class Updates:
    # getUpdates
        @staticmethod
        async def getUpdates(offset=None):
            async with AsyncClient() as client:
                try:
                    payload = {'offset': offset}
                    r = await client.get(f'{endpoint}/getUpdates', params=payload)
                    return r.json()
                except:
                    pass

    class Methods:
        # sendMessage
        @staticmethod
        async def sendMessage(
            chat_id: Optional[Union[int,str]]= None,
            text: Optional[Union[str]] = None,
            parse_mode: Optional[Literal['Markdown', 'MarkdownV2', 'HTML']] = 'MarkdownV2',
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
        ):
            async with AsyncClient() as client:
                payload = {
                    'chat_id': chat_id,
                    'text': text,
                    'parse_mode': parse_mode,
                    'disable_notification': disable_notification,
                    'protect_content': protect_content
                }
                r = await client.post(f"{endpoint}/sendMessage", json=payload)
                return r.json()


bot = bot()