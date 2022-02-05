from Bot.cogs.battlemetric import *
from Bot.cogs.reactroles import *
from Bot.cogs.planetside2 import emeraldPopulation

from Bot.core.bot import Bot

logger = logging.getLogger(__name__)


class StartUp(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
            self.loopserverembedstatus.start()
            self.loopservervoicestatus.start()
            self.startupupdateembed.start()
            # self.loopmembervoicestatus.start()
            # self.loopps2voicestatus.start()
        except:
            logging.exception("Got exception on main handler")
            raise

    @loop(minutes=2)
    async def loopserverembedstatus(self):
        """
    Server background operation
    Used for updating the embeds
        """
        await self.client.wait_until_ready()
        server = {
            # "squad": [Squad(), "Squad"],
            # "mordhau": [Mordhau(), "Mordhau"]
            # "risingstorm": [RisingStorm(), "RisingStorm"],
            # "btw": [BTW(), "BTW"]
        }
        for key, Server in server.items():
            target = Server[0]
            targetinfo = Server[1]
            messageID, channelID, voiceID = channelInfo(targetinfo)
            channel = self.client.get_channel(channelID)
            message = await channel.fetch_message(messageID)
            await message.edit(embed=target.Embed)
        logger.info(f"{server} embed has been updated")

    @loop(minutes=5)
    async def loopservervoicestatus(self):
        """
    Server background operation
    Used for updating the voice
        """
        await self.client.wait_until_ready()
        server = {
            # "squad": [Squad(), "Squad"],
            # "mordhau": [Mordhau(), "Mordhau"]
            # "risingstorm": [RisingStorm(), "RisingStorm"],
            # "btw": [BTW(), "BTW"]
        }
        for key, Server in server.items():
            target = Server[0]
            targetinfo = Server[1]
            messageID, channelID, voiceID = channelInfo(targetinfo)
            voicechannel = self.client.get_channel(voiceID)
            await voicechannel.edit(name=f"Status: {target.Status}| {target.currentPlayers}/{target.maxPlayers}")
        logger.info(f"{server} voice has been updated")

    @loop(hours=1)
    async def startupupdateembed(self):
        await self.client.wait_until_ready()
        embedWhitelist = {
            "member": [Member(), "Member"],
            "casual": [Casual(), "Casual"],
            # "application": [Application(), "Application"],
            # "newworld": [Newworld(), "Newworld"], # with this disabled, it won't add new react for roles
            # "ps2": [PS2(), "PS2"],
            # "rl": [RL(), "RL"],
            # "commandrecruit": [CommandRecruit(), "CommandRecruit"],
            "populargames": [PopularGames(), "PopularGames"],
            "generalroles": [GeneralRoles(), "GeneralRoles"],
            "discover20r": [Discover20r(), "Discover20r"],
            #"welcome20r": [Welcome20r(), "Welcome20r"],
            "region20r": [Region20r(), "Region20r"],
            "member20r": [Member20r(), "Member20r"],
            "rules": [Rules(), "Rules"]
        }
        for key, Server in embedWhitelist.items():
            target = Server[0]
            messageID = target.messageInfo
            channelID = target.channelInfo
            channel = self.client.get_channel(channelID)
            embedMessage = await channel.fetch_message(messageID)
            await embedMessage.edit(embed=target.embedMessage)
            for reaction in target.Roles:
                await embedMessage.add_reaction(nextcord.utils.get(embedMessage.guild.emojis, name=reaction))
        logger.info(f"{embedWhitelist} embed has been updated")



    # @loop(minutes=5)
    # async def loopps2voicestatus(self):
    #     """
    # Server background operation
    # Used for updating the voice channel of member count
    #     """
    #     await self.client.wait_until_ready()
    #     voiceChannel = self.client.get_channel(753780062599381102)
    #     population = emeraldPopulation()
    #     await voiceChannel.edit(name=f"Emerald's Population: {population}")
    #     logger.info("planetside status channel has been updated")

    # @loop(minutes=5)
    # async def loopmembervoicestatus(self):
    #     """
    # Server background operation
    # Used for updating the voice channel of member count
    #     """
    #     await self.client.wait_until_ready()
    #     Guild = self.client.get_guild(531243268256694313)
    #     # channels_info = {
    #     #     "total categories": len(Guild.categories),
    #     #     "total channels": len(Guild.channels),
    #     #     "total text channels": len(Guild.text_channels),
    #     #     "total voice channels": len(Guild.voice_channels)
    #     # }
    #     # members_info = {
    #     #     "total users": Guild.member_count,
    #     #     "total online members": sum(
    #     #         member.status == nextcord.Status.online and not member.bot for member in Guild.members),
    #     #     "total offline members": sum(
    #     #         member.status == nextcord.Status.offline and not member.bot for member in Guild.members),
    #     #     "total humans": sum(not member.bot for member in Guild.members),
    #     #     "total bots": sum(member.bot for member in Guild.members)
    #     # }
    #     user_count_channel = self.client.get_channel(764222186122117131)
    #     voice_count_channel = self.client.get_channel(764223239407796244)
    #     # user_count = sum(not member.bot for member in Guild.members)  # doesn't include bots
    #     # print(user_count)
    #     # print(Guild.member_count)
    #     connected_members = sum(
    #         [len(voice_channel.members) for voice_channel in voice_count_channel.guild.voice_channels])
    #     await user_count_channel.edit(name=f"𝐌𝐞𝐦𝐛𝐞𝐫 𝐂𝐨𝐮𝐧𝐭: {Guild.member_count}")
    #     await voice_count_channel.edit(name=f"𝐕𝐨𝐢𝐜𝐞 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧: {connected_members}")


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(StartUp(client))
    logging.info("StartUp loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("StartUp unloaded!")
