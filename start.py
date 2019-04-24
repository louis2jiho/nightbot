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
        await client.send_message(channel,"@ncno1434#4788 이랍니다!!" )
    if message.content == '==모두모여':
        await client.send_message(channel, "@everyone")
    if message.content.startswith('==')
        if message.author.server_permissions.administrator or id in owner:
            learn = message.content.split(' ')
            mgs = []
            number = int(learn[1])
            async for x in client.logs_from(message.channel, limit = number+1):
                 mgs.append(x)
            await client.delete_messages(mgs)
            delembed = discord.Embed(title=메세지 삭제됨",color=0x4286f4)
            delmsg = await client.send_message(channel,embed = delembed)
            await asyncio.sleep(5)
            await client.delete_message(delmsg)


access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
