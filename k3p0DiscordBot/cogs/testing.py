import discord
from discord.ext import commands

class Testing(commands.Cog):
    """Commands to test the bot and make sure it works"""
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None

    @commands.command(brief = "Does it work?", description = "Does it work?")
    async def test(self, ctx):
        await ctx.send("It works.")

    @commands.command(brief = "You know the answer.", description = "You already know the answer.")
    async def areyouon(self, ctx):
        await ctx.send("Yes.")

    @commands.command(brief = "Need you even ask?", description = "Why bother asking?")
    async def whatisthepoint(self, ctx):
        await ctx.send("Only a fool would think there is one.")

    @commands.command(brief = "If you are reading this, this test is a failure", description = "You can't see me, can you?", hidden = True)
    async def hiddentest(self, ctx):
        await ctx.send("You've found me!")
