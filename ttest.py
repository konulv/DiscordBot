from discord.ext.commands import Bot, Cog
from discord.channel import DMChannel
import asyncio
import pickle

TOKEN = ""

with open("tokens.dat", "rb") as file:
    TOKEN = pickle.load(file)["test"]

BOT_PREFIX = ("?", "!")

bot = Bot(command_prefix=BOT_PREFIX)

queue = []
usr = ""
chat = False


@bot.event
async def on_message(message):
    global chat
    global queue
    global usr
    userID = message.author.id
    myID = 234374447413329920 # your ID
    myChannel = 673097522956337152 # channel ID between u and bot

    if message.author.bot:
        return

    if isinstance(message.channel, DMChannel):
        if message.channel not in queue and usr != message.author and userID != myID:
            queue.append(message.channel)

    if chat and userID == myID:
        # a stop point
        if message.content == "!finish":
            try:
                del queue[0]
            except IndexError:
                pass
            usr = ""
            chat = False
            return

        await usr.send(message.content)

    if chat and message.channel == usr:
        channel = bot.get_channel(myChannel)
        await channel.send(message.content)

    try:
        await bot.process_commands(message)
    except AttributeError:
        print("wrong command u bastard")


@bot.command(name="connectMe",
             brief="admin use in helping out ppl through bot")
async def connectme(ctx):
    print("a")
    global chat
    chat = True
    await ctx.send("help me")


@bot.event
async def on_ready():
    global queue
    global usr
    global chat
    print("Logged in as " + bot.user.name)
    while True:
        # checks queue
        if usr == "":
            try:
                usr = queue[0]
            except IndexError:
                pass

        if usr != "":
            #connect the ppl
            pass

        print(chat, usr, queue)
        await asyncio.sleep(5)

bot.run(TOKEN)