import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait





@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
            f = "administrators"
            async for member in client.iter_chat_members(chat_id, filter=f):
               if member.status == "creator":
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"**- 𝒈𝒓𝒐𝒖𝒑 𝒐𝒘𝒏𝒆𝒓 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 : \n\n⌁︙ 𝒏𝒂𝒎𝒆 : {m.first_name}\n\n⌁︙ 𝒖𝒔𝒆𝒓 : @{m.username}\n\n⌁︙ 𝒃𝒊𝒐 :\n{m.bio}",reply_markup=key)
                 else:
                    return await message.reply("• " + member.user.mention)
                    
                    
   

   
@app.on_message(command(["اسمي","‹ اسمي ›"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""**- اسمك ›**  {message.from_user.mention()}""") 

@app.on_message(command(""))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"︙اوامر البنك كالاتي : \n. — — — — —  — — — — — .\n⌯︙انشاء حساب بنكي\n⌯︙راتب ، بخشيش\n⌯︙استثمار + ( رقم ) \n ⌯︙مضاربه + ( رقم )\n ⌯︙حظ + ( رقم )\n ⌯︙حسابي ، فلوسي\n ⌯︙حسابه ، فلوسه ( بالرد )\n ⌯︙زرف ( بالرد )\n ⌯︙تحويل + رقم ( بالرد )\n ⌯︙توب الحراميه\n ⌯︙توب الفلوس \n ⌯︙تصفير الفلوس \n⌯︙تفعيل ، تعطيل البنك\n. — — — — —  — — — — — .\n⌯︙للمطور الاساسي :\n⌯︙اضف فلوس + مبلغ (بالرد ، بالمعرف)  \n⌯︙تصفير فلوسه ( بالرد ، بالمعرف )\n. — — — — —  — — — — — .")



@app.on_message(command(["",""]) & filters.group )
async def tom(client, message):
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in ahmed:
        ahmed[chat_id] = {}
    if user_id not in ahmed[chat_id]:
        ahmed[chat_id][user_id] = 1
    else:
        ahmed[chat_id][user_id] += 1
    await message.reply_text(f"{ahmed[chat_id][user_id]}")
    if ahmed[chat_id][user_id] >= tom_max:
        try:
        	del ahmed[chat_id][user_id]
        	await client.ban_chat_member(chat_id, user_id)
        	await message.reply("تم طرد العضو")   	
        except:
        	await message.reply("ماعرف اطرده والله ")
        


array = []
@app.on_message(command(["@all", "تاك","تاك للكل"]) & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("**التاك قيد التشغيل حالياً ،**")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🐉**")
    return
  await message.reply_text("**لايقاف الامر اضغط **\n /cancel او اكتب كافي")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("نادي الكل","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.iter_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 5:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(command(["كافي", "/cancel","بس منشن"]))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🐉")
    return
  if message.chat.id not in array:
     await message.reply("**المنشن متوقف بالفعل**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("**تم ايقاف المنشن بنجاح*\n√*")
    return



