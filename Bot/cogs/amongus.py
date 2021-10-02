import logging
import json
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.ext.tasks import *

from Bot.core.bot import Bot

logger = logging.getLogger(__name__)


class AmongUs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lobby(self, ctx, code, region):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        region_list = ["na", "eu", "asia"]
        if ctx.channel.id == 762429962778574868:  # Amongus-LFG
            if region.lower() in region_list:
                if hasattr(ctx.author.voice, 'channel') and ctx.author.voice.channel.category_id == 762378710099034112:
                    roomLink = await ctx.author.voice.channel.create_invite(max_age=1800)
                    roomLimit = ctx.author.voice.channel.user_limit
                    if roomLimit == 0 or roomLimit >= 11:
                        roomLimit = 10
                    embed = discord.Embed(colour=discord.Colour(0x2DC7FF), description=
                    f"[:arrow_right: **Click to join the voice channel!** :arrow_left:]({roomLink})\nIf you want to "
                    f"make your own party, join a voice channel and type \n **!invite *code* *region***",
                                          timestamp=ctx.message.created_at)
                    embed.set_author(name=f"{ctx.author} is looking for party members!",
                                     icon_url=f"{ctx.author.avatar_url}")
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/723773769289695253/764919925302755378/86e7cffeeb.png")
                    embed.add_field(name="**__Channel__**", value=f"**{ctx.author.voice.channel}**", inline=True)
                    embed.add_field(name="**__Party Size__**",
                                    value=f"**{len(ctx.author.voice.channel.members)} / {roomLimit}**",
                                    inline=True)
                    embed.add_field(name="**__Room Code & Region__**",
                                    value=f"**{code.upper()}** || **{region.upper()}**",
                                    inline=True)
                    embed.set_footer(text="20r Gaming", icon_url=Bot.LOGO)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Please join a voice channel first in the AMONG US category!", delete_after=5)
            else:
                await ctx.send(f"please input a valid region {', '.join(region_list)}")
        else:
            await ctx.send("Please enter this command in <#762429962778574868>",
                           delete_after=5)  # tells user to enter in lfg


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(AmongUs(client))
    logging.info("AmongUs loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("AmongUs unloaded!")

