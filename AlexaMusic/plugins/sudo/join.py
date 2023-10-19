from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AlexaMusic import app
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not SUPPORT_IQ:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(SUPPORT_IQ, msg.from_user.id)
        except UserNotParticipant:
            if SUPPORT_IQ.isalpha():
                link = "https://t.me/" + SUPPORT_IQ
            else:
                chat_info = await bot.get_chat(SUPPORT_IQ)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"**⚠️ | عزيزي المشترك عليك الاشتراك في قنـاة البوت @ZZZ7iZ • تأكد من الاشتراك ثم اضغط /start ✅**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("‹ اضغط هنا ›", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {SUPPORT_IQ} !")
