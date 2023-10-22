#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AlexaMusic.utils.database import is_on_off
from AlexaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "محادثه خاصه"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**💞 {MUSIC_BOT_NAME} سجل التشغيل **
**━━━━━━━━━━━━━━━**
** اسم المجموعة : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
** اسم المستخدم : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
** يوزر المستخدم : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
** ايدي المستخدم : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
** رابط الكروب : >** {chatusername}
**━━━━━━━━━━━━━━━**
** المطلوب :** {message.text}
**━━━━━━━━━━━━━━━**
**نوع التشغيل :** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
