import logging

import discord
from discord import app_commands
from discord.ext import commands
from typing import Literal

from ..tasks import task_remind

logger = logging.getLogger(__name__)


class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping")
    async def slash_cmd_ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong", ephemeral=True)

    @app_commands.command(name="remind")
    async def slash_cmd_remind(
        self,
        interaction: discord.Interaction,
        what: str,
        every: app_commands.Range[int, 1],
        type: Literal["seconds", "minutes", "hours"],
    ):
        guild_id = interaction.guild.id
        channel_id = interaction.channel.id
        user_id = interaction.user.id
        task_ctx = {type: every}
        self.bot.scheduler.add_job(
            task_remind,
            args=(
                self.bot.settings.discord_token,
                guild_id,
                channel_id,
                user_id,
                what,
            ),
            id=f"remind_user_is_awesome:{guild_id}:{channel_id}:{user_id}",
            trigger="interval",
            **task_ctx,
        )
        await interaction.response.send_message(
            f'I will remind you about "{discord.utils.escape_markdown(what)}" every {every} {type}',
            ephemeral=True,
        )

    @commands.hybrid_command(name="sync")
    async def cmd_sync(self, ctx: commands.Context):
        synced = await self.bot.tree.sync()
        await ctx.reply(f"{len(synced)} commands has been synced.")

    async def cog_load(self):
        logger.info(f"{self.__class__.__name__} loaded")

    async def cog_unload(self):
        logger.info(f"{self.__class__.__name__} unloaded")


async def setup(bot):
    await bot.add_cog(BasicCog(bot=bot))
