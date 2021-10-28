import discord
from discord import channel
from discord.ext import commands
import json
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata= json.load(jFile)
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(">>Bot is online<<")
@bot.event
async def on_member_join():
    channel=bot.get_channel(903191490350706698)
    await channel.send('{member} join!')
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')
bot.run(jdata['Token'])

