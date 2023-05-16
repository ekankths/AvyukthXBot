import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from EkankthRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from EkankthRobot import telethn as tbot
from EkankthRobot.events import register

PHOTO = [
    "https://te.legra.ph/file/4bd5a55cb80993471d589.mp4",
    "https://te.legra.ph/file/4bd5a55cb80993471d589.mp4",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ {dispatcher.bot.first_name}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝄟🐰❤️Pragyan​💞𝄟](https://t.me/PragyanIITIAN)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("👑𝐊𝐈𝐍𝐆👑", f"https://t.me/AboutPragyanIITIAN"),
            Button.url("​👸𝐐𝐔𝐄𝐄𝐍👸", f"https://t.me/KabutarGang"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "👑𝐀𝐋𝐈𝐕𝐄👸"
