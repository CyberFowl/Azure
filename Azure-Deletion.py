import discord
import re
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

        await client.change_presence(activity=discord.Game("Azure is awesome!!"))

    async def on_message(self, message):

        msg = message.content.upper()

#ARCHIVE TRASH CHUTE
    
        if message.channel.id == 781442301867982879:
            print ("trash")
            await message.delete()
        
        if message.author != client.user:

#AUTO-DELETION CHANNELS

    #AUTO LINK DELETION

                
            
            #msg_true = re.search("^HTTPS.*\/$",msg)

            if msg.startswith("HTTP"):
                if message.guild.id != 775901922871214101:
                    if message.channel.id != 784189280187973762 and message.channel.id != 795887721834872852 and message.channel.id != 753861219798089729: 
                        await message.delete()
                        await message.channel.send("No links allowed!") 



    #CULT O COFFEE TRASH CHUTE

            if message.channel.id == 798509966566490131 and message.author.id != 743009565242556526 and message.author.id != 690227486721966130:
                print ("trash")
                await message.delete()

            if message.channel.id == 769568632278614037 and message.author.id == 397646331415494694:
                print ("dad bot trash")
                await message.delete()

print("Code is running")

client = MyClient()
client.run("NzgzNjQ4NDg1MTUyNzg0NDA2.X8dzhg.PpH4az9OSnakulXAB66HxMNWqBk")
