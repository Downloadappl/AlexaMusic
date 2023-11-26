import asyncio


import random
from AlexaMusic import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "**[تحديثات نيكست 🧚🏻](http://t.me/H_M_Dr)**",
            
            

        ]


        


@app.on_message(command([".","", ""]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
