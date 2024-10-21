# Load Library
from RvLProMaster.EnvironmentHandler.Environment import TelegramBOT_TOKEN
from httpx import AsyncClient, ReadTimeout
import json
from typing import Tuple

# Environment BOT
token = TelegramBOT_TOKEN
endpoint = f'https://api.telegram.org/bot{token}'

# Clear Log
class bot:
    """
    Bot Method
    """
    try:
        @staticmethod
        async def ClearLog():
            """
            Clear Update Log
            """
            async with AsyncClient() as client:
                r_c = await client.get(f"{endpoint}/getUpdates")
                d_r = r_c.json()

                if d_r["result"]:
                    ls = max(u["update_id"] for u in d_r["result"])
                    p_c = {
                        'offset': ls + 1
                    }
                    await client.get(f"{endpoint}/getUpdates", params=p_c)
                else:
                    print("Logs Tidak Ada Yang Perlu Di Clear, Skipping")
                    pass
                
        # GetUpdates
        @staticmethod
        async def getUpdates(offset=None):
            try:
                p_gU = {
                    'offset': offset,
                    'timeout': 20
                }
                async with AsyncClient() as client:
                    r_gU = await client.get(f'{endpoint}/getUpdates', params=p_gU)
                    return r_gU.json()
            except:
                pass

        # Send Message
        @staticmethod
        async def sendMessage(chat_id, chat, parse_mode=None, replychat=None):
            """Use this method to send text messages

            Parameters:
                chat_id (int or str): Unique identifier for the target chat or username of the target channel
                chat (str): Text of the message to be sent, 1-4096 characters after entities parsing
                parse_mode (str): Mode for parsing entities in the message text (HTML/Markdown/MarkdownV2)
                replychat (str): Replied Chat? default No
            """
            try:
                p_sM = {
                    'chat_id': chat_id,
                    'text': chat,
                    'parse_mode': parse_mode,
                    'reply_to_message_id': replychat
                }
                async with AsyncClient() as client:
                    r_sM = await client.post(f'{endpoint}/sendMessage', data=p_sM)
                    return r_sM.json()
            except:
                pass
        
        # ChatJoinRequest
        @staticmethod
        async def approveChatJoinRequest(chat_id, user_id):
            try:
                p_aCJR = {
                    'chat_id': chat_id,
                    'user_id': user_id
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/approveChatJoinRequest', data=p_aCJR)
            except:
                pass
        
        # unpinChatMessage
        @staticmethod
        async def unpinChatMessage(chat_id, message_id):
            """Use this method to remove a message from the list of pinned messages in a chat

            Parameters:
                chat_id (int or str): Unique identifier for the target chat or username of the target channel
                message_id (int): Identifier of a message to unpin
            """
            try:
                p_pCM = {
                    'chat_id': chat_id,
                    'message_id': message_id
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/unpinChatMessage', data=p_pCM)
            except:
                pass
        # pinChatMessage
        @staticmethod
        async def pinChatMessage(chat_id, message_id):
            """Use this method to add a message to the list of pinned messages in a chat

            Parameters:
                chat_id (int or str): Unique identifier for the target chat or username of the target channel
                message_id (int): Identifier of a message to pin
            """
            try:
                p_pCM = {
                    'chat_id': chat_id,
                    'message_id': message_id
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/pinChatMessage', data=p_pCM)
            except:
                pass
        
        # sendPhoto
        @staticmethod
        async def sendPhoto(chat_id, photo , caption, parse_mode=None, replychat=None):
            """Use this method to send photos

            Parameters:
                chat_id (int): Unique identifier for the target chat or username of the target channel
                photo (str): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. 
                caption (str): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
                parse_mode (str): Mode for parsing entities in the message text (HTML/Markdown/MarkdownV2)
                replychat (str): Replied Chat? default No
            """
            try:
                async with AsyncClient() as client:
                    p_sP = {
                        'chat_id': chat_id,
                        'caption': caption,
                        'parse_mode': parse_mode,
                        'reply_to_message_id': replychat
                    }
                    if photo.startswith('http://') or photo.startswith('https://'):
                        p_sP['photo'] = photo
                        r_sP = await client.post(f'{endpoint}/sendPhoto', data=p_sP)
                    elif photo.startswith('.jpg') or photo.startswith('.png'):
                        with open(f'{photo}', 'rb') as read_image_binary:
                            read_image = read_image_binary.read()
                            image_path = {
                                'photo': read_image_binary
                            }
                            r_sP = await client.post(f'{endpoint}/sendPhoto', data=p_sP, files=image_path)
                    else:
                        p_sP['photo'] = photo
                        r_sP = await client.post(f'{endpoint}/sendPhoto', data=p_sP)
                    return r_sP.json()
            except:
                pass

        # sendVideo
        @staticmethod
        async def sendVideo(chat_id, video , caption, parse_mode=None, replychat=None):
            """Use this method to send video file

            Parameters:
                chat_id (int): Unique identifier for the target chat or username of the target channel
                video (str): Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. 
                caption (str): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
                parse_mode (str): Mode for parsing entities in the message text (HTML/Markdown/MarkdownV2)
                replychat (str): Replied Chat? default No
            """
            try:
                async with AsyncClient() as client:
                    p_sV = {
                        'chat_id': chat_id,
                        'caption': caption,
                        'parse_mode': parse_mode,
                        'reply_to_message_id': replychat
                    }
                    with open(f'{video}', 'rb') as read_video_binary:
                        video_path = {
                            'video': read_video_binary
                        }
                        r_sV = await client.post(f'{endpoint}/sendVideo', data=p_sV, files=video_path)
                        return r_sV.json()
            except:
                pass

        # sendVideo
        @staticmethod
        async def sendDocument(chat_id, document, caption=None, parse_mode=None, replychat=None):
            """Use this method to send Document file

            Parameters:
                chat_id (int): Unique identifier for the target chat or username of the target channel
                document (str): Document to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. 
                caption (str): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
                parse_mode (str): Mode for parsing entities in the message text (HTML/Markdown/MarkdownV2)
                replychat (str): Replied Chat? default No
            """
            try:
                async with AsyncClient() as client:
                    p_sV = {
                        'chat_id': chat_id,
                        'caption': caption,
                        'parse_mode': parse_mode,
                        'reply_to_message_id': replychat
                    }
                    with open(f'{document}', 'rb') as read_document_binary:
                        document_path = {
                            'document': read_document_binary
                        }
                        r_sV = await client.post(f'{endpoint}/sendDocument', data=p_sV, files=document_path)
                        return r_sV.json()
            except:
                pass

        # getChatMember
        @staticmethod
        async def getChatMember(chat_id, user_id):
            """Use this method to get information about a member of a chat

            Parameters:
                chat_id (int or string): _description_
                user_id (int): _description_
            """
            try:
                async with AsyncClient() as client:
                    p_gCM  = {
                        'chat_id': chat_id,
                        'user_id': user_id
                    }
                    r_gCM = await client.post(f'{endpoint}/getChatMember', data=p_gCM)
                    return r_gCM.json()
            except:
                pass
            
        # restrictChatMember
        @staticmethod
        async def restrictChatMember(chat_id, user_id, until_date=None):
            """Use this method to restrict a user in a supergroup.

            Parameters:
                chat_id (int or str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
                user_id (int): Unique identifier of the target user
                until_date (int): Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
            """
            try:
                p_rCM = {
                    'chat_id': chat_id,
                    'user_id': user_id,
                    'until_date': until_date,
                    'can_send_messages': False,
                    'can_send_audios': False,
                    'can_send_documents': False,
                    'can_send_photos': False,
                    'can_send_videos': False,
                    'can_send_video_notes': False,
                    'can_send_voice_notes': False,
                    'can_send_polls': False,
                    'can_send_other_messages': False,
                    'can_add_web_page_previews': False,
                    'can_change_info': False,
                    'can_invite_users': False,
                    'can_pin_messages': False,
                    'can_manage_topics': False
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/restrictChatMember', data=p_rCM)
            except:
                pass
            
        # unrestrictChatMember
        @staticmethod
        async def unrestrictChatMember(chat_id, user_id, until_date=None):
            """Use this method to unrestricted a user in a supergroup.

            Parameters:
                chat_id (int or str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
                user_id (int): Unique identifier of the target user
                until_date (int): Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
            """
            try:
                p_rCM = {
                    'chat_id': chat_id,
                    'user_id': user_id,
                    'until_date': until_date,
                    'can_send_messages': True,
                    'can_send_audios': True,
                    'can_send_documents': True,
                    'can_send_photos': True,
                    'can_send_videos': True,
                    'can_send_video_notes': True,
                    'can_send_voice_notes': True,
                    'can_send_other_messages': True,
                    'can_add_web_page_previews': True
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/restrictChatMember', data=p_rCM)
            except:
                pass
            
        # Inline Button
        @staticmethod
        async def inlineButton(chat_id, inline_keyboard, text_inlineButton):
            """Use This Method For Sending Inline Button

            Parameters:
                chat_id (str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
                inline_keyboard (str): Spesificy the payload inline keyboard: [{"text": "Tombol", "callback_data": "button1"}]
                text_inlineButton (str): spesify your text wants to send
            """
            try:
                p_iB = {
                    'chat_id': chat_id,
                    'text': text_inlineButton,
                    'reply_markup': {
                        "inline_keyboard": inline_keyboard
                    }
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/sendMessage', json=p_iB)
            except:
                pass
        
        # getUserProfilePhotos
        @staticmethod
        async def getUserProfilePhotos(chat_id, user_id):
            """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object, output will showing automatic file_id

            Parameters:
                chat_id (int): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
                user_id (int): Unique identifier of the target user
            """
            try:
                p_gUPP = {
                    'chat_id': chat_id,
                    'user_id': user_id,
                    'offset': None,
                    'limit': '1'
                }
                async with AsyncClient() as client:
                    r_gUPP = await client.get(f'{endpoint}/getUserProfilePhotos', params=p_gUPP)
                    response_gUPP = r_gUPP.json()
                    return response_gUPP['result']['photos'][0][0]['file_id']
            except:
                pass
            
        # getFile
        @staticmethod
        async def getFile(file_id):
            """Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.

            Parameters:
                file_id (str): File identifier to get information about
            """
            try:
                p_gF = {
                    'file_id': file_id
                }
                async with AsyncClient() as client:
                    r_gF = await client.get(f'{endpoint}/getFile', params=p_gF)
                    return_gF = r_gF.json()
                    return return_gF
            except:
                pass
            
        # deleteMessage
        @staticmethod
        async def deleteMessage(chat_id: int, message_id: int) -> int:
            """Use this method to delete a message, including service messages, with the following limitations:
            - A message can only be deleted if it was sent less than 48 hours ago.
            - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
            - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
            - Bots can delete outgoing messages in private chats, groups, and supergroups.
            - Bots can delete incoming messages in private chats.
            - Bots granted can_post_messages permissions can delete outgoing messages in channels.
            - If the bot is an administrator of a group, it can delete any message there.
            - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
            Returns True on success.

            Parameters:
                chat_id (int): 	Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                message_id (int): Identifier of the message to delete

            """
            try:
                p_sM = {
                    'chat_id': chat_id,
                    'message_id': message_id
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/deleteMessage', data=p_sM)
            except:
                pass
            
        # promoteChatMember
        @staticmethod
        async def promoteChatMember(chat_id: int | str, user_id: int) -> int | str:
            try:
                p_pCM = {
                    'chat_id': chat_id,
                    'user_id': user_id,
                    'can_change_info': True,
                    'can_post_messages': True,
                    'can_edit_messages': True,
                    'can_delete_messages': True,
                    'can_invite_users': True,
                    'can_restrict_members': True,
                    'can_pin_messages': True,
                    'can_manage_video_chats': True,
                    'can_promote_members': True
                }
                
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/promoteChatMember', data=p_pCM)
            except:
                pass
        # setChatAdministratorCustomTitle
        @staticmethod
        async def setChatAdministratorCustomTitle(chat_id: int, user_id: int, custom_title: str ) -> Tuple[int, str]:
            try:
                p_sCACT = {
                    'chat_id': chat_id,
                    'user_id': user_id,
                    'custom_title': custom_title
                }
                async with AsyncClient() as client:
                    await client.post(f'{endpoint}/setChatAdministratorCustomTitle', data=p_sCACT)
            except:
                pass
        # Try(line 15)
    except:
        pass
        