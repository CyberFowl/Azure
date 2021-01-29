import discord
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

        runloop = True

        while runloop:
            await client.change_presence(activity=discord.Game("Azure is awesome!!"))
            time.sleep(30)
            await client.change_presence(activity=discord.Game("XD"))
            time.sleep(30)

print("Code is running")

client = MyClient()
client.run("BOT_TOKEN_HERE")
