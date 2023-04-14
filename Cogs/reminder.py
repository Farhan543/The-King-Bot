import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime,date
import asyncio

class reminder(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client =client

    @app_commands.command(name="reminder",description="Adding a reminder.")
    async def reminder(self,interaction:discord.Interaction,message:str,future_date:str,future_time:str):
        current_time = datetime.now()
        curent_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        date_one = datetime.strptime(curent_time_str,"%Y-%m-%d %H:%M:%S")
        future_rem = future_date + " " + future_time
        date_two = datetime.strptime(future_rem,"%Y-%m-%d %H:%M:%S")
        delta = date_two - date_one
        total_seconds = delta.total_seconds()
        member = interaction.user
        await interaction.channel.send("Reminder has been set")
        channel = self.client.get_channel(int('1095015393137004554'))
        await asyncio.sleep(total_seconds)
        await channel.send(content=f"**{member.mention} Here is your reminder -** {message}")

        
async def setup(client:commands.Bot) -> None:
    await client.add_cog(reminder(client))