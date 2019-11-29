import discord
from discord.ext import commands
import random
import time
import asyncio

class Jokes(commands.Cog):
    """Jokes and memes"""
    def __init__(self, bot):
        self.bot = bot

    def getBiden(self):
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
        f.close()

    @commands.command(brief = "Send random Joe Biden meme", description = "Sends a link to a random Joe Biden meme")
    async def biden(self, ctx):
        #await self.bot.say(self.getBiden())
        await ctx.send("Mr. Biden is too busy campaigning to provide memes at this time.  Please try again later.")

    @commands.command(brief = "Submit link to Joe Biden meme", description = "Submit a link to a Joe Biden meme for the rotation")
    async def votebiden(self, ctx, data):
        f = open('bidenmemes_submissions', 'a')
        f.write('{0}\n'.format(data))
        f.close()
        await ctx.send("Thank you for your submission")
        


    @commands.command(brief = "A torture device", description="Tells the Monk Joke, in a new and improved form")
    async def monk(self, ctx):
        '''
        joke = open('MonkJokeUltimate', 'r')
        for line in joke:
            print(line)
            self.bot.say(line)
            time.sleep(10)
        joke.close()
        '''
        await ctx.send("You have been spared fromm The Monk Joke.  This time.")
