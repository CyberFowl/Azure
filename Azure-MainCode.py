import discord
import random
import sys
from time import time, ctime, sleep

msgNo = 0
t = time()

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is online!")

#        These are just statuses that you can play around with:        
        
#        await client.change_presence(status = discord.Status.idle)
#        await client.change_presence(activity=discord.Game(name="tag with the wolves"))
#        await client.change_presence(activity=discord.Streaming(name="for the wolves", url="https://twitch.tv/cyberfowl"))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the wolves howl"))
#        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="leadership"))
#        await client.change_presence(activity=discord.Activity.watching, name="the pack")

    async def on_member_join(member):
        await client.send_message(member,"Welcome!")

    async def on_message(self, message):

        global recall, msgNo, link, phrase, space, time

        mcu = message.content.upper()
        justmc = message.content
       
#NITRO EMOJI VARIABLES
    #RTX
        dragontears = client.get_emoji(795731101083500564)
        drafonexcite = client.get_emoji(795724032510394389)
        dragonbigsmile = client.get_emoji(795731340439191655)
        dragonblush = client.get_emoji(795731217877565491)
        dragonchoco = client.get_emoji(795433637511561247)
        dragoncool = client.get_emoji(795731424204030002)
        dragoncringe = client.get_emoji(795731369748594750)
        dragoncry = client.get_emoji(795724064567853079)
        dragonhappy = client.get_emoji(795433742734590012)
        dragonheadband = client.get_emoji(795731397628657714)
        dragonheart = client.get_emoji(795723974701088839)
        dragonhearteyes = client.get_emoji(795731172595990538)
        dragonlove = client.get_emoji(795723937081589840)
        dragonmlem = client.get_emoji(795731308831440916)
        dragonnoop = client.get_emoji(795731139087826964)
        dragonsad = client.get_emoji(795731059211632660)
        dragonsmirk = client.get_emoji(795433540380262440)
        dragonsurprised = client.get_emoji(795731256352309259)

#POLLS 
        if message.guild.id == 775901922871214101:
            if mcu.startswith("Z!POLL"):
                print("POLL - CHOCO SERVER")
                op1 = justmc.split(":")[-2]
                op2 = justmc.split(":")[-1]
                embed = discord.Embed(title = "Poll by " + str(message.author), color = 0xff0033)
                embed.add_field(name = op1, value = "Option 1 :one:", inline = False)
                embed.add_field(name = op2, value = "Option 2 :two:", inline = False)
                embed.add_field(name = "Note:", value = "For now, this command only supports only two polls." + "\n" + "Syntax: <z!poll :option 1:option 2>")
                embed.set_footer(text = "Made and owned by CyberFowl#8931")
                channel = client.get_channel(776217580595445770)
                await channel.send("Poll:", embed = embed)
            
        if message.guild.id == 769557583429369867:
            if mcu.startswith("Z!POLL"):
                print("POLL - COFFEE SERVER")
                op1 = justmc.split(":")[-2]
                op2 = justmc.split(":")[-1]
                embed = discord.Embed(title = "Poll by " + str(message.author), color = 0xff0033)
                embed.add_field(name = op1, value = "Option 1 :one:", inline = False)
                embed.add_field(name = op2, value = "Option 2 :two:", inline = False)
                embed.add_field(name = "Note:", value = "For now, this command only supports only two options." + "\n" + "Syntax: <z!poll :option 1:option 2>")
                embed.set_footer(text = "Made and owned by CyberFowl#8931")
                channel = client.get_channel(774983135606734888)
                await channel.send("Poll:", embed = embed)

#IN      

        if message.author != client.user:
            
            if "doggo" in mcu:
                print("Message received")
                await message.channel.send(":heart_eyes:")
                
#STARTS WITH

            if mcu.startswith("YAY"):
                await message.channel.send(":tada:")
            if mcu.startswith("YEY"):
                await message.channel.send(":tada:")
            if mcu.startswith("Z!AA"):
                await message.channel.send("https://tenor.com/view/angry-anger-pixar-inside-out-aaah-gif-5628546")
            if message.author.id != 743009565242556526:
                if mcu.startswith("KILL") and "@" in mcu:
                    print("NO HITMAN STRIKE")
                    await message.channel.send("Sorry, only <@!743009565242556526> can order hitman strikes")

            if message.author.id == 743009565242556526:
                if mcu.startswith("Z!KILL"):
                    killed = mcu.split(" ")[-1]
                    print("KILLED USER")
                    await message.channel.send("Shot " + killed + "\n" + "https://tenor.com/view/shoot-gift-gif-13384546")
#VARIABLES/LISTS
            ball_response = ["As I see it, yes", "Yes", "No", "Very likely", "Very unlikely", "Not even close", "Maybe", "Ask again later", "Better not tell you now", "Don't count on it", "It is certain"]
            lucky_phrase = random.randint(0,len(ball_response)-1)

            space = " "

#EVERYBODY
            if mcu.startswith("Z!8BALL"):
                print("8ball")
                await message.channel.send(ball_response[lucky_phrase])
            
            if mcu == "Z!COINFLIP":
                coinflip = random.choice(["Heads", "Tails"])
                print(coinflip)
                await message.channel.send(coinflip)
            
            if mcu == "Z!DICE":
                dice = random.choice(["1","2","3","4","5","6"])
                print("Roll a die")
                await message.channel.send(dice)

            if mcu == "Z!BEGIN":
                await message.channel.send("Azure was last restarted at " + str(ctime(t)) + " IST")
                await message.channel.send(f"Also, the ping is ***{round(client.latency * 1000)}ms***")

            if mcu == "F FOR RESPECT":
                print("F FOR RESPECT")
                sleep(2)
                await message.channel.send("F")

            if mcu == "BRUH":
                print("BRUH MOMENT")
                await message.channel.send("*(Bruh moment)*")

            if mcu.startswith("Z!HBD"):
                bday = mcu.split(" ")[-1]
                print("Message received")
                await message.channel.send(":tada: :tada: Happy birthday" + bday + "!!!! :tada: :tada:" + "\n" + "https://tenor.com/bdecb.gif")

            if mcu.startswith("Z!HUG"):
                hug = mcu.split(" ")[-1]
                print("hug")
                await message.channel.send("You hug " + hug + "\n" + "https://tenor.com/view/dog-hug-bff-best-friend-friend-gif-9512793")

            if mcu == 'Z!PING':
                print('Z!ping') 
                await message.channel.send(f":ping_pong: Pong! | Message took ***{round(client.latency * 1000)}ms*** to respond")

            if mcu.startswith("Z!PURGE"):
                purge = mcu.split(" ")[-1]
                await message.channel.purge(limit = int((purge)) + 1)

            if mcu == "Z!SPOTIFY" and message.author.id != 743009565242556526:
                embed=discord.Embed(title="Spotify: Liked songs", url="https://open.spotify.com/collection/tracks")
                await message.channel.send(embed=embed)

            if mcu == "Z!INVITE":
                embed=discord.Embed(title="Invite the bot", description="Ivite the bot here^", url="https://discord.com/api/oauth2/authorize?client_id=783648485152784406&permissions=518208&scope=bot")
                await message.channel.send(embed=embed)


#P!OWNER
                
    #ATLANTIS
            if mcu == "P!OWNER" and message.guild.id == 788293597379166228:
                print ("ping saanvi")
                for i in range(1,6):
                    await message.channel.send("<@!727964715216797697>")
                    sleep(2)

    #CULT O COFFEE
            if mcu == "P!OWNER" and message.guild.id == 769557583429369867:
                print ("ping ree the des")
                for i in range(1,6):
                    await message.channel.send("<@!690227486721966130>")
                    sleep(2)

    #CHOCOLATE CULT
            if mcu == "P!OWNER" and message.guild.id == 775901922871214101:
                print ("ping anna")
                for i in range(1,6):
                    await message.channel.send("<@!760603081573400576>")
                    sleep(2)

    #TECH TERRAIN
            if mcu == "P!OWNER" and message.guild.id == 746952048053977148:
                print ("ping rammy")
                for i in range(1,6):
                    await message.channel.send("<@!737661910194847836>")
                    sleep(2)

#CYBERFOWL

            if message.author.id == 743009565242556526 or message.author.id == 690227486721966130:

        #REMEMBERING STUFF

                if mcu.startswith("<@!783648485152784406>") and "LINK" in mcu:
                    print("REMEMBER LINK")
                    link = justmc.split(" ")[-1]
                    await message.channel.send("Added link")
                    await message.channel.send("<:drafonexcite:795724032510394389>")

                if mcu.startswith("<@!783648485152784406>") and "PHRASE" in mcu:
                    print("REMEMBER PHRASE")
                    phrase = justmc.split(" ")[2:]
                    await message.channel.send("Added phrase")
                    await message.channel.send("<:drafonexcite:795724032510394389>")

                if mcu == "<@!783648485152784406> DL":
                    print("DISPLAY LINK")
                    await message.channel.send("Here it is: ")
                    await message.channel.send(link)
                    await message.channel.send("<:drafonexcite:795724032510394389>")
                   
                if mcu == "<@!783648485152784406> DP":
                    print("DISPLAY PHRASE")
                    await message.channel.send("Here it is: ")
                    phrase = space.join(phrase)
                    await message.channel.send(phrase)
                    await message.channel.send("<:drafonexcite:795724032510394389>")

        #NORMAL COMMANDS

                if mcu.startswith("GN"):
                    print("GOOD NIGHT")
                    await message.channel.send("Good Night!!")

                if mcu == "Z!Gah":
                    await message.channel.send()

                if mcu.startswith("Z!YEET"):
                    print("YEETED SOMEBODY")
                    await message.channel.send("YEETED" + "\n" + "https://tenor.com/view/yeet-lion-king-simba-rafiki-throw-gif-16194362")

                if mcu.startswith("Z!PINGY"):
                    ping = justmc.split(" ")[-1]
                    print("PING " + ping)
                    for i in range(1,6):
                        await message.channel.send(ping)
                        sleep(2)

                if mcu == "Z!SPOTIFY":
                    print("spotify link - boss")
                    embed=discord.Embed(title="Spotify: Liked Songs.", url="https://open.spotify.com/collection/tracks")
                    await message.channel.send(embed=embed)
                    await message.channel.send("Here you go boss!")
                    
                if mcu == "HELP":
                    print("Message received")
                    await message.channel.send("¯\_(ツ)_/¯ What do you want help with? ||(Keeping in mind that I can't help a lot anyway)||")
                if mcu == "HMM CAN YOU MAKE ME A COFFEE?":
                    print("Message received")
                    await message.channel.send("Sorry, I'm not *that* advanced... Maybe ask me in, what? 5 years? Hopefully I can do it then... Hopefully...")

#REEEEE THE DESTROYER

            if message.author.id == 690227486721966130:

                if mcu == "HELP":
                    print("Message received")
                    await message.channel.send("¯\_(ツ)_/¯ What do you want help with? ||(Keeping in mind that I can't help a lot anyway)||")
                if "COFFEE" in mcu:
                    print("Message received")
                    await message.channel.send("Sorry, I don't make coffee lol")

#REEEEBEKA_
            
            if message.author.id == 762793879522639904:

                if mcu == "G!HELP":
                    for i in range(1,11):
                        await message.channel.send("<@!743009565242556526>")
                        sleep(2)

#MEMBER COUNT - CYBERFOWL ONLY

            if message.author.id == 743009565242556526:

                if mcu.startswith("Z!") and "MEMBERS" in mcu:
                    print("MEMBER COUNT")
                    memberCount == mcu.split(" ")[1]
                    await message.channel.send(":tada: :tada: YAY!!! " + memberCount  + " MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")

#EMOJIS
            if mcu== "Z!<@!783648485152784406>":
                print("Azure avatar")
                await message.channel.send("<:Azure:800679821013024769>")

            if mcu == ":SPOOKEDHAMSTER:" or mcu == ":SPOOKED HAMSTER:":
                print(":spookedhamster:")
                await message.channel.send("<:Hamster_spooked:793356985609093150>")

            if mcu == "Z!NITRO FLEX" and message.author.id == 743009565242556526:
                print("NITRO FLEX")
                await message.channel.send("<:CFLogo:800679960532615179>")
                sleep(1)
                await message.channel.send("<:NightHawk:800679902923456553>")
                sleep(1)
                await message.channel.send("<:Griffin2k20:800679874309390346>")
                sleep(1)
                await message.channel.send("<:Azure:800679821013024769>")
                
            if mcu.startswith("Z!DISTRACT"):
                print("Distraction dance")
                for i in range(1,6):
                    await message.channel.send("<a:AmongDistracted:803394547203309619> " * 5)
                    sleep(2)

#EDITS - STILL EXPERIMENTING
            if mcu == "Z!EDIT":
                edit = await message.channel.send("This")
                sleep(2)
                await edit.edit(content = "This is")
                sleep(2)
                await edit.edit(content = "This is a")
                sleep(2)
                await edit.edit(content = "This is a long")
                sleep(2)
                await edit.edit(content = "This is a long message.")
                sleep(2)

#REACTIONS
            if mcu == "OH K":
                print("OH K")
                thonkingbutcool = client.get_emoji(793356545127612456)
                await message.add_reaction(thonkingbutcool)

#ROLE STUFF (IN PROGRESS)
            if message.guild.id == 769557583429369867:
                role = discord.Object(777211683315253288)
                if mcu == "Z!ADD REBEL":
                    print("REBEL ALERT!!")
                    await message.author.add_roles(role)
                    await message.channel.send("You are a rebel now :cry: Well, that's unfortunate...")
                if mcu == "Z!REMOVE REBEL":
                    print("Back from the dark side!!")
                    await message.author.remove_roles(role)
                    await message.channel.send("Yay!! You are not a rebel anymore!!")

#EMBEDIFY
            if mcu.startswith("Z!EMBED"):
                print("Message recieved")
                content = justmc.split(" ")[1:]
                space = " "
                string = space.join(content)
                embed = discord.Embed(title = string, color = 0xff0033)
                embed.set_footer(text = "Made and owned by CyberFowl#8931")
                await message.channel.send(embed = embed)
                print("Made an embed")

#TESTING GROUND
            if message.guild.id == 773042587308785664:
                if mcu == "Z!T":
                    print("Code works...")
                    owner = discord.Guild.owner.id
                    await message.channel.send()
        
            if mcu == "Z!ME":
                print("User info")
                await message.channel.send("Name = " + str(message.author.name) + "\n" + "Discriminator = #" + str(message.author.discriminator) + "\n" + "Display name = " + str(message.author.display_name) + "\n" + "Avatar = " + "https://cdn.discordapp.com/avatars/" + str(message.author.id) + "/" + str(message.author.avatar) + ".png?size=128")

#CREDITS
            if mcu == "Z!CREDS" or mcu == "Z!CREDITS":
                print("CREDITS")
                embed = discord.Embed(title = "<:drafonexcite:795724032510394389> Credits: (z!creds/z!credits)", description = "Members who (contributed to/helped me make) this bot", color = 0x53f200)
                embed.add_field(name = "<:drafonexcite:795724032510394389> LordBusiness", value = "LordBusiness taught me how to make a bot, and also helped me when I had bugs/errors")
                embed.add_field(name = "<:drafonexcite:795724032510394389> reeeeethedes", value = "ree was my partner and we both solved problems, stayed up late, and learnt more together")
                embed.add_field(name = "<:drafonexcite:795724032510394389> Anaton", value = "Being a pro discord.py bot developer, he was always there when I could not find out how to do something as much as I searched")
                embed.add_field(name = "<:drafonexcite:795724032510394389> rammy", value = "rammy supplied me with so many ideas that helped my bot become more advanced and fun!")
                embed.add_field(name = "<:drafonexcite:795724032510394389> Rt/Rtx", value = "Rt drew all the dragon emojis in some of the commands, that look so cool!! *(Some of which are in this embed!)*")
                embed.set_footer(text = "Made and owned by CyberFowl#8931")
                await message.channel.send(embed = embed)

#FAILSAFE
            if mcu == "Z!EXIT":
                await message.delete()
                await message.channel.send("Bot is shutting down now.")
                await message.channel.send("<@!743009565242556526>, bot was shutdown by <@!" + str(message.author.id) + ">")
                sys.exit()

print("Booting up...")

client = MyClient()
client.run("BOT_TOKEN_HERE")
