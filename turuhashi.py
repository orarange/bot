import os
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import requests
from pprint import pprint
import aiohttp 
import random 

intent=discord.Intents.all()

bot=commands.Bot(command_prefix='!',case_insensitive=True,intents=intent)

bot.author_id=757106917947605034

@bot.event
async def on_ready():
  print('on')

bot.load_extension('jishaku')

bot.load_extension("turuhashicogs.weakup")

bot.run('ODcwMTI0NTQxMjcwMTcxNzgw.YQIMoA._6BZr1uWoWWAvF6j7JKWBxKu3TU')