import discord
import time
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

        #game = discord.Game("with the API")
        await client.change_presence(status = discord.Status.idle)#, activity = game)

    async def on_message(self, message):

        mcu = message.content.upper()

        if message.author != client.user:
            
            if "doggo" in mcu:
                print("Message received")
                await message.channel.send(":heart_eyes:")
                
#SWEAR STOP
            if "||" not in mcu and message.guild.id != 570023579215724547 and message.author != 727964715216797697:
                if "WTF" in mcu:
                    print("wtf")
                    await message.channel.send("HEY!!! NO SWEARING!!!")
                if "FECK" in mcu:
                    print("feck")
                    await message.channel.send("What *is* 'Feck'?!? :joy:")
                if "FUCK" in mcu:
                    print("fuck")
                    await message.channel.send("LANGUAGE!!!")
                if "SHIT" in mcu:
                    print("shit")
                    await message.channel.send("LANGUAGE!!!")
                if "BITCH" in mcu:
                    print("bitch")
                    await message.channel.send("LANGUAGE!!!")
                if "BASTARD" in mcu:
                    print("bastard")
                    await message.channel.send("HEY!!! NO SWEARING!!!")
                if "RETARDED" in mcu:
                    print("retarded")
                    await message.channel.send("LANGUAGE!!!")
                if "NIGGER" in mcu:
                    print("nigger")
                    await message.channel.send("HEY!!! NO SWEARING!!!")
                if "NIGGA" in mcu:
                    print("nigga")
                    await message.channel.send("LANGUAGE!!!")
                if "SH*T" in mcu:
                    print("sh*t")
                    await message.channel.send("HEY!!! NO SWEARING!!!")
                if "STFU" in mcu:
                    print("stfu")
                    await message.channel.send("LANGUAGE!!!")
                if "ASSHOLE" in mcu:
                    print("asshole")
                    await message.channel.send("LANGUAGE!!!")
                if "FECKING" in mcu:
                    print("fecking")
                    await message.channel.send("HEY!!! NO SWEARING!!!")
                    
                if "DAMN" in mcu:
                    print("damn")
                    await message.channel.send("I'm not going to 'LANGUAGE!!!' you, but, don't use ||damn|| too much...")

#STARTS WITH

            if mcu.startswith("YAY"):
                await message.channel.send(":tada:")
            if mcu.startswith("YEY"):
                await message.channel.send(":tada:")
            #if message.author.id != 743009565242556526:
                #if mcu.startswith("KILL"):
                    #print("NO HITMAN STRIKE")
                    #await message.channel.send("Sorry, only <@!743009565242556526> can order hitman strikes")

            if message.author.id == 743009565242556526:
                if mcu.startswith("Z!KILL"):
                    killed = mcu.split(" ")[-1]
                    print("KILLED USER")
                    await message.channel.send("Shot " + killed + "\n" + "https://tenor.com/view/shoot-gift-gif-13384546")
            #if mcu.startswith("HALLO"):
                #await message.channel.send("Hey")

#EVERYBODY - Fun

            if mcu == "Z!OWNER":
                print("Griffin info")

            #h = ["Heads","Tails"]
            #if mcu == "Z!COINFLIP":
                #n = random.randint(h[0],h[1])
                #print("Coinflip")
                #await message.channel.send(n)

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

            
#P!OWNER
                
    #ATLANTIS
            if mcu == "P!OWNER" and message.guild.id == 788293597379166228:
                print ("ping saanvi")
                await message.channel.send("<@!727964715216797697>")
                time.sleep(2)
                await message.channel.send("Successfully Pinged Owner")

    #CULT O COFFEE
            if mcu == "P!OWNER" and message.guild.id == 769557583429369867:
                print ("ping ree the des")
                await message.channel.send("<@!690227486721966130>")
                time.sleep(2)
                await message.channel.send("Successfully Pinged Owner")

    #CHOCOLATE CULT
            if mcu == "P!OWNER" and message.guild.id == 775901922871214101:
                print ("ping anna")
                await message.channel.send("<@!760603081573400576>")
                time.sleep(2)
                await message.channel.send("Successfully Pinged Owner")

    #TECH TERRAIN
            if mcu == "P!OWNER" and message.guild.id == 746952048053977148:
                print ("ping rammy")
                await message.channel.send("<@!737661910194847836>")
                time.sleep(2)
                await message.channel.send("Successfully Pinged Owner")

#CYBERFOWL

            if message.author.id == 743009565242556526 or message.author.id == 690227486721966130:

                if mcu.startswith("GN"):
                    print("GOOD NIGHT")
                    await message.channel.send("Good Night!!")

                if mcu.startswith("YEET"):
                    print("YEETED SOMEBODY")
                    await message.channel.send("YEETED" + "\n" + "https://tenor.com/view/yeet-lion-king-simba-rafiki-throw-gif-16194362")

                if mcu == ("WHOOOOO"):
                    print("WHOOOOO")
                    await message.channel.send(":tada: :confetti_ball:")
                    await message.channel.send(":confetti_ball: :tada:")

                if mcu == "AZURE STATUS":
                    print("status report")
                    await message.channel.send("https://tenor.com/view/status-tired-dead-haggard-gif-11733031")

                if mcu == "IS AR WEIRD?":
                    print("Message received")
                    await message.channel.send("Yep")

                if mcu == "MUSIC PLS":
                    print("spotify link - boss")
                    embed=discord.Embed(title="Music", url="https://open.spotify.com/collection/tracks")
                    await message.channel.send(embed=embed)

                if msg.startswith("z!remember"):
                    recall = msg.split(" ")[1:]
                    await message.channel.send("Remembered. Use z!recall to display it again.")
                listToStr = " ".join(recall)
                if msg == "z!recall":
                    await message.channel.send(listToStr)
                    await message.channel.send("Here you go ^")

                if msg.startswith("z!remember2"):
                    recall2 = msg.split(" ")[1:]
                    await message.channel.send("Remembered. Use z!recall2 to display it again.")
                listToStr2 = " ".join(recall2)
                if msg == "z!recall2":
                    await message.channel.send(listToStr2)
                    await message.channel.send("Here you go ^")

                if msg.startswith("z!remember3"):
                    recall3 = msg.split(" ")[1:]
                    await message.channel.send("Remembered. Use z!recall3 to display it again.")
                listToStr3 = " ".join(recall3)
                if msg == "z!recall3":
                    await message.channel.send(listToStr3)
                    await message.channel.send("Here you go ^")

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
                if mcu == "HMM CAN YOU MAKE ME A COFFEE?":
                    print("Message received")
                    await message.channel.send("Sorry, I'm not *that* advanced... Maybe ask me in, what? 5 years? Hopefully I can do it then... Hopefully...")

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
                    await message.channel.send(":tada: :tada: YAY!!! 200 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")

                if mcu == "300 MEMBERS":
                    print("Message received")
                    await message.channel.send(":tada: :tada: YAY!!! 200 MEMBERS!!! :tada: :tada:" + "\n" + "https://tenor.com/view/minion-woohoo-yeah-excited-cheer-gif-5002827")                 

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
                await message.channel.send("<a:AmongDistracted:803394547203309619>")

#EDITS
            if mcu == "EDIT TEST":
                edit = await message.channel.send("This")
                time.sleep(1)
                await edit.edit(content = "This is")
                time.sleep(2)
                await edit.edit(content = "This is a")
                time.sleep(2)
                await edit.edit(content = "This is a long")
                time.sleep(2)
                await edit.edit(content = "This is a long message.")
                time.sleep(2)

#REACTIONS
            if mcu == "HUH?":
                print("Huh?")
                thonkingbutcool = client.get_emoji(793356545127612456)
                await message.add_reaction(thonkingbutcool)

            #if mcu == "OH K":
                #print("OH K")
                #thonkingbutcool = client.get_emoji(793356545127612456)
                #await message.add_reaction(thonkingbutcool)


print("Code is running")

client = MyClient()
client.run("BOT_TOKEN_HERE")
