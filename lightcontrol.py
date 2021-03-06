import discord
from discord.ext import commands
import sys, traceback

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['!']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.hue',
                      'cogs.wiz',
                      'cogs.tuya']

with open ("TOKEN", "r") as tokenFile:
    token = tokenFile.readline()

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    bot = commands.Bot(command_prefix=get_prefix, description='Lighting Control.')

    for extension in initial_extensions:
        bot.load_extension(extension)

    bot.run(token, bot=True, reconnect=True)
