from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME
from helpers.filters import command
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> Heii {message.from_user.first_name} Aku [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ┏┛\n
Aku Memiliki Banyak Fitur Praktis Seperti:

~ Memutar Musik.
~ Mendownload Lagu.
~ Mencari Lagu Yang ingin di Putar atau di Download.

Ketik » /help « Untuk Melihat Daftar Perintah
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Tambahkan Ke Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "Asisten ku", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "🔥Owner", url="https://t.me/xskull7"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )


@Client.on_message(command(["start", "start@dimastapimusic_bot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""Aku aktif!\n<b>Up sejak:</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥Owner", url="https://t.me/xskull7"
                    ),
                    InlineKeyboardButton(
                        "🌹Website", url="https://darkskull7.my.to"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hei {message.from_user.first_name}!
\n/play (judul lagu) - Untuk Memutar lagu yang Anda minta melalui YouTube
/playlist - Untuk Menampilkan daftar putar Lagu sekarang
/current - Untuk Menunjukkan  Lagu sekarang yang sedang diputar
/song (judul lagu) - Untuk Mendownload lagu dari YouTube 
/search (judul video) - Untuk Mencari Video di YouTube dengan detail
/video (judul video) - Untuk Mendownload Video di YouTube dengan detail
\n**Admins Only:**
/player - Open music player settings panel
/pause - Untuk Menjeda pemutaran Lagu
/resume - Untuk Melanjutkan pemutaran Lagu yang di pause
/skip - Untuk Menskip pemutaran lagu ke Lagu berikutnya
/end - Untuk Memberhentikan pemutaran Lagu
/userbotjoin - Untuk Mengundang asisten ke obrolan Anda
/reload - Untuk Merefresh admin list
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Website", url="https://darkskull7.my.to"
                    ),
                    InlineKeyboardButton(
                        "Creator", url="https://t.me/xskull7"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("ping") & ~filters.edited)
async def ping_pong(client: Client, m: Message):
    start = time()
    m_reply = await m.reply_text("`Memeriksa kekuatan sinyal...`")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"{emoji.PING_PONG} **DORR!!**\n"
        f"`{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command("uptime") & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"{emoji.ROBOT}\n"
        f"• **Waktu aktif:** `{uptime}`\n"
        f"• **Waktu mulai:** `{START_TIME_ISO}`"
    )
