import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("--------")

@bot.command()
async def help(ctx):
    await ctx.send('Available commands: !help, !status, !roll')

@bot.command()
async def status(ctx):
    await ctx.send('Bot is running!')

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

bot.run('NzM4MTk4OTA3NDYwNTE3ODk4.XyIbTg.k1s6Cm42Ss4OklnJLhXDNnFaftQ')
