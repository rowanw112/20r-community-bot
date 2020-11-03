import logging
import json
from Bot.core.bot import Bot

logger = logging.getLogger(__name__)


prefixes = "[R] ", "[Ⅰ] ", "[ⅠⅠ] ", "[ⅠⅠⅠ] ", "[ⅠⅤ] ", "[Ⅴ] ", "[A] ", "[L] ", "[I] ", "[DA] ", "[DL] ", "[REC] ", "[CO] ", "[VG] ", "[AS] ", "[D] ", "[SPC] "
#   These are the prefixes that the bot ignores for assigning [R] tag.
prefixesRemoval = "[R] ", "[Ⅰ] ", "[ⅠⅠ] ", "[ⅠⅠⅠ] ", "[ⅠⅤ] ", "[Ⅴ] ", "[A] ", "[L] ", "[I] ", "[REC] ", "[SPC] "
#   These are the prefixes that the bot will remove upon a removal command.
prefixesExempt = "[A] ", "[L] ", "[DA] ", "[DL] ", "[CO] ", "[VG] ", "[AS] ", "[D] ", "[TS] "


def switcherLoad():
    """
loads the switcher of roles : ids
    """
    with open(Bot.JSONDirectory + os.sep + "Roles" + os.sep + "switcherID.json", "r", encoding="utf-8") as f:
        JSON = json.load(f)
        for data in JSON:
            switcher = data["Switcher"]
    return switcher


async def assignPermissions(ctx, member, permissionString):
    """
    Assigning roles by looking up roles on the switcher.
    :param ctx:
    :param member:
    :param permissionString:
    """
    permissionId = switcherLoad().get(permissionString)
    if permissionId is not None:
        for permissionUnit in permissionId:
            await member.add_roles(ctx.guild.get_role(permissionUnit), atomic=True)


async def removePermissions(ctx, member, permissionString):
    """
    Function of removing roles by the name, by searching them from the switcher.
    :param ctx:
    :param member:
    :param permissionString:
    """
    permissionId = switcherLoad().get(permissionString)
    if permissionId is not None:
        for permissionUnit in permissionId:
            await member.remove_roles(ctx.guild.get_role(permissionUnit), atomic=True)


async def purgePermissions(ctx, member):
    """
    function of removing all roles from the user beside the ones that are excluded,
    assigns stranger role to them once been purged.
    :param ctx:
    :param member:
    """
    for role in member.roles:
        if role.id in Bot.permissionwhiteList:
            continue
        await member.remove_roles(ctx.guild.get_role(role.id), atomic=True)
    await assignPermissions(ctx, member, "20rStranger")
