import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]
GIF_ID =[
        "CgACAgUAAx0Cc6P3UQACA9Bk4Xity-rDQgFbOW_QnuP_c8KzCwACbQsAAiIGEVfBwSVBH4zqZDAE"
]

Mukesh = [
    [
        InlineKeyboardButton(text="ɴᴏᴏʙ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="🥷𝗦𝘂𝗺𝗺𝗼𝗻 𝗺𝗲🥷",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAx0CbwIllwACKIBk4Xy2WIfxwWoeKhKM6P0M1KTXvQACIwkAAuWAeVVBWKnc-78DkzAE"
    )
    umm = await m.reply_gif(
        "CgACAgUAAx0Cc6P3UQACA9Bk4Xity-rDQgFbOW_QnuP_c8KzCwACbQsAAiIGEVfBwSVBH4zqZDAE"
    ) 
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        START_IMG, 
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
   ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [ᴏᴡɴᴇʀ](tg://user?id={OWNER_ID})
  » Mᴇ, I ᴀᴍ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ ᴀs ᴀ ɢᴜɴ. 
  No problem. 
   ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
