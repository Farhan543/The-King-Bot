import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class serverinfo(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client =client

    @app_commands.command(name="serverinfo",description="Gives server info in an embed.")
    async def serverinfo(self,interaction: discord.Interaction):
        embed = discord.Embed(title = "Server Info",description = f"Here is the server info of {interaction.guild.name}", color=discord.Color.blue(),timestamp=datetime.utcnow())
        embed.set_thumbnail(url=interaction.guild.icon)
        embed.add_field(name="Members",value=interaction.guild.member_count)
        embed.add_field(name="Channels",value=f"{len(interaction.guild.text_channels)} text | {len(interaction.guild.voice_channels)} voice")
        embed.add_field(name="Server Owner",value=interaction.guild.owner.mention)
        embed.add_field(name="Description",value=interaction.guild.description)
        embed.add_field(name="Created at",value=interaction.guild.created_at.strftime("%a, %B %#d, %Y, %I:%M %p "))
        await interaction.response.send_message(embed=embed) #only one interaction.response.send_message per command but you can use interact.channel.send also

async def setup(client:commands.Bot) -> None:
    await client.add_cog(serverinfo(client))