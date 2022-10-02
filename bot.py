import discord
import logging
import json

#JSON HANDLING
config = open("config.json")
data = json.load(config)

#LOGGING
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents)
client.run(data["TOKEN"], log_handler=handler)
