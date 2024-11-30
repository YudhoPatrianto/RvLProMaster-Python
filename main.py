from RvLProMaster.run import run
from RvLProMaster.bot import bot
from RvLProMaster.Tools.CekGempa import CekGempa
from json import dumps
import asyncio

async def main():
    while True:
        obtain, user_id, first_name, last_name, username, chat_id, group_title, group_username, chat, reply, channel_title = await run()
        
        # Group/Forums
        if 'message' in obtain:
            if chat == '/start':
                await bot.sendMessage(chat_id, f"*Hi @{username}*\n\n"
                                            f"*First Name: `{first_name}`*\n"
                                            f"*Last Name: `{last_name}`*\n"
                                            f"*User ID: `{user_id}`*\n"
                                            f"*Username: `{username}`*\n\n"
                                            f"*Selamat Datang Di Grup `{group_title}`*\n"
                                            "*Gunakan Command /help Untuk Melihat Semua Command*", 'MarkdownV2', False, False, reply)
            elif chat == '/gempa':
                tanggal_gempa, jam_gempa, datetime_gempa, coordinate_gempa, lintang_gempa, bujur_gempa, magnitude_gempa, kedalaman_gempa, wilayah_gempa, dirasakan_gempa, shakemap_photo = await CekGempa()
                await bot.sendPhoto(chat_id, f"{shakemap_photo}", f"*Gempa Berdasarkan Data Dari [BMKG](https://data.bmkg.go.id/gempabumi)*\n\n" 
                                                                f"*Tanggal: `{tanggal_gempa}`*\n"
                                                                f"*Jam: `{jam_gempa}`*\n"
                                                                f"*Tanggal Dan Waktu: `{datetime_gempa}`*\n"
                                                                f"*Koordinat Gempa: `{coordinate_gempa}`*\n"
                                                                f"*Lintang Gempa: `{lintang_gempa}`*\n"
                                                                f"*Bujur Gempa: `{bujur_gempa}`*\n"
                                                                f"*Magnitude Gempa: `{magnitude_gempa}`*\n"
                                                                f"*Kedalaman Gempa: `{kedalaman_gempa}`*\n"
                                                                f"*Wilayah: `{wilayah_gempa}`*\n"
                                                                f"*Dirasakan Gempa: `{dirasakan_gempa}`*\n\n"
                                                                f"*Informasi Lebih Lanjut Dapat Dilihat* [Disini](https://warning.bmkg.go.id)", 'MarkdownV2', False, False, reply)
        # Channel 
        if 'channel_post' in obtain:
            if chat == '/start':
                await bot.sendMessage(chat_id, f"*Hi I'm Currently Send Message In `Channel` *", 'MarkdownV2', False)

if __name__ == "__main__":
    asyncio.run(main())