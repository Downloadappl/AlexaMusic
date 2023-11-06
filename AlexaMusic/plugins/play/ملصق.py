from strings.filters import command
from AlexaMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
stiklok =[]

@app.on_message(
    filters.command(["قفل الملصقات","تعطيل الملصقات"])
 
   
)
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفله من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"عزيزي {message.from_user.mention} انت لست مشرف")
    
    
    

@app.on_message(
    filters.command(["فتح الملصقات","تفعيل الملصقات"])
 
   
)
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"عزيزي< {message.from_user.mention} الملصقات مفعله من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم فتح الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"عزيزي {message.from_user.mention} انت لست مشرف")
    
