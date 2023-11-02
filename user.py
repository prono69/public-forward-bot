from config import Config
from config import LOGGER
from pyrogram import Client, __version__
import asyncio
BOT_USERNAME=Config.BOT_USERNAME

class User(Client):
    def __init__(self):
        super().__init__(
            name="user_session",
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            session_string=Config.SESSION,
            workers=10
        )
        self.LOGGER = LOGGER
        self.storage.session_string=Config.SESSION

    async def start(self):
        await super().start()
        if BOT_USERNAME:
            await User.send_message(self, chat_id=BOT_USERNAME, text="/forward")
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
