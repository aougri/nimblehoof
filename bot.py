import discord
import logging
import os

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message.content = True

client = Bot(intents=intents)
client.run(os.environ['TOKEN'], log_handler=handler)
