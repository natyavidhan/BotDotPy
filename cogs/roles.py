import discord
from discord.ext import commands
import os
import json

class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.roles = json.load(open('roles.json'))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == int(os.getenv('ROLES_MESSAGE_ID')):
            guild = self.client.get_guild(payload.guild_id)
            for role in self.roles:
                if payload.emoji.name == role['emoji']:
                    member = payload.member
                    await member.add_roles(discord.utils.get(guild.roles, id=role['role']))
                    break

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == int(os.getenv('ROLES_MESSAGE_ID')):
            guild = self.client.get_guild(payload.guild_id)
            for role in self.roles:
                if payload.emoji.name == role['emoji']:
                    member = await guild.fetch_member(payload.user_id)
                    await member.remove_roles(discord.utils.get(guild.roles, id=role['role']))
                    break
        
def setup(bot):
    bot.add_cog(Roles(bot))