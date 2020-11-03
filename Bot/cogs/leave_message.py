from discord.ext import commands
from discord.ext.tasks import *
from Bot.core.bot import Bot
logger = logging.getLogger(__name__)


class LeaveMessage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        try:
            channel = self.client.get_channel(589941950837293070)
            # embed = discord.Embed(colour=discord.Colour(16711680),
            #                       description=f'{member.display_name}\n\n **has left the server**')
            # embed.set_thumbnail(url=member.avatar_url)
            # embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            # await channel.send(embed=embed)
            await channel.send(f"{member.display_name} has left the server")
        except:
            logging.exception("Got exception on main handler")
            raise


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(LeaveMessage(client))
    logging.info("LeaveMessage loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("SteamAPI unloaded!")
