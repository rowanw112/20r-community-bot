import asyncio
import logging
import os
import pkgutil
import sys
import time
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

import nextcord
from nextcord.ext import commands
import git


__depth__ = 2

__path__ = os.path.abspath(os.path.dirname(__name__))

pkgutil.extend_path(__path__, __name__)

__cwd__ = os.path.abspath(__path__ + "{}..".format(os.sep))
sys.path.append(__cwd__)
__cwd__ = os.path.abspath(__path__ + str("{}..".format(os.sep) * 2))
sys.path.append(__cwd__)

sys.path.append(__cwd__)

from Bot.core.bot import Bot

try:
    log_path = os.path.abspath(Bot.config["logpath"])
    Path(log_path).mkdir(parents=True, exist_ok=True)
except KeyError as missing_key:
    print(f"There is no Key \"{missing_key}\". Please enter the key in token:.")
    sys.exit(1)

# Log handling
logFormatter = logging.Formatter(
    "[%(asctime)s][%(threadName)s][%(name)s][%(lineno)d][%(levelname)s] %(message)s")
logger = logging.getLogger()
fileHandler = TimedRotatingFileHandler(os.path.join(log_path, "bot.log"), encoding="utf8", when="midnight",
                                       backupCount=7)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logging.getLogger("Discord")
############################


if Bot.config:
    try:
        client = Bot(
            command_prefix=(Bot.config["prefix"]),  # sets the prefix the commands for the bot
            case_insensitive=(Bot.config["case_insensitive"]),  # sets the case sensitivity for commands
            activity=nextcord.Game(name=Bot.config["activity"])  # sets the status of the bot
        )
        client.remove_command('help')
    except KeyError as missing_key:
        logger.critical(f"There is no config item {missing_key}. You have likely modified a key name in bot.yml,"
                        f" ensure bot.yml is correctly created.")
        sys.exit(1)
    if not "JSONDirectory" in Bot.config.keys():
        logger.critical(f"There is no config item \"JSONDirectory\". "
                        f"You have likely modified a key name in bot.yml, ensure bot.yml is correctly created.")
        sys.exit(1)
else:
    logger.critical("Exiting, config file was not properly loaded!")
    sys.exit(1)


# Load Cogs Command
@client.command()
@commands.check_any(commands.is_owner(),
                    commands.has_guild_permissions(administrator=True))
async def load(ctx, extension):
    try:
        gitpull()
    except:
        pass
    client.load_extension(f"Bot.cogs.{extension.lower()}")
    await ctx.send(f"`{extension} loaded!`", delete_after=10)
    await ctx.message.delete(delay=10)


# Unload Cogs Command
@client.command()
@commands.check_any(commands.is_owner(),
                    commands.has_guild_permissions(administrator=True))
async def unload(ctx, extension):
    try:
        client.unload_extension(f"Bot.cogs.{extension.lower()}")
        await ctx.send(f"`{extension} unloaded!`", delete_after=10)
        await ctx.message.delete(delay=10)
    except:
        logging.exception("Got exception on main handler")
        raise


# Restart Specific Cog Command
@client.command()
@commands.check_any(commands.is_owner(),
                    commands.has_guild_permissions(administrator=True))
async def restart(ctx, extension):
    try:
        gitpull()
    except:
        pass
    try:
        try:
            client.unload_extension(f"Bot.cogs.{extension.lower()}")
        except:
            pass
        client.load_extension(f"Bot.cogs.{extension.lower()}")
        await ctx.send(f"`{extension} restarted!`", delete_after=10)
        await ctx.message.delete(delay=10)
    except:
        logging.exception("Got exception on main handler")
        raise


@client.command()
@commands.check_any(commands.is_owner(),
                    commands.has_guild_permissions(administrator=True))
async def restartbot(ctx):
    """
    restarts the bot
    :param ctx:
    """
    await ctx.send(f"Bot is restarting", delete_after=5)
    sys.exit()


# Reload All Cogs Command
@client.command()
@commands.check_any(commands.is_owner(),
                    commands.has_guild_permissions(administrator=True))
async def reload(ctx):
    try:
        gitpull()
    except:
        pass
    try:
        for cog in os.listdir("..{0}cogs".format(
                os.sep
        )):
            if cog.endswith(".py"):
                try:
                    client.unload_extension(f"Bot.cogs.{cog[:-3]}")
                except:
                    pass
                client.load_extension(f"Bot.cogs.{cog[:-3]}")
                await ctx.send(f"`{cog[:-3]} loaded!`", delete_after=10)
        await ctx.send("`All cogs reloaded!`", delete_after=10)
        await ctx.message.delete(delay=10)
    except:
        logging.exception("Got exception on main handler")
        raise


# Function For Loading All Logs
def load_all_cogs():
    for filename in os.listdir(Bot.CogDirectory):
        if filename.endswith(".py"):
            client.load_extension(f"Bot.cogs.{filename[:-3]}")
    logging.info("All cogs loaded!")


def gitpull():
    try:
        repo = git.Repo(__cwd__)
        # blast any current changes
        repo.git.reset('--hard')
        # ensure master is checked out
        repo.heads.master.checkout()
        # blast any changes there (only if it wasn't checked out)
        repo.git.reset('--hard')
        # pull in the changes from from the remote
        repo.remotes.origin.pull("master")

        # repo.git.reset('--hard')
        # repo.remotes.origin.pull("Development")
        logging.info("git pulled")
        return
    except:
        logging.exception("Got exception on main handler")
        raise


try:
    logger.setLevel(client.config["log level"])
except ValueError:
    logger.setLevel("INFO")
    logger.warning("Set level to INFO, log level was incorrectly set in bot.yml")
    time.sleep(10)


@client.event
async def on_ready():
    """
    Function called for when the bot is up and ready!
    """
    logging.info(
        f"Bot online. Logged in as \nName: {client.user} \nID: ({client.user.id})")
    logging.info(f"Currently have access to the following guilds: "
                 f"{', '.join([f'{guild.name} ({guild.id})' for guild in client.guilds])}")
    logging.info("Current command prefix " + f"\"{client.command_prefix}\"")


def start_bot():
    """
    Function for starting the bot
    Loads all the cogs in bot.yml
    :return:
    """
    load_all_cogs()
    try:
        if not client.config["devStart"]:
            asyncio.get_event_loop().run_until_complete(
                client.start(client.config["token"]))
        else:
            asyncio.get_event_loop().run_until_complete(
                client.start(client.config["devToken"]))
    except discord.errors.LoginFailure:
        logger.critical(f"Could not login. Check your bot token!")
    except KeyError as missing_key:
        logger.critical(f"There is no config item {missing_key}. You have likely modified a key name in bot.yml,"
                        f" ensure bot.yml is correctly created.")


if __name__ == "__main__":
    start_bot()
