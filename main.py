from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

if os.path.isfile('.env'):
    load_dotenv()

cogs = ['cogs.admin', 'cogs.roles', 'cogs.logger', 'cogs.error_handler', 'cogs.fun']

client = commands.Bot(command_prefix=os.getenv('PREFIX'), guild_subscriptions=True)
client.load_extension('jishaku')
for cog in cogs:
    client.load_extension(cog)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_connect():
    activity = discord.Activity(name=os.getenv('ACTIVITY'), type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)

if __name__ == '__main__':
    client.run(os.getenv('TOKEN'))