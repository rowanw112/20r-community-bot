from Bot.cogs.reactroles import *

logger = logging.getLogger(__name__)


class RawReactAdd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        member = reaction.member
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
                emojiRoles = Member().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Public().messageInfo:
                emojiRoles = Public().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
            if reaction.message_id == Casual().messageInfo:
                emojiRoles = Casual().Roles.get(emoji)
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
            if reaction.message_id == Comp().messageInfo:
                emojiRoles = Comp().Roles.get(emoji)
                for emojiReaction in emojiRoles:
                    await member.add_roles(member.guild.get_role(emojiReaction), atomic=True)
        else:
            return


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(RawReactAdd(client))
    logging.info("RawReactAdd loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("RawReactAdd unloaded!")