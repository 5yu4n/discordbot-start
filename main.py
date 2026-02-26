import discord
from discord.ext import commands

intents=discord.Intents.default()
bot=commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="cat",description="say meow!")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message("meow!")

bot.run("yourbottoken")
