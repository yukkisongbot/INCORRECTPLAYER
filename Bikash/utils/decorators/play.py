# Powered By @BikashHalder @AdityaHalder
# ©️ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Bikash.config import PLAYLIST_IMG_URL, PRIVATE_BOT_MODE, adminlist
from Bikash.strings import get_string
from Bikash import YouTube, app
from Bikash.misc import SUDOERS
from Bikash.utils.database import (get_cmode, get_lang,
                                       get_playmode, get_playtype,
                                       is_active_chat,
                                       is_commanddelete_on,
                                       is_served_private_chat)
from Bikash.utils.database.memorydatabase import is_maintenance
from Bikash.utils.inline.playlist import botplaylist_markup


def PlayWrapper(command):
    async def wrapper(client, message):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "🥀 𝐁𝐨𝐭 𝐈𝐬 𝐔𝐧𝐝𝐞𝐫 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐀𝐧𝐜𝐞 , 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰  𝐌𝐢𝐧𝐮𝐭𝐞𝐬, 𝐘𝐨𝐮 𝐒𝐞𝐞 𝐓𝐡𝐞 𝐑𝐞𝐚𝐬𝐨𝐧 𝐓𝐡𝐞𝐧 𝐉𝐨𝐢𝐧 [𝐇𝐞𝐫𝐞](https://t.me/Yukkisongsupport) 🥀"
                )
        if PRIVATE_BOT_MODE == str(True):
            if not await is_served_private_chat(message.chat.id):
                await message.reply_text(
                    "**🔒 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐌𝐮𝐬𝐢𝐜  𝐁𝐨𝐭 🔊**\n\n✅ 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐂𝐡𝐚𝐭𝐬 𝐅𝐫𝐨𝐦 𝐓𝐡𝐞 [𝐎𝐰𝐧𝐞𝐫](https://t.me/JK_ABHISHEK) . 🌷 𝐀𝐬𝐤 𝐌𝐲 👑 𝐎𝐰𝐧𝐞𝐫 𝐓𝐨 𝐀𝐥𝐥𝐨𝐰 𝐘𝐨𝐮𝐫 𝐂𝐇𝐚𝐭 𝐅𝐫𝐢𝐬𝐭 🌸"
                )
                return await app.leave_chat(message.chat.id)
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        audio_telegram = (
            (
                message.reply_to_message.audio
                or message.reply_to_message.voice
            )
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (
                message.reply_to_message.video
                or message.reply_to_message.document
            )
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if (
            audio_telegram is None
            and video_telegram is None
            and url is None
        ):
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_text(_["playlist_1"]
                )
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🛠️ 𝐇𝐨𝐰 𝐓𝐨 𝐅𝐢𝐱 𝐓𝐡𝐢𝐬 ⚒️",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(
                _["general_4"], reply_markup=upl
            )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_18"])
            fplay = True
        else:
            fplay = None
        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
