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
	    await client.send_message(channel, '안녕하세요 ==명령어 한번씩 쳐주세요')
    if message.content == '안녕':
	    await client.send_message(channel, '안녕하세요 ==명령어 한번씩 쳐주세요')
    if message.content == 'ㅎㅇ':
	    await client.send_message(channel, '안녕하세요 ==명령어 한번씩 쳐주세요')
    if message.content == 'ㅎㅇ요':
	    await client.send_message(channel, '안녕하세요 ==명령어 한번씩 쳐주세요')
    if message.content == '하이요':
	    await client.send_message(channel, '안녕하세요 ==명령어 한번씩 쳐주세요')
    if message.content == '하이':
	    await client.send_message(channel, '안녕하세요 ==명령어 한번씩 쳐주세요')

    if message.content == '==명령어':
	    await client.send_message(channel,'==제작자 , ==모두모여')
    if message.content == '==제작자':
	    await client.send_message(channel, '안녕하세요! Jiho Night(@ncno1434#4788) 입니다')
    if message.content == '==모두모여':
	    await client.send_message(channel, "@everyone")



access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
