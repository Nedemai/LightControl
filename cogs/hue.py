import discord
from discord.ext import commands

from phue import Bridge

from itertools import repeat
import time
import math

b = Bridge('IPADDY')

class HueCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Hue Cog Loaded.')

    @commands.command(name='hueinfo')
    async def get_P1(self, ctx):
        """List Hue Info."""
        try:
            await ctx.send('Sending Hue Command....')
            b.connect()
            #data = b.get_api()
            #for d in data:
                #print(d)
            lights = b.lights
            output = ''
            for l in lights:
                #print(l) 
                #print(l.name)

                print('Name: ' + str(l.name))
                print('On: ' + str(l.on))
                print('Colormode: ' + str(l.colormode))
                print('Hue: ' + str(l.hue))
                print('Brightness: ' + str(l.brightness))
                print('Saturation: ' + str(l.saturation))
                print('Colortemp: ' + str(l.colortemp) + '\n')

                output += 'Light Name: ' + str(l.name) + '\nBrightness: ' +  str(l.brightness) + '\nColour: ' +  str(l.hue) + '\n'
            await ctx.send('```' +output+ '```')
        except (RuntimeError, AttributeError):
             await ctx.send('Hue Command Failed.')

    @commands.command(name='huebrightness')
    async def get_P2(self, ctx, Var):
        """Set Hue Brightness."""
        try:
            await ctx.send('Sending Hue Command....')
            b.connect()
            #data = b.get_api()
            #for d in data:
                #print(d)
            lights = b.lights
            output = ''
            for l in lights:
                #print(l) 
                #print(l.name)
                if Var.isdigit():
                    Var = Var
                    #print(Var)
                    #print(l.brightness)
                    l.brightness = int(Var)
                output += 'Light Name: ' + str(l.name) + '\nBrightness: ' +  str(l.brightness) + '\n'
            await ctx.send('```' +output+ '```')
        except (RuntimeError, AttributeError):
             await ctx.send('Hue Command Failed.')

    @commands.command(name='hueblue')
    async def get_P3(self, ctx):
        """Set Hue Blue."""
        try:
            await ctx.send('Sending Hue Command....')
            b.connect()
            lights = b.lights
            for l in lights:
                #print(l) 
                l.hue = 47104         # blue  (43690 Light Blue)
                l.saturation = 254
                #l.colortemp = 154

                #l.brightness = 100
                #time.sleep(1)
                #l.brightness = 254

            await ctx.send('Hue Command Finished....')
        except (RuntimeError, AttributeError):
             await ctx.send('Hue Command Failed.')

def setup(bot):
    bot.add_cog(HueCog(bot))

# Hue Colours.
# ------------------
# 47104 Blue.
# 43690 Light Blue.