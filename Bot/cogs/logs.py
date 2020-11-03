from discord.ext import commands
from discord.ext.tasks import *
from Bot.core.bot import Bot
from discord import File
logger = logging.getLogger(__name__)


class Logs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission))
    async def logs(self, ctx):
        with open(f"/opt/rowans-bot/logs/bot.log", "rb") as f: # TODO - Incorrect Use of f-string
            await ctx.send("Log file")
            await ctx.send(file=discord.File(f,"bot.log"))


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(Logs(client))
    logging.info("LeaveMessage loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("SteamAPI unloaded!")
