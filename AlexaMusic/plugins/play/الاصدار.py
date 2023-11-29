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
    command(["."])
  
)
async def bkouqw(client: Client, message: Message):
        caption=f"""**[تحديثات بلاك 🧚‍♀️](t.me/H_M_Dr)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🧚‍♀️", url=f"https://t.me/H_M_Dr"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

