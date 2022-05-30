from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from server import keep_alive

if os.path.isfile('.env'):
    load_dotenv()

cogs = ['cogs.admin']

client = commands.Bot(command_prefix='>')
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
    keep_alive()
    client.run(os.getenv('TOKEN'))