from os import environ
from typing import Optional
from ..database import Guild
from discord import Guild as DiscordGuild

DEFAULT_PREFIX = environ['DEFAULT_PREFIX']

def get_prefix(guild: Optional[DiscordGuild]):
    if guild and (db_guild := Guild.objects(id=guild.id).first()):
        return db_guild.prefix or DEFAULT_PREFIX
    return DEFAULT_PREFIX