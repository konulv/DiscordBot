from discord.ext.commands import Cog, command, Bot
import random

class General(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="8ball",
                 description="idk",
                 brief="random insults and stuff",
                 aliases=["eight_ball", "eightball"])
    async def eight_ball(self, ctx):
        possible_response = [
            "ya're a prick",
            "i like trains",
            "fly you fools",
            "Boi",
            "Ah, the sound of the majestic space duck...",
            "try me bitch",
            "free real estate",
            "english motherfucker, do you speak it?",
            "muffin button",
            "say what again",
            "If your DNA was off by one percentage point, you'd be a dolphin",
            "Hey dragon, wake the fuck up! It's already past noon! Get your shit together!"
        ]
        await ctx.send(random.choice(possible_response))

    @command(name="annoyDev",
                     aliases=["annoydev"])
    async def annoy_dev(self, ctx):
        myid = "<@234374447413329920>"
        await ctx.send("\*poke* " + myid)


    @command()
    async def hello(self, ctx):
        possible_response = "hi"
        await ctx.send(possible_response + ", " + ctx.message.author.mention)


def setup(bot):
    bot.add_cog(General(bot))

