from urllib import request
from json import loads

from discord.ext.commands import Bot, Cog, command


class Info(Cog, description="Display bot information/ info for Minecraft server."):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.ip_json = "https://ipinfo.io/json"
        self.port = 25569

    @property
    def ip_from_json(self):
        with request.urlopen(self.ip_json) as json:
            return loads(json.read().decode())["ip"]

    @command(description="Bot \"about me\"/ description.")
    async def about(self, ctx):
        await ctx.send("This is a place holder.")

    @command(description="Return the Minecraft server IP & port.")
    async def ip(self, ctx):
        await ctx.send(f"__Address__\nip: {self.ip_from_json}\nport: {self.port}\nfull: {self.ip_from_json}:{self.port}")
