from Bikash.strings import get_string
from Bikash.misc import SUDOERS
from Bikash.utils.database import (get_lang, is_commanddelete_on,
                                       is_maintenance)


def language(mystic):
    async def wrapper(_, message, **kwargs):
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
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    "🥀 𝐁𝐨𝐭 𝐈𝐬 𝐔𝐧𝐝𝐞𝐫 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐀𝐧𝐜𝐞 , 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰  𝐌𝐢𝐧𝐮𝐭𝐞𝐬, 𝐘𝐨𝐮 𝐒𝐞𝐞 𝐓𝐡𝐞 𝐑𝐞𝐚𝐬𝐨𝐧 𝐓𝐡𝐞𝐧 𝐉𝐨𝐢𝐧 [𝐇𝐞𝐫𝐞](https://t.me/Yukkisongsupport) 🥀",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
