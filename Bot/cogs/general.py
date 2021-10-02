from Bot.core.bot import *

logger = logging.getLogger(__name__)


class General(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    async def merch(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Merch.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Help.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def patreon(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Patreon.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def donate(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Donate.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def staff(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Staff.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def social(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Socials.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def staffapp(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Staffapp.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def divapp(self, ctx):
        with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Divapp.json", 'r') as f:
            JSON = json.load(f)
            embed = discord.Embed.from_dict(JSON)
        await ctx.channel.send(embed=embed)

# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(General(client))
    logging.info("General loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("General unloaded!")
