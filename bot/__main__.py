import asyncio

from ._discord.bot import DiscordBot
from ._logging import setup_logging
from ._sched import get_scheduler
from ._twitch.bot import TwitchBot
from .settings import Settings


async def main():
    settings = Settings()
    
    setup_logging(debug=settings.debug)

    scheduler = get_scheduler()

    discord_bot = DiscordBot(
        settings=settings,
        scheduler=scheduler,
    )
    twitch_bot = TwitchBot(
        token=settings.twitch_token,
        prefix=settings.twitch_prefix,
        channels=settings.twitch_channels,
    )

    async with asyncio.TaskGroup() as tg:
        tg.create_task(twitch_bot.start())
        tg.create_task(discord_bot.start(settings.discord_token))

        scheduler.start()


asyncio.run(main())
