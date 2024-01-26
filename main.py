import discord
from discord.ext import commands
import dotenv, os

dotenv.load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot("!", intents=discord.Intents.all())

@bot.tree.command(name="5000yen")
async def yen_generater(interaction: discord.Interaction, top: str, bottom: str):
    await interaction.response.send_message(f"https://gsapi.cbrx.io/image?top={top}&bottom={bottom}", ephemeral=True)

@bot.event
async def on_ready():
    await bot.tree.sync()

bot.run(token=token)