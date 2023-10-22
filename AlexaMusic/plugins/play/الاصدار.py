import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d3bed0d2eb1fd5a154369.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس فوكس
★᚜ اسم سورس : فوكس

★᚜ نوع : ميوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : Fox بوت ميوزك
★᚜ الاصدار 1.0
★᚜ تاريخ التأسيس : 2023/11/20

★᚜ مؤسس فوكس : [ ﻿حِــۘـمَــٓد | 🇮🇶](https://t.me/IIIlIIv)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ғᴏх.", url=f"https://t.me/H_M_Dr"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

