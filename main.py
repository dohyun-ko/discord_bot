import discord
import asyncio
from discord.ext import commands, tasks

# client = discord.Client()
bot = commands.Bot(command_prefix='')


@bot.event
async def on_ready():
    print("login")
    print("----------------")


'''@bot.event
async def on_message(message):
    if message.author.bot:
        return None

    print(message.author, message.content'''


@bot.command()
async def 들어와(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def 나가(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    await vc.disconnect()
#    if message.content.startswith('!hi'):
#       await message.channel.send('hello')


bot.run('ODEwMDA5NjQ3MzI2Mjk4MTMy.YCdaRQ.rLB2Qmq1SlmDmA9K2O6G032gp30')


