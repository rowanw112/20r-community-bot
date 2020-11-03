import os

from discord.ext import commands
from discord.ext.tasks import *

from Bot.utils.updatepermissions import *

logger = logging.getLogger(__name__)

API_ENDPOINT = Bot.config['api20rkey']  # loads the 20r gsheets api key

regionList = ["eu", "na", "me", "oce"]
gamesList = ["mordhau", "ps2", "eft", "squad", "rl", "r6", "mb", "valorant", "minecraft", "cod",
             "halo", "hll", "dnd", "rust", "amongus", "strategy", "wt"]


class ReactRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission),
                        commands.has_guild_permissions(manage_roles=True))
    async def embed(self, ctx, message):
        embedWhitelist = {
            "verification": [Verification(message), "Verification"],
            "member": [Member(message), "Member"],
            "public": [Public(message), "Public"],
            "casual": [Casual(message), "Casual"],
            "rules": [Rules(message), "Rules"],
            "welcome": [Welcome(message), "Welcome"],
            "application": [Application(message), "Application"],
            "comp": [Comp(message), "Comp"]
        }
        try:
            await ctx.message.delete()
        except Exception:
            pass
        try:
            target = embedWhitelist[message.lower()][0]
            embeddedMessage = await ctx.send(embed=target.embedMessage)
            _object = embedWhitelist[message][0]
            _object.updateMessageInfo(embedWhitelist[message.lower()][1], embeddedMessage)
            for reaction in target.Roles:
                await embeddedMessage.add_reaction(discord.utils.get(ctx.guild.emojis, name=reaction))
        except KeyError:
            await ctx.send("The embedded message does not exist")


class Embed(object):

    messageData = Bot.JSONDirectory + os.sep + "Embed" + os.sep + "Message.json"
    embedData = Bot.JSONDirectory + os.sep + "Message" + os.sep
    rolesData = Bot.JSONDirectory + os.sep + "Roles" + os.sep + "Roles.json"

    def __init__(self, Message, *argv, **kwargs):
        self.message = Message
        with open(self.messageData, "r", encoding="utf-8") as f:
            JSON = json.load(f)
            try:
                self.messageID = JSON["Division"][f"{self.message}"]["Message"]
                self.channelID = JSON["Division"][f"{self.message}"]["Channel"]
            except KeyError:
                self.messageID = ""
                self.channelID = ""
        with open(self.rolesData, "r", encoding="utf-8") as f:
            JSON = json.load(f)
            try:
                self.reaction = JSON["Roles"][f"{self.message}"]
            except KeyError:
                self.reaction = ""
        with open(self.embedData + f"{Message}.json", "r", encoding="utf-8") as f:
            self.embed = json.load(f)

    @staticmethod
    def updateMessageInfo(name: str, message):
        """
        1. Load JSON Data from Object & File
        2. Combine the New JSON Data and the Old JSON Data
            *Overwrite Old Data with New*
        3. Write the New, Combined Data to the JSON File
        :param name:
        :param message:
        :param targetMessageID:
        :return:
        """
        newMessageID = message.id
        newChannelID = message.channel.id
        with open(Embed.messageData, "r+", encoding="utf-8") as JSON:
            source = json.load(JSON)
            source["Division"][f"{name}"]["Message"] = newMessageID
            source["Division"][f"{name}"]["Channel"] = newChannelID
            JSON.seek(0)
            json.dump(source, JSON, indent=4)
            JSON.truncate()

    @property
    def embedMessage(self):
        return discord.Embed.from_dict(self.embed)

    @property
    def Roles(self):
        return self.reaction

    @property
    def messageInfo(self):
        return self.messageID

    @property
    def channelInfo(self):
        return self.channelID


class Verification(Embed):
    Name = "Verification"

    def __init__(self, *argv, **kwargs):
        super(Verification, self).__init__(self.Name)


class Member(Embed):
    Name = "Member"

    def __init__(self, *argv, **kwargs):
        super(Member, self).__init__(self.Name)


class Public(Embed):
    Name = "Public"

    def __init__(self, *argv, **kwargs):
        super(Public, self).__init__(self.Name)


class Casual(Embed):
    Name = "Casual"

    def __init__(self, *argv, **kwargs):
        super(Casual, self).__init__(self.Name)


class Rules(Embed):
    Name = "Rules"

    def __init__(self, *argv, **kwargs):
        super(Rules, self).__init__(self.Name)


class Welcome(Embed):
    Name = "Welcome"

    def __init__(self, *argv, **kwargs):
        super(Welcome, self).__init__(self.Name)


class Application(Embed):
    Name = "Application"

    def __init__(self, *argv, **kwargs):
        super(Application, self).__init__(self.Name)


class Comp(Embed):
    Name = "Comp"

    def __init__(self, *argv, **kwargs):
        super(Comp, self).__init__(self.Name)


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(ReactRoles(client))
    logging.info("ReactRoles loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("ReactRoles unloaded!")