from Bot.cogs.battlemetric import *
from Bot.cogs.reactroles import *
from Bot.cogs.planetside2 import emeraldPopulation

logger = logging.getLogger(__name__)

Voicechannel = 797958943216762880


class voicechat(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel.id == Voicechannel:  # if it's twitch voice channel
            with open(Bot.JSONDirectory + "/" + "Message" + "/" + "TwitchPM.json", 'r') as f:
                JSON = json.load(f)
                embed = discord.Embed.from_dict(JSON)
            await member.send(embed=embed)
        else:
            pass



# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(voicechat(client))
    logging.info("Voicechat loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("Voicechat unloaded!")
