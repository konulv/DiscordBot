# url https://discordapp.com/oauth2/authorize?client_id=506514227276808192&scope=bot
# discord documentation https://tinyurl.com/y9nuae8t

import pickle
import asyncio
import random
import requests

from datetime import datetime
from discord import Game
from discord.ext.commands import Bot


TOKEN = ""
with open("tokens.dat", "rb") as file:
    TOKEN = pickle.load(file)["main"]

BOT_PREFIX = ("?", "!")
spamBool = True

bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(name="8ball",
                description="idk",
                brief="random insults and stuff",
                aliases=["eight_ball", "eightball"])
async def eight_ball(ctx):
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
        "If your DNA was off by one percentage point you'd be a dolphin"
    ]
    await ctx.send(random.choice(possible_response))


@bot.command(name="annoyDev",
                aliases=["annoydev"])
async def annoy_dev(ctx):
    myid = "<@234374447413329920>"
    await ctx.send("\*poke* " + myid)


@bot.command(pass_context=True)
async def hello(ctx):
    possible_response = "hi"
    await ctx.send(possible_response + ", " + ctx.message.author.mention)


@bot.command()
async def bitcoin(ctx):
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    value = response.json()["bpi"]["USD"]["rate"]
    await ctx.send("Bitcoin price is: $" + value)


@bot.command(name="spam",
             brief="sets status for spamming",
             description='do "True" if ya want to spam, "False" otherwise.')
async def spam(ctx):
    content = ctx.message.content[6:].lower()
    boolean = content == "true"
    set_spam_status(boolean)
    await ctx.send("spamming been stopped" if not(get_spam_status()) else "spam continues")


def get_spam_status():
    return spamBool


def set_spam_status(boolean):
    global spamBool
    spamBool = boolean


@bot.command(name="spamChat",
             brief="rn just spams chat every 30s",
             description="proof of concept, completely useless currently")
async def spam_chat(ctx):
    while get_spam_status():
        time = datetime.today()
        if time.second % 30 == 0:
            await ctx.send("30s has passed")
        await asyncio.sleep(1)


@bot.event
async def on_ready():
    game = Game("Type !help for cmds")
    await bot.change_presence(activity=game)
    print("Logged in as " + bot.user.name)


bot.run(TOKEN)
