import discord
from discord.ext import commands
from characterRecord import *

class Sheets:
    """Commands related to character sheets"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Create new sheet", description = "Create an empty character sheet")
    async def newsheet(self, name):
        sheet = CreateSheet()
        sheet.new_sheet(name)
        await self.bot.say("`Created new charcter sheet with name {0}`".format(name))

    @commands.command(brief = "Add to sheet", description = "Add line of data to charcter sheet")
    async def addto(self, name, data):
        sheet = WriteToSheet()
        sheet.add_line(name, data)
        if(sheet.add_line(name, data)):
            await self.bot.say("`Added line \"{0}\" to {1}`".format(data, name))
        else:
            await self.bot.say("`Didn't add line to sheet`")

    @commands.command(brief = "Print entire sheet", description = "Print entire character sheet")
    async def showsheet(self, name):
        sheet = ReadFromSheet()
        await self.bot.say("```{0}```".format(sheet.read_sheet(name)))

    @commands.command(brief = "Read specific line", description = "Print specific data line from charcter sheet")
    async def showline(self, name, data):
        sheet = ReadFromSheet()
        await self.bot.say("```{0}```".format(sheet.read_sheet_data(name, data)))

def setup(bot):
    bot.add_cog(Sheets(bot))
