import discord
from discord.ext import commands

from itertools import repeat
import time
import math

import pytuya
light = pytuya.BulbDevice('VIRTUAL-DEVICE-ID', 'INTERNAL-IP', 'LOCAL-KEY') # Refer To Dozens Of Guides Of How To Aquire A Local Key
bar = pytuya.OutletDevice('VIRTUAL-DEVICE-ID', 'INTERNAL-IP', 'LOCAL-KEY') # Refer To Dozens Of Guides Of How To Aquire A Local Key

def blueredblink(data):
    for x in range(0, 10):
        data = light.set_colour(255,0,0)
        time.sleep(1)
        data = light.set_colour(0,0,255)
        time.sleep(1)

def redgreenblink(data):
    for x in range(0, 10):
        data = light.set_colour(0,255,0)
        time.sleep(0.3)
        data = light.set_colour(255,0,0)
        time.sleep(0.3)

class TuyaCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Tuya Cog Loaded.')

    @commands.command(name='tuyaalert')
    async def get_T1(self, ctx):
        """Send Tuya Alert."""
        data = light.status()
        try:
            await ctx.send('Pinging Alert Light....')
            print('Dictionary %r' % data)
            print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device
            if data['dps']['1'] == True:
                # Toggle Blue/Red
                switch_state = data['dps']['5']
                blueredblink(data)
                if data:
                    print('set_colour() result %r' % data)
            else:
                print('Alert Light Is Off.')
                await ctx.send('Alert Light Is Off. Try Again Later.')
            # Toggle switch state
            #switch_state = ldata['dps']['1']
            #ldata = light.set_status(not switch_state)  # This requires a valid key
            #if ldata:
                #print('set_status() result %r' % ldata)
            await ctx.send('Ping Finished....')
        except (RuntimeError, AttributeError):
            await ctx.send('Tuya Light Command Failed.')

    @commands.command(name='tuyaxmas')
    async def get_T2(self, ctx):
        """Send Tuya Xmas."""
        data = light.status()
        try:
            await ctx.send('Pinging Xmas Alert Light....')
            print('Dictionary %r' % data)
            print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device
            if data['dps']['1'] == True:
                # Toggle Blue/Red
                switch_state = data['dps']['5']
                redgreenblink(data)
                if data:
                    print('set_colour() result %r' % data)
            else:
                print('Alert Light Is Off.')
                await ctx.send('Alert Light Is Off. Try Again Later.')
            await ctx.send('Ping Finished....')
        except (RuntimeError, AttributeError):
            await ctx.send('Tuya Light Command Failed.')

    @commands.command(name='tuyablue')
    async def get_T3(self, ctx):
        """Set Tuya Blue."""
        data = light.status()
        try:
            await ctx.send('Sending Tuya Light Command....')

            print('Dictionary %r' % data)
            print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device

            # Toggle Blue
            switch_state = data['dps']['5']
            data = light.set_colour(0,0,255)  # This requires a valid key
            if data:
                print('set_colour() result %r' % data)

            # Toggle switch state
            #switch_state = ldata['dps']['1']
            #ldata = light.set_status(not switch_state)  # This requires a valid key
            #if ldata:
                #print('set_status() result %r' % ldata)

            await ctx.send('Tuya Light Command Finished....')
        except (RuntimeError, AttributeError):
            await ctx.send('Tuya Light Command Failed.')

    @commands.command(name='tuyabar')
    async def get_T4(self, ctx):
        """Set Tuya Bar."""
        data = bar.status()
        try:
            await ctx.send('Sending Tuya Bar Command....')

            print('Dictionary %r' % data)
            print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device

            # Toggle switch state
            switch_state = data['dps']['1']
            data = bar.set_status(not switch_state)  # This requires a valid key
            if data:
                print('set_status() result %r' % data)

            await ctx.send('Tuya Bar Command Finished....')
        except (RuntimeError, AttributeError):
            await ctx.send('Tuya Bar Command Failed.')

def setup(bot):
    bot.add_cog(TuyaCog(bot))
