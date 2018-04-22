import discord
from discord.ext import commands
import random
import time
import asyncio

class Jokes:
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
    async def biden(self):
        await self.bot.say(self.getBiden())

    @commands.command(brief = "A torture device", description="Tells the Monk Joke, in a new and improved form")
    async def monk(self):
        '''
        joke = open('MonkJokeUltimate', 'r')
        for line in joke:
            print(line)
            self.bot.say(line)
            time.sleep(10)
        joke.close()
        '''


def setup(bot):
    bot.add_cog(Jokes(bot))
