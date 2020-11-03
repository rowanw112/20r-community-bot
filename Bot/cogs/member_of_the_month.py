from Bot.cogs.battlemetric import *
from Bot.cogs.reactroles import *

logger = logging.getLogger(__name__)


class MemberMonth(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def mom(self, ctx, member: discord.Member):
        mydate = datetime.datetime.now()
        month = mydate.strftime("%B")
        await ctx.message.delete()
        embed = discord.Embed(title=f"**Member of the Month**", colour=discord.Colour(4886754),
                              description=f"Congratulations {member.mention} for the Member of the Month of **{month}**")
        embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
        embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
        embed.set_image(url=member.avatar_url)
        await member.edit(nick=str(member.display_name) + "🥇️")
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def dom(self, ctx, member: discord.Member):
        mydate = datetime.datetime.now()
        month = mydate.strftime("%B")
        await ctx.message.delete()
        embed = discord.Embed(title=f"**Donator of the Month**", colour=discord.Colour(131071),
                              description=f"Congratulations {member.mention} for the Donator of the Month of **{month}**")
        embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
        embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
        embed.set_image(url=member.avatar_url)
        await member.edit(nick=str(member.display_name) + "💲")
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def som(self, ctx, member: discord.Member):
        mydate = datetime.datetime.now()
        month = mydate.strftime("%B")
        await ctx.message.delete()
        embed = discord.Embed(title=f"**Staff member of the Month**", colour=discord.Colour(15135079),
                              description=f"Congratulations {member.mention} for the Staff member of the Month of **{month}**")
        embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
        embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
        embed.set_image(url=member.avatar_url)
        await member.edit(nick=str(member.display_name) + "🏆️")
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def rom(self, ctx, member: discord.Member):
        mydate = datetime.datetime.now()
        month = mydate.strftime("%B")
        await ctx.message.delete()
        embed = discord.Embed(title=f"**Recruiter of the Month**", colour=discord.Colour(850946),
                              description=f"Congratulations {member.mention} for the Recruiter of the Month of **{month}**")
        embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
        embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
        embed.set_image(url=member.avatar_url)
        await member.edit(nick=str(member.display_name) + "🏅️")
        await ctx.channel.send(embed=embed)


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(MemberMonth(client))
    logging.info("MemberMonth loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("MemberMonth unloaded!")
