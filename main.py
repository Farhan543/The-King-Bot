import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import time
import platform
from datetime import datetime
from dotenv import load_dotenv
import openai
import os
client = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@client.event
async def on_ready():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    prfx = (Back.BLACK + Fore.GREEN + current_time + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prfx + " Logged in as " + Fore.YELLOW + client.user.name)
    print(prfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
    print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
    print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
    synced= await client.tree.sync()
    print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)))

load_dotenv()
openai.api_key=os.getenv('OPENAI_KEY')
discord_token=os.getenv("DISCORD_TOKEN")

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model ="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=1000
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        query_response = response_dict[0]["text"]
    return query_response

@client.tree.command(name="chat",description="For chatting with ChatGPT.")
async def chat(interaction: discord.Interaction, args:str):
    bot_response=chatgpt_response(prompt=args)
    await interaction.channel.send(bot_response)


@client.tree.command(name = "shutdown",description="To shut down the bot.")
async def shutdown(interaction : discord.Interaction):
    await interaction.response.send_message(content="Shutting bot down!")
    await client.close()
    print("Bot successfully shut down")

@client.tree.command(name="userinfo",description="Gives the user's info.")
async def userinfo(interaction: discord.Interaction,member:discord.Member=None):
    if(member == None):
        member = interaction.user
    roles = [role for role in member.roles]
    embed = discord.Embed(title="User Info",description=f"Here is the user info of {member.mention}",color=discord.Color.green(),timestamp=datetime.utcnow())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID",value= member.id)
    embed.add_field(name="Name",value=f"{member.name}#{member.discriminator}")
    embed.add_field(name="Nickname",value=member.display_name)
    embed.add_field(name="Status",value=member.status)
    embed.add_field(name="Created at",value=member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p "))
    embed.add_field(name="Joined at",value=member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p "))
    embed.add_field(name=f"Roles ({len(roles)})",value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role",value=member.top_role.mention)
    await interaction.response.send_message(embed=embed) #Use Emphermal = True to mae it visble to you only

@client.tree.command(name="serverinfo",description="Gives server info in an embed.")
async def serverinfo(interaction: discord.Interaction):
    embed = discord.Embed(title = "Server Info",description = f"Here is the server info of {interaction.guild.name}", color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.set_thumbnail(url=interaction.guild.icon)
    embed.add_field(name="Members",value=interaction.guild.member_count)
    embed.add_field(name="Channels",value=f"{len(interaction.guild.text_channels)} text | {len(interaction.guild.voice_channels)} voice")
    embed.add_field(name="Server Owner",value=interaction.guild.owner.mention)
    embed.add_field(name="Description",value=interaction.guild.description)
    embed.add_field(name="Created at",value=interaction.guild.created_at.strftime("%a, %B %#d, %Y, %I:%M %p "))
    await interaction.response.send_message(embed=embed) #only one interaction.response.send_message per command but you can use interact.channel.send also

client.run(discord_token)