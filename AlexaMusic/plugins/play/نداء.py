
import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AlexaMusic import app
from strings.filters import command

@app.on_message(command(['نداء','ن']))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"**وجهـڪ ڪمر وضحڪتڪ العيد :** {random_member_mention}",
        f"**حبــي الـڪ ادمان :** {random_member_mention}",
        f"**سبلـوش تــوت :** {random_member_mention}",
        f"**تعـا نورنـھَہّ يقمر :** {random_member_mention}",
        f"**تع ابوسـڪ يعسل :** {random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')



@app.on_message(command(['زوجني','ز']))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"**⌔︙الف مبروك تم زواجك من :** {random_member_mention} \n **",
        f"**⌔︙الف مبروك تم زواجك من :** \n {random_member_mention} \n **"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')



