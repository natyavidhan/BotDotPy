from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

if os.path.isfile('.env'):
    load_dotenv()

cogs = ['cogs.admin', 'cogs.roles', 'cogs.logger', 'cogs.error_handler']

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

if __name__ == '__main__':
    client.run(os.getenv('TOKEN'))