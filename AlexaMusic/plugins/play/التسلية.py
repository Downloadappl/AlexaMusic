import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from AlexaMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "**اليك اوامر التسلية **"




REPLY_MESSAGE_BUTTONS = [

         [

             ("‹ غنيلي ›"),                   

             ("‹ متحركه ›")




          ],

          [

             ("‹ اقتباسات ›"),

             ("‹ اسمي ›")

          ],

          [
              
             ("━━━━━━━━━━━━"),
              
          ],

          [
              
              ("‹ لو خيروك ›"),                   

             ("‹ كت تويت ›")
              
          ],

          [ 
              
              ("‹ فيلم ›"),                   

             ("‹ صراحه ›")

          ],

          [
              
             ("━━━━━━━━━━━━"),
              
          ],

          [ 

             ("‹ انمي ›"),

             ("‹ صور ›")

          ],

          [

             ("‹ ستوريات ›"),

             ("‹ قصائد ›")

          ],

          [
              
             ("━━━━━━━━━━━━"),

          ],

          [

             ("‹ هيدرات ›"),

             ("‹ قران ›")

          ],

          [
     
             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^‹ اوامر التسليه ›$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("**- تم اخفاء الازرار بنجاح**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("."))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""[تحديثات بلاك 🧚](https://t.me/H_M_Dr)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🧚", url=f"https://t.me/H_M_Dr"),
                ],[
                    InlineKeyboardButton(
                        "", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
