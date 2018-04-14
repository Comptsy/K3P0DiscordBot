import discord
from discord.ext import commands
from expcalc import ExpCalc
import random
from characterRecord import *

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

@bot.command(brief = "You've always wondered", description = "Tells the meaning of life")
async def meaningoflife():
    choice = random.randint(0,1)
    if(choice == 0):
        await bot.say("42.")
    elif(choice == 1):
        await bot.say("Try to be nice to people, avoid eating fat, read a good book every now and then, get some walking in, and try to live in peace and harmony with people of all creeds and nations.")
    else:
        await bot.say("If this message appeared, you broke it.  Good job.")

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
            'd3':random.randint(1,3), 'd2':random.randint(1,2), 'd30':random.randint(1,30), 'd%':random.randint(1,100)}
            thisRoll = rolls[die]
            roll = roll + rolls[die]
            print(thisRoll)
        await bot.say("`Total roll is {0}`".format(roll))
    else:
        await bot.say("I don't know that die!")

@bot.command(brief = "Create new sheet", description = "Create an empty character sheet")
async def newsheet(name):
    sheet = CreateSheet()
    sheet.new_sheet(name)
    await bot.say("`Created new charcter sheet with name {0}`".format(name))

@bot.command(brief = "Add to sheet", description = "Add line of data to charcter sheet")
async def addto(name, data):
    sheet = WriteToSheet()
    sheet.add_line(name, data)
    await bot.say("`Added line \"{0}\" to {1}`".format(data, name))

@bot.command(brief = "Print entire sheet", description = "Print entire character sheet")
async def showsheet(name):
    sheet = ReadFromSheet()
    await bot.say("```{0}```".format(sheet.read_sheet(name)))

@bot.command(brief = "Read specific line", description = "Print specific data line from charcter sheet")
async def showline(name, data):
    sheet = ReadFromSheet()
    await bot.say("```{0}```".format(sheet.read_sheet_data(name, data)))


