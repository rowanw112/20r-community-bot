from discord.ext import commands
from discord.ext.tasks import *
from Bot.core.bot import Bot
from discord import File

logger = logging.getLogger(__name__)


class Logs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def logs(self, ctx):
        with open(Bot.LogDirectory + "/bot.log", "rb") as f:
            await ctx.send("Log file")
            await ctx.send(file=discord.File(f, "bot.log"))


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(Logs(client))
    logging.info("LeaveMessage loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("SteamAPI unloaded!")
