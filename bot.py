import discord
from discord.ext import commands
import os
import aiohttp

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

API_URL = "https://abuelabed.mh4d.eu.org/api/joke"

@bot.event
async def on_ready():
    print(f"✅ Marhabeh anne {bot.user}!")

@bot.command(name="joke")
async def abu_el_abed_joke(ctx):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(API_URL) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    joke = data.get("joke", "😅 Couldn't find a joke!")
                    await ctx.send(f"🤣 {joke}")
                else:
                    await ctx.send("😵‍💫 The joke machine is down. Try again later.")
        except Exception as e:
            await ctx.send("❌ Error fetching the joke.")
            print("Error:", e)

bot.run(os.getenv("DISCORD_TOKEN"))
