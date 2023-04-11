import discord
from discord.ext import commands
from discord import app_commands

class shutdown(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client =client
    
    @app_commands.command(name = "shutdown",description="To shut down the bot.")
    async def shutdown(self,interaction : discord.Interaction):
        await interaction.response.send_message(content="Shutting bot down!")
        await client.close()
        print("Bot successfully shut down")

async def setup(client:commands.Bot) -> None:
    await client.add_cog(shutdown(client))