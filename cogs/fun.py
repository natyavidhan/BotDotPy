import discord
from discord.ext import commands
import random
import requests
import re

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title=f':ping_pong: Pong! ({round(self.client.latency * 1000)} ms)', colour=0x00ff00)
        await ctx.send(embed=embed)

    @commands.command()
    async def emojify(self, ctx, *, text):
        emoji_string = ""
        for char in text:
            if re.match(r'[a-zA-Z]', char):
                emoji = f":regional_indicator_{char.lower()}:"
                emoji_string += emoji
            else:
                emoji_string += char
        await ctx.send(emoji_string)

def setup(client):
    client.add_cog(Fun(client))