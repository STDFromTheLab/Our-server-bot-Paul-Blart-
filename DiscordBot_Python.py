
import discord
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
import datetime
from discord.utils import get
import time

Contents = open("Token.txt", "r")
if Contents.mode == 'r':
    Token = Contents.read()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print('Totally not spying on the server ;)'.format(self.user))

    async def on_message(self, message):
        print(
            'Message from {0.author} in {0.channel}: {0.content}'.format(message))
        if message.author == client.user:

            print('Message from Bot detected... skipping response')
            return


client = MyClient()
client.run(Token)
