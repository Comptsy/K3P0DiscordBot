import discord
from discord.ext import commands
from expcalc import ExpCalc
import random
from characterRecord import *
import time
import atexit
import cogs.testing as T
import cogs.dnd as D
import cogs.jokes as J
import cogs.sheets as S
import cogs.philosophy as P


bot = commands.Bot(command_prefix='%', description='Multi-purpose D&D bot, Human-Cyborg relations')

@bot.event
async def on_connect():
    print("Connection established")

game = discord.Game("Human-Cyborg Relations")
@bot.event
async def on_ready():
    print("I am fluent in over 6 million forms of communication")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    if "didn't expect" in message.content.lower() or "wasn't expecting" in message.content.lower():
        await message.channel.send("NOBODY expects the Spanish Inquisition!")
    await bot.process_commands(message)

#Commands that don't fit in a category
@bot.command(brief = "Translate from English to Groot", description = "Translate from English to the language spoken by Groot in \"Guardians of the Galaxy\"")
async def groot(ctx, *, phrase):
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
        await ctx.send(final[0] + ' ' + final[1] + ' ' + final[2])

@bot.command(brief = "Identify material based on scent", description = "Identifies any substance or material based entirely on scent. Give an item as an argument, and Cheesoid will determine what it is made from.")
async def cheesoid(ctx, item):
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
        await ctx.send(p)
    elif("cheese" in item):
        await ctx.send(p)
    elif(item in petrols):
        await ctx.send(c)
    else:
        spam = random.randint(0,1)
        if(spam == 0):
            await ctx.send(c)
        else:
            await ctx.send(p)

@bot.command(brief = "Never gonna give you up...", description = "We're no strangers to love; you know the rules, and so do I.  A full commitment's what I'm thinking of, you wouldn't get this from any other bot", hidden = True)
async def rickroll(ctx, user: discord.Member):
    await user.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@bot.command(brief = "Plays a relaxing video", description = "Plays a nice, relaxing video in times of stress")
async def relax(ctx):
    await ctx.send("https://www.youtube.com/watch?v=V-_O7nl0Ii0&feature=youtu.be")
    
@bot.command(brief = "Contribute to development", description = "Help make K-3P0 better by contributing code on GitHub!")
async def contribute(ctx):
    await ctx.send("View the source code and contribute here:\n https://github.com/Comptsy/K3P0DiscordBot")


bot.add_cog(T.Testing(bot))
bot.add_cog(D.DnD(bot))
bot.add_cog(J.Jokes(bot))
bot.add_cog(S.Sheets(bot))
bot.add_cog(P.Philosophy(bot))

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
