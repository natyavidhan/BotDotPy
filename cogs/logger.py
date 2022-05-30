import discord
from discord.ext import commands
import os

class Logger(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.logs_channel = discord.utils.get(self.client.get_all_channels(), id=int(os.getenv('LOGS_CHANNEL_ID')))

    async def send_log(self, message:dict, ctx, fields:list=None):
        embed = discord.Embed(
            title=message['title'],
            description=message['description'],
            color=0x516151
        )
        if fields:
            for field in fields:
                embed.add_field(name=field['name'], value=field['value'])
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        await self.logs_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.send_log({
            'title': 'Joined',
            'description': f'{member} joined the server'
        }, member)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.send_log({
            'title': 'Left',
            'description': f'{member} left the server'
        }, member)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.nick != after.nick:
            await self.send_log({
                'title': 'Nickname Changed',
                'description': f'{before} changed their nickname'
            }, before,
            [
                {
                    'name': 'Before',
                    'value': before.nick
                },
                {
                    'name': 'After',
                    'value': after.nick
                }
            ])

        elif before.roles != after.roles:
            await self.send_log({
                'title': 'Role Changed',
                'description': f'{before} changed their role'
            }, before,
            [
                {
                    'name': 'Before',
                    'value': ', '.join([role.mention for role in before.roles])
                },
                {
                    'name': 'After',
                    'value': ', '.join([role.mention for role in after.roles])
                }
            ])
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await self.send_log({
            'title': 'Message Deleted',
            'description': f'{message.author} deleted a message'
        }, message, [
            {
                'name': 'Message',
                'value': message.content
            }
        ])

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content != after.content:
            await self.send_log({
                'title': 'Message Edited',
                'description': f'{before.author} edited a message'
            }, before, [
                {
                    'name': 'Before',
                    'value': before.content
                },
                {
                    'name': 'After',
                    'value': after.content
                }
            ])

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        await self.send_log({
            'title': 'Channel Created',
            'description': f'{channel.guild} created a channel'
        }, channel, [
            {
                'name': 'Channel',
                'value': channel.mention
            }
        ])

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        await self.send_log({
            'title': 'Channel Deleted',
            'description': f'{channel.guild} deleted a channel'
        }, channel, [
            {
                'name': 'Channel',
                'value': channel.mention
            }
        ])

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if before.name != after.name:
            await self.send_log({
                'title': 'Channel Name Changed',
                'description': f'{before.guild} changed a channel\'s name'
            }, before, [
                {
                    'name': 'Before',
                    'value': before.name
                },
                {
                    'name': 'After',
                    'value': after.name
                }
            ])

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        await self.send_log({
            'title': 'Role Created',
            'description': f'{role.guild} created a role'
        }, role, [
            {
                'name': 'Role',
                'value': role.mention
            }
        ])

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        await self.send_log({
            'title': 'Role Deleted',
            'description': f'{role.guild} deleted a role'
        }, role, [
            {
                'name': 'Role',
                'value': role.mention
            }
        ])

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        if before.name != after.name:
            await self.send_log({
                'title': 'Role Name Changed',
                'description': f'{before.guild} changed a role\'s name'
            }, before, [
                {
                    'name': 'Before',
                    'value': before.name
                },
                {
                    'name': 'After',
                    'value': after.name
                }
            ])
    



def setup(bot):
    bot.add_cog(Logger(bot))