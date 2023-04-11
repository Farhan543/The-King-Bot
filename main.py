import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import platform
from datetime import datetime
from dotenv import load_dotenv
import os
import openai

load_dotenv()
discord_token=os.getenv("DISCORD_TOKEN")

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'),intents=discord.Intents.all())
        self.coglist = ["Cogs.userinfo","Cogs.serverinfo","Cogs.shutdown","Cogs.chat","Cogs.reminder"]

    async def setup_hook(self):
        for ext in self.coglist:
            await self.load_extension(ext)
            
    async def on_ready(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        prfx = (Back.BLACK + Fore.GREEN + current_time + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + client.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        synced= await client.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)))

client = Client()
client.run(discord_token)