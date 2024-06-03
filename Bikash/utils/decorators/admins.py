from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Bikash.config import adminlist
from Bikash.strings import get_string
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database import (get_authuser_names, get_cmode,
                                       get_lang, is_active_chat,
                                       is_commanddelete_on,
                                       is_maintenance,
                                       is_nonadmin_chat)

from ..formatters import int_to_alpha


def AdminRightsCheck(mystic):
    async def wrapper(client, message):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "🥀 𝐁𝐨𝐭 𝐈𝐬 𝐔𝐧𝐝𝐞𝐫 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐀𝐧𝐜𝐞 , 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰  𝐌𝐢𝐧𝐮𝐭𝐞𝐬, 𝐘𝐨𝐮 𝐒𝐞𝐞 𝐓𝐡𝐞 𝐑𝐞𝐚𝐬𝐨𝐧 𝐓𝐡𝐞𝐧 𝐉𝐨𝐢𝐧 [𝐇𝐞𝐫𝐞](https://t.me/Yukkisongsupport) 🥀"
                )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
        except:
            _ = get_string("en")
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="⚒️ 𝐇𝐨𝐰 𝐓𝐨 𝐅𝐢𝐱 𝐓𝐡𝐢𝐬 ? 🛠️",
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
                await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
        else:
            chat_id = message.chat.id
        if not await is_active_chat(chat_id):
            return await message.reply_text(_["general_6"])
        is_non_admin = await is_nonadmin_chat(message.chat.id)
        if not is_non_admin:
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["admin_19"])
        return await mystic(client, message, _, chat_id)

    return wrapper


def AdminActual(mystic):
    async def wrapper(client, message):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "🥀 𝐁𝐨𝐭 𝐈𝐬 𝐔𝐧𝐝𝐞𝐫 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐀𝐧𝐜𝐞 , 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰  𝐌𝐢𝐧𝐮𝐭𝐞𝐬, 𝐘𝐨𝐮 𝐒𝐞𝐞 𝐓𝐡𝐞 𝐑𝐞𝐚𝐬𝐨𝐧 𝐓𝐡𝐞𝐧 𝐉𝐨𝐢𝐧 [𝐇𝐞𝐫𝐞](https://t.me/Yukkisongsupport) 🥀"
                )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
        except:
            _ = get_string("en")
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="⚒️ 𝐇𝐨𝐰 𝐓𝐨 𝐅𝐢𝐱 𝐓𝐡𝐢𝐬 ? 🛠",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(
                _["general_4"], reply_markup=upl
            )
        if message.from_user.id not in SUDOERS:
            try:
                member = await app.get_chat_member(
                    message.chat.id, message.from_user.id
                )
            except:
                return
            if not member.can_manage_voice_chats:
                return await message.reply(_["general_5"])
        return await mystic(client, message, _)

    return wrapper


def ActualAdminCB(mystic):
    async def wrapper(client, CallbackQuery):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    "🥀 𝐁𝐨𝐭 𝐈𝐬 𝐔𝐧𝐝𝐞𝐫 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐀𝐧𝐜𝐞 , 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰  𝐌𝐢𝐧𝐮𝐭𝐞𝐬, 𝐘𝐨𝐮 𝐒𝐞𝐞 𝐓𝐡𝐞 𝐑𝐞𝐚𝐬𝐨𝐧 𝐓𝐡𝐞𝐧 𝐉𝐨𝐢𝐧 [𝐇𝐞𝐫𝐞](https://t.me/Yukkisongsupport) 🥀",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            _ = get_string(language)
        except:
            _ = get_string("en")
        if CallbackQuery.message.chat.type == "private":
            return await mystic(client, CallbackQuery, _)
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            try:
                a = await app.get_chat_member(
                    CallbackQuery.message.chat.id,
                    CallbackQuery.from_user.id,
                )
            except:
                return await CallbackQuery.answer(
                    _["general_5"], show_alert=True
                )
            if not a.can_manage_voice_chats:
                if CallbackQuery.from_user.id not in SUDOERS:
                    token = await int_to_alpha(
                        CallbackQuery.from_user.id
                    )
                    _check = await get_authuser_names(
                        CallbackQuery.from_user.id
                    )
                    if token not in _check:
                        try:
                            return await CallbackQuery.answer(
                                _["general_5"],
                                show_alert=True,
                            )
                        except:
                            return
        return await mystic(client, CallbackQuery, _)

    return wrapper
