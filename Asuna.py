#Adit is a bitch

import discord, random, asyncio
from discord.ext import commands

with open('authcode.txt') as f:
    AUTH_TOKEN = f.readline()

intents = discord.Intents.all()

asuna = commands.Bot(command_prefix='asuna ',intents=intents)


#asuna Commands
@asuna.command()
async def hello(ctx):
    await ctx.send('Hello!')

# @asuna.command()
# async def rps(ctx):
#     embed = discord.Embed(
#         title = "Rock Paper Scissors",
#         description = "Pick Rock, Paper, or Scissors"
        
#     )
#     embed.add_field(name = 'Rock', value = '✊', inline= True)
#     embed.add_field(name = 'Paper', value = '🖐️', inline= True)
#     embed.add_field(name = 'Scissors', value = '✌️', inline= True)
    
#     await ctx.send(embed=embed)



# @asuna.command()
# async def rps123(ctx):
#     rps = ['rock', 'paper', 'scissors']
#     cpu_pick = rps[random.randint(0,2)]
#     await ctx.send('**Playing Against Asuna** \nPick Rock, Paper or Scissors')
#     @asuna.event
#     async def on_message(message):
#         if message.content.lower() == 'rock' and cpu_pick == 'paper' or message.content.lower() == 'paper' and cpu_pick == 'scissors' or message.content.lower() == 'scissors' and cpu_pick == 'rock':
#             await ctx.send(f'Asuna Picked {cpu_pick}')
#             await ctx.send('You Lose!')
            
#         elif message.content.lower() == 'paper' and cpu_pick == 'rock' or message.content.lower() == 'scissors' and cpu_pick == 'paper' or message.content.lower() == 'rock' and cpu_pick == 'scissors':
#             await ctx.send(f'Asuna Picked {cpu_pick}')
#             await ctx.send('You Won!')
#         elif message.content.lower() == cpu_pick:
#             await ctx.send(f'Asuna Picked {cpu_pick}')
#             await ctx.send("It's a Draw!")
#    



@asuna.command()
async def roll(ctx, num:int):
    roll = random.randint(1, num)
    embed = discord.Embed(
        title = (f'Roll: {roll}'),
        description = (f'Rolled a {num} sided die'),
        color = 15277667
    )
    await ctx.send(embed = embed)

@asuna.event
async def on_message(message):
    if message.content.startswith('asuna rps'):
        channel = message.channel
        await channel.send('**Playing Against Asuna** \nPick Rock, Paper or Scissors')
        rps = ['rock', 'paper', 'scissors']
        cpu_pick = rps[random.randint(0,2)]
        def check(m):
            return m.content.lower() == 'rock' or m.content.lower() == 'paper' or m.content.lower() == 'scissors'
        
        msg = await asuna.wait_for('message', check=check)

@asuna.event
async def on_message(message):
    msg = message.content.lower()
    ctx = await asuna.get_context(message)
    if message.author.id == 1025559734134263880:
        return
    elif msg == 'asuna roll':
        await roll(ctx, 6)

    else:  
        await asuna.process_commands(message)\

@asuna.event
async def on_ready():
    print('We have logged on as {0.user}'.format(asuna))


asuna.run(AUTH_TOKEN)
