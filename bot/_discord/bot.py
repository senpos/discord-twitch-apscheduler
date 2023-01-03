import asyncio
import logging

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

COGS = ("basic",)


class DiscordBot(commands.Bot):
    def __init__(self, *, settings, scheduler) -> None:
        self.settings = settings
        self.scheduler = scheduler
        super().__init__(
            command_prefix=commands.when_mentioned_or(settings.discord_prefix),
            help_command=None,
            intents=discord.Intents.default(),
        )

    async def setup_hook(self) -> None:
        logging.debug(f"loading {len(COGS)} cogs")
        await asyncio.gather(*[self.load_extension(f"bot._discord.cogs.{cog}") for cog in COGS])
