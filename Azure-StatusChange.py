import discord
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

        runloop = True

        while runloop:
            await client.change_presence(status = discord.Status.idle)
            time.sleep(60)
            await client.change_presence(activity = discord.Game(name = "tag"))
            time.sleep(60)
            await client.change_presence(activity = discord.Streaming(name = "GitHub.com/CyberFowl/Azure", url = "https://niny.io/CyberFowlStudiosYT"))
            time.sleep(60)
            await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "the wolves howl"))
            time.sleep(60)
            await client.change_presence(activity = discord.Activity(type = discord.ActivityType.competing, name = "leadership"))
            time.sleep(60)
            await client.change_presence(activity = discord.Activity(type = discord.Activity.watching, name = "the pack"))
            time.sleep(60)

print("Code is running")

client = MyClient()
client.run("NzgzNjQ4NDg1MTUyNzg0NDA2.X8dzhg.PpH4az9OSnakulXAB66HxMNWqBk")
