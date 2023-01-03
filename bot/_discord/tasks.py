from .bot import get_discord_bot


async def task_remind(channel_id: int, what: str):
    channel = get_discord_bot().get_channel(channel_id)
    await channel.send(what)
