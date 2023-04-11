import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class userinfo(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client =client

    @app_commands.command(name="userinfo",description="Gives the user's info.")
    async def userinfo(self,interaction: discord.Interaction,member:discord.Member=None):
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
        await interaction.response.send_message(embed=embed) #Use Emphermal = True to make it visble to you only

async def setup(client:commands.Bot) -> None:
    await client.add_cog(userinfo(client))