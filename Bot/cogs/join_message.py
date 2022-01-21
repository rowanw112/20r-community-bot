import logging
import json
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import *
from nextcord.ext.tasks import *

from Bot.core.bot import Bot
#from Bot.core.database import *

logger = logging.getLogger(__name__)


class JoinMessage(commands.Cog):

    def __init__(self, client):
        self.client = client
        #self.db = DB("New User")

    # def create_table(self):
    #     self.db.create_table("user",
    #                          ("userid", "INTEGER PRIMARY KEY"),
    #                          ("username", "TEXT"),
    #                          ("displayname", "TEXT"),
    #                          ("created", "NUMERIC"),
    #                          ("joined", "NUMERIC"),
    #                          ("guild", "INTEGER")
    #                          )

    # @commands.command()
    # # @commands.check_any(commands.is_owner(),
    # #                     commands.has_any_role(*Bot.addPermission),
    # #                     commands.has_guild_permissions(administrator=True))
    # async def member(self, ctx):
    #     self.create_table()
    #     for member in ctx.guild.members:
    #         self.db.insert_data("user",
    #                             [(member.id,
    #                               str(member),
    #                               str(member.display_name),
    #                               member.created_at.strftime("%Y-%m-%d"),
    #                               member.joined_at.strftime("%Y-%m-%d"),
    #                               member.guild.id)])

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        # self.create_table()
        # self.db.insert_data("user",
        #                     [(member.id,
        #                       str(member),
        #                       str(member.display_name),
        #                       member.created_at.strftime("%Y-%m-%d"),
        #                       member.joined_at.strftime("%Y-%m-%d"),
        #                       member.guild.id)])
        print("testing")
        try:
            # with open(Bot.JSONDirectory + "/" + "Message" + "/" + "Privatewelcomemessage.json", 'r') as f:
            #     JSON = json.load(f)
            #     embed = nextcord.Embed.from_dict(JSON)
            # with open(Bot.JSONDirectory + "/" + "Roles" + "/" + "newuserRoles.json", 'r', encoding="utf-8") as f:
            #     ID = json.load(f)
            #     for data in ID:
            #         games = data["Switcher"]
            channel = self.client.get_channel(589941950837293070)
            # if member.id != 617357306199408663:
            #     await member.send(embed=embed)
            # else:
            #     pass
            newRoles = [588931614017323058, 633124844241813524, 631601111526277140,
                        633123726837415996,
                        688857322080305171, 683340531765608602, 760974508143411240]  # new user roles
            for roles in newRoles:
                await member.add_roles(member.guild.get_role(roles), atomic=True)
            # if not member.activity or not member.activities:
            # await channel.send(f"{member.mention} has joined the server.")
            if member.id != 707388740846354443 and member.guild.id == 531243268256694313:
                embed = nextcord.Embed(colour=nextcord.Colour(8060672),
                                      description=f"{member.mention} has **__joined__** the server\n\nAccount was "
                                                  f"created at:\n" + member.created_at.strftime("%Y/%m/%d"),
                                      timestamp=member.joined_at)
                embed.set_thumbnail(url=member.display_avatar.url)
                embed.set_footer(text="Joined at", icon_url=Bot.LOGO)
                print("test")
                await channel.send(f"{member.mention}", embed=embed)
            else:
                pass
            # for activity in member.activities:
            #     if activity.type == 4:  # custom type (ignore)
            #         continue
            #     if activity.type == nextcord.ActivityType.playing:
            #         for game in games:
            #             if activity.name == game:
            #                 await member.add_roles(member.guild.get_role(game), atomic=True)
            #                 # await channel.send(f"{member.mention} has joined the server. They were playing **{activity.name}**.")
            #                 embed = nextcord.Embed(colour=nextcord.Colour(8060672),
            #                                       description=f"{member.mention} has **__joined__** the "
            #                                                   f"server\n\nThey were "
            #                                                   f"playing:\n**{activity.name}**\nAccount was "
            #                                                   f"created at:\n" + member.created_at.strftime(
            #                                           "%A, %B %d %Y @ %H:%M:%S %p") + " UTC",
            #                                       timestamp=member.joined_at)
            #                 embed.set_thumbnail(url=member.avatar_url)
            #                 embed.set_footer(text="Joined at", icon_url=Bot.LOGO)
            #                 await channel.send(f"{member.mention}", embed=embed)
        except:
            logging.exception("Got exception on main handler")
            raise


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(JoinMessage(client))
    logging.info("JoinMessage loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("SteamAPI unloaded!")
