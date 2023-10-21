#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="‹ ايقاف التشغيل موقتاً ›",
            description=f"يقوم بإيقاف التشغيل الحالي على مكالمة الجماعية.",
            thumb_url="https://telegra.ph/file/3221f131bcd35f4a41b04.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="‹ استئناف التشغيل ›",
            description=f"استئناف التشغيل الجاري على مكالمة جماعية.",
            thumb_url="https://telegra.ph/file/ca05aaa4964a13f04090e.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="‹ تخطي الاغنية المشغلة ›",
            description=f"تخطي الاغنيه. | للحصول على رقم المسار المحدد : /skip [رقم المسار] ",
            thumb_url="https://telegra.ph/file/6b4d8c79473c7279f877f.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="‹ انهاء ↫ ايقاف التشغيل ›",
            description="أوقف التشغيل الجاري على المكالمة الجماعية.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="‹ تكرار الاغنية ›",
            description="لتكرار الاغنيه قيد التشغيا الحاليه - تكرار",
            thumb_url="https://telegra.ph/file/25b586a6c4769e80ce50a.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="‹ كتم صوت التشغيل ›",
            description="كتم الصوت المشغل في مكالمة المجموعة.",
            thumb_url="https://telegra.ph/file/7649d9aade76cc63d7165.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
    ]
)
