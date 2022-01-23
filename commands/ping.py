import disnake
from disnake.ext import commands
import config

class ping(commands.Cog):

    def __init__(self, client):
       self.client = client

    @commands.command()
    async def ping(self, ctx):
         await ctx.reply(f'Pong! **{round(self.client.latency * 1000)}** ms', mention_author=False) # odpowiadanie na wiadomość

def setup(client):
   client.add_cog(ping(client))