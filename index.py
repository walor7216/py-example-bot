import disnake
from disnake.ext import commands 
import os
import config

intents = disnake.Intents().all() # deklarowanie intentów
client = commands.Bot(command_prefix = commands.when_mentioned_or(config.prefix), intents=intents) # 

client.remove_command('help') # usuwa defaultową komendę help

for file in os.listdir('./commands'):
    if file.endswith('.py'):
        client.load_extension(f'commands.{file[:-3]}')
for file in os.listdir('./events'):
    if file.endswith('.py'):
        client.load_extension(f'events.{file[:-3]}')
for file in os.listdir('./slash-commands'):
    if file.endswith('.py'):
        client.load_extension(f'slash-commands.{file[:-3]}')


client.run(config.token) # włączanie bota
