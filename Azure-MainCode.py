import discord
import time
import random
import sys

msgNo = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is online!")

#        These are just statuses that you can play around with:        
        
#        await client.change_presence(status = discord.Status.idle)
#        await client.change_presence(activity=discord.Game(name="tag with the wolves"))
#        await client.change_presence(activity=discord.Streaming(name="for the wolves", url="https://twitch.tv/cyberfowl"))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=""))
#        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="leadership"))
#        await client.change_presence(activity=discord.Activity.watching, name="the pack")

    async def on_member_join(member):
        await client.send_message(member,"Welcome!")

    async def on_message(self, message):

        global recall
        global msgNo

        mcu = message.content.upper()
        justmc = message.content
        
        if mcu.startswith("Z!POLL"):
            print("POLL")
            op1 = justmc.split(":")[-2]
            op2 = justmc.split(":")[-1]
            embed = discord.Embed(title = "Poll by " + str(message.author), color = 0xff0033)
            embed.add_field(name = op1, value = "Option 1 :one:", inline = False)
            embed.add_field(name = op2, value = "Option 2 :two:", inline = False)
            embed.add_field(name = "Note:", value = "For now, this command only supports only two polls." + "\n" + "Syntax: <z!poll :option 1:option 2>")
            embed.set_footer(text = "Made and owned by CyberFowl#8931")
            await message.channel.send("Poll:", embed = embed)
      
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

#EVERYBODY - Fun
            if mcu.startswith("Z!8BALL"):
                print("8ball")
                await message.channel.send(ball_response[lucky_phrase])

            if mcu == "Z!OWNER":
                print("Griffin info")
            
            if mcu == "REE IS DUMB":
                print("Message received")
                await message.channel.send("NO, NEITHER REEEEE THE DESTROYER NOR REEEEBEKA IS DUMB!! ||Though maybe you are!!||")

            if mcu == "TOILET":
                print("elmo in a toilet")
                await message.channel.send("https://tenor.com/view/elmo-poop-pooping-time-to-poop-bathroom-gif-5885298")

            if mcu == "F FOR RESPECT":
                print("F FOR RESPECT")
                time.sleep(2)
                await message.channel.send("F")

            if mcu == "BRUH":
                print("BRUH MOMENT")
                await message.channel.send("*(Bruh moment)*")

            if mcu == "DRYICE CHARACTER SKETCH":
                print("Message received")
                await message.channel.send("DryIce weird bruh.")

            if mcu == "HOMEWORK TIME" or mcu == "I GTG DO HOMEWORK":
                print("Message received")
                await message.channel.send("Ugh homework sux")

            if mcu.startswith("Z!HBD"):
                bday = mcu.split(" ")[-1]
                print("Message received")
                await message.channel.send(":tada: :tada: Happy birthday" + bday + "!!!! :tada: :tada:" + "\n" + "https://tenor.com/bdecb.gif")

            if mcu.startswith("Z!HUG"):
                hug = mcu.split(" ")[-1]
                print("hug")
                await message.channel.send("You hug " + hug + "\n" + "https://tenor.com/view/dog-hug-bff-best-friend-friend-gif-9512793")

            if mcu == "WHOS RAMMY?":
                print("Message received")
                await message.channel.send("Rammy's weird, bruh.")

            if mcu == "PMUB D!":
                print("PMUB D!")
                await message.channel.send("!d bump")

            if mcu == "RR PLS":
                print ("rickroll")
                embed=discord.Embed(title = "RR", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                await message.channel.send(embed=embed)

            if mcu == "IS GRIFFIN WEIRD?" and message.author.id != 743009565242556526:
                await message.channel.send("NOPE, Griffin created me!!")

            if mcu == "I LOVE COFFEE":
                print("COFFEE!!")
                await message.channel.send("<:red_archive:777977960359526401>")

            if mcu == 'Z!PING':
                print('Z!ping') 
                await message.channel.send(f":ping_pong: Pong! | Message took ***{round(client.latency * 1000)}ms*** to respond")

            if mcu == "SACRIFICE!!":
                print("Sacrifice!!")
                await message.channel.send("https://tenor.com/view/dance-dancing-tribe-tribal-the-tribe-has-spoken-gif-16960649")

            if mcu == "FLAMING ELMO":
                print("Flaming elmo")
                await message.channel.send("https://tenor.com/view/elmo-satan-fire-flame-burn-gif-4507786")

            if mcu.startswith("Z!PURGE"):
                purge = mcu.split(" ")[-1]
                await message.channel.purge(limit = int((purge)) + 1)

            
            if mcu == "MUSIC PLS" and message.author.id != 743009565242556526:
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
                    time.sleep(2)

    #CULT O COFFEE
            if mcu == "P!OWNER" and message.guild.id == 769557583429369867:
                print ("ping ree the des")
                for i in range(1,6):
                    await message.channel.send("<@!690227486721966130>")
                    time.sleep(2)

    #CHOCOLATE CULT
            if mcu == "P!OWNER" and message.guild.id == 775901922871214101:
                print ("ping anna")
                for i in range(1,6):
                    await message.channel.send("<@!760603081573400576>")
                    time.sleep(2)

    #TECH TERRAIN
            if mcu == "P!OWNER" and message.guild.id == 746952048053977148:
                print ("ping rammy")
                for i in range(1,6):
                    await message.channel.send("<@!737661910194847836>")
                    time.sleep(2)

#CYBERFOWL

            if message.author.id == 743009565242556526 or message.author.id == 690227486721966130:

                if mcu.startswith("GN"):
                    print("GOOD NIGHT")
                    await message.channel.send("Good Night!!")

                if mcu.startswith("YEET"):
                    print("YEETED SOMEBODY")
                    await message.channel.send("YEETED" + "\n" + "https://tenor.com/view/yeet-lion-king-simba-rafiki-throw-gif-16194362")

                if mcu == ("P!RTD"):
                    print("PING REE THE DES")
                    for i in range(1,6):
                        await message.channel.send("<@!690227486721966130>")
                        time.sleep(2)

                if mcu == ("P!RMY"):
                    print("PING RAMMY")
                    for i in range(1,6):
                        await message.channel.send("<@!737661910194847836>")

                if mcu == "IS AR WEIRD?":
                    print("Message received")
                    await message.channel.send("Yep")

                if mcu == "MUSIC PLS":
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

#CODENINJAS
            if message.author.id == 743009565242556526 or message.author.id == 737661910194847836 or message.author.id == 690227486721966130:

                if mcu == "Z!H":
                    print("Next Hackathon")
                    embed=discord.Embed(title = "Latest Hackathon", url = "https://organize.mlh.io/participants/events/6413-hackthrob", color = 0xff0033)
                    embed.set_thumbnail(url = "https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_thumbnails/001/359/964/datas/original.png")
                    embed.add_field(name = "HackThrob", value = "Do something related to Valentines Day.", inline = False)
                    embed.add_field(name = "Prizes:", value = "~", inline = False)
                    embed.add_field(name = ":star: First Overall", value = "Google Nest Hub + MLH Swag", inline = False)
                    embed.add_field(name = ":star: Second Overall", value = "Anker Soundcore Wireless Earbuds + MLH Swag", inline = False)
                    embed.add_field(name = ":star: Third Overall", value = "Anker PowerCore Portable Charger + MLH Swag", inline = False)
                    embed.add_field(name = ":star: Most Heartfelt Hack", value = "It's Valentine's Day weekend and hacking is in the air! Why don't you celebrate by creating your favorite on-theme hacks? The best hack will win Minipresso Portable Expresso Machine.", inline = False)
                    embed.add_field(name = ":star: Achy Breaky Hack", value = "Listen to your achy breaky heart and try something new this weekend. Work with new technologies and explore different domains for the first time. If you're a beginner, this is your chance to build a project from scratch. The winning team members take home Fuji Film Instax Camera.", inline = False)
                    embed.add_field(name = ":star: Best use of Google Cloud", value = "Build your hackathon project with a suite of secure storage, powerful compute, and integrated data analytics products provided by Google Cloud. See full list of products here: g.co/cloud. Each winning team member will receive a Google Branded Parkland Academy Backpack.", inline = False)
                    embed.add_field(name = ":star: Best Domain Name from Domain.com", value = "Register a .tech, .space, or .online domain name using Domain.com during the weekend. Each team may submit one entry per person on the team. Each winning team member will receive a PowerSquare Qi Wireless Phone Charger & Domain.com Backpack.", inline = False)
                    embed.add_field(name = ":star: Best Hardware Hack presented by Digi-Key (2)", value = "Using your preferred hardware or hardware emulator, build a hack for your chance to win a Grove Beginner Kit, with Arduino Uno R3 included. We select two winning teams for this category. Each winning team member will receive a prize!", inline = False)
                    embed.add_field(name = ":star: Best Domain Name from GoDaddy Registry [APAC Only]", value = "GoDaddy Registry is giving you everything you need to be the best hacker no matter where you are. Register your domain name with GoDaddy Registry for a chance to win a Hack from Home Kit! Each Kit contains wireless earbuds, blue light glasses, selfie ring light and a pouch for easy transport.", inline = False)
                    embed.add_field(name = ":star: Best Use of CockroachDB", value = "Build your hackathon project on CockroachDB's open source and indestructible SQL database. Utilize CockroachDB in your hack for a chance to win a 3D printing pen for each team member. What's more, ALL projects submitted that use CockroachDB will receive a free t-shirt!", inline = False)
                    embed.set_footer(text="Made and owned by CyberFowl#8931")
                    await message.channel.send(embed = embed)

                if mcu == "Z!AIM":
                    print("Prize Aim")
                    embed=discord.Embed(title = "Prize Aim", description = "The prize we are going for!", url = "https://organize.mlh.io/participants/events/6413-hackthrob", color = 0xff0033)
                    #embed.add_field(name = ":star:", value = "", inline = False)
                    embed.add_field(name = "404 Aim Not Found", value = "Aim not speccified/decided yet.", inline = False)
                    embed.set_footer(text="Made and owned by CyberFowl#8931")
                    await message.channel.send(embed = embed)

#REEEEE THE DESTROYER

            if message.author.id == 690227486721966130:

                if mcu == "HELP":
                    print("Message received")
                    await message.channel.send("¯\_(ツ)_/¯ What do you want help with? ||(Keeping in mind that I can't help a lot anyway)||")
                if mcu == "HMM CAN YOU MAKE ME A COFFEE?":
                    print("Message received")
                    await message.channel.send("Sorry, I'm not *that* advanced... Maybe ask me in, what? 5 years? Hopefully I can do it then... Hopefully...")

#REEEEBEKA_
            
            if message.author.id == 762793879522639904:

                if mcu == "G!HELP":
                    for i in range(1,11):
                        await message.channel.send("<@!743009565242556526>")
                        time.sleep(2)

#MEMBER COUNT - CYBERFOWL ONLY

            if message.author.id == 743009565242556526:

                if mcu == "50 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 50 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")
                    
                if mcu == "100 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 100 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")
 
                if mcu == "150 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 150 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")
 
                if mcu == "200 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 200 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")

                if mcu == "250 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 250 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")

                if mcu == "300 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 300 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")                 

#EMOJIS
            if mcu== "Z!AVATAR":
                print("Azure avatar")
                await message.channel.send("<:Azure:800679821013024769>")

            if mcu == ":SPOOKEDHAMSTER:" or mcu == ":SPOOKED HAMSTER:":
                print(":spookedhamster:")
                await message.channel.send("<:Hamster_spooked:793356985609093150>")

            if mcu == "JS":
                print("JS LOGO")
                await message.channel.send("<:JavaScriptlogo:800618033068245012>")
            if mcu == "PYTHON":
                print("PYTHON LOGO")
                await message.channel.send("<:pythonlogo:800620334554415115>")            
            if mcu == "Z!NITRO FLEX" and message.author.id == 743009565242556526:
                print("NITRO FLEX")
                await message.channel.send("<:CFLogo:800679960532615179>")
                time.sleep(1)
                await message.channel.send("<:NightHawk:800679902923456553>")
                time.sleep(1)
                await message.channel.send("<:Griffin2k20:800679874309390346>")
                time.sleep(1)
                await message.channel.send("<:Azure:800679821013024769>")
                
            if mcu.startswith("DISTRACT THEM") or mcu.startswith("DISTRACT HIM"):
                print("Distraction dance")
                for i in range(1,6):
                    await message.channel.send("<a:AmongDistracted:803394547203309619> <a:AmongDistracted:803394547203309619> <a:AmongDistracted:803394547203309619> <a:AmongDistracted:803394547203309619> <a:AmongDistracted:803394547203309619>")
                    time.sleep(2)
#EDITS
            if mcu == "EDIT TEST":
                edit = await message.channel.send("This")
                time.sleep(2)
                await edit.edit(content = "This is")
                time.sleep(2)
                await edit.edit(content = "This is a")
                time.sleep(2)
                await edit.edit(content = "This is a long")
                time.sleep(2)
                await edit.edit(content = "This is a long message.")
                time.sleep(2)

#VALENTINES DAY LOL
        msgNo = msgNo + 1
        if msgNo == 5:
            love = client.get_emoji(810454892015648769)
            await message.add_reaction(love)
            msgNo = 0

#REACTIONS
#            thonkingbutcool = client.get_emoji(793356545127612456)
#            await message.add_reaction(thonkingbutcool)

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

#FAILSAFE
            if mcu == "Z!EXIT":
                await message.delete()
                await message.channel.send("Bot is shutting down now.")
                await message.channel.send("<@!743009565242556526>, bot was shutdown by <@!" + str(message.author.id) + ">")
                sys.exit()

print("Booting up...")

client = MyClient()
client.run("BOT_TOKEN_HERE")
