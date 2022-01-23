import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
import config

class pings(commands.Cog):

    def __init__(self, client):
       self.client = client

    @commands.slash_command(name='ping', description='Pokazuje ping bota.')
    async def ping(self, inter:ApplicationCommandInteraction):
       await inter.send(f'Pong! **{round(self.client.latency * 1000)}** ms') # wysyłanie wiadomości

def setup(client):
   client.add_cog(pings(client))