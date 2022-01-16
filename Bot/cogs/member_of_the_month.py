from Bot.cogs.battlemetric import *
from Bot.cogs.reactroles import *

logger = logging.getLogger(__name__)


class MemberMonth(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def mom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            await ctx.message.delete()
            if month is None:
                month = mydate.strftime("%B")
            embed = nextcord.Embed(title=f"**Member of the Month**", colour=nextcord.Colour(4886754),
                                  description=f"Congratulations {member.mention} for the Member of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "🥇️")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def dom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Donator of the Month**", colour=nextcord.Colour(131071),
                                  description=f"Congratulations {member.mention} for the Donator of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "💲")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def som(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Staff member of the Month**", colour=nextcord.Colour(15135079),
                                  description=f"Congratulations {member.mention} for the Staff member of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "🏆️")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def rom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Recruiter of the Month**", colour=nextcord.Colour(850946),
                                  description=f"Congratulations {member.mention} for the Recruiter of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "🏅️")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def asom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Administrative Staff of the Month**", colour=nextcord.Colour(850946),
                                  description=f"Congratulations {member.mention} for the Administrative Staff of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "🗝️")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def dsom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Division Staff of the Month**", colour=nextcord.Colour(850946),
                                  description=f"Congratulations {member.mention} for the Division Staff of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "🔑️")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def eom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**eSports Spotlight of the Month**", colour=nextcord.Colour(850946),
                                  description=f"Congratulations {member.mention} for being the eSports player of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            try:
                await member.edit(nick=str(member.display_name) + "💯")
            except nextcord.Forbidden as Error:
                await ctx.author.send(
                    f"Error occured while editing {member.display_name}, most likely their permissions is higher than "
                    "mine")
                pass
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def esom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Experimental Staff of the Month**", colour=nextcord.Colour(850946),
                                  description=f"Congratulations {member.mention} for being the Experimental Staff of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def suom(self, ctx, member: nextcord.Member, month=None):
        try:
            mydate = datetime.datetime.now()
            if month is None:
                month = mydate.strftime("%B")
            await ctx.message.delete()
            embed = nextcord.Embed(title=f"**Supporter of the Month**", colour=nextcord.Colour(850946),
                                  description=f"Congratulations {member.mention} for being the Supporter of the Month of {month.capitalize()}")
            embed.set_thumbnail(url=Bot.LOGO)
            embed.set_author(name="20r Gaming", icon_url=Bot.LOGO)
            embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
            embed.set_image(url=member.avatar_url)
            await ctx.channel.send(embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(MemberMonth(client))
    logging.info("MemberMonth loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("MemberMonth unloaded!")
