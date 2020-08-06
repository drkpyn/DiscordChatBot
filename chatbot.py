# get required dependencies
import os
import psycopg2
import discord
from discord.ext import commands
import random

# set up connection to local Postgres instance
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# create new bot
bot = commands.Bot(command_prefix='!')

# begin defining commands
@bot.command()
async def status(ctx):
    await ctx.send('Bot is running!')
    
@bot.command()
async def rps(ctx, choice: str):
    if choice == 'rock':
        botchoice = 'paper'
    elif choice == 'paper':
        botchoice = 'scissors'
    elif choice == 'scissors':
        botchoice = 'rock'
    else:
        await ctx.send('Please only choose rock, paper, or scissors')
        return
    await ctx.send('Your choice: {}'.format(choice))
    await ctx.send('Bot\'s choice: {}'.format(botchoice))
    await ctx.send('YOU LOSE!')

@bot.command()
async def roll(ctx, input: str, mod: int = 0):
    try:
        rolls, limit = map(int, input.split('d'))
    except Exception:
        await ctx.send('Format is NdN (+/-)N!')
        return

    results = []
    total = 0

    for i in range(rolls):
        roll = random.randint(1,limit)
        results.append(roll)

    for x in results:
        total += x

    await ctx.send('Rolling {}d{}+{}'.format(rolls, limit, mod))
    await ctx.send('Rolls: {}'.format(results))
    await ctx.send('Total: {}'.format(total + mod))

@bot.command()
async def dm(ctx, subCommand: str, subArgument: str):
    if (subCommand == 'new'):
        try:
            tempname = subArgument + 'CharDict'
            globals()[tempname] = sampleCharDict
            await ctx.send(print(tempname))
        except Exception:
            await ctx.send('An error occured')
            return

# start the bot and connect to Discord
TOKEN = os.environ['DISCORD_TOKEN']
bot.run(TOKEN)
