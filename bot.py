import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1403526849371574452

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    print("-R- is ready!")

    await channel.send(f"Hello! -R- is here!")

bot.run(TOKEN)