from urllib import request
from json import loads
from os import path, uname
from typing import Optional, Any

from discord.ext.commands import Bot, Cog, command


class Info(Cog, description="Display bot information/ info for Minecraft server."):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    _IP_JSON = "https://ipinfo.io/json"
    _PORT = 25569
    _GITHUB = "https://github.com/sa-lad/saladbot"

    @property
    def _ip_from_json(self) -> str:
        """ Get IP addr from ipinfo.io and return fromatted json data. """
        with request.urlopen(self._IP_JSON) as json:
            return loads(json.read().decode())["ip"]

    @property
    def _read_description(self) -> None | str:
        """ Read description file to make code a bit cleaner. """
        filepath = "./assets/description.txt"
        if path.exists(filepath) is False:  # Description file not present -> None.
            return None
        with open(filepath, "r") as fileobj:
            return fileobj.read()

    # Commands section.

    @command(description="Github repository for the bot.")
    async def github(self, ctx):
        await ctx.send(f"__Github__\nCheck out the project: {self._GITHUB}")

    @command(description="Bot \"about me\"/ description.")
    async def about(self, ctx):
        await ctx.send(f"{self._read_description}")

    @command(description="Return the Minecraft server IP & port.")
    async def ip(self, ctx):
        await ctx.send(f"__Address__\nIP: {self._ip_from_json}\nPort: {self._PORT}\nFull: {self._ip_from_json}:{self._PORT}")

    @command(description="Display host/ server information.")
    async def os(self, ctx):
        await ctx.send(f"__Host Information__\nOS Name: {uname().sysname}\nKernal: {uname().release}\nVersion: {uname().version}")
