# url https://discordapp.com/oauth2/authorize?client_id=506514227276808192&scope=bot
# discord documentation https://tinyurl.com/y9nuae8t

import pickle
import asyncio
import requests


from discord import Embed

from datetime import datetime
from discord import Game
from discord.ext.commands import Bot, Cog

TOKEN = ""
with open("tokens.dat", "rb") as file:
    TOKEN = pickle.load(file)["main"]

BOT_PREFIX = ("?", "!")
spamBool = True

bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(name="whereYaGoing")
async def emoji1(ctx):
    img = Embed().set_image(url="http://i.imgur.com/fVDH5bN.gif")
    await ctx.send(embed=img)  #


@bot.command(name="niggaWhat")
async def emoji2(ctx):
    img = Embed().set_image(url="https://i.imgur.com/22sgHi6.gif")
    await ctx.send(embed=img)


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
    await ctx.send("spamming been stopped" if not (get_spam_status()) else "spam continues")


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
        if time.second % 5 == 0:
            await ctx.send("@Konulv#5775")
        await asyncio.sleep(1)


@bot.event
async def on_ready():
    game = Game("Type !help for cmds")
    await bot.change_presence(activity=game)
    print("Logged in as " + bot.user.name)

bot.load_extension("general")

bot.run(TOKEN)
