from discord.ext import commands
import asyncio
import os
from redbot.core import commands
import random
import re
from typing import Match
import discord
from discord import Message


class Mercury(commands.Cog):
    """These support slash command usage!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def support(self, ctx):
        await ctx.send("Need bot support? Message @duckylai on Discord!")

    @commands.hybrid_command()
    async def starlight(self, ctx):
        await ctx.send("https://www.nationstates.net/region=starlight")

    @commands.hybrid_command()
    async def recruitment(self, ctx):
        await ctx.send(f"## How To Recruit: https://www.nationstates.net/page=dispatch/id=2579818\n## Where to Recruit -> https://discord.com/channels/1312834845797515416/1312856185795252295\n### [Starlight Recruitment Template](https://www.nationstates.net/page=dispatch/id=2579819)")

    @commands.hybrid_command()
    async def saymessage(self, ctx, *, message=None):
        embed = discord.Embed(
            title=f"{ctx.author.name} says:",
            description=f"{message}",
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    async def areducksgood(self, ctx):
        await ctx.reply("Yes!!")

    @commands.hybrid_command()
    async def itisso(self, ctx):
        await ctx.reply("<:itisso:1306458895832715294>")

    @commands.hybrid_command()
    async def lessgoo(self, ctx):
        await ctx.reply("<:lessgoo:1306555548833021992>")

    @commands.hybrid_command()
    async def hyper(self, ctx):
        await ctx.reply("<:hyper:1306555558404423721>")

    @commands.hybrid_command()
    async def disgust(self, ctx):
        await ctx.reply("<:disgust:1306555761672982529>")

    @commands.hybrid_command()
    async def choochoo(self, ctx):
        await ctx.reply("<:choochoo:1306555766433382410>")

    @commands.hybrid_command()
    async def hyperwarden(self, ctx):
        await ctx.reply("<:hyperwarden:1306555771898560594>")

    @commands.hybrid_command()
    async def shibaheart(self, ctx):
        await ctx.reply("<:shibaheart:1312859566051954830>")

    @commands.hybrid_command()
    async def poolnoodle(self, ctx):
        await ctx.reply("<:poolnoodle:1323901818589282377>")

    @commands.hybrid_command()
    async def message(self, ctx, user: discord.Member, *, message=None):
        await user.send(
            f"{message}\nSent by {ctx.author.name}, replying will not do anything, this is automated."
        )

    @commands.hybrid_command()
    async def getpoolnoodled(self, ctx, user: discord.Member, *, message=None):
        embed = discord.Embed(
            title=f"{ctx.author.name} pool noodles {user}!",
            description=f"GET POOL NOODLED <:poolnoodle:1323901818589282377> <:poolnoodle:1323901818589282377> <:poolnoodle:1323901818589282377>",
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    async def slowmode(self, ctx, seconds: int):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        channel = message.channel

        author = message.author
        valid_user = isinstance(author, discord.Member) and not author.bot
        if not valid_user:
            return

        if await self.bot.is_automod_immune(message):
            return

        match = re.search(r".*whats a region.*", message.content, re.IGNORECASE)
        if match:
            await channel.send(">:(")

        match = re.search(r".*what’s a region.*", message.content, re.IGNORECASE)
        if match:
            await channel.send(">:(")

        match = re.search(r".*what's a region.*", message.content, re.IGNORECASE)
        if match:
            await channel.send(">:(")

        match = re.search(r".*\.here.*", message.content, re.IGNORECASE)
        if match:
            await channel.send(".kickban")

        match = re.search("nerd", message.content, re.IGNORECASE)
        if match:
            await message.add_reaction("<:poolnoodle:1323901818589282377>")
            await channel.send("not nerd")

        match = re.search("antiweeb", message.content, re.IGNORECASE)
        if match:
            await message.add_reaction("<:poolnoodle:1323901818589282377>")
            await channel.send("weeb")

        match = re.search(r".*pool noodle.*", message.content, re.IGNORECASE)
        if match:
            await message.add_reaction("<:poolnoodle:1323901818589282377>")
            await channel.send("get pool noodled")