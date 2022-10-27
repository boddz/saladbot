from discord import Member
from discord.ext.commands import Cog, Bot, command, check, check_any, is_owner, has_permissions


class Admin(Cog, description="Commands for server Admins."):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    # Command section.

    @command(description="Print out user perms value. Not really just for admins.")
    async def uperms(self, ctx, member: Member):
        await ctx.send(ctx.permissions)

    @has_permissions(kick_members=True, administrator=True)
    @command(description="Well, kick a user of course... provided you have permission.")
    async def kick(self, ctx, member: Member):
        await member.kick()
        await ctx.send(f"**{member}** was kicked.")

    @has_permissions(ban_members=True, administrator=True)
    @command(description="Ban hammer said individual... provided you have permission.")
    async def ban(self, ctx, member: Member):
        await member.ban()
        await ctx.send(f"**{member}** was banned!")
