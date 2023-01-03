import httpx


client = httpx.AsyncClient(base_url="https://discord.com/api/")


async def task_remind(
    token: str,
    channel_id: int,
    what: str,
):
    data = {"content": what}
    response = await client.post(
        f"channels/{channel_id}/messages",
        headers={"Authorization": f"Bot {token}"},
        json=data,
    )
    response.raise_for_status()
