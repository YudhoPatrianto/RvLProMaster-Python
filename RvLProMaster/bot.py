from RvLProMaster.Secret.secret import GetSecret
from httpx import AsyncClient

endpoint = GetSecret.endpoint

class bot:
    # getMe
    @staticmethod
    async def getMe():
        async with AsyncClient() as client:
            try:
                r = await client.get(f'{endpoint}/getMe')
                return r.json()
            except:
                pass
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

    # sendMessage
    @staticmethod
    async def sendMessage(chat_id, chat, parse_mode='MarkdownV2', disable_notification=False, protect_content=False, reply=None):
        """Use this method to send text messages

        Parameters:
            chat_id (int): 	Unique identifier for the target chat
            chat (str): Text of the message to be sent, 1-4096 characters after entities parsing
            parse_mode (Markdown/MarkdownV2/HTML): Mode for parsing entities in the message text. 
            disable_notification (True/False): Sends the message silently. Users will receive a notification with no sound. Default False
            protect_content (True/False): Protects the contents of the sent message from forwarding and saving
            reply: Reply Message? Default Yes
        """
        async with AsyncClient() as client:
            try:
                payload = {
                    'chat_id': chat_id,
                    'text': chat,
                    'parse_mode': parse_mode,
                    'disable_notification': disable_notification,
                    'protect_content': protect_content,
                    'reply_to_message_id': reply
                }
                r = await client.post(f'{endpoint}/sendMessage', data=payload)
                return r.json()
            except:
                pass
                
    # getChat
    @staticmethod
    async def getChat(chat_id: int):
        async with AsyncClient() as client:
            try:
                payload = {'chat_id': chat_id}
                r = await client.get(f'{endpoint}/getChat', params=payload)
                return r.json()
            except:
                pass
    
    # getChatMember
    @staticmethod
    async def getChatMember(chat_id, user_id):
        async with AsyncClient() as client:
            try:
                payload = {
                    'chat_id': chat_id,
                    'user_id': user_id
                }
                r = await client.get(f'{endpoint}/getChatMember', params=payload)
                return r.json()
            except:
                pass
            
    # sendPhoto
    @staticmethod
    async def sendPhoto(chat_id, photo, caption, parse_mode='MarkdownV2' ,disable_notification=False, protect_content=False, reply=None):
        async with AsyncClient() as client:
            try:
                if 'https' and 'http' in photo:
                    try:
                        payload = {
                            'chat_id': chat_id,
                            'photo': photo,
                            'caption': caption,
                            'parse_mode': parse_mode,
                            'disable_notification': disable_notification,
                            'protect_content': protect_content,
                            'reply_to_message_id': reply
                        }
                        r = await client.get(f'{endpoint}/sendPhoto', params=payload)
                        return r.json()
                    except:
                        pass
                elif '.jpg' or '.png' or '.gif' in photo:
                    try:
                        payload = {
                            'chat_id': chat_id,
                            'caption': caption,
                            'parse_mode': parse_mode,
                            'disable_notification': disable_notification,
                            'protect_content': protect_content,
                            'reply_to_message_id': reply
                        }
                        img_payload = {'photo': open(photo, 'rb')}
                        r = await client.post(f'{endpoint}/sendPhoto', data=payload, files=img_payload)
                        return r.json()
                    except:
                        pass
            except:
                pass
    
    @staticmethod
    async def sendInlineButton(chat_id, chat, parse_mode='MarkdownV2', disable_notification=False, protect_content=False, reply_markup=None, reply=None):
        """Use this method to send inline button

        Parameters:
            chat_id (int): 	Unique identifier for the target chat
            chat (str): Text of the message to be sent, 1-4096 characters after entities parsing
            parse_mode (Markdown/MarkdownV2/HTML): Mode for parsing entities in the message text. 
            disable_notification (True/False): Sends the message silently. Users will receive a notification with no sound. Default False
            protect_content (True/False): Protects the contents of the sent message from forwarding and saving
            reply_markup (str): Json button
            reply: Reply Message? Default Yes
        """
        async with AsyncClient() as client:
            try:
                payload = {
                    'chat_id': chat_id,
                    'text': chat,
                    'parse_mode': parse_mode,
                    'disable_notification': disable_notification,
                    'protect_content': protect_content,
                    'reply_markup': reply_markup,
                    'reply_to_message_id': reply
                }
                r = await client.post(f'{endpoint}/sendMessage', data=payload)
                return r.json()
            except:
                pass