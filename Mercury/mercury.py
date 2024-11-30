import discord
from discord.ext import commands
import asyncio
import os
from redbot.core import commands


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
        await ctx.send(f"## How To Recruit: https://www.nationstates.net/page=dispatch/id=2579818\n## Where to Recruit -> https://discord.com/channels/1299450621044330616/1306695718869930054")

    @commands.hybrid_command()
    async def say(self, ctx, *, message=None):
        embed = discord.Embed(
            title=f"{ctx.author.name} says:",
            description=f"{message}",
        )
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    async def addrecruiter(self, ctx, user: discord.Member, role: discord.Role):
        if ctx.message.author.id == 691583562608148501 or ctx.author.guild_permissions.manage_roles:
            if role.id == 1301383500678692935:
                await user.add_roles(role)
                await ctx.reply(f"Successfully added the Recruiter role")
            else:
                await ctx.reply(f"hey you dont have permission to add this role >:(")
        else:
            await ctx.reply(f"hey you dont have permission to use this command >:(")

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
    async def message(self, ctx, user: discord.Member, *, message=None):
        await user.send(
            f"{message}\nSent by {ctx.author.name}, replying will not do anything, this is automated."
        )


    @commands.hybrid_command()
    async def slowmode(self, ctx, seconds: int):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")