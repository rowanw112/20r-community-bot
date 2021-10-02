from Bot.cogs.reactroles import *

logger = logging.getLogger(__name__)


class RawReactAdd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        member = reaction.member
        stranger = discord.utils.get(member.roles, id=int(588931614017323058))
        try:
            emoji = str(reaction.emoji)
            emoji = emoji.split(":", 2)
            emoji = emoji[1]
        except IndexError:
            emoji = str(reaction.emoji)
        logger.info(emoji)
        if member != self.client.user:  # Makes it so the bot ignores itself
            if reaction.message_id == Verification().messageInfo:
                emojiRoles = Verification().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.send(
                        f"Congratulations {member.mention}, You have been verified, you may access rest of the discord.")
                    await member.remove_roles(member.guild.get_role(emojiReaction), atomic=True)

            if reaction.message_id == Member().messageInfo:
                if stranger in member.guild.roles: # if user has stranger, it assigns public roles
                    emojiRoles = Public().Roles.get(emoji)
                    for emojiReaction in emojiRoles:
                        await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
                else:
                    emojiRoles = Member().Roles.get(emoji)
                    for emojiReaction in emojiRoles: # else if user does not have stranger, it assigns member roles
                        await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Casual().messageInfo:
                emojiRoles = Casual().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == PopularGames().messageInfo:
                emojiRoles = PopularGames().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Rules().messageInfo:
                emojiRoles = Rules().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Welcome().messageInfo:
                emojiRoles = Welcome().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Application().messageInfo:
                emojiRoles = Application().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Strategy().messageInfo:
                emojiRoles = Strategy().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Comp().messageInfo:
                emojiRoles = Comp().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == PS2().messageInfo:
                emojiRoles = PS2().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == CommandRecruit().messageInfo:
                emojiRoles = CommandRecruit().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == RL().messageInfo:
                emojiRoles = RL().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == GeneralRoles().messageInfo:
                emojiRoles = GeneralRoles().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Discover20r().messageInfo:
                emojiRoles = Discover20r().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
                    await member.remove_roles(member.guild.get_role(599430915789160450), atomic=True)  # removes stranger role
            # if reaction.message_id == Welcome20r().messageInfo:
            #     emojiRoles = Welcome20r().Roles.get(emoji)
            #     for emojiReaction in emojiRoles:
            #         await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Region20r().messageInfo:
                emojiRoles = Region20r().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Member20r().messageInfo:
                skipAdd = False
                emojiRoles = Member20r().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
                    await member.remove_roles(member.guild.get_role(588931614017323058), atomic=True) # removes stranger role
        else:
            return


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(RawReactAdd(client))
    logging.info("RawReactAdd loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("RawReactAdd unloaded!")
