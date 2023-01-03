import asyncio

from ._discord.bot import get_discord_bot
from ._logging import setup_logging
from ._sched import get_scheduler
from ._twitch.bot import get_twitch_bot
from .settings import get_settings


async def main():
    settings = get_settings()
    setup_logging(debug=settings.debug)
    async with asyncio.TaskGroup() as tg:
        tg.create_task(get_twitch_bot().start())
        tg.create_task(get_discord_bot().start(settings.discord_token))
        get_scheduler().start()


asyncio.run(main())
