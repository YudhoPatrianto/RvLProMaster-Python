# Load Library
from RvLProMaster.EnvironmentHandler.Environment import MONGODB, TelegramBOT_TOKEN
from RvLProMaster.bot import bot
from pymongo import MongoClient
from RvLProMaster.AI.SelectAI import AI
from RvLProMaster.Utils.CekGempa import CekGempa
from RvLProMaster.Utils.PythonTerminal import Run
from RvLProMaster.Utils.Download import DownloadFrom
from RvLProMaster.UserHandling.CheckUser import CheckUser
from RvLProMaster.Utils.Speedtest import Speedtest
from RvLProMaster.Utils.ConvertTime import ConvertTimeTo
from RvLProMaster.Utils.LinkDownloader import Download
from RvLProMaster.Utils.WriteTelegraph import Telegraph
from RvLProMaster.ChatSecure.Filtering import FilterChat
from RvLProMaster.GroupUtils.AddWhitelistGroup import AddWhitelistGroup
from RvLProMaster.GroupUtils.RemoveWhitelistGroup import DeleteWhitelistGroup
from RvLProMaster.GroupUtils.CheckGroupWhitelist import CheckGroup
from RvLProMaster.ChatSecure.AddPayload import AddBadword
from pathlib import Path
import json
import asyncio
import os

# Get Database Directory
db_path = os.getcwd()

# Get Video Path
class GetFilePath:
    @staticmethod
    def FileMP4():
        try:
            current_dir = next(Path(__file__).resolve().parent.parent.rglob("*.mp4"))
            return str(current_dir)
        except StopIteration as stp_ltr:
            return ""
    @staticmethod
    def FileJPG():
        try:
            current_dir = next(Path(__file__).resolve().parent.parent.rglob("*.jpg"))
            return str(current_dir)
        except StopIteration as stp_ltr:
            return ""

VideoPath = GetFilePath.FileMP4()

# Run BOT
async def main():
    print(f'Running Bot')
    offset = None
    while True:
        updateLogs = await bot.getUpdates(offset)
        if updateLogs and 'result' in updateLogs:
            for getLogs in updateLogs['result']:
                offset = getLogs['update_id'] + 1
                
                CheckBadword = FilterChat.Badword()
                CheckChatKriptod = FilterChat.Kriptod()
                
                # Send Into Mongodb
                tree_view = json.dumps(getLogs, indent=2)
                minify_view = json.loads(tree_view)
                client = MongoClient(MONGODB)
                database = client[''] # Database Name
                collection = database[''] # Database Collection Name
                collection.insert_one(minify_view)

                # Json Beauty
                beautify_getLogs = json.dumps(getLogs, indent=2)

                # Save Logs
                with open(f'{db_path}/RvLProMaster/Logs/currentlog.json', "w") as write_database: # Logs Current
                    json.dump(getLogs, write_database, indent=4)
                    write_database.write('\n')
                with open(f'{db_path}/RvLProMaster/Logs/database.json', 'a') as write_db: # Logs All Database
                    json.dump(getLogs, write_db, indent=4)
                    write_db.write('\n')
#####################Chat Join Requested########################################################################################################################################################################
                if 'chat_join_request' in getLogs:
                    chat_join_request = getLogs['chat_join_request']
                    
                    # Environment chat_join_request
                    chat_id = chat_join_request['chat'].get('id', '') # Chat ID
                    group_title = chat_join_request['chat'].get('title', '') # Group Title
                    user_id = chat_join_request['from'].get('id', '') # User ID User Request
                    first_name = chat_join_request['from'].get('first_name', '') # First Name User Request
                    last_name = chat_join_request['from'].get('last_name', '') # Last Name User Request 
                    username = chat_join_request['from'].get('username', '') # User ID User Request 
                    
                    # Send Notify
                    await bot.sendMessage(chat_id, f'*Informasi User Meminta Join Grup*\n\n*First Name:* `{first_name}`\n*Last Name:* `{last_name}`\n*User ID:* `{user_id}`\n*Username:* @{username}\n\n*Meminta Bergabung Ke Grup* `{group_title}`', 'Markdown')
                    await asyncio.sleep(2)
                    await bot.approveChatJoinRequest(chat_id, user_id)
################new_chat_participant###################################################################################################################################################################
                if 'message' in getLogs:
                    if 'new_chat_participant' in getLogs['message']:
                        new_chat_participant = getLogs['message']

                        # Environment new_chat_participant
                        chat_id = new_chat_participant['chat'].get('id', '') # Chat ID
                        group_title = new_chat_participant['chat'].get('title', '') # Group Title
                        user_id = new_chat_participant['new_chat_participant'].get('id', '') # User ID User Request new_chat_participant
                        first_name = new_chat_participant['new_chat_participant'].get('first_name', '') # First Name User Request new_chat_participant
                        last_name = new_chat_participant['new_chat_participant'].get('last_name', '') # Last Name User Request new_chat_participant
                        username = new_chat_participant['new_chat_participant'].get('username', '') # User ID User Request new_chat_participant
                        message_id = new_chat_participant.get('message_id', '')
                        # Send Notify
                        await bot.sendMessage(chat_id, f'*Selamat Datang* @{username}\n\n*First Name:* `{first_name}`\n*Last Name:* `{last_name}`\n*User ID:* `{user_id}`\n*Username:* @{username}\n\n*Di Grup* `{group_title}` *Semoga Betah!*', 'Markdown', replychat=message_id)
    ##################left_chat_participant#############################################################################################################################################################################
                if 'message' in getLogs:
                    if 'left_chat_participant' in getLogs['message']:
                        left_chat_participant = getLogs['message']

                        # Environment new_chat_participant
                        chat_id = left_chat_participant['chat'].get('id', '') # Chat ID
                        user_id = left_chat_participant['left_chat_participant'].get('id', '') # User ID User Request left_chat_participant
                        first_name = left_chat_participant['left_chat_participant'].get('first_name', '') # First Name User Request left_chat_participant
                        last_name = left_chat_participant['left_chat_participant'].get('last_name', '') # Last Name User Request left_chat_participant
                        username = left_chat_participant['left_chat_participant'].get('username', '') # User ID User Request left_chat_participant
                        
                        # Send Notify
                        await bot.sendMessage(chat_id, f'*Selamat Tinggal* @{username}\n\n*First Name:* `{first_name}`\n*Last Name:* `{last_name}`\n*User ID:* `{user_id}`\n*Username:* @{username}', 'Markdown')
    ####################################################################################################################################################################################################################
                if 'message' in getLogs:

                    # Environment Normal
                    chat_id = getLogs["message"]['chat']['id']
                    chat = getLogs["message"].get("text", "")
                    replychat = getLogs["message"].get("message_id", "")
                    username = getLogs["message"]["from"].get("username", "")
                    first_name = getLogs["message"]["from"].get("first_name", "")
                    last_name = getLogs["message"]["from"].get("last_name", "")
                    user_id = getLogs["message"]["from"].get("id", "")
                    gemini_text = getLogs['message'].get('text', '') or getLogs['message'].get('caption', '')
                    openai_text = getLogs['message'].get('caption', '') or getLogs['message'].get('text', '')
                    message_id = getLogs['message'].get('message_id', '')
                    
                    # status member admin Or Not
                    load_gCM = await bot.getChatMember(chat_id, user_id)
                    status_member = load_gCM["result"]["status"]
                    # Command
                    if chat == '/start': # /Start
                        await bot.sendMessage(chat_id, f"*Hallo👋*\n\n*First Name: * `{first_name}`\n*Last Name: * `{last_name}`\n*Username: * `{username}`\n*User ID: * `{user_id}`\n", "Markdown", replychat)
                    elif chat =='/help': # /Help
                        await bot.sendMessage(chat_id, f"*Ini Dari Help*", "Markdown", replychat)
                    elif chat == '/cekgempa': # Gempa
                        Tanggal, Jam, DateTime, Coordinates, Lintang, Bujur, Magnitude, Kedalaman, Wilayah, Potensi, Dirasakan, Shakemap = await CekGempa.ObtainInfo()
                        await bot.sendPhoto(chat_id, f"{Shakemap}", f"*⚠Informasi Gempa*\n\n"
                                            f"*Tanggal*: `{Tanggal}`\n"
                                            f"*Jam*: `{Jam}`\n"
                                            f"*Hari Dan Waktu*: `{DateTime}`\n"
                                            f"*Koordinat*: `{Coordinates}`\n"
                                            f"*Lintang*: `{Lintang}`\n"
                                            f"*Bujur*: `{Bujur}`\n"
                                            f"*Magnitude*: `{Magnitude}`\n"
                                            f"*Kedalaman*: `{Kedalaman}`\n"
                                            f"*Wilayah*: `{Wilayah}`\n"
                                            f"*Potensi*: `{Potensi}`\n"
                                            f"*Dirasakan*: `{Dirasakan}`\n\n"
                                            f"[Informasi Lebih Lanjut Dapat Dilihat Disini](https://warning.bmkg.go.id)", "Markdown", replychat)
                    elif chat == '/speedtest':
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            download, upload, ping, provider, isp, location, speedtest_picture = Speedtest.Active()
                            await bot.sendPhoto(chat_id, f"{speedtest_picture}", f"*Download:* `{download}` *Mbps*\n*Upload:* `{upload}` *Mbps*\n*Ping:* `{ping}` *ms*\n*Provider:* `{provider}`\n*Location:* `{location}`\n*ISP:* `{isp}`", "Markdown", replychat)
                        else:
                            print(f"User ID: {user_id} Tidak Berada Di AcceptedList")
                            await bot.sendMessage(chat_id, f"*Maaf Seperti Anda Tidak Memiliki Hak Penuh Untuk Melakukan Speedtest*", "Markdown", replychat)
                    elif chat == '!unmute':
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            in_unmute = getLogs['message']
                            beautify_unmute = json.dumps(in_unmute, indent=2)
                            if "forward_from" in beautify_unmute:
                                forward_from = in_unmute['reply_to_message']['forward_from']
                                
                                # User Info
                                forward_from_user_id = forward_from['id']
                                forward_from_username = forward_from.get('username', '')
                                await bot.unrestrictChatMember(chat_id, user_id=forward_from_user_id)
                                await bot.sendMessage(chat_id, f"*User* @{forward_from_username} *Telah Dilepaskan Dari Bisu*", "Markdown", replychat)
                            elif "reply_to_message" in beautify_unmute:
                                reply_to_message = in_unmute['reply_to_message']['from']
                                
                                # User Info
                                reply_to_message_user_id = reply_to_message['id']
                                reply_to_message_username = reply_to_message.get('username', '')
                                await bot.unrestrictChatMember(chat_id, user_id=reply_to_message_user_id)
                                await bot.sendMessage(chat_id, f"*User* @{reply_to_message_username} *Telah Dilepaskan Dari Bisu*", "Markdown")
                            else:
                                await bot.sendMessage(chat_id, "*Saya Tidak Dapat Melepaskan Bisu Seseorang Tanpa Chat Yang Sudah Dibalas,Silahkan Balas Chat User Yang Anda Kirim Untuk Lepas Bisu Nya*", "Markdown", replychat)
                        else:
                            pass
                        
                    elif chat == '!info':
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            info_users = getLogs['message']
                            beautify_info_user = json.dumps(info_users, indent=2)
                            if "forward_from" in beautify_info_user:
                                forward_from = info_users['reply_to_message']['forward_from']
                                
                                # User Info
                                first_name_forward_from = forward_from.get('first_name', '')
                                last_name_forward_from = forward_from.get('last_name', '')
                                user_id_forward_from = forward_from.get('id', '')
                                username_forward_from = forward_from.get('username', '')
                                
                                #print('forward_from')
                                # Get Photo
                                file_id = await bot.getUserProfilePhotos(chat_id, user_id_forward_from)                                
                                # Send Photo
                                await bot.sendPhoto(chat_id, f'{file_id}', f'*Information User*\n\n*First Name:* `{first_name_forward_from}`\n*Last Name:* `{last_name_forward_from}`\n*User ID:* `{user_id_forward_from}`\n*Username:* @{username_forward_from}\n ', 'Markdown', replychat)
                            elif "reply_to_message" in beautify_info_user:
                                reply_to_message = info_users['reply_to_message']['from']
                                
                                # User Info
                                first_name_reply_to_message = reply_to_message.get('first_name', '')
                                last_name_reply_to_message = reply_to_message.get('last_name', '')
                                user_id_reply_to_message = reply_to_message.get('id', '')
                                username_reply_to_message = reply_to_message.get('username', '')
                                
                                #print('reply_to_message')
                                # Get Photo
                                file_id = await bot.getUserProfilePhotos(chat_id, user_id_reply_to_message)                                
                                # Send Photo
                                await bot.sendPhoto(chat_id, f'{file_id}', f'*Information User*\n\n*First Name:* `{first_name_reply_to_message}`\n*Last Name:* `{last_name_reply_to_message}`\n*User ID:* `{user_id_reply_to_message}`\n*Username:* @{username_reply_to_message}\n ', 'Markdown', replychat)
                            else:
                                await bot.sendMessage(chat_id, '*Saya Tidak Dapat Mendapatkan Info Seorang Tanpa Anda Membalas Pesan Orang Yang Ingin Di ketahui Informasinya*', 'Markdown', replychat)
                        else:
                            pass
                    elif chat == '!whitelist_group':
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            target_group = getLogs['message']['chat'].get('title', '')
                            target_chat_id = getLogs['message']['chat'].get('id', '')
                            AddWhitelistGroup.Group(target_group=target_chat_id)
                            await bot.sendMessage(chat_id, f'*Grup* `{target_group}`\n\n *Telah Di Tambahkan Ke Whitelist Grup, Grup Ini Akan Diabaikan Dari Mute BOT Jika Ada Badword/Kriptod*', 'Markdown', replychat)
                        else:
                            pass
                    elif chat == '!unwhitelist_group':
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            target_group = getLogs['message']['chat'].get('title', '')
                            target_chat_id = getLogs['message']['chat'].get('id', '')
                            DeleteWhitelistGroup.Group(target_group=target_chat_id)
                            await bot.sendMessage(chat_id, f'*Grup* `{target_group}`\n\n *Telah Di Hapus Kedalam Whitelist Grup, BOT Akan Mute Jika Ada Badword/Kriptod*', 'Markdown', replychat)
                        else:
                            pass
                    elif chat == '!promote_user':
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            await bot.sendMessage(chat_id, f'*Tolong Berikan Title Untuk Memberikan Hak Admin Ke User Contoh: !promote_user * `<title admin>`', 'Markdown', replychat)
                        else:
                            pass
###################startswith########################################################################################################################################################################                    
                    elif chat.startswith('!promote_user '):
                        custom_title = chat[14:]
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            user_id = getLogs['message']['reply_to_message']['from'].get('id', '')
                            username = getLogs['message']['reply_to_message']['from'].get('username', '')
                            
                            await bot.promoteChatMember(chat_id, user_id)
                            await bot.setChatAdministratorCustomTitle(chat_id, user_id, custom_title)
                            await bot.sendMessage(chat_id, f"*User* @{username} *Telah di Promosikan Menjadi Admin*", "Markdown", replychat)
                        else:
                            pass
                    elif chat.startswith('/add_filter '):
                        TargetText = chat[12:]
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            AddBadword.Target(Badword=TargetText)
                            await bot.sendMessage(chat_id, f"*Teks* `{TargetText}` *Telah Ditambahkan Ke Filter*", "Markdown", replychat)
                        else:
                            pass
                    elif chat.startswith('/download '): # Download Video
                        VidUrl = chat[10:]
                        DownloadFrom.Video(VidUrl)
                        await bot.sendVideo(chat_id, f"{GetFilePath.FileMP4()}", f"Downloaded Video From: `{VidUrl}`", "Markdown", replychat)
                        if ".mp4" in GetFilePath.FileMP4():
                            try:
                                os.remove(GetFilePath.FileMP4())
                            except:
                                print(f"Unable To Deleted Video From Path: {GetFilePath.FileMP4()}")
                    elif chat.startswith('/duckchat '): # /duckchat
                        question = chat[10:]
                        DuckChatAnswer = await AI.DuckDuckGoAI(question)
                        await asyncio.sleep(1)
                        await bot.sendMessage(chat_id, f"{DuckChatAnswer}", "Markdown", replychat)
                    elif gemini_text.startswith('/gemini '): # /gemini
                        if 'message' in getLogs:
                            if 'photo' in getLogs['message']:
                                json_photo = getLogs['message']
                                
                                # Environment Photo
                                ask = getLogs['message'].get('caption', '')
                                question = ask[8:] # Caption Image
                                file_id = (
                                    getLogs['message']['photo'][4].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 4 else '' or
                                    getLogs['message']['photo'][3].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 3 else '' or
                                    getLogs['message']['photo'][2].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 2 else '' or
                                    getLogs['message']['photo'][1].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 1 else ''
                                )
                                get_filepath = await bot.getFile(file_id)
                                file_path = get_filepath['result']['file_path']
                                url_path = f'https://api.telegram.org/file/bot{TelegramBOT_TOKEN}/{file_path}'
                                
                                # Download Image
                                await Download.Image(target_url=url_path)
                                image_dir = GetFilePath.FileJPG()
                                
                                
                                # Gemini Answer
                                GeminiPictureAnswer = ""
                                GeminiPictureAnswer = await AI.Gemini.Images(question)

                                # Write To Telegraph
                                get_users = getLogs['message']['from'].get('username', '')
                                title_telegraph = f"Result Answer From: {get_users}"
                                TelegraphLinks = Telegraph.Write(text=GeminiPictureAnswer, question=title_telegraph)
                                
                                if len(GeminiPictureAnswer)> 4097:
                                    await bot.sendMessage(chat_id, f'*Maaf Jawaban Kamu Melebihi 4096 Karakter Dikarenakan Pembatasan Telegram BOT API, Maka Silahkan Melihat Melewati Link Dibawah Ini\n*[Klik Disini Untuk Melihat Jawaban]({TelegraphLinks})', 'Markdown', replychat)
                                else:
                                    await bot.sendMessage(chat_id, f'{GeminiPictureAnswer}', 'Markdown', replychat)
                                    try:
                                        os.remove(image_dir)
                                    except:
                                        pass
                            else:
                                ask = getLogs['message'].get('text', '')
                                question = ask[8:]
                                GeminiTextAnswer = ""
                                GeminiTextAnswer = await AI.Gemini.Text(question)

                                # Write To Telegraph
                                get_users = getLogs['message']['from'].get('username', '')
                                title_telegraph = f"Result Answer From: {get_users}"
                                TelegraphLinks = Telegraph.Write(text=GeminiTextAnswer, question=title_telegraph)
                                                                
                                if len(GeminiTextAnswer) > 4097:
                                    await bot.sendMessage(chat_id, f'*Maaf Jawaban Kamu Melebihi 4096 Karakter Dikarenakan Pembatasan Telegram BOT API, Maka Silahkan Melihat Melewati Link Dibawah Ini\n*[Klik Disini Untuk Melihat Jawaban]({TelegraphLinks})', 'Markdown', replychat)
                                else:
                                    await bot.sendMessage(chat_id, f'{GeminiTextAnswer}', 'Markdown', replychat)
                    elif openai_text.startswith('/gpt '): # Azure ChatGPT
                        if 'message' in getLogs:
                            if 'photo' in getLogs['message']:
                                question = openai_text[5:]
                                file_id = (
                                    getLogs['message']['photo'][4].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 4 else '' or
                                    getLogs['message']['photo'][3].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 3 else '' or
                                    getLogs['message']['photo'][2].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 2 else '' or
                                    getLogs['message']['photo'][1].get('file_id', '')
                                    if len(getLogs['message']['photo']) > 1 else ''
                                )
                                get_filepath = await bot.getFile(file_id)
                                file_path = get_filepath['result']['file_path']
                                url_path = f'https://api.telegram.org/file/bot{TelegramBOT_TOKEN}/{file_path}'
                                
                                # Download Image
                                await Download.Image(target_url=url_path)
                                image_dir = GetFilePath.FileJPG()
                                
                                # OpenAI Answer
                                OpenAIImg = None
                                OpenAIImg = AI.AzureOpenAI.Images(question)
                                
                                # Write To Telegraph
                                get_users = getLogs['message']['from'].get('username', '')
                                title_telegraph = f"Result Answer From: {get_users}"
                                TelegraphLinks = Telegraph.Write(text=OpenAIImg, question=title_telegraph)
                                
                                # Check Text Caracter
                                if len(OpenAIImg) > 4097:
                                    await bot.sendMessage(chat_id, f'*Maaf Jawaban Kamu Melebihi 4096 Karakter Dikarenakan Pembatasan Telegram BOT API, Maka Silahkan Melihat Melewati Link Dibawah Ini\n*[Klik Disini Untuk Melihat Jawaban]({TelegraphLinks})', 'Markdown', replychat)
                                    try:
                                        os.remove(image_dir)
                                    except:
                                        pass
                                else:
                                    await bot.sendMessage(chat_id, f"{OpenAIImg}", "Markdown", replychat)
                                    try:
                                        os.remove(image_dir)
                                    except:
                                        pass
                            else:
                                question = openai_text[5:]
                                OpenAIText = AI.AzureOpenAI.Text(question)
                                
                                # Write To Telegraph
                                get_users = getLogs['message']['from'].get('username', '')
                                title_telegraph = f"Result Answer From: {get_users}"
                                TelegraphLinks = Telegraph.Write(text=OpenAIText, question=title_telegraph)
                                
                                # Check Message More Than 4097 Character
                                if len(OpenAIText) > 4097:
                                    await bot.sendMessage(chat_id, f'*Maaf Jawaban Kamu Melebihi 4096 Karakter Dikarenakan Pembatasan Telegram BOT API, Maka Silahkan Melihat Melewati Link Dibawah Ini\n*[Klik Disini Untuk Melihat Jawaban]({TelegraphLinks})', 'Markdown', replychat)
                                else:
                                    await bot.sendMessage(chat_id, f"{OpenAIText}", "Markdown", replychat)
                    elif chat == '/pin':
                        user_id = getLogs["message"]["from"]["id"]
                        message_id = getLogs["message"]["reply_to_message"]["message_id"]
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            await bot.pinChatMessage(chat_id, message_id)
                            await asyncio.sleep(2)
                            await bot.sendMessage(chat_id, f"*Pesan Sudah Saya Pin*", "Markdown", replychat)
                        else:
                            await bot.sendMessage(chat_id, f"*Maaf Seperti Anda Tidak Memiliki Hak Penuh Untuk Melakukan Pin Pesan*", "Markdown", replychat)
                    elif chat == '/unpin':
                        user_id = getLogs["message"]["from"]["id"]
                        message_id = getLogs["message"]["reply_to_message"]["message_id"]
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            await bot.unpinChatMessage(chat_id, message_id)
                            await asyncio.sleep(2)
                            await bot.sendMessage(chat_id, f"*Pesan Sudah Saya Unpin*", "Markdown", replychat)
                        else:
                            await bot.sendMessage(chat_id, f"*Maaf Seperti Anda Tidak Memiliki Hak Penuh Untuk Melakukan Unpin Pesan*", "Markdown", replychat)
                    elif chat.startswith('!py '):
                        command_in = chat[4:]
                        user_id = getLogs["message"]["from"]["id"]
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            result_command = Run.PythonTerminal(command_in)
                            await bot.sendMessage(chat_id, f"<b>Input Command</b>\n<pre language='python'>{command_in}</pre>\n\n<b>Output Command</b>\n<pre>{result_command}</pre>", "HTML", replychat)
                        else:
                            await bot.sendMessage(chat_id, f"*Maaf Seperti Anda Tidak Memiliki Hak Penuh Untuk Menjalankan Command Ini*", "Markdown", replychat)
                    elif chat.startswith('!info'):
                        pass
#######################################################################################################################################################################################################
                    if CheckGroup.Whitelist(target_group=chat_id):
                        pass
                    else:
                        if status_member == "creator" or status_member == "admin" and CheckUser.Approval(user_id):
                            pass
                        else:
                            chat_users = chat
                            if CheckBadword.ChatUser(chat_users):
                                await bot.restrictChatMember(chat_id, user_id, until_date=ConvertTimeTo.UnixTime.oneday())
                                await bot.sendMessage(chat_id, f"*User* @{username} *Telah Dibisukan Selama 1 Hari\nAlasan:* `Badword`", "Markdown")
                            elif CheckChatKriptod.ChatUser(chat_users):
                                await bot.restrictChatMember(chat_id, user_id)
                                await bot.deleteMessage(chat_id, message_id=message_id)
                                await bot.sendMessage(chat_id, f"*User* @{username} *Telah Dibisukan Permanent\nAlasan:* `Kriptod`", "Markdown")
                            else:
                                pass
#######################################################################################################################################################################################################
        await asyncio.sleep(1)

# Run
try:
    asyncio.run(bot.ClearLog())
    asyncio.run(main())
except Exception as ex:
    print(f'[ERROR] Unable To Running BOT\nReason: {ex}')
    print(f'[INFO] Trying To Running BOT Again')    
    try:
        asyncio.run(bot.ClearLog())
        asyncio.run(main())
    except:
        print(f'[ERROR]: Unable To Running Bot')
        print(f'[INFO] Trying To Running BOT Again')
        try:
            print(f'[INFO] Success Running BOT Again')
            # Run Bot Again
            asyncio.run(bot.ClearLog())
            asyncio.run(main())
        except:
            print(f'[CRITICAL] Unable To Running BOT Again')
except KeyboardInterrupt as key_int:
    print(f'[INFO] Bot Killed\nReason: {key_int}')


