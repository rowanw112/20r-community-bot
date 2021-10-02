from Bot.cogs.battlemetric import *
from Bot.cogs.reactroles import *

logger = logging.getLogger(__name__)


class member_update(commands.Cog):
    def __init__(self, client):
        self.client = client

    @staticmethod
    async def uniquerole(after, Uniqueroles, newRoleid):
        Uniqueroles.remove(newRoleid)
        for roles in Uniqueroles:
            await after.remove_roles(after.guild.get_role(roles), atomic=True)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        prefixes = "[R]", "[Ⅰ]", "[ⅠⅠ]", "[ⅠⅠⅠ]", "[ⅠⅤ]", "[Ⅴ]"
        exemptprefixes = "[A]", "[L]", "[DA]", "[DL]", "[VG]", "[D]", "[M]", "[IN]", "[TS]"
        staff = False  # defaults to non-staff
        Uniquememberroles = [588816938202038292, 876573382521540678, 876573539749216287, 880225900174667837,
                             880225940901359646,
                             880225976376758353]  # R, I, II, III, IV, V
        Uniquestaffroles = [622594532793516072, 772257836654002176, 531857509103697920,
                            531857333664481280, 611442318305787914,
                            605857237407236097]  # IN, TS, Assist, Lead, DA, DL
        if len(before.roles) < len(after.roles):  # The user has gained a new role
            newRole = next(role for role in after.roles if role not in before.roles)
            """
            Unique Member Roles
            """
            if newRole.id == 588816938202038292:  # R
                prefixwanted = "[R]"
                await after.remove_roles(after.guild.get_role(531857621603450881), atomic=True)  # removes member role
                await self.uniquerole(after, Uniquememberroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 876573382521540678:  # I
                prefixwanted = "[Ⅰ]"
                await after.add_roles(after.guild.get_role(531857621603450881), atomic=True) # assigns member role
                await self.uniquerole(after, Uniquememberroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 876573539749216287:  # II
                prefixwanted = "[ⅠⅠ]"
                await after.add_roles(after.guild.get_role(531857621603450881), atomic=True)  # assigns member role
                await self.uniquerole(after, Uniquememberroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 880225900174667837:  # III
                prefixwanted = "[ⅠⅠⅠ]"
                await after.add_roles(after.guild.get_role(531857621603450881), atomic=True)  # assigns member role
                await self.uniquerole(after, Uniquememberroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 880225940901359646:  # IV
                prefixwanted = "[ⅠⅤ]"
                await after.add_roles(after.guild.get_role(531857621603450881), atomic=True)  # assigns member role
                await self.uniquerole(after, Uniquememberroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 880225976376758353:  # V
                await after.add_roles(after.guild.get_role(531857621603450881), atomic=True)  # assigns member role
                prefixwanted = "[Ⅴ]"
                await self.uniquerole(after, Uniquememberroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            """
                Vanguard Role
            """
            if newRole.id == 599080943755591695:  # Vanguard
                prefixwanted = "[VG]"
                await self.updatedprefix(after, prefixwanted, staff)
            """
            Unique Staff Roles
            """
            if newRole.id == 622594532793516072:  # IN role
                prefixwanted = "[IN]"
                staff = True
                await self.uniquerole(after, Uniquestaffroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 772257836654002176:  # TS role
                prefixwanted = "[TS]"
                staff = True
                await self.uniquerole(after, Uniquestaffroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 531857509103697920:  # A role
                prefixwanted = "[A]"
                staff = True
                await self.uniquerole(after, Uniquestaffroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 531857333664481280:  # L role
                prefixwanted = "[L]"
                staff = True
                print("1")
                await self.uniquerole(after, Uniquestaffroles, newRole.id)
                print("2")
                await self.updatedprefix(after, prefixwanted, staff)
                print("3")
            if newRole.id == 611442318305787914:  # DA role
                prefixwanted = "[DA]"
                staff = True
                await self.uniquerole(after, Uniquestaffroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
            if newRole.id == 605857237407236097:  # DL role
                prefixwanted = "[DL]"
                staff = True
                await self.uniquerole(after, Uniquestaffroles, newRole.id)
                await self.updatedprefix(after, prefixwanted, staff)
        if len(after.roles) < len(before.roles):  # The user has lost a role
            oldRole = next(role for role in before.roles if role not in after.roles)
            if oldRole.id == 599080943755591695:  # Vanguard
                prefixwanted = ""
                prefix = "[VG]"
                await after.edit(nick=str(after.display_name).replace(prefix, prefixwanted))


    @staticmethod
    async def updatedprefix(after, prefixWanted, staff):
        prefixes = ["[R]", "[Ⅰ]", "[ⅠⅠ]", "[ⅠⅠⅠ]", "[ⅠⅤ]", "[Ⅴ]"]
        exemptprefixes = ["[VG]", "[A]", "[L]", "[DA]", "[DL]", "[D]", "[M]", "[IN]", "[TS]"]
        allprefixes = ["[R]", "[Ⅰ]", "[ⅠⅠ]", "[ⅠⅠⅠ]", "[ⅠⅤ]", "[Ⅴ]", "[A]", "[L]", "[VG]", "[IN]", "[TS]"]
        exempt = False
        replace = False
        noPrefix = True  # to say if the user does not have a prefix
        finished = False  # to prevent looping

        for prefix in prefixes:
            for exemptprefix in exemptprefixes:  # if user has a exempt prefix like staff
                if exemptprefix in after.display_name:
                    exempt = True  # if user has exemptprefixes
            for prefixes in allprefixes:
                if prefixes in after.display_name:
                    noPrefix = False  # to confirm if the user has a prefix
            if prefix in after.display_name and not noPrefix and not finished:
                replace = True  # if user has one of the prefixes, then it needs replacing
            if replace and not exempt and not staff and not finished:  # if user has replace and not exempt
                await after.edit(nick=str(after.display_name).replace(prefix, prefixWanted))
                finished = True
            if noPrefix and not finished and not exempt:  # if user does not have a prefix, then they're being given one
                await after.edit(nick=prefixWanted + " " + str(after.display_name))
                noPrefix = False
                finished = True
            if staff and not finished:  # if user is gaining a staff role
                for prefix in allprefixes:
                    await after.edit(nick=str(after.display_name).replace(prefix, prefixWanted))
                    finished = True

        # if len(before.roles) < len(after.roles): # The user has gained a new role
        #     newRole = next(role for role in after.roles if role not in before.roles)
        #     if newRole.id == Uniquerole1:
        #         print(f"{after} was assigned unique role 1")
        #
        # if len(after.roles) < len(before.roles): # The user has lost a role
        #     oldRole = next(role for role in before.roles if role not in after.roles)
        #     if oldRole.id == Uniquerole1:
        #         print(f"{after} has removed unique role 1")


# Called To Load Cog And Connect To Client
def setup(client):
    client.add_cog(member_update(client))
    logging.info("member_update loaded!")


# Called When Cog Is Unloaded
def teardown():
    logging.info("member_update unloaded!")
