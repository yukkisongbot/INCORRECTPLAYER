# Powered By @BikashHalder@AdityaHalder

from typing import Union
from pyrogram.types import InlineKeyboardButton

from Bikash.config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from Bikash import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ✨",
                url=f"https://t.me/{app.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬",
                url=f"https://t.me/YukkiSongUpdate",
            ),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"https://t.me/Yukkisongsupport",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ]
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬",
                url=f"https://t.me/YukkiSongUpdate"),
            InlineKeyboardButton(
                text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬",
                url=f"https://t.me/Yukkisongsupport")
        ],
        [
            InlineKeyboardButton(
                text="⚙ ❰ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ❱ ⚙",
                callback_data="settings_back_helper"
            )
        ]
    ]
            
    return buttons
