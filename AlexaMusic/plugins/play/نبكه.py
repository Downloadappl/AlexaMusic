import asyncio

import random

from AlexaMusic import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)

from strings.filters import command

from pyrogram import filters, Client





txt = [


" ︙اوامر البنك كالاتي : \n. — — — — —  — — — — — .\n⌯︙انشاء حساب بنكي\n⌯︙راتب ، بخشيش\n⌯︙استثمار + ( رقم ) \n ⌯︙مضاربه + ( رقم )\n ⌯︙حظ + ( رقم )\n ⌯︙حسابي ، فلوسي\n ⌯︙حسابه ، فلوسه ( بالرد )\n ⌯︙زرف ( بالرد )\n ⌯︙تحويل + رقم ( بالرد )\n ⌯︙توب الحراميه\n ⌯︙توب الفلوس \n ⌯︙تصفير الفلوس \n⌯︙تفعيل ، تعطيل البنك\n. — — — — —  — — — — — .\n⌯︙للمطور الاساسي :\n⌯︙اضف فلوس + مبلغ (بالرد ، بالمعرف)  \n⌯︙تصفير فلوسه ( بالرد ، بالمعرف )\n. — — — — —  — — — — — .  ",


        ]


        


@app.on_message(command(["","البنك"]))

async def ahrof(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
