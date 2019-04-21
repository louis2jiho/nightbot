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
    if message.content == '==명령어':
        await client.send_message(channel,'==제작자')
    if message.content == '==제작자':
        await client.send_message(channel, '안녕하세요! Jiho Night 입니다')
        if message.content.startswith("==모두모여"):
        await client.send_message(message.channel, "@everyone")

    if message.content.startswith("==들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client== None:
            await client.send_message(message.channel, '들어왔습니다') # 호오.... 나를 부르는건가? 네녀석.. 각오는 되있겠지?
            await client.join_voice_channel(channel)
        else:
            await client.send_message(message.channel, '봇이 이미 들어와있습니다.') # 응 이미 들어와있어 응쓰게싸




    if message.content.startswith("==나가"):
            server = message.server
            voice_client = client.voice_client_in(server)
            print("나가")
            print(voice_client)
            print("나가")
            if voice_client == None:
                await client.send_message(message.channel,'봇이 음성채널에 접속하지 않았습니다.') # 원래나가있었음 바보녀석 니녀석의 죄는 "어리석음" 이라는 .것.이.다.
                pass
            else:
                await client.send_message(message.channel, '나갑니다') # 나가드림
                await voice_client.disconnect()


    if message.content.startswith("==재생"):

        server = message.server
        voice_client = client.voice_client_in(server)
        msg1 = message.content.split(" ")
        url = msg1[1]
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player.is_playing())
        players[server.id] = player
        await client.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
        print(player.is_playing())
        player.start()




    if message.content.startswith("==일시정지"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="장비를 정비합니다"))
        players[id].pause()

    if message.content.startswith("==다시재생"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="다시재생한다!!!!"))
        players[id].resume()

    if message.content.startswith("==멈춰"):
        id = message.server.id
        await client.send_message(message.channel, embed=discord.Embed(description="세계의 시간은 멈춰있다..."))
        players[id].stop()
        print(players[id].is_playing())

    if message.content.startswith('==예약'):
        msg1 = message.content.split(" ")
        url = msg1[1]
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player)

        if server.id in queues:
            queues[server.id].append(player)
            print('if 1 '+str(queues[server.id])) #queues배열 확인
        else:
            queues[server.id] = [player] #딕셔너리 쌍 추가
            print('else 1' + str(queues[server.id]))#queues배열 확인
        await client.send_message(message.channel,'예약 완료\n')
        musiclist.append(url) #대기목록 링크


    if message.content.startswith('==대기목록'):

        server = message.server
        msg1 = message.content.split(" ")
        mList = msg1[1]
        num = 0
        bSize = len(musiclist)

        if mList =='보기':
            embed = discord.Embed(
                title='대기중인 곡 들',
                description='대기중.....',
                colour=discord.Colour.blue()
            )
            for i in musiclist:
                print('예약리스트 : ' + i)
                embed.add_field(name='대기중인 곡', value=i, inline=False)
            await client.send_message(message.channel, embed=embed)

        if mList =='취소':
            while num<bSize:
                del musiclist[0]
                num = num+1

            del queues[server.id]
            await client.send_message(message.channel,'예약중인 음악 모두 취소 완료')

        #if message.content.startswith('!'):






        

access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
