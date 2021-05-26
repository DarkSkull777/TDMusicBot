from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Haii {message.from_user.first_name} My Name is TD Music Bot ┏┛\n Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah Saya Memiliki Banyak Fitur Praktis Seperti : ┏━━━━━━━━━━━━━━ ┣• Memutar Musik. ┣• Mendownload Lagu. ┣• Mencari Lagu Yang ingin di Putar atau di Download. ┗━━━━━━━━━━━━━━ ❃ Managed With ☕️ By : [Tofik Denianto](https://t.me/tofik_dn) ━━━━━━━━━━━━━━━ Ingin Menambahkan Saya ke Group Anda? Tambahkan Saya Ke Group Anda! </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Group ➕", url="https://t.me/tofikdnbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "📷 Instagram", url="https://www.instagram.com/tofik_dn"
                    ),
                    InlineKeyboardButton(
                        "💾 Project Man", url="https://t.me/Lunatic0de"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/tofik_dn"
                    ),
                    InlineKeyboardButton(
                        "Project Man", url="https://t.me/Lunatic0de"
                    )
                ]
            ]
        )
    )
