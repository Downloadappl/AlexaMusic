import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["اوامر البوت","الاوامر",""])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"",
        caption=f"""اهلا بك اوامر سورس فوكس الرسمي

⌯  غنيلي - اغاني جميله ترند

⌯  هيدرات - هيدرات تمبلر

⌯ صوره - صوره منوعه عشوائي

⌯ اقتباس - اقتباسات عشوائيه جميله

⌯ انمي - انمي عشوائي

⌯ افتار شباب - يرسل لك افتارات شباب 

⌯ افتار بنات - يرسل لك افتارات بنات

⌯ @H_M_Dr
⌯ فيلم - يقوم بأرسل فيلم عشوائي

⌯ استوري - يرسل ستوريات عشوائيه لك

⌯ قران - يرسلك لك قران عشوائي

⌯ الاوامر - لعرض قائمه الاوامر

⌯ متحركه - يرسل لك متحركة عشوائيه""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/H_M_Dr"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Ng_45bot"),
                ],
                [
                   InlineKeyboardButton(
                        "", url=f"https://t.me/N_G_12"),
                ],       
            ]
        ),
    )
