from Bot.core.bot import *
import os

logger = logging.getLogger(__name__)


class Twitch(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    async def twitch(self, ctx, name=None):
        files = os.listdir(Bot.JSONDirectory + "/" + "streamers")
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        if name == None:
            await ctx.send("Please choose a partnered twitch user")
            for file in files:
                await ctx.send(file[:-5]) # to remove .json
        else:
            try:
                with open(Bot.JSONDirectory + "/" + "streamers" + "/" + f"{name}.json", 'r') as f:
                    JSON = json.load(f)
                    embed = discord.Embed.from_dict(JSON)
                    await ctx.send(embed=embed)
            except:
                await ctx.send("partnered twitch user does not exist")



# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(Twitch(client))
    logging.info("StartUp loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("StartUp unloaded!")
