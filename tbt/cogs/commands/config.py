from discord.ext.commands import Bot, Cog, Context, command, guild_only
from ...database import Guild

class Config(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command()
    async def prefix(self, ctx: Context, *, new_prefix):
        if len(new_prefix) > 10:
            return await ctx.send('The prefix can\'t be longer than 10 characters!')
        Guild(id=ctx.guild.id, prefix=new_prefix).save()
        await ctx.send('Your prefix has been successfully changed to ' + new_prefix)

    async def cog_check(self, ctx):
        return await guild_only().predicate(ctx)

def setup(bot):
    bot.add_cog(Config(bot))