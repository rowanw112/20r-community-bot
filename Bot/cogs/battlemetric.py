import logging
import json
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.ext.tasks import *
import sys
import json
import requests
import discord
import os

from pprint import pprint

from Bot.core.bot import Bot

logger = logging.getLogger(__name__)

API_ENDPOINT = Bot.config['steamkey']  # loads the 20r steam key


class SteamAPI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission),
                        commands.has_guild_permissions(administrator=True))
    async def squadseed(self, ctx):
        """ Notifies the users about seeding the server """
        try:
            await ctx.message.delete()
        except:
            pass
        squadRole = discord.utils.get(ctx.guild.roles, name="Squad")
        squadDRole = discord.utils.get(ctx.guild.roles, name="Squad Division")
        embed = Squad().squadseedNotification
        await ctx.send(content=f"{squadRole.mention} {squadDRole.mention}", embed=embed)


    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_any_role(*Bot.addPermission),
                        commands.has_guild_permissions(administrator=True))
    async def seed(self, ctx, game, seedteam=None):
        """ Notifies the users about seeding the server """
        try:
            await ctx.message.delete()
        except:
            pass
        rolename = game.capitalize()
        Game = {
            "squad": Squad(),
            "mordhau": Mordhau(),
            "btw": BTW()
            #"rust": Rust()
        }
        target = Game[game.lower()]
        Role0 = discord.utils.get(ctx.guild.roles, name="Seed")
        Role1 = discord.utils.get(ctx.guild.roles, name=rolename)
        Role2 = discord.utils.get(ctx.guild.roles, name=f"{rolename} Division")
        embed = target.squadseedNotification
        if seedteam == None:
            await ctx.send(content=f"{Role1.mention} {Role2.mention}", embed=embed)
        else:
            await ctx.send(content=f"{Role0.mention} {Role1.mention} {Role2.mention}", embed=embed)

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def updatestatus(self, ctx, server):
        Server = {
            "squad": [Squad(), "Squad"],
            "mordhau": [Mordhau(), "Mordhau"],
            # "risingstorm": [RisingStorm(), "RisingStorm"],
            "btw": [BTW(), "BTW"]
        }
        try:
            target = Server[server.lower()][0]
            targetinfo = Server[server.lower()][1]
            messageID, channelID, voiceID = channelInfo(targetinfo)
            channel = self.client.get_channel(channelID)
            message = await channel.fetch_message(messageID)
            await message.edit(embed=target.Embed)
        except KeyError:
            await ctx.send("The embedded message does not exist")

    @commands.command()
    @commands.check_any(commands.is_owner(),
                        commands.has_guild_permissions(administrator=True))
    async def createstatus(self, ctx, server):
        Server = {
            "squad": [Squad(), "Squad"],
            "mordhau": [Mordhau(), "Mordhau"],
            # "risingstorm": [RisingStorm(), "RisingStorm"],
            "btw": [BTW(), "BTW"]
        }
        try:
            await ctx.message.delete()
        except Exception:
            pass
        try:
            target = Server[server.lower()][0]
            embeddedMessage = await ctx.send(embed=target.Embed)
            _object = Server[server][0]
            _object.updateMessageInfo(Server[server.lower()][1], embeddedMessage)
        except KeyError:
            await ctx.send("The embedded message does not exist")


def channelInfo(targetinfo):
    messageData = Bot.JSONDirectory + os.sep + "Embed" + os.sep + "Message.json"
    with open(messageData, "r", encoding="utf-8") as f:
        JSON = json.load(f)
        try:
            messageID = JSON["Division"][f"{targetinfo}Status"]["Message"]
            channelID = JSON["Division"][f"{targetinfo}Status"]["Channel"]
            voiceID = JSON["Division"][f"{targetinfo}Status"]["Voice"]
        except KeyError:
            messageID = ""
            channelID = ""
            voiceID = ""
        return messageID, channelID, voiceID


class Metric(object):
    messageData = Bot.JSONDirectory + os.sep + "Embed" + os.sep + "Message.json"
    """
    URI (str): scheme:[//authority]path[?query][#fragment]
    """
    scheme = "https"
    authority = "api.battlemetrics.com"
    path = "servers"
    query = ""
    fragment = ""

    _URI = (scheme, authority, path, query, fragment)
    _URL = scheme + ":" + "//" + authority + "/" + path

    def __init__(self, ID, *argv, **kwargs):
        try:
            self.json = requests.get(Metric._URL + "/" + ID).json()
            self.serverName = self.json["data"]["attributes"]["name"]
            self.gameName = self.json["data"]["relationships"]["game"]["data"]["id"]
            try:
                self.IP = self.json["data"]["attributes"]["ip"]
            except Exception as Error:
                logger.warning(Error)
                self.IP = ""
                pass
            self.gamePort = self.json["data"]["attributes"]["port"]
            self.queryPort = self.json["data"]["attributes"]["portQuery"]
            self.country = self.json["data"]["attributes"]["country"]
            self.serverStatus = self.json["data"]["attributes"]["status"]
            self._Status = self.json["data"]["attributes"]["status"]
            self.maxPlayers = self.json["data"]["attributes"]["maxPlayers"]
            self.currentPlayers = self.json["data"]["attributes"]["players"]
            self.map = self.json["data"]["attributes"]["details"]["map"]

            self.optionals = dict()

            try:
                self.serverLicensed = self.json["data"]["attributes"]["details"]["licensedServer"]
            except KeyError:
                self.serverLicensed = self.json["data"]["attributes"]["details"]["official"]
            except Exception as Error:
                logger.info(Error)
                self.serverLicensed = ""
            finally:
                self.optionals = {
                    **self.optionals,
                    **{
                        "Licensed": self.serverLicensed
                    }
                }
            self.ID = ID
            self.scheme = Metric.scheme + ":"
            self.authority = "//" + Metric.authority
            self.path = "/" + Metric.path + "/" + self.ID
        except Exception as Error:
            logger.info(Error)

    def generateNotification(self, event_title: str, event_body: str, event_image: str):
        embed = discord.Embed(title="20r Gaming Server",
                              description=f'Connect: steam://connect/{self.IP}:{self.queryPort}')
        embed.add_field(name=event_title,
                        value=event_body,
                        inline=False)
        embed.set_image(
            url=event_image)
        embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name=f"20r Gaming - {0} - {1}".format(
            self.gameName, "NA Server" \
                if self.country == "US" \
                else "EU Server"),
            url="https://discord.gg/20r",
            icon_url=Bot.LOGO)
        return embed

    @staticmethod
    def updateMessageInfo(name: str, message):
        """
        1. Load JSON Data from Object & File
        2. Combine the New JSON Data and the Old JSON Data
            *Overwrite Old Data with New*
        3. Write the New, Combined Data to the JSON File
        :param message:
        :param targetMessageID:
        :return:
        """
        newMessageID = message.id
        newChannelID = message.channel.id
        with open(Metric.messageData, "r+", encoding="utf-8") as JSON:
            source = json.load(JSON)
            source["Division"][f"{name}Status"]["Message"] = newMessageID
            source["Division"][f"{name}Status"]["Channel"] = newChannelID
            JSON.seek(0)
            json.dump(source, JSON, indent=4)
            JSON.truncate()

    @property
    def squadseedNotification(self):
        embed = discord.Embed(title="20r Gaming Server",
                              description=f'Connect: steam://connect/{self.IP}:{self.queryPort}')
        embed.add_field(name="Server Seeding",
                        value=f"We current have **{self.currentPlayers}/{self.maxPlayers}** players"
                              f"\n Come join us and help us seed the server! AFKs are welcome! "
                              f"\n Just click the Steam Connect Link!",
                        inline=False)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/711777537977614336/757362630338805913/20redit.png")
        embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name="20r Gaming", url="https://discord.gg/20r",
                         icon_url=Bot.LOGO)
        return embed

    @property
    def Status(self):
        if self.serverStatus == "online":
            colourserverStatus = "🟢 Online"
        elif self.serverStatus == "offline":
            colourserverStatus = "🔴 Offline"
        else:
            colourserverStatus = "🟡 Unknown"
        return colourserverStatus

    @property
    def gameLogo(self):
        if self.gameName == "mordhau":
            gameICON = "https://cdn.discordapp.com/attachments/728789872139173960/771480991029264404/dd7wuqp-ac2ccff9-605f-477d-9e32-f3111cf547e8.png"
        elif self.gameName == "squad":
            gameICON = "https://cdn.discordapp.com/attachments/728789872139173960/771483612939812864/23-238309_transparent-don-t-forget-clipart-squad-game-logo.png"
        elif self.gameName == "rs2vietnam":
            gameICON = "https://cdn.discordapp.com/attachments/728789872139173960/771480586765729822/rs2.png"
        elif self.gameName == "btw":
            gameICON = "https://cdn.discordapp.com/attachments/728789872139173960/771480497867456552/btw_logo.png"
        else:
            gameICON = Bot.LOGO
        return gameICON

    @property
    def Embed(self):
        embed = discord.Embed(title="", colour=discord.Colour(4886754),
                              description=f'Click to Connect:\n steam://connect/{self.IP}:{self.queryPort}')
        try:
            embed.set_thumbnail(url=self.gameLogo)
        except AttributeError:
            embed.set_thumbnail(url=Bot.LOGO)
        embed.set_author(name=self.serverName, url="https://discord.gg/20r",
                         icon_url=Bot.LOGO)
        embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
        embed.add_field(name="Server Status", value=self.Status, inline=True)
        embed.add_field(name="Address:Port", value=f"{self.IP}:{self.queryPort}", inline=True)
        embed.add_field(name="Location", value=f":flag_{self.country.casefold()}: {self.country}", inline=True)
        try:
            embed.add_field(name="Game", value=self.gameName.capitalize(), inline=True)
        except AttributeError:
            pass
        embed.add_field(name="Current Map", value=f"{self.map}", inline=True)
        embed.add_field(name="Players", value=f"{self.currentPlayers}/{self.maxPlayers}", inline=True)
        return embed

    @property
    def URI(self):
        return self.scheme, self.authority, self.path, self.query, self.fragment

    @property
    def URL(self):
        return "".join(str(index) for index in self.URI)


class Squad(Metric):
    ID = "9173175"

    def __init__(self, *argv, **kwargs):
        super(Squad, self).__init__(self.ID)


class Mordhau(Metric):
    ID = "8295414"

    def __init__(self, *argv, **kwargs):
        super(Mordhau, self).__init__(self.ID)


# class RisingStorm(Metric):
#     ID = "8774729"
#
#     def __init__(self, *argv, **kwargs):
#         super(RisingStorm, self).__init__(self.ID)


class BTW(Metric):
    ID = "8892250"

    def __init__(self, *argv, **kwargs):
        super(BTW, self).__init__(self.ID)


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(SteamAPI(client))
    logging.info("SteamAPI loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("SteamAPI unloaded!")
