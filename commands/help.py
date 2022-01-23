import disnake
from disnake.ext import commands

class help(commands.Cog):

   def __init__(self, client):
       self.client = client

   @commands.command()
   async def help(self, ctx):
       embed = disnake.Embed(color=0x00D2FF) # tworzenie embeda
       embed.add_field(name='Komendy', value='`help` - pokazuje tą wiadomość \n `ping` - pokazuje ping bota') # dodawanie embed fielda
       await ctx.reply(embed=embed, mention_author=False) # odpowiadanie embedem na wiadomość

def setup(client):
   client.add_cog(help(client))