
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")




@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content == '!커맨드':
        await client.send_message(channel, '커맨드')
    if message.content == '!커맨드2':
        await client.send_message(channel, '커맨드2')

access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
