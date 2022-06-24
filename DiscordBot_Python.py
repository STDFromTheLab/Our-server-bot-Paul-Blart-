import os
import discord


client = discord.Client()
Contents = open("Token.txt", "r")
if Contents.mode == 'r':
    Token = Contents.read()
contents2 = open("Guild.txt", "r")
if contents2.mode == 'r':
    GUILD = contents2.read()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
    channel = client.get_channel(780257119701696552)
    await channel.send(
        "ya boy is back online bitches. all of yall gettin banned now")


@client.event
async def on_message(message):
    print(
        'Message from {0.author} in {0.channel}: {0.content}')
    if message.author == client.user:
        print('Message from Bot detected... skipping response')
    if 'suck' in message.content.lower():
        print('SKILL ISSUE TRIGGERED!')
    channel = client.get_channel(780257119701696552)
    await channel.send(
        'https://tenor.com/view/ez-noob-skill-issue-simply-a-difference-in-skill-gif-20780203'
    )
    return


async def on_message(message):
    if message.content.lower().startswith('$$shutdown'):
        if message.author.id == '414248282873921556':
            print('client shutting down goodnight')
            channel = await client.get_channel(780257119701696552)
            await channel.send('goodnight father :)')
            await client.close()
    else:
        channel = client.get_channel(780257119701696552)
        await channel.send(
            "You're not that guy, you're not that guy pal!"
            "https://tenor.com/view/yellow-sapphire-monkey-drippy-monkey-crypto-gemology-crypto-gemology-yellow-sapphire-yellow-sapphire-gif-24565694"
        )
    return


client.run(Token)
