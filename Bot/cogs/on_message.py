import logging
import json
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import *
from nextcord.ext.tasks import *

from Bot.core.bot import Bot

logger = logging.getLogger(__name__)



class onMessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        donor = 0
        author = message.author
        donatorRoles = [591210327002054660, 701869901492650104, 591043526939377678, 795413904616062987,
                        794624216439586825, 591043464238465054, 794624212878491708, 794624205416431628,
                        764625200565321738, 794624205416431628, 764625200565321738, 591043464238465054,
                        590910479841361972]
        # Donator roles Silver+ as well and esports
        if message.channel.id == 778094721394147338:  # venting void
            await message.delete() # auto delete any messages send into that channel
        if message.channel.id == 782305812558774272:  # esports venting void
            await message.delete() # auto delete any messages send into that channel
        if message.channel.id == 673436198751961088: # self-promo
            print(author.roles)
            if author != self.client.user:  # Makes it so the bot ignores itself
                for donator in donatorRoles:
                    Donator = nextcord.utils.get(author.roles, id=int(donator))
                    if Donator in author.roles:
                        donor = 1
                if donor == 0:
                    await message.delete()
                    embed = nextcord.Embed(title=f"**__Donators Only__**", colour=nextcord.Colour(4886754),
                                          description=f'Sorry {author.mention}\n'
                                                      f'This channel is authorised for <@&794624205416431628> and above\n'
                                                      f'If you are interested in promoting on our discord,\n'
                                                      f'please donate at our [Patreon](https://www.patreon.com/20r).\n'
                                                      f'**Our Patreon:**\n'
                                                      f'https://www.patreon.com/20r')
                    embed.set_thumbnail(url=Bot.LOGO)
                    await message.channel.send(f"{author.mention}", embed=embed, delete_after=20)



# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(onMessage(client))
    logging.info("onMessage loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("onMessage unloaded!")
