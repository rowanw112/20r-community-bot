import requests
from discord.ext import commands
from discord.ext.tasks import *
from Bot.utils.updatepermissions import *
from Bot.core.bot import Bot

logger = logging.getLogger(__name__)

API_ENDPOINT = Bot.config['apips2key']  # loads the 20r gsheets api key


class PlanetSide2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name='ps2add',
        description='to register planetside 2 user onto spreadsheet and assign roles accordingly',
        pass_contxt=True,
        usage='@discordid planetside2-ingame-name'
    )
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission, 730606807298343024))
    async def ps2add(self, ctx, member: discord.Member, *, cName):
        """
        Adds the user to the spreadsheet, assigns them the correct ps2 role and recruit tag
        :param ctx:
        :param member:
        :param cName:
        """
        rUser = ctx.message.author
        message, outfitId = ps2botadd(rUser, member, cName)
        skipAdd = False
        if outfitId is not None:
            prefixWanted = "[R] "
            for prefix in prefixes:
                if prefix in member.display_name:
                    skipAdd = True
                if prefix.replace(" ", "") in member.display_name:
                    skipAdd = True
            if not skipAdd:
                await member.edit(nick=prefixWanted + str(member.display_name))
                await removePermissions(ctx, member, "20rStranger")
                await assignPermissions(ctx, member, "20rstartAdd")
            await assignPermissions(ctx, member, outfitId)
            await ctx.send(f"{member.mention}: " + message)
        else:
            await ctx.send(f"{member.mention}: " + message)

    @commands.command(pass_contxt=True)
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission, 730606807298343024))
    async def ps2friend(self, ctx, member: discord.Member):
        """
        Assigns the friend role tags for players who don't want to join 20r as a member
        :param ctx:
        :param member:
        """
        await assignPermissions(ctx, member, "ps2na")
        await assignPermissions(ctx, member, "ps2")
        await assignPermissions(ctx, member, "20rFriend")
        await removePermissions(ctx, member, "20rStranger")
        await ctx.send(f"{member.mention} has been added to PS2 NA Division")

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission, 730606807298343024))
    async def ps2delete(self, ctx, member: discord.Member, *, cName):
        """
        Removes users roles and from the ps2 spreadsheet
        :param ctx:
        :param member:
        :param cName:
        """
        message, gamePermissions = ps2botdelete(cName)
        await ctx.send(message)
        for prefix in prefixesRemoval:
            if prefix in member.display_name:
                await member.edit(nick=str(member.display_name).replace(prefix, ""))
            if prefix.replace(" ", "") in member.display_name:
                await member.edit(nick=str(member.display_name).replace(prefix.replace(" ", ""), ""))
        await removePermissions(ctx, member, "20rPS2Delete")
        await assignPermissions(ctx, member, "20rStranger")
        await ctx.send(f"{member.mention} has been removed from their division and their roles have been deleted")

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission, 730606807298343024))
    async def ps2forcedelete(self, ctx, *, cName):
        """
        Removes player from the ps2 spreadsheet without a need of mentioning name
        :param ctx:
        :param cName:
        """
        message, gamePermissions = ps2botdelete(cName)
        await ctx.send(message)
        await ctx.send(f"{cName} has been removed from their division")


def emeraldPopulation():
    emeraldFisu = requests.get(url="https://ps2.fisu.pw/api/population/?world=17").json()
    for data in emeraldFisu["result"]:
        vs = data["vs"]
        nc = data["nc"]
        tr = data["tr"]
        ns = data["ns"]
        population = vs + nc + tr + ns
        return population


def ps2botadd(rUser, member, cName):
    data1 = '{"recruiter":' + json.dumps(str(rUser)) + ', "discordId": ' + json.dumps(
        str(member)) + ', "inGameName": ' + json.dumps(str(cName)) + '}'
    try:
        gamePermissions = None
        r = requests.post(url=API_ENDPOINT, data=data1)  # gsheets, you need to add haling of response here
        d = json.loads(r.text)
        logger.info(d)
        if d['message'] == "OK":
            if len(d["game"]) > 0:
                if d["game"][0]["message"] == "Added":
                    gamePermissions = (d["game"][0]["permissions"])
                return f"{cName} {d['game'][0]['message']}", gamePermissions
    except:
        return "Error", None
    return "Error2", None


def ps2botdelete(cName):
    data1 = '{"inGameName": ' + json.dumps(str(cName)) + ', "remove": true}'
    try:
        r = requests.post(url=API_ENDPOINT, data=data1)  # gsheets, you need to add haling of response here
        d = json.loads(r.text)
        gamePermissions = None
        if d['message'] == "Deleted" or d['message'] == "Not Deleted":
            if len(d["game"]) > 0:
                if d["game"][0]["message"] == "Deleted":
                    gamePermissions = (d["game"][0]["id"])
                return f"{cName} {d['game'][0]['message']}", gamePermissions
            else:
                return f"Google API Failed", None
    except:
        logger.info("String could not be converted to JSON")
    return f"Google API failed", None


def ps2botdeletemember(member):
    data1 = '{"discordId": ' + json.dumps(str(member)) + ', "remove": true}'
    try:
        r = requests.post(url=API_ENDPOINT, data=data1)  # gsheets, you need to add haling of response here
        d = json.loads(r.text)
        gamePermissions = None
        if d['message'] == "Deleted" or d['message'] == "Not Deleted":
            if len(d["game"]) > 0:
                if d["game"][0]["message"] == "Deleted":
                    gamePermissions = (d["game"][0]["id"])
                return f"{member} {d['game'][0]['message']}", gamePermissions
            else:
                return f"Google API Failed", None
    except:
        logger.info("String could not be converted to JSON")
    return f"Google API failed", None


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(PlanetSide2(client))
    logging.info("PlanetSide2 loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("PlanetSide2 unloaded!")
