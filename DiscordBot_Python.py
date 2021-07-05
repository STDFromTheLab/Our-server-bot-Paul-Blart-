import random
import asyncio
import aiohttp
import discord
import json
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
import datetime
from discord.utils import get
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print ('Totally not spying on the server ;)'.format(self.user))
    async def on_message(self, message):
        print('Message from {0.author} in {0.channel}: {0.content}'.format(message))
        if message.author == client.user:
        
            print('Message from Bot detected... skipping respond')
            return
        if message.content.startswith('beaner gang'):           
            await message.channel.send('beaner gang is ass')
        
        
Token = open("Token.txt", "r")
if Token.mode == 'r':
    contents = Token.read()
client = MyClient()
client.run(contents)