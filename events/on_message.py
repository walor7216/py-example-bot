import disnake
from disnake.ext import commands
import config

class on_message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == f'<@!{self.client.user.id}>': # sprawdza czy wiadomość to spingowanie bota
            await msg.reply(f'Hej! Mój prefix to `{config.prefix}`', mention_author=False) # odpowiadanie na wiadomość

def setup(client):
   client.add_cog(on_message(client))