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

    if message.content == '안녕하세요':
        await client.send_message(channel, '안녕하세요 !명령어 한번씩 쳐주세요')
    if message.content == '!명령어':
        await client.send_message(channel,'!blacklist, !clean, !clear, !disconnect, !id, !joinserver, !listids, !np, !pause, !perms, !play, !pldump, !queue, !restart, !resume, !save, !search, !setavatar, !setname, !setnick, !shuffle, !shutdown, !skip, !stream, !summon, !volume, !제작자')
    if message.content == '!제작자':
        await client.send_message(channel, '안녕하세요! Jiho Night 입니다')

        

access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
