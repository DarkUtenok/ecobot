from aiohttp import ClientConnectionError
import discord 
from credits import TOKEN
from discord.ext import commands
from random import choice


bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    
@bot.command()
async def fact(ctx):
    with open("Memobotik\\memasiki\\ecobot\\facts.txt", "r", encoding="utf-8") as f:
        facts = f.read().split("***")
    await ctx.send(choice(facts))
    print (1)


bot.run(TOKEN)
