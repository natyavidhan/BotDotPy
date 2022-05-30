import discord
from discord.ext import commands
import os

class ErrHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if ctx.command is not None:
            if ctx.command.has_error_handler():
                return

        if isinstance(error,commands.errors.MissingRequiredArgument):
            missing_argument_embed = discord.Embed(title='Error', colour=0xff0000)
            missing_argument_embed.description="Missing arguments"
            await ctx.send(embed = missing_argument_embed)

        elif isinstance(error,commands.errors.MissingPermissions):
            missing_permissions_embed = discord.Embed(title='Error', colour=0xff0000)
            missing_permissions_embed.description="You do not have permission to use that command"
            await ctx.send(embed=missing_permissions_embed)

        elif isinstance(error,commands.errors.NoPrivateMessage):
            no_dm_embed = discord.Embed(title='Error', colour=0xff0000)
            no_dm_embed.description="Enter a proper argument"
            await ctx.send(embed=no_dm_embed)

        elif isinstance(error,commands.errors.BadArgument):
            bad_argument_embed = discord.Embed(title='Error', colour=0xff0000)
            bad_argument_embed.description="Enter a proper argument"
            await ctx.send(embed=bad_argument_embed)

        
        elif isinstance(error,commands.errors.MissingRole):
            missing_role_embed = discord.Embed(title='Error', colour=0xff0000)
            missing_role_embed.description="You do not have permission to use that command"
            await ctx.send(embed=missing_role_embed)

        elif isinstance(error,commands.errors.CommandNotFound):
            pass
        
        elif isinstance(error,commands.errors.NotOwner):
            missing_role_embed = discord.Embed(title='Error', colour=0xff0000)
            missing_role_embed.description="Don't be too smart \nDevs Are smarter than you"
            await ctx.send(embed=missing_role_embed)

        elif isinstance(error,commands.errors.BotMissingPermissions):
            missing_permissions_embed = discord.Embed(title='Error', colour=0xff0000)
            missing_permissions_embed.description="I do not have permission to use that command"
            await ctx.send(embed=missing_permissions_embed)

        elif isinstance(error,commands.errors.CommandOnCooldown):
            cooldown_embed = discord.Embed(title='Error', colour=0xff0000)
            cooldown_embed.description="You are on cooldown"
            await ctx.send(embed=cooldown_embed)

        else:
            await ctx.send(f'An error has occured: {error}')

def setup(bot):
    bot.add_cog(ErrHandler(bot))