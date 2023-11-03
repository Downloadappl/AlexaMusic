from functools import wraps
from config.config import MUST_JOIN
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


def must_join_channel(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(MUST_JOIN, message.from_user.id)
            if MUST_JOIN.isalpha():          
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await message._client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
        except UserNotParticipant:
            return await message.reply(
                    f"🗽يجب ان تشترك في قنـاة البــوب \n **🤖قنـاة الـبـوت ⬅️** @{MUST_JOIN} »\n ♡ \n🖥¦حتى تتمكن من استخدامي\n◍ اشترك ثم اضغط « شغل والاغنيه » مره اخري√",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("‹ اضغط هنا ›", url=f"https://t.me/{MUST_JOIN}"),
                            ],
                            [
                                InlineKeyboardButton("", url=f"https://t.me/SOURCE VEGA "),
                            ] 
                         ] 
                      ) 
                   ) 
        return await func(_, message)    
    return sz_message
