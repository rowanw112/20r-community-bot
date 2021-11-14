import logging
import json
import discord
import requests
from discord.ext import commands
from discord.ext.commands import *
from discord.ext.tasks import *

from Bot.core.bot import Bot
from Bot.utils.updatepermissions import *

logger = logging.getLogger(__name__)

API_ENDPOINT = Bot.config['api20rkey']  # loads the 20r gsheets api key

regionList = ["eu", "na", "asia", "oce"]
gamesList = ["mordhau", "ps2", "eft", "squad", "royals","rl", "r6", "mb", "valorant", "minecraft", "cod", "halo", "hll", "dnd",
             "rust", "amongus", "strategy", "wt", "btw", "elite", "eve", "bf2", "lol", "sot", "squadrons", "outriders",
             "warzone", "wow", "dayz", "destiny", "arma", "enlisted", "chiv", "foxhole", "newworld", "7d2d"]


class Recruitment(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name='games',
        description='list of games that are supported for the .add command',
        pass_contxt=True,
    )
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission),
                        commands.has_guild_permissions(administrator=True))
    async def games(self, ctx):
        try:
            await ctx.message.delete(delay=10)
        except:
            pass
        embed = discord.Embed(colour=discord.Colour(8060672),
                              title="Supported Games",
                              description=f"**{', '.join(gamesList)}**")
        await ctx.send(embed=embed)

    @commands.command(
        name='add',
        description='Adds user to the spreadsheet. Please use games from .game command! You can input multiple games '
                    'at once',
        pass_contxt=True,
        usage='@discordid region game'
    )
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission),
                        commands.has_guild_permissions(administrator=True))
    async def add(self, ctx, member: discord.Member, region, *args):
        """
        Adds the user to the 20r spreadsheet, assigns them roles based on which game they were added to
        :param ctx:
        :param member:
        :param region:
        :param args:
        """

        memberId = member.id
        memberId = str(memberId)
        memberText = str(member)
        region = region.lower()
        if region in regionList:
            if len(args) >= 1:
                Game = ""
                for GameUnit in args:
                    Game += GameUnit
                errorOccured = False
                Game = Game.lower().replace(" ", "")
                gamesSplit = Game.split(",")
                for gameString in gamesSplit:
                    if gameString not in gamesList:
                        errorOccured = True
                        await ctx.send(f"You have input an incorrect game, Please use the games from below:")
                        await ctx.send(f"{', '.join(gamesList)}")
                        break
                if not errorOccured:
                    rUser = ctx.message.author
                    message, permissions = useradd(rUser, memberText, memberId, region, Game)
                    if permissions is not None:
                        for gaming in permissions:
                            await assignPermissions(ctx, member, gaming)  # assigning Division roles
                            await assignPermissions(ctx, member, gaming + region)  # assigning region Division roles
                    skipAdd = False
                    prefixWanted = "[R] "
                    for prefix in prefixes:
                        if prefix in member.display_name:
                            skipAdd = True
                        if prefix.replace(" ", "") in member.display_name:
                            skipAdd = True
                    if not skipAdd:
                        await member.edit(nick=prefixWanted + str(member.display_name))
                        await removePermissions(ctx, member, "20rStranger")
                        await removePermissions(ctx, member, "20rFriend")
                        await assignPermissions(ctx, member, "20rstartAdd")
                        await assignPermissions(ctx, member, region)  # assigning Region roles
                    embed = discord.Embed(title=f"**{member.display_name}**", colour=discord.Colour(4886754),
                                          description=f'**Has been added to:**\n\n**{message}**\n\nRecruited by **{ctx.author.display_name}**')
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_author(name="Recruitment Form", icon_url=Bot.LOGO)
                    embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
                    await ctx.channel.send(f"{member.mention}", embed=embed)
            else:
                await ctx.send("Please input the command correctly .add @discordid region game")
        else:
            await ctx.send(f"please input a correct region {', '.join(regionList)}")

    @commands.command(
        name='friend',
        description='to add user to the friends list, Please use games from .game command! You can input multiple games at once',
        pass_contxt=True,
        usage='@discordid region game'
    )
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission),
                        commands.has_guild_permissions(administrator=True))
    async def friend(self, ctx, member: discord.Member, region, *args):
        """
        assigns them friend role and the game that they were added on too
        :param ctx:
        :param member:
        :param region:
        :param args:
        """
        region = region.lower()
        ment = member.mention
        if region in regionList:
            if len(args) >= 1:
                Game = ""
                for GameUnit in args:
                    Game += GameUnit
                errorOccured = False
                Game = Game.lower().replace(" ", "")
                gamesSplit = Game.split(",")
                for gameString in gamesSplit:
                    if gameString not in gamesList:
                        errorOccured = True
                        await ctx.send(f"You have input an incorrect game, Please use the games from below:")
                        await ctx.send(f"{', '.join(gamesList)}")
                        break
                    if gameString in gamesList:
                        await assignPermissions(ctx, member, gameString)  # assigning Division roles
                        await assignPermissions(ctx, member, gameString + region)  # assigning region Division roles
                if not errorOccured:
                    await assignPermissions(ctx, member, region)  # assigning region Division roles
                    await assignPermissions(ctx, member, "20rFriend")
                    await removePermissions(ctx, member, "20rStranger")
                    await ctx.send(f"{ment} was added to {', '.join(args)}'s division as a friend")
            else:
                await ctx.send("Please input the command correctly .add @discordid region game")
        else:
            await ctx.send(f"please input a correct region {', '.join(regionList)}")

    @commands.command(
        name='delete',
        description='to remove a user from the spreadsheet and to remove their roles.',
        pass_contxt=True,
        usage='@discordid region game'
    )
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.deletePermission),
                        commands.has_guild_permissions(administrator=True))
    async def delete(self, ctx, member: discord.Member, *args):
        """
        Removes the user from the spreadsheet and purges their roles.
        :param ctx:
        :param member:
        :param args:
        """
        ment = member.mention
        memberId = member.id
        memberId = str(memberId)
        memberText = str(member)
        message, permissions = userdel(memberText, memberId)
        await purgePermissions(ctx, member)
        await assignPermissions(ctx, member, "20rStranger")
        for prefix in prefixesRemoval:
            if prefix in member.display_name:
                await member.edit(nick=str(member.display_name).replace(prefix, ""))
            if prefix.replace(" ", "") in member.display_name:
                await member.edit(nick=str(member.display_name).replace(prefix.replace(" ", ""), ""))
        await ctx.send(f"{ment}: " + message)


def useradd(rUser, memberText, memberId, region, Game):
    Game = Game.replace(" ", "")
    data1 = \
        '{"recruiter":' + json.dumps(str(rUser)) + ', ' + \
        '"memberId": ' + json.dumps(memberId) + ', ' + \
        '"discordId": ' + json.dumps(str(memberText)) + ', ' + \
        '"games": ' + json.dumps(str(Game)) + ', ' + \
        '"region": ' + json.dumps(str(region)) + '}'
    try:
        r = requests.post(url=API_ENDPOINT, data=data1)
        d = json.loads(r.text)
        if d['message'] == "OK":
            returnText = ""
            gamePermissions = []
            for gameItem in d['game']:
                returnText += gameItem['id'] + "-" + gameItem['message'] + ", "
                if gameItem['message'] == "Added":
                    gamePermissions.append(gameItem['id'])
            return f"{returnText}", gamePermissions
        else:
            return f"Google API Failed", None
    except:
        logger.info("String could not be converted to JSON")
    return f"Google API Failed", None


def userdel(memberText, memberId):
    data1 = \
        '{"memberId": ' + json.dumps(memberId) + ', ' + \
        '"discordId": ' + json.dumps(memberText) + ', "remove": true}'
    try:
        r = requests.post(url=API_ENDPOINT, data=data1)
        d = json.loads(r.text)
        logger.info(data1)
        logger.info(r)
        logger.info(d)
        if d['message'] == "Deleted":
            returnText = ""
            gamePermissions = []
            for gameItem in d['game']:
                if gameItem['message'] == "Deleted":
                    returnText += gameItem['id'] + "-" + gameItem['message'] + ", "
                    gamePermissions.append(gameItem['id'])
            return f"{memberText}: {returnText}", gamePermissions
        elif d['message'] == "Not Deleted":
            return f"{memberText} was not in the spreadsheet but their roles were removed", None
        else:
            return f"Google API Failed", None
    except:
        logger.info("String could not be converted to JSON")
    return f"Google API failed", None


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(Recruitment(client))
    logging.info("Recruitment loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("Recruitment unloaded!")
