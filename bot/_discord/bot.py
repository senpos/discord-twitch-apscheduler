import asyncio
import logging
from functools import lru_cache

import discord
from discord.ext import commands

from ..settings import get_settings

logger = logging.getLogger(__name__)

COGS = ("basic",)


class DiscordBot(commands.Bot):
    def __init__(self, *, settings) -> None:
        self.settings = settings

        prefix = commands.when_mentioned_or(settings.discord_prefix)
        intents = discord.Intents.default()
        super().__init__(command_prefix=prefix, help_command=None, intents=intents)

    async def setup_hook(self) -> None:
        logging.debug(f"loading {len(COGS)} cogs")
        await asyncio.gather(*[self.load_extension(f"bot._discord.cogs.{cog}") for cog in COGS])


@lru_cache(maxsize=1)
def get_discord_bot():
    bot = DiscordBot(settings=get_settings())
    return bot
