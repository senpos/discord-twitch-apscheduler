from twitchio.ext import commands


class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def cmd_ping(self, ctx: commands.Context):
        await ctx.reply("pong")


def prepare(bot: commands.Bot):
    bot.add_cog(BasicCog(bot))
