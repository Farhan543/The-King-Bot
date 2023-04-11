import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import openai
import os
load_dotenv()
openai.api_key=os.getenv('OPENAI_KEY')

class chat(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client =client
    

    @app_commands.command(name="chat",description="Gives the user's info.")
    async def chat(self,interaction: discord.Interaction,prompt:str):
        response = openai.Completion.create(
            model ="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=1000
        )
        response_dict = response.get("choices")
        if response_dict and len(response_dict) > 0:
            query_response = response_dict[0]["text"]
        await interaction.channel.send(query_response)

async def setup(client:commands.Bot) -> None:
    await client.add_cog(chat(client))    


