import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
import config

class helps(commands.Cog):

   def __init__(self, client):
       self.client = client

   @commands.slash_command(name='help', description='Pokazuje listę komend')
   async def help(self, inter: ApplicationCommandInteraction):
       embed = disnake.Embed(color=0x00D2FF) # tworzenie embeda
       embed.add_field(name='Komendy', value='`help` - pokazuje tą wiadomość \n `ping` - pokazuje ping bota') # dodawanie embed fielda
       await inter.send(embed=embed) # wysyłanie embeda


def setup(client):
   client.add_cog(helps(client))