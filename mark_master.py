
from utils import *
import discord
from discord import ChannelType
from tokens import *

games = [
    "Xonotic",
    "Master Chief",
    "El Dorito",
    "Minecraft Hunger Games",
    "TF2",
    "Skribblio",
]
from random import choice
import pickle

class Mark:

    def __init__(self, TOKEN, bind_channel=None):
        client = commands.Bot(command_prefix=".")
        client.bind_channel = bind_channel
        self.loop = False

        @client.command(pass_context=True)
        async def join(ctx):
            print("Joining...")
            channel = ctx.message.author.voice.channel
            voice = get(client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                try:
                    await channel.connect()
                except Exception as e:
                    print(e)
                    await channel.disconnect()
                    await channel.connect

        @client.command(pass_context=True)
        async def leave(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)
            await voice.disconnect()

        @client.command(pass_context=True)
        async def stop(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)
            voice.stop()

        @client.command(pass_context=True)
        async def resume(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)
            voice.resume()

        @client.command(pass_context=True)
        async def pause(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)
            voice.pause()

        @client.command(pass_content=True)
        async def spam(ctx, member):
            member = int(member.replace('<', "").replace('>', "").replace('@', "").replace('!',""))

            if member == 284378594963357696:
                member = ctx.message.author
                rand_cont = 'fuck YOU!'
            else:
                member = client.get_user(member)
                rand_cont = random.choice(ha)
            print(member)
            dm_channel = await member.create_dm()
            await dm_channel.send(rand_cont)

        @client.command(pass_content=True)
        async def game(ctx):
            channel = ctx.message.channel
            if re.search('list', ctx.message.content, re.IGNORECASE):
                for game in games:
                    await channel.send(game)
            else:
                await channel.send("You WILL play " + choice(games))

        @client.command(pass_content=True)
        async def bind(ctx):
            #global bind_channel
            client.bind_channel = ctx.message.author.voice
            print(f'Bound to: {client.bind_channel}')

        async def play(scr, channel, ctx):

            if scr != None:
                try:
                    voice = await channel.connect()
                except:
                    voice = get(client.voice_clients, guild=ctx.guild)
                    voice.stop()

                url = await get_url(scr)

                def repeat(scr):
                    print('Replaing')
                    #voice.play(scr, after=lambda e: repeat(scr))
                    #voice.is_playing()

                if url == None:
                    channel = ctx.message.channel
                    await channel.send('I am being fucking SEXED so I can\'t play fnaf right now')
                else:
                    scr = discord.FFmpegPCMAudio(url)
                    print(scr)

                    try:
                        if channel and not voice.is_playing():
                            voice.play(scr)#, after=lambda e: repeat(scr))
                            voice.is_playing()
                    except Exception as e:
                        print(e)
                        await channel.connect()



        @client.command(pass_context=True)
        async def loop(ctx):
            print('Looping')
            self.loop = not self.loop


        @client.command(pass_context=True)
        async def p(ctx, *, word):
            message = ctx.message
            if client.bind_channel != None:
                channel = client.get_channel(client.bind_channel)
            else:
                try:
                    channel = message.author.voice.channel
                except:
                    channel = get_max_channel(message.guild)

            voice = get(client.voice_clients, guild=ctx.guild)

            if voice != None:
                if channel != voice.channel:
                    await voice.disconnect()
            link = getSearch(word)
            await play(link, channel, ctx)

        @client.command(pass_context=True)
        async def check_perm(ctx, guild_id: int):
            if ctx.message.channel.type == ChannelType.private:
                guild = await client.fetch_guild(guild_id)
                channels = guild.channels
                user_id = ctx.message.author.id
                user = guild.get_member(user_id)

                dm = ctx.message.channel

                all_access = True
                for channel in channels:
                    perm = user.permissions_in(channel)
                    if perm.view_channel != True:
                        all_access = False
                        await dm.send("You are not able to view " + str(channel.name) + ": " + str(channel.type))
                        #if channel.type == ChannelType.text:
                        #    messages = await channel.history(limit=1000).flatten()
                        #    for message in messages:
                        #        await dm.send(message.author.name + message.content)


                if all_access:
                    await dm.send("You have access to all channels")

        @client.event
        async def on_message(message, *args):

            await client.process_commands(message)
            # ctx = await client.get_context(message)
            # print(ctx.guild)
            # voice = get(client.voice_clients, guild=ctx.guild)
            #
            #
            # if client.bind_channel != None:
            #     channel = client.get_channel(client.bind_channel)
            # else:
            #     try:
            #         channel = message.author.voice.channel
            #     except:
            #         channel = get_max_channel(message.guild)
            #
            # if voice != None:
            #     if channel != voice.channel:
            #         await voice.disconnect()
            #
            # content = str(message.content)
            # print(content)
            # if re.search('kyle', content, re.IGNORECASE):
            #     print("Sending kyle pic...")
            #     dm = await message.author.create_dm()
            #     await dm.send(random.choice(kyle_links))
            #
            # url = get_fnaf_link(content)
            # voice = await play(url, channel, ctx)
            # # await queue_songs(url, voice)
            # print(url)

        @client.event
        async def on_ready():
            print("cummy FUCK")

        self.client_start = client.start(TOKEN)



mark =[]

#for token in TOKENS:
#    mark.append(Mark(token).client_start)
#mark.append(Mark(luke_token).client_start)

mark.append(Mark(TOKENS[4]).client_start)

loop = asyncio.get_event_loop()

loop.run_until_complete( asyncio.wait(mark) )
