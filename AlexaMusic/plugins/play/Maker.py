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
        photo=f"https://telegra.ph/file/d3bed0d2eb1fd5a154369.jpg",
        caption=f"""**اليك اوامر السورس**
        
**⌯︰اوامر التشغيل في المجموعه او القناة ↯.

⌯︰ تشغيل ↫ لتشغيل الموسيقى  
⌯︰فيديو  ↫ لتشغيل مقطع فيديو 
⌯︰تشغيل عشوائي  ↫ لتشغيل اغنيه عشوائيه 


⌯︰اوامر تفعيل البوت ↯.

⌯︰اضف البوت الى المجموعه او القناة
⌯︰ارفع البوت ادمن مع كل الصلاحيات
⌯︰ابدأ مكالمه جماعيه جديده
⌯︰ارسل تشغيل مع اسم المقطع المطلوب
⌯︰سينظم المساعد تلقائيا ويبدا التشغيل
⌯︰في حال لم ينضم المساعد راسل المطور**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/H_M_Dr"),
                    InlineKeyboardButton(
                        "", url=f""),
                ],
                [
                   InlineKeyboardButton(
                        "", url=f"https://t.me/N_G_12"),
                ],       
            ]
        ),
    )
