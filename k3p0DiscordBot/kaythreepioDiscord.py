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

@bot.command(brief = "Gives the answer", description = "Tells the answer to the Ultimate Question of Life, the Universe, and Everything")
async def answer():
    await bot.say("42.")

@bot.command(brief = "Gives the question", description = "Tells the Ultimate Question of Life, the Universe and Everything, to which the answer is 42")
async def question():
    eggs = random.randint(0,6)
    questions = ["What do you get if you multiply six by nine?", "How many roads must a man walk down?", "What's six times seven?", "Why?", "Are we stronger than the elements?", "What's yellow and dangerous?", "How many vogons does it take to change a lightbulb?"]
    await bot.say(questions[eggs])

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

@bot.command(brief = "Identify material based on scent", description = "Identifies any substance or material based entirely on scent. Give an item as an argument, and Cheesoid will determine what it is made from.")
async def cheesoid(item):
    c = """
    Cheesoid:
    `CHEESE!`
    """
    p = """
    Cheesoid:
    `PETRIL!`
    """
    cheeses = ['cheese', 'cheddar', 'gouda', 'brie', 'mozzerella', 'parmesean', 'feta', 'marscapone', 'gruyere', 'burrata', 'camebert', 'grana pedano', 'roquefort', 'emmental', 'taleggio', 'stilton', 'pecorino romano', 'fromage blanc', 'fontina', 'tete de moine',
    'caciocavallo', 'comte', 'epoisses de bourgogne', 'morbier', 'brunost', 'fourme d\'ambert', 'saint marcellin', 'tilsit', 'tomme de savoie', 'crottin de chavignol', 'ossau-iraty', 'castelmagno', 'mahon', 'bleu', 'manouri', 'pecorino sardo', 'sbrinz', 'delice de bourgogne',
    'fromager d\'affinois', 'brillat-savarin', 'humboldt fog', 'pont-l\'evêque', 'caerphilly', 'chabichou', 'shropshire blue', 'bucheron', 'l\'etivaz', 'langres', 'valdeon', 'sottocenere al tartufo', 'sainte-maure de touraine', 'pag', 'pepato']
    petrols = ['petrol', 'petril', 'plastic', 'petroleum', 'gas', 'gasoline']
    if(item in cheeses):
        await bot.say(p)
    elif("cheese" in item):
        await bot.say(p)
    elif(item in petrols):
        await bot.say(c)
    else:
        spam = random.randint(0,1)
        if(spam == 0):
            await bot.say(c)
        else:
            await bot.say(p)

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
