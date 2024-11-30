from .mercury import Mercury


async def setup(bot):
    await bot.add_cog(Mercury(bot))