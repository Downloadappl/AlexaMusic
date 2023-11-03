# سورس افيونا @ww_2_2

import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**صل على محمد وآل محمد**"

REPLY_MESSAGE_BUTTONS = [
    [
        (""),
    ],
    [
        ("‹ اوامر التشغيل ›"),
        ("‹ اوامرالتفعيل ›")
    ],
    [
        ("‹ المطور ›")
    ],
    [
        (""),
        ("")
    ],
    [
        ("")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي. 🎙")
    ],
    [
        ("صوره"),
        ("")
    ],
    [
        ("")
    ],
    [
        (""),
        ("")
    ],
    [
        ("")
    ],
    [
        (""),
        ("")
    ],
    [
        ("")
    ],
    [
        (""),
        ("")
    ],
    [
        ("")
        
    ],
    [
        (""),
        ("")
    ],
    [
        ("")
        
    ],
    [
        (""),
        ("")
    ],
    [
       ("")
        
    ],
    [
        ("‹ اخفاء الازرار ›")
    ]
]

@app.on_message(filters.regex("^الاعدادات"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^‹ اخفاء الازرار ›$"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح . 🐰\n\n- لاظهار كيب الارشادات /ARN   \n. 🕷**\n\n- لاظهار كيب الاعضاء والتسليه  /AFYN  \n. 🕷**", reply_markup= ReplyKeyboardRemove(selective=True))



@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/9082f22163efb73912bab.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ", url=f"https://t.me/N_G_12"),
            ]
         ]
     )
  )

