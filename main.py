from discord.ext.commands import Bot
from dotenv import load_dotenv
from os import environ

if __name__ == '__main__': 
    load_dotenv()
    bot = Bot(environ['DEFAULT_PREFIX'], None)
    bot.run(environ['TOKEN'])
