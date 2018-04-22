import discord
from discord.ext import commands
from expcalc import ExpCalc
import random
from characterRecord import *
import time
import atexit


bot = commands.Bot(command_prefix='$', description='Multi-purpose D&D bot, Human-Cyborg relations')

#Commands that don't fit in a category
@bot.command(brief = "You've always wondered", description = "Tells the meaning of life")
async def meaningoflife():
    choice = random.randint(0,1)
    if(choice == 0):
        await bot.say("42.")
    elif(choice == 1):
        await bot.say("Try to be nice to people, avoid eating fat, read a good book every now and then, get some walking in, and try to live in peace and harmony with people of all creeds and nations.")
    else:
        await bot.say("If this message appeared, you broke it.  Good job.")

@bot.command(brief = "Translate from English to Groot", description = "Translate from English to the language spoken by Groot in \"Guardians of the Galaxy\"")
async def groot(*, phrase):
        groot = ["I", "am", "Groot."]
        final = []
        for i in groot:
            emph = random.randint(0,2)
            if(emph == 0):
                i = "{0}".format(i)
            elif(emph == 1):
                i = "*{0}*".format(i)
            else:
                i = "**{0}**".format(i)
            final.append(i)
            print(i)
        await bot.say(final[0] + ' ' + final[1] + ' ' + final[2])

if(__name__ == '__main__'):
    bot.load_extension('cogs.testing')
    bot.load_extension('cogs.dnd')
    bot.load_extension('cogs.sheets')
    bot.load_extension('cogs.jokes')

#Displays in console on program end
def on_shutdown():
    print("End of line.")

atexit.register(on_shutdown)

f = open('bot_id', 'r')
token = f.readline()
f.close()
token = token.replace('\n', '')
#print(token)
bot.run(token)
