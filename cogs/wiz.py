import discord
from discord.ext import commands

import asyncio
from pywizlight.bulb import wizlight, PilotBuilder
# create/get the current thread's asyncio loop
loop = asyncio.get_event_loop()
# setup a standard light
light = wizlight('IPADDY')
light2 = wizlight('IPADDY')
light3 = wizlight('IPADDY')

from itertools import repeat
import time
import math

class WizCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Wiz Cog Loaded.')

    @commands.command(name='wizinfo')
    async def get_W1(self, ctx):
        """List Wiz Info."""
        try:
            await ctx.send('Sending Wiz Command....')
            #message = '{"method": "getPilot", "id": 24, "params": {}}'
            #test = await light.sendUDPMessage(message, timeout = 60, send_interval = 0.5, max_send_datagrams = 100)
            #print(test)
            state = await light.updateState()
            state2 = await light2.updateState()
            state3 = await light3.updateState()
            config = await light.getBulbConfig()
            config2 = await light2.getBulbConfig()
            config3 = await light3.getBulbConfig()
            name = config.get('result').get('mac')
            name2 = config2.get('result').get('mac')
            name3 = config3.get('result').get('mac')
            r, g, b = state.get_rgb()
            r2, g2, b2 = state2.get_rgb()
            r3, g3, b3 = state3.get_rgb()
            brightness = state.get_brightness()
            brightness2 = state2.get_brightness()
            brightness3 = state3.get_brightness()
            output = 'Light 1\nMac: ' + str(name) + '\nBrightness: ' +  str(brightness) + '\nRBGColour: ' +  str(r) + ' ' + str(g) + ' ' + str(b) + '\n' + \
                     'Light 2\nMac: ' + str(name2) + '\nBrightness: ' +  str(brightness2) + '\nRBGColour: ' +  str(r2) + ' ' + str(g2) + ' ' + str(b2) + '\n' + \
                     'Light 3\nMac: ' + str(name3) + '\nBrightness: ' +  str(brightness3) + '\nRBGColour: ' +  str(r3) + ' ' + str(g3) + ' ' + str(b3) + '\n'
            await ctx.send('```' +output+ '```')
        except (RuntimeError, AttributeError):
            await ctx.send('Wiz Command Failed.')

    @commands.command(name='wizblue')
    async def get_W2(self, ctx):
        """Set Wiz Blue."""
        try:
            await ctx.send('Sending Wiz Command....')

            # turn on the light into "rhythm mode"
            await light.turn_on(PilotBuilder())
            # set bulb brightness
            await light.turn_on(PilotBuilder(brightness = 255))
            await light.turn_on(PilotBuilder(rgb = (0, 0, 255)))

            await ctx.send('Wiz Command Finished....')
        except (RuntimeError, AttributeError):
            await ctx.send('Wiz Command Failed.')

def setup(bot):
    bot.add_cog(WizCog(bot))
