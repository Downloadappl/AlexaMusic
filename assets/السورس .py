import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["","","",""])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dec37b1ceff618f25a39a.jpg",
        caption=f"""**[ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 sᴏᴜʀᴄᴇ ғᴏх.](https://t.me/H_M_Dr)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ المطور ›", url=f"https://t.me/IIIlIIv"), 
                    
                
                    InlineKeyboardButton(
                        "‹ لتنصيب بوت ›", url=f"tg://user?id=5012406813"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/H_M_Dr"),
                
        ],

            ]

        ),

    )
