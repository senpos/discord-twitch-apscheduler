import logging


from twitchio.ext import commands

logger = logging.getLogger(__name__)
COGS = ("basic",)


class TwitchBot(commands.Bot):
    def __init__(self, *, token, prefix, channels):

        super().__init__(token=token, prefix=prefix, initial_channels=channels)

    async def event_ready(self):
        logging.debug(f"loading {len(COGS)} cogs")
        for cog in COGS:
            self.load_module(f"bot._twitch.cogs.{cog}")
        logger.info(f"logged in as {self.nick}")
