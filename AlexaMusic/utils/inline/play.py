from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_GROUP, SUPPORT_CHANNEL
import random

## After Edits with Timer Bar


selections = [
    "▁▄▂▇▄▅▄▅▃",
    "▁▃▇▂▅▇▄▅▃",
    "▃▁▇▂▅▃▄▃▅",
    "▃▄▂▄▇▅▃▅▁",
    "▁▃▄▂▇▃▄▅▃",
    "▃▁▄▂▅▃▇▃▅",
    "▁▇▄▂▅▄▅▃▄",
    "▁▃▅▇▂▅▄▃▇",
    "▃▅▂▅▇▁▄▃▁",
    "▇▅▂▅▃▄▃▁▃",
    "▃▇▂▅▁▅▄▃▁",
    "▅▄▇▂▅▂▄▇▁",
    "▃▅▂▅▃▇▄▅▃",
]


## After Edits with Timer Bar


def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",     
            )
        ],
        [   
            InlineKeyboardButton(
                text="‹ قوائم التشغيل ›",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="", url=f"https://t.me/ZZZ7iZ"
         ),   

            InlineKeyboardButton(
                text="‹ قائمة التحكم ›",
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
                    
            ),
            InlineKeyboardButton(text="", url=f"https://t.me/ZZZ7iZ"),

            InlineKeyboardButton(
                text=f"",
                url=f"https://t.me/Alexa_ManagementBot",
                )
        ],
        [
    return buttons

def telegram_markup_timer(_, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قوائم التشغيل ›",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(text="", url=f"https://t.me/Jankari_Ki_Duniya"),
        
        
            InlineKeyboardButton(
                text="‹ قائمة التحكم ›",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(text="", url=f""),
        ],
        [
    return buttons


## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ قوائم التشغيل ›",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(text="", url=f""),
        

            InlineKeyboardButton(
                text="‹ قائمة التحكم ›",
                callback_data=f"PanelMarkup None|{chat_id}",                
            ),
            InlineKeyboardButton(text="", url=f""),
        ],
        [
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ قائمة التحكم ›",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(text="‹ اغلاق ›", callback_data="close"),
        ],
        [
    return buttons


## By Anon
close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="‹ اغلاق ›", callback_data="close")]]
)

## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
        [
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"‹ قوائم التشغيل › {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"‹ قوائم التشغيل › {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
        [
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"‹ قائمة التحكم › {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
         ],
    [
    return buttons


## Slider Query Markup


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(text="▶️ استئناف ⤈", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏯ تخطي ⤈", callback_data=f"ADMIN Skip|{chat_id}"),
                    ],
                    [
            InlineKeyboardButton(text="⏹ انهاء • ايقاف ⤈", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="",
                url=f"{SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 𝟏𝟎 ثواني ⤈",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 𝟏𝟎 ثواني ⤈",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 𝟑𝟎 ثواني ⤈",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 𝟑𝟎 ثواني ⤈",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="‹ اغلاق ›",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


## Queue Markup Anon


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=">",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(text="⏸ ايقاف مؤقت ⤈", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️ استئناف ⤈", callback_data=f"add_playlist {videoid}"),
        ],
        [    
        
            InlineKeyboardButton(text="⏯ تخطي ⤈", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹ انهاء - ايقاف ⤈", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="‹ اغلاق ›", callback_data=f"ADMIN CloseA|{chat_id}"
            )
        ],
    ]
    return buttons
