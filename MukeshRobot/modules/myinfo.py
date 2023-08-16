import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from MukeshRobot import telethn as bot,BOT_NAME
from MukeshRobot import telethn as tgbot
from MukeshRobot.events import register

edit_time = 5
f""" ======================={BOT_NAME}====================== """
file1 = "https://te.legra.ph/file/3ba3f11b3872fa647c658.jpg"
file2 = "https://te.legra.ph/file/e2ccd9c6dd5fbbaa7b240.jpg"
file3 = "https://te.legra.ph/file/87bb36875aca1300b494f.jpg"
file4 = "https://te.legra.ph/file/80b90b137bd511ce4e089.jpg"
file5 = "https://telegra.ph/file/701028ce085ecfa961a36.jpg"
""" ======================={BOT_NAME}====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("ɪɴғᴏʀᴍᴀᴛɪᴏɴ", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"ʜᴇʏ {firstname}, \nᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ \n ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ʏᴏᴜ",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME}\n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ: {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ: {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        LILIE += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
        LILIE += f"ᴜsᴇʀ ɪᴅ: {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : @{PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
__mod_name__ = "Iɴғᴏ"
__help__ = """
 /myinfo  ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏ """
