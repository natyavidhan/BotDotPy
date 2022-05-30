import discord
from discord.ext import commands
import os

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.logs_channel = discord.utils.get(self.client.get_all_channels(), id=int(os.getenv('LOGS_CHANNEL_ID')))

    async def send_log(self, message:dict, ctx):
        embed = discord.Embed(
            title=message['title'],
            description=message['description'],
            color=0x516151
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        await self.logs_channel.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await self.send_log({
            'title': 'Kicked',
            'description': f'{member.mention} was kicked by {ctx.author.mention} for `{reason}`'
        }, ctx)
        await ctx.send(f'{member} was kicked for `{reason}` :skull:')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await self.send_log({
            'title': 'Banned',
            'description': f'{member.mention} was banned by {ctx.author.mention} for `{reason}`'
        }, ctx)
        await ctx.send(f'{member} was banned for `{reason}` :skull:')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        await ctx.guild.unban(discord.Object(id=member))
        await self.send_log({
            'title': 'Unbanned',
            'description': f'{member} was unbanned by {ctx.author.mention}'
        }, ctx)
        await ctx.send(f'{member} was unbanned')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(role, reason=reason)
        await self.send_log({
            'title': 'Muted',
            'description': f'{member.mention} was muted by {ctx.author.mention} for `{reason}`'
        }, ctx)
        await ctx.send(f'{member} was muted for `{reason}` :skull:')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role, reason=None)
        await self.send_log({
            'title': 'Unmuted',
            'description': f'{member.mention} was unmuted by {ctx.author.mention}'
        }, ctx)
        await ctx.send(f'{member} was unmuted')

def setup(bot):
    bot.add_cog(Admin(bot))