import discord
from discord.ext import commands
from expcalc import ExpCalc
import random


class DnD(commands.Cog):
    """Commands to help with D&D, from die rollers to exp calculation"""
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    #D&D-related commands
    @commands.command(brief = "Helps the DM", description = "Says what the DM is sick of saying")
    async def dm(self, ctx, arg=None):
        a = "Shut the hell up and get back on the quest!"
        b = "Stop trying to turn the campaign into a dating sim!"
        c = "No, you can't seduce that so don't even try!"
        d = "Is it really so hard to focus for 10 seconds‽"
        e = "It's a rule now, so shut up about it!"
        f = "The guard looks at you after you ignore him. \"What in the name of God didst thou claim of me, thou miserable wretch? I must inform thee that I am a knight of unsurpassed valor and I have many a time participated in raids against the Viking rebels and have assuredly slain thirtyscore of them. I have trained in the art of simian warfare and none can challenge my skills of archery. Thou art nought in my eyes but another target. I shall exterminate thee with such accuracy that has never before been seen upon this mortal plane, hear me now. Didst thou truly believe thou couldst slander me so upon the tapestry? Reconsider your position, fool. As I write this, I am in the process of contacting my network of assassins across the land of England and they are tracking your movements at this instant, so thou would be wise to prepare thyself for the coming storm. The storm that destroys the unfortunate object you refer to as your life. Thou art assuredly deceased, knave. I can appear at any location and at any time, and can end thy life in seventyscore ways, and that be only when using my bare hands. But I am not solely skilled in fisticuffs; I also posess access to the entirety of Duke William\'s armory and I will make full use of it when banishing your body from the entirety of the earth. Thou scoundrel, perhaps hadst thou known what apocalyptic vengeance thy \"clever\" jests were to bring upon thee thou wouldst have held thy tongue. But thou couldst not, nor did not, and now thou art paying the due price of thy actions, fool. I shall defecate fury upon thee and thou shall flounder within it. Thou art truly smote, knave.\""

        args = {'quiet':a, 'dating':b, 'seduce':c, 'focus':d, 'rule':e, 'guard':f}
        if(args.get(arg)):
            print("Argument given")
            await ctx.send(args[arg])
        else:
            argsn = [a, b, c, d, e, f]
            num = random.randint(0,5)
            print("Sending random phrase")
            await ctx.send(argsn[num])

    @commands.command(brief = "Calculate EXP from monster", description = "Calculate EXP from a known monster by giving monster, average party level, and number of party members.")
    async def exp(self, ctx, monster, partyLvl, partyNum):
        monster = monster.title()
        partyLvl = partyLvl
        partyNum = partyNum
        await ctx.send("EXP per player is " + str(ExpCalc.calcExp(monster, partyLvl, partyNum)))

    @commands.command(brief = "Roll dice", description = "Roll number of dice, type of die")
    async def roll(self, ctx, die, sign=None, add=0):
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
                    await ctx.send("Invalid Sign")
        if(int(num[0]) > 256):
            print("Somebody tried to use an obscenely large number again!")
            await ctx.send("Nice try! Not falling for that again, Sean!")
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
                        await ctx.send("`Critical success: natural 20!`")
                    elif(die == 'd20' and thisRoll == 1):
                        print("Nat 1")
                        await ctx.send("`Critical failure: natural 1!`")
                    elif(die == 'd30' and thisRoll == 30):
                        print("Nat 30")
                        await ctx.send("`Critical success: natural 30!`")
                    elif(die == 'd30' and thisRoll == 1):
                        print("Nat 1 (d30)")
                        await ctx.send("`Critical failure: natural 1!`")
                    else:
                        pass
                    roll = roll + rolls[die]
                    print(thisRoll)
                roll = roll + int(add)
                await ctx.send("`Total roll is {0}`".format(roll))
            else:
                await ctx.send("I don't know that die!")
