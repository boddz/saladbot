#!/usr/bin/env python

from discord import Intents, Status, ActivityType, Activity
from discord.ext.commands import Bot, Cog

from cogs import Info


class BundleBot(Bot):
    def __str__(self) -> None:
        return f"Bot description: {self.description}"

    @staticmethod
    def parse_bot_token(filepath: str) -> str:
        """ Possibly will be removed or moved in future. """
        with open(filepath, "r") as token:
            return token.read().strip()

    async def parse_cogs(self, *cogs: Cog) -> None:
        """
        Parse cog/cogs and add to bot.
        
        Args
        ----
        *cogs: The cog class to add to bot
        """
        for i in range(len(cogs)):
            await self.add_cog(cogs[i](bot))
        
    async def on_ready(self) -> None:
        """ This funtion is called by `Bot` upon ready. """ 
        await self.change_presence(status=Status.online, activity=Activity(type=ActivityType.watching, name=f"{len(self.guilds)} guilds..."))
        await self.parse_cogs(Info)
        print(f"{self.user}: {self.status}")

        
if __name__ == "__main__":
    bot = BundleBot(command_prefix="%", description="A bot for Sadlad's server.", intents=Intents.all())
    bot.run(bot.parse_bot_token("./token.txt"))
