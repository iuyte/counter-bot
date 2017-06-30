import discord
import asyncio 
import re
from time import gmtime, strftime
from db import DB

with open('../counter_token.txt', 'r') as discord_file:
    DISCORD_TOKEN = discord_file.read().split(";")[0]
    print(DISCORD_TOKEN, end=';\n')

prefix = ";"
client = discord.Client()
color = discord.Color(3312582)
db = DB("328899063892148224", "db/messages.p", prefix)

@client.event
@asyncio.coroutine
def on_ready():
    global db
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------\n')
    yield from client.send_message(client.get_channel("315552571823489024"), "Connected at " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    db.load()

@client.event
@asyncio.coroutine
def on_message(message):
    db.save(message)
    if not message.content.startswith(prefix):
        return
    command = message.content[1:].strip().split(" ")
    args = command[1:]
    command = command[0]
    if command.startswith("count"):
        regex = ""
        user = ""
        if len(args) > 1 and (len(message.mentions) is not 0 or args[-1].startswith("me")):
            regex = " ".join(args[:-1]).strip()
            if args[-1].strip().lower().startswith("me"):
                user = message.author.id
            else:
                user = message.mentions[0].id#"".join(re.findall(r'\d+', args[-1]))
        else:
            regex = regex = " ".join(args).strip()
        num = db.count(regex, user)
        if user is "":
            user = "anyone"
        elif args[-1] is "me":
            user = message.author.name
        else:
            user = message.mentions[0].name
        em = discord.Embed(title="Number of Times " + user.title() + " Has Said " + regex, description=str(num), color=color)
        yield from client.send_message(message.channel, embed=em)

@client.event
@asyncio.coroutine
def on_message_edit(before, after):
    db.save(after, str(before.id))

client.run(DISCORD_TOKEN)
