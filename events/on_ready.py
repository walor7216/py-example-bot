import disnake
from disnake.ext import commands
import config

class on_ready(commands.Cog):

   def __init__(self, client):
       self.client = client

   @commands.Cog.listener()
   async def on_ready(self):
        print('Jestem gotowy!') # wysyła log o włączeniu bota
        await self.client.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name='poleceń')) # zmienianie aktywności bota

def setup(client):
   client.add_cog(on_ready(client))