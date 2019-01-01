# url https://discordapp.com/oauth2/authorize?client_id=519864297656942602&scope=bot
# pip3 install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice] for discord.py update
# discord documentation https://tinyurl.com/y969aalx

import pickle
import asyncio
from discord import Game
from discord import Embed
from discord.ext.commands import Bot
from datetime import datetime

TOKEN = ""
with open("tokens.dat", "rb") as file:
    TOKEN = pickle.load(file)["test"]


BOT_PREFIX = ("?", ".")
spamBool = True

bot = Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_message(msg):
    userID = msg.author.id
    myID = 234374447413329920
    ctx = await bot.get_context(msg)
    try:
        if ctx.command.instance is None:
            if msg.author.bot:
                return
            elif userID == myID:
                await bot.process_commands(msg)
            else:
                img = Embed().set_image(url="http://i.imgur.com/fVDH5bN.gif")
                await ctx.send(embed=img)
    except AttributeError:
        pass


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
        if (time.second % 30 == 0):
            await ctx.send("30s has passed")
        await asyncio.sleep(1)

@bot.command(name="ping",
             brief="random command",
             description="ya wot mate?")
async def ping(ctx):
    await ctx.send(bot.latency)



@bot.command(name="annoyDev",
             aliases=["annoydev"])
async def annoy_dev(ctx):
    myid = "<@234374447413329920>"
    await ctx.send("\*poke* " + myid)


@bot.command()
async def hello(ctx):
    possible_response = "hello"
    await ctx.send(possible_response + ", " + ctx.message.author.mention)


@bot.event
async def on_ready():
    game = Game("type .help for cmds")
    await bot.change_presence(activity=game)
    print("Logged in as " + bot.user.name)


bot.run(TOKEN)
