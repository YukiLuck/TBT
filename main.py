from discord.ext.commands import Bot
from mongoengine import connect
from dotenv import load_dotenv
from os import environ

extensions = {
    'commands': ['info']
}

if __name__ == '__main__': 
    load_dotenv()
    bot = Bot(environ['DEFAULT_PREFIX'], None)
    connect(host=environ['MONGO_URI'])
    for key, value in extensions.items():
        for ext in value:
            try:
                bot.load_extension(f'tbt.cogs.{key}.{ext}')
                print(f'Loaded extension {ext}.')
            except Exception as exception:
                print(f'Failed to load extension {ext}: {exception}')
    bot.run(environ['TOKEN'])
