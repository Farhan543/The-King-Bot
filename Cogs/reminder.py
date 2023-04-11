import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime,date
import asyncio

class reminder(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client =client

    @app_commands.command(name="reminder",description="Adding a reminder.")
    async def reminder(self,interaction:discord.Interaction,message:str,day:int,month:int,year:int,hour:int,minute:int,second:int):

        current_date = date.today()
        today_date = date(current_date.year,current_date.month,current_date.day)
        reminder_date = date(year,month,day)
        total_days = (reminder_date - current_date).days
        seconds = (hour * 60 * 60) + (minute * 60) +second
        total_seconds = (total_days * 24 * 60 * 60) + seconds
        await interaction.channel.send("Reminder has been set")
        channel = self.client.get_channel(int('1095015393137004554'))
        await asyncio.sleep(total_seconds)
        await channel.send(content=f"{message}")
async def setup(client:commands.Bot) -> None:
    await client.add_cog(reminder(client))