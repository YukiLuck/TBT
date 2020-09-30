from discord.ext.commands import Cog, Context, command

class Info(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command()
    async def help(self, ctx: Context):
        await ctx.send("This is a help command!")

def setup(bot):
    bot.add_cog(Info(bot))