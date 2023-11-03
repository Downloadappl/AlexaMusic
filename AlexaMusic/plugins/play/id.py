import asyncio
import pyrogram
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import LOG, LOG_GROUP_ID
from AlexaMusic import app
from AlexaMusic.utils.database import is_on_off
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from AlexaMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from AlexaMusic.misc import SUDOERS
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj







#@app.on_message(command(["ا"]) & filters.group &
#async def khalid(client: Client, message: Message):
    #usr = await client.get_users(message.from_user.id)
    #name = usr.first_name
    #async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    #await message.reply_photo(photo.file_id,       caption=f"""ᴜsᴇʀ -› {message.from_user.mention}\n𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 -› @{message.from_user.username}\nɪᴅ -› {message.from_user.id}\nbio » {bio}""", 
        #reply_markup=InlineKeyboardMarkup(

            #[

                #[

                    #InlineKeyboardButton(

                        #name, url=f"https://t.me/{message.from_user.id}")

                #],

            #]

        #),

    #)

@app.on_message(filters.regex("^ا$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""• In the end, you are the bad, and they are the innocent\n\n• 𝑵𝒂𝒎𝒆 -› {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 -› @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 -› Developer Mira\n• 𝑩𝒊𝒐 -› {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=5012406813)

                ],

            ]

        ),

    )
    
    
