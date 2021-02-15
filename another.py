import discord
from discord.ext import commands

app = commands.Bot(command_prefix='!')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await ctx.send('Hello, world')


app.run('ODEwMDA5NjQ3MzI2Mjk4MTMy.YCdaRQ.rLB2Qmq1SlmDmA9K2O6G032gp30')