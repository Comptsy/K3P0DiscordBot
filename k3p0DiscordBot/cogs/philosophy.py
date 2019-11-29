import discord
from discord.ext import commands

class Philosophy(commands.Cog):
    """Commands providing philosophical speculation and absolute answers"""
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    @commands.command(brief = "You've always wondered", description = "Tells the meaning of life")
    async def meaningoflife(self, ctx):
        choice = random.randint(0,1)
        if(choice == 0):
            await ctx.send("42.")
        elif(choice == 1):
            await ctx.send("Try to be nice to people, avoid eating fat, read a good book every now and then, get some walking in, and try to live in peace and harmony with people of all creeds and nations.")
        else:
            await ctx.send("If this message appeared, you broke it.  Good job.")

    @commands.command(brief = "Gives the answer", description = "Tells the answer to the Ultimate Question of Life, the Universe, and Everything")
    async def answer(ctx):
        await ctx.send("42.")

    @commands.command(brief = "Gives the question", description = "Tells the Ultimate Question of Life, the Universe and Everything, to which the answer is 42")
    async def question(ctx):
        eggs = random.randint(0,6)
        questions = ["What do you get if you multiply six by nine?", "How many roads must a man walk down?", "What's six times seven?", "Why?", "Are we stronger than the elements?", "What's yellow and dangerous?", "How many vogons does it take to change a lightbulb?"]
        await ctx.send(questions[eggs])



    