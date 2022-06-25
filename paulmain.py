
import asyncio

import os
import random
from typing_extensions import Self

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = '780251364735057990'
Client = discord.Client()
Funny_Text1 = 'Deez nuts HAHAHAHAHAHA!'
Funny_Text_List = [
    'Deez nuts HAHAHAHAHAHA!',
    '911 was an inside job lol',
    'It takes three wipes to realize you needed two',
    'Sleepy joe sniffer 3000',
    'Gay wanna be',
    'I love going online spreading miss information',
    "Don't look up Dr Fauci's financial ties",
    'Bill Clinton is a rapist',
    "Epstein didn't kill himself",
    "I sure hope the FBI isn't watching this server",
    "I'm not to fond of" ' "The Blacks"',
    "I'm very horny right now, I'm out here stroking my shit right now."
]
#Random_Index = random.randrange(len(Funny_Text_List))

Main = Client.get_channel('780257119701696552')
for guild in Client.guilds:
    if guild.name == GUILD:
        break


@Client.event
async def on_ready():
    for guild in Client.guilds:
        if guild.name == GUILD:
            break
    await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name='We do not racism', url='https://www.twitch.tv/std_monsterman'))

    print(f'{Client.user} is online!'
          f' and is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
          )
    Members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {Members}')


@Client.event
async def on_message(Message):
    print('Message from {0.author}: {0.content}'.format(Message))

    if Message.content.startswith('$$paul'):
        await Message.channel.send(random.choice(Funny_Text_List))
    if Message.content.startswith('$$pfp'):
        await Message.channel.send('https://cdn.discordapp.com/attachments/780257119701696552/988573337217290310/unknown.png')
   # if Message.content.upper().startswith('$$BAN'):
       # if "988577231485947994" in [role.id for role in Message.author.roles]:
       #  async def ban (ctx, member:discord.User=None, reason =None):
       #   if member == None or member == ctx.message.author:
       #    await ctx.channel.send("You cannot ban yourself")
        return
       #    if reason == None:
       #     reason = "For being a jerk!"
       #     message = f"You have been banned from {ctx.guild.name} for {reason}"
       #     await member.send(message)
    # await ctx.guild.ban(member, reason=reason)
       #     await ctx.channel.send(f"{member} is banned!")


Client.run(TOKEN, bot=True)
