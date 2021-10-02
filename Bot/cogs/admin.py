from Bot.core.bot import *

logger = logging.getLogger(__name__)


class Admin(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def updatenames(self, ctx, Oldprefix, Newprefix):
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        if Newprefix == "[]":
            Newprefix = ""
        try:
            await ctx.send(f"Attempting to changes users with names of {Oldprefix} to {Newprefix}", delete_after=10)
            await ctx.send(f"This will take time as i am going through every member one by one", delete_after=10)
            for member in ctx.guild.members:
                if Oldprefix in member.display_name:
                    print(member.display_name)
                    await member.edit(nick=str(member.display_name).replace(Oldprefix, Newprefix))
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def updateroles(self, ctx, oldrole, newrole):
        oldroleid = oldrole.replace("<", "").replace(">", "").replace("@", "").replace("&", "")
        newroleid = newrole.replace("<", "").replace(">", "").replace("@", "").replace("&", "")
        Oldrole = discord.utils.get(ctx.guild.roles, id=int(oldroleid))
        Newrole = discord.utils.get(ctx.guild.roles, id=int(newroleid))
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        try:
            await ctx.send(f"Attempting to changes users with roles from {Oldrole} to {Newrole}", delete_after=10)
            await ctx.send(f"This will take time as i am going through every member one by one", delete_after=10)
            for member in ctx.guild.members:
                if Oldrole in member.roles:
                    await member.add_roles(member.guild.get_role(int(newroleid)), atomic=True)
                    await member.remove_roles(member.guild.get_role(int(oldroleid)), atomic=True)
        except:
            logging.exception("Got exception on main handler")
            raise


    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def userroles(self, ctx, role):
        oldroleid = role.replace("<", "").replace(">", "").replace("@", "").replace("&", "")
        Oldrole = discord.utils.get(ctx.guild.roles, id=int(oldroleid))
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        try:
            for member in ctx.guild.members:
                if Oldrole in member.roles:
                    print(member)
        except:
            logging.exception("Got exception on main handler")
            raise




    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def created(self, ctx, member: discord.Member):
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        try:
            await ctx.send(f"{member.mention} account was created at " + member.created_at.strftime(
                "%A, %B %d %Y @ %H:%M:%S %p") + " UTC")
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def changename(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=588816938202038292)
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        try:
            await ctx.send(f"This will take time as i am going through every member one by one", delete_after=10)
            for member in ctx.guild.members:
                if role in member.roles:
                    print(member.display_name)
                    await member.edit(nick=str(member.display_name).replace("[Ⅰ]", "[R]"))
        except:
            logging.exception("Got exception on main handler")
            raise

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def tester(self, ctx):
        await ctx.send(f"test22", delete_after=10)


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(Admin(client))
    logging.info("StartUp loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("StartUp unloaded!")
