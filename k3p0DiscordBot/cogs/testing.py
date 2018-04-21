import discord
from discord.ext import commands

class Testing:
    """Commands to test the bot and make sure it works"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Does it work?", description = "Does it work?")
    async def test(self):
        await self.bot.say("It works.")

    @commands.command(brief = "You know the answer.", description = "You already know the answer.")
    async def areyouon(self):
        await self.bot.say("Yes.")

    @commands.command(brief = "Need you even ask?", description = "Why bother asking?")
    async def whatisthepoint(self):
        await self.bot.say("Only a fool would think there is one.")

#    @commands.command(brief = "Further testing", description = "Additional testing command")
#    async def test2(self):
#        self.test()

    @commands.command(brief = "If you are reading this, this test is a failure", description = "You can't see me, can you?", hidden = True)
    async def hiddentest(self):
        await self.bot.say("You've found me!")


def setup(bot):
    bot.add_cog(Testing(bot))
