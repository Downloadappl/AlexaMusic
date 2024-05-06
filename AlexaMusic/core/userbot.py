# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with a variety of purposes.
Copyright (c) 2024 - present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and modify
as you want or you can collaborate if you have new ideas.
"""
from AlexaMusic.core.userbot import Userbot
import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AlexaOne",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AlexaTwo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AlexaThree",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AlexaFour",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AlexaFive",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients...")
        for num in range(1, 6):
            client = getattr(self, f"_{num}")
            if getattr(config, f"STRING{num}"):
                await client.start()
                try:
                    await client.join_chat("Alexa_Help")
                    await client.join_chat("TheTeamAlexa")
                    await client.join_chat("Alexa_BotUpdates")
                except:
                    pass
                assistants.append(num)
                try:
                    await client.send_message(
                        config.LOG_GROUP_ID,
                        "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                    )
                except:
                    LOGGER(__name__).error(
                        f"Assistant Account {num} has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                    )
                    sys.exit()
                get_me = await client.get_me()
                client.username = get_me.username
                client.id = get_me.id
                assistantids.append(get_me.id)
                if get_me.last_name:
                    client.name = get_me.first_name + " " + get_me.last_name
                else:
                    client.name = get_me.first_name
                LOGGER(__name__).info(f"Assistant {num} Started as {client.name}")
