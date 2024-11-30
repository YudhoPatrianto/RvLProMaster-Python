from RvLProMaster.Polling.polling import polling
from RvLProMaster.Polling.clear_log import clear_log
from json import dumps

async def run():
    def zero_values(total, value=''):
        return(value,) * total
    
    # Initialize Information As Blank
    obtain, user_id, first_name, last_name, username, chat_id, group_title, group_username, chat, reply, channel_title = zero_values(11)

    while True:
        obtain = await polling()
        polling_beautify = dumps(obtain, indent=2)
        try:
            with open('polling.json', 'w') as rw_polling:
                rw_polling.write(polling_beautify)
            # Group/Forums
            if 'message' in obtain:
                get_msg = obtain['message'] # type: ignore
                
                # User Information
                user_id = get_msg['from'].get('id', '')
                first_name = get_msg['from'].get('first_name', '')
                last_name = get_msg['from'].get('last_name', '')
                username = get_msg['from'].get('username', '')
                
                # Group Information
                chat_id = get_msg['chat'].get('id', '')
                group_title = get_msg['chat'].get('title', '')
                group_username = get_msg['chat'].get('username', '')

                # Message Info
                chat = get_msg.get('text', '')
                reply = get_msg.get('message_id', '')
                
                with open('msg.json', 'w') as rw_ch:
                    rw_ch.write(dumps(get_msg, indent=2))
            # Channel
            if 'channel_post' in obtain:
                get_channel = obtain['channel_post']
                snd_chat = get_channel['sender_chat']
                
                # Channel Information
                chat_id = snd_chat.get('id', '')
                channel_title = get_channel['chat'].get('title', '')
                
                # Message Info
                chat =  get_channel.get('text', '')
                reply = get_channel.get('message_id', '')
            return obtain, user_id, first_name, last_name, username, chat_id, group_title, group_username, chat, reply, channel_title
        except Exception as err_run:
            print(f'Error!\nDetails:{err_run}')