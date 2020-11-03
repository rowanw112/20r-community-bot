""" [Null-Byte]
This file, especially, needs some docstrings at the very least.

`on_command_error` is some of the more nested, complicated Python code I've
seen; however, I'm not even sure whose fault such would be as it looks like
you're doing all you can to provide messages back to the calling user.

Programmatically, please provide a docstring in the aforementioned section
to maybe perhaps shed some light on what's exactly going on.
"""

import traceback
import datetime
import json
import discord

from discord import *
from discord.ext import commands
from datetime import *

from Bot.core.config import *

logger = logging.getLogger(__name__)


class Bot(commands.AutoShardedBot):
    config = configfile()  # loads the config file from config.py
    JSONDirectory = config["JSONDirectory"]
    CogDirectory = config["CogDirectory"]
    GITRepo = config["GITRepo"]
    LOGO = "https://cdn.discordapp.com/attachments/721427319381688320/758831668949418004/20r_Logo_2020.png"
    """ Loads all the permissions """
    with open(JSONDirectory + os.sep + "Roles" + os.sep + "permissionSwitcher.json", "r", encoding="utf-8") as f:
        JSON = json.load(f)
        for data in JSON:
            permissionwhiteList = data["Switcher"]["permissionwhiteList"]
            addPermission = data["Switcher"]["addPermission"]
            deletePermission = data["Switcher"]["deletePermission"]

    def __init__(self, *args, **kwargs):
        self.start_time = datetime.now(tz=timezone.utc)
        super().__init__(*args, **kwargs)

    async def on_command_error(self, ctx: commands.Context, exception: commands.errors.CommandInvokeError):
        error = getattr(exception, "original", exception)
        if isinstance(exception, commands.errors.BadArgument):
            await ctx.send(f"{str(exception).replace('int', 'whole number')}"
                           f"\n\nEnsure you're passing the correct values for each parameter.", delete_after=10)
        elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole, commands.MissingPermissions)):
            await ctx.send(f"{ctx.message.author.mention} You do not have permissions to use this command", delete_after=10)
        elif isinstance(exception, commands.errors.MissingRequiredArgument):
            await ctx.send(f"{(str(exception).split()[0].title() + ' ' + ' '.join(str(exception).split()[1:]))}", delete_after=10)
        elif isinstance(exception, commands.errors.CheckAnyFailure):
            await ctx.send(f"{str(exception)}", delete_after=10)
        elif isinstance(error, commands.CommandNotFound):
            logger.info(f"{ctx.author.display_name} issued a command that does not exist")
        elif isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace("_", " ").replace("guild", "server").title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = " and ".join(missing)
            _message = "I need the **{}** permission(s) to run this command.".format(fmt)
            await ctx.send(_message, delete_after=10)
        elif isinstance(exception, commands.errors.CheckFailure):
            await ctx.send("You lack permissions to use this command!", delete_after=10)
        else:
            logger.exception(traceback.print_exception(type(error), error, error.__traceback__))
            await ctx.send(
                f"{ctx.message.author.mention} There was an unexpected error while executing this command! My creator has been notified", delete_after=10)

    async def on_command(self, ctx: commands.Context):
        try:
            logger.info(f'{ctx.author.display_name} ({ctx.author.id}) invoked a command '
                        f'\"{ctx.message.content}\" in the guild {ctx.guild} ({ctx.guild.id}) in the channel '
                        f'{ctx.channel.name} ({ctx.channel.id})')
        except AttributeError:
            logger.info(f'{ctx.author.display_name} ({ctx.author.id}) invoked a command '
                        f'\"{ctx.message.content}\" in DMs')

