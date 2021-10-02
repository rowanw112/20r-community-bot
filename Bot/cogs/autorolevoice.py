from Bot.cogs.battlemetric import *
from Bot.cogs.reactroles import *
from Bot.cogs.planetside2 import emeraldPopulation

logger = logging.getLogger(__name__)



class autorolevoice(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        hoi4channel = 795365146649690182
        eu4channel = 800505052221407252
        generalstratchannel = 762297713601544193
        hoi4roles = [762295789266796585, 793760640543883274] # Strat division + hoi4
        eu4roles = [762295789266796585, 774395657196404789]  # Strat division + eu4
        strat_role = [762295789266796585] # strat division role
        if after.channel.id == hoi4channel:  # if it's hoi4 voice channel
            for roles in hoi4roles:
                await member.add_roles(member.guild.get_role(roles), atomic=True)
        elif after.channel.id == eu4channel:  # if it's eu4 voice channel
            for roles in eu4roles:
                await member.add_roles(member.guild.get_role(roles), atomic=True)
        elif after.channel.id == generalstratchannel:  # if it's strat voice channel
            for roles in strat_role:
                await member.add_roles(member.guild.get_role(roles), atomic=True)
        else:
            pass



# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(autorolevoice(client))
    logging.info("Voicechat loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("Voicechat unloaded!")
