import discord
from discord.ext import commands
from expcalc import ExpCalc
import random

bot = commands.Bot(command_prefix='$', description='Multi-purpose D&D bot, Human-Cyborg relations')

@bot.command(brief = "Does it work?", description = "Does it work?")
async def test():
    await bot.say("It works.")

@bot.command(brief = "You know the answer.")
async def areyouon():
    await bot.say("Yes.")

@bot.command(brief = "Need you even ask?")
async def whatisthepoint():
    await bot.say("Only a fool would think there is one.")

@bot.command(brief = "Calculate EXP from monster", description = "Calculate EXP from a known monster by giving monster, average party level, and number of party members.")
async def exp(monster, partyLvl, partyNum):
    monster = monster
    partyLvl = partyLvl
    partyNum = partyNum
    await bot.say("EXP per player is " + str(ExpCalc.calcExp(monster, partyLvl, partyNum)))

@bot.command(brief = "Roll dice", description = "Roll number of dice, type of die")
async def roll(number, die):
    dice = ['d20', 'd12', 'd10', 'd8', 'd6', 'd4', 'd3', 'd%', 'd30', 'd2']
    roll = 0
    if die in dice:
        for i in range(1, int(number) + 1):
            rolls = {'d20':random.randint(1,20), 'd12':random.randint(1,12), 'd10':random.randint(1,10),
            'd8':random.randint(1,8), 'd6':random.randint(1,6), 'd4':random.randint(1,4),
            'd3':random.randint(1,3), 'd2':random.randint(1,2), 'd30':random.randint(1,30)}
            thisRoll = rolls[die]
            roll = roll + rolls[die]
            print(thisRoll)
        await bot.say("`Total roll is %a`" % roll)
    else:
        await bot.say("I don't know that die!")


bot.run('Mzk0MjgyNjI4NzI1MDgwMDY0.DSCD6w.rWN9RAK09bsqvDj-X_ZlxWFp8iE')

#https://discordapp.com/api/oauth2/authorize?client_id=394282628725080064&permissions=201353217&scope=bot
