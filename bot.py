import discord
import asyncio 
from time import gmtime, strftime
from db import DB

with open('../counter_token.txt', 'r') as discord_file:
    DISCORD_TOKEN = discord_file.read().split(";")[0]
    print(DISCORD_TOKEN, end=';\n')

prefix = ";"
client = discord.Client()
color = discord.Color(15452014)
db = None

@client.event
@asyncio.coroutine
def on_ready():
    global db
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------\n')
    yield from client.send_message(client.get_channel("315552571823489024"), "Connected at " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    db = DB(client.user.id)

@client.event
@asyncio.coroutine
def on_message(message):
    db.save(message)
    if not message.content.startswith(prefix):
        return
    command = message.content[1:].strip().split(" ")
    args = command[1:]
    command = command[0]
    if command is "count":
        regex = " ".join(args[:-1 or None])
        user = ""
        if len(args) > 1:
            if args[-1] is "me":
                user = message.author.id
            else:
                user = "".join(re.findall(r'\d+', args[-1])
        num = db.count(regex, user)
        if user = "":
            user = "anyone"
        else:
            user = get_user_info(user).display_name
        em = discord.Embed(title="Number of Times " + user.title() + " Has Said " + regex, color=color)
        em.add_field(name="Total Count", value="**" + str(num) + "**")
        yield from client.send_message(message.channel, embed=em)

@client.event
@asyncio.coroutine
def on_message_edit(before, after):
    db.save(after, str(before.id))

