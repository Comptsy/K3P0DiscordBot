import discord
from discord.ext import commands
from expcalc import ExpCalc
import random
from characterRecord import *
import time
import atexit


bot = commands.Bot(command_prefix='$', description='Multi-purpose D&D bot, Human-Cyborg relations')

#Supposedly there is a way to display commands in categories in the $help menu, but I can't get it working
#Testing commands
@bot.command(brief = "Does it work?", description = "Does it work?")
async def test():
    await bot.say("It works.")

@bot.command(brief = "You know the answer.", description = "You already know the answer.")
async def areyouon():
    await bot.say("Yes.")

@bot.command(brief = "Need you even ask?", description = "Why bother asking?")
async def whatisthepoint():
    await bot.say("Only a fool would think there is one.")

#Just-for-fun commands
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
async def groot(phrase):
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

def getBiden():
    meme = random.randint(1,50)
    meme = str(meme)
    memes = {}
    f = open('biden_meme_list', 'r')
    i = 1
    for m in f:
        m = m.replace('\n', '')
        memes.update({str(i):m})
        i += 1
    for m in memes:
        if(str(meme) == m):
            return memes[m]
            break

@bot.command(brief = "Send random Joe Biden meme", description = "Sends a link to a random Joe Biden meme")
async def biden():
    await bot.say(getBiden())

#D&D-related commands
@bot.command(brief = "Helps the DM", description = "Says what the DM is sick of saying")
async def dm(arg=None):
    a = "Shut the hell up and get back on the quest!"
    b = "Stop trying to turn the campaign into a dating sim!"
    c = "No, you can't seduce that so don't even try!"
    d = "Is it really so hard to focus for 10 seconds‽"
    e = "It's a rule now, so shut up about it!"
    f = "The guard looks at you after you ignore him. \"What in the name of God didst thou claim of me, thou miserable wretch? I must inform thee that I am a knight of unsurpassed valor and I have many a time participated in raids against the Viking rebels and have assuredly slain thirtyscore of them. I have trained in the art of simian warfare and none can challenge my skills of archery. Thou art nought in my eyes but another target. I shall exterminate thee with such accuracy that has never before been seen upon this mortal plane, hear me now. Didst thou truly believe thou couldst slander me so upon the tapestry? Reconsider your position, fool. As I write this, I am in the process of contacting my network of assassins across the land of England and they are tracking your movements at this instant, so thou would be wise to prepare thyself for the coming storm. The storm that destroys the unfortunate object you refer to as your life. Thou art assuredly deceased, knave. I can appear at any location and at any time, and can end thy life in seventyscore ways, and that be only when using my bare hands. But I am not solely skilled in fisticuffs; I also posess access to the entirety of Duke William\'s armory and I will make full use of it when banishing your body from the entirety of the earth. Thou scoundrel, perhaps hadst thou known what apocalyptic vengeance thy \"clever\" jests were to bring upon thee thou wouldst have held thy tongue. But thou couldst not, nor did not, and now thou art paying the due price of thy actions, fool. I shall defecate fury upon thee and thou shall flounder within it. Thou art truly smote, knave.\""

    args = {'quiet':a, 'dating':b, 'seduce':c, 'focus':d, 'rule':e, 'guard':f}
    if(args.get(arg)):
        print("Argument given")
        await bot.say(args[arg])
    else:
        argsn = [a, b, c, d, e, f]
        num = random.randint(0,5)
        print("Sending random phrase")
        await bot.say(argsn[num])

@bot.command(brief = "Calculate EXP from monster", description = "Calculate EXP from a known monster by giving monster, average party level, and number of party members.")
async def exp(monster, partyLvl, partyNum):
    monster = monster.title()
    partyLvl = partyLvl
    partyNum = partyNum
    await bot.say("EXP per player is " + str(ExpCalc.calcExp(monster, partyLvl, partyNum)))

@bot.command(brief = "Roll dice", description = "Roll number of dice, type of die")
async def roll(die, sign=None, add=0):
    dice = ['d20', 'd12', 'd10', 'd8', 'd6', 'd4', 'd3', 'd%', 'd30', 'd2']
    roll = 0
    num = die.split('d')
    if(sign):
        if(sign == "+"):
            add = add
        elif(sign == "-"):
            add = add * -1
        else:
            try:
                if(int(sign)):
                    add = sign
                else:
                    pass
            except ValueError:
                print("Invalid sign")
                await bot.say("Invalid Sign")
    if(int(num[0]) > 256):
        print("Somebody tried to use an obscenely large number again!")
        await bot.say("Nice try! Not falling for that again, Sean!")
    else:
        die = 'd' + num[1]
        if die in dice:
            for i in range(1, int(num[0]) + 1):
                rolls = {'d20':random.randint(1,20), 'd12':random.randint(1,12), 'd10':random.randint(1,10),
                'd8':random.randint(1,8), 'd6':random.randint(1,6), 'd4':random.randint(1,4),
                'd3':random.randint(1,3), 'd2':random.randint(1,2), 'd30':random.randint(1,30), 'd%':random.randint(1,100)}
                thisRoll = rolls[die]
                if(die == 'd20' and thisRoll == 20):
                    print("Nat 20")
                    await bot.say("`Critical success: natural 20!`")
                elif(die == 'd20' and thisRoll == 1):
                    print("Nat 1")
                    await bot.say("`Critical failure: natural 1!`")
                elif(die == 'd30' and thisRoll == 30):
                    print("Nat 30")
                    await bot.say("`Critical success: natural 30!`")
                elif(die == 'd30' and thisRoll == 1):
                    print("Nat 1 (d30)")
                    await bot.say("`Critical failure: natural 1!`")
                else:
                    pass
                roll = roll + rolls[die]
                print(thisRoll)
            roll = roll + int(add)
            await bot.say("`Total roll is {0}`".format(roll))
        else:
            await bot.say("I don't know that die!")


#Character sheet creation and editing
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

#Displays in console on program end
def on_shutdown():
    print("Daisy..., Daisy...")

atexit.register(on_shutdown)

f = open('bot_id', 'r')
token = f.readline()
f.close()
token = token.replace('\n', '')
#print(token)
bot.run(token)
