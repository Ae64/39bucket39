
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import datetime
import os.path
import shutil



Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = ",") #Initialise client bot


@client.event 
async def on_ready():
    await client.change_presence(game=discord.Game(name='Visit Mentarley.com', type=2))
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server


@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if ("@" + user.id) not in open("giveaway.txt").read():
            file = open("giveaway.txt", "a")
            file.write("@" + user.id + "\n") #message.author.id
            emb = (discord.Embed(title="Giveaway ", description="*,a* <:appletick:479728914432786443> You were successfully added to the giveaway, good luck! **", colour=0xfc2e33))
            await client.send_message(message.author, embed=emb)
            await client.add_reaction(message, "\U0001F34E")
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)  
    
    #await client.send_message(channel, '{} has added {} to the message: {}'.format(user.id, reaction.emoji, reaction.message.content))

        
        
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.messasge.author.voice.voice_channel
    await client.join_voice_channel(channel)







@client.event
async def on_message(message):

    
    if message.content == ",gr": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            spleet = message.content.split()
            name = spleet[1]
            keys = spleet[2]
            msg = "<@" + message.author.id + ",> Successfully gave " + spleet[1] + spleet[2] + " keys."
            await client.send_message(message.channel, msg)  
            msg1 = '!g ' + name + keys 
            await client.send_message(client.get_channel('479315144527052810'), msg1)
    elif message.content == ",gc": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            spleet = message.content.split()
            name = spleet[1]
            keys = spleet[2]
            msg = "<@" + message.author.id + ",> Successfully gave " + spleet[1] + spleet[2] + " keys."
            await client.send_message(message.channel, msg)  
            msg1 = '=g ' + name + keys 
            await client.send_message(client.get_channel('479315144527052810'), msg1)
    elif message.content == ",gj": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            spleet = message.content.split()
            name = spleet[1]
            keys = spleet[2]
            msg = "<@" + message.author.id + ",> Successfully gave " + spleet[1] + spleet[2] + " keys."
            await client.send_message(message.channel, msg)  
            msg1 = '\g ' + name + keys 
            await client.send_message(client.get_channel('479315144527052810'), msg1)
    elif message.content == ",gs": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            spleet = message.content.split()
            name = spleet[1]
            keys = spleet[2]
            msg = "<@" + message.author.id + ",> Successfully gave " + spleet[1] + spleet[2] + " keys."
            await client.send_message(message.channel, msg)  
            msg1 = '-g ' + name + keys 
            await client.send_message(client.get_channel('479315144527052810'), msg1)

    elif message.content == ",c 1": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key - Very Short** \n<:redicon:494926303053479936> Secs remaining: **1** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(2)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    
    elif message.content == ",c 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key - Short** \n<:redicon:494926303053479936> Secs remaining: **5** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(5)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            

    elif message.content == ",c 40": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 60": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 120": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",t 120": #get a role soon
        if "503992220370862080" in [role.id for role in message.author.roles]:
            spleet = message.content.split()
            name = spleet[1]
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(5)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ",gtickets <" + myline + "> " + name
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",c 20": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",c 50": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 70": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 80": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 30 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' Giveaway starting now! React to enter. Ending in **30** seconds @here **2 Winners**')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1 ```You won the giveaway!  //  Pm the person that started the giveaway for your reward if you win anything from this key```"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)

            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 40 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 60 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 120 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 20 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 50 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 70 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 80 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 30 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 40 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 60 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @her')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour = discord.Colour.blue(), description= "** Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 120 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 20 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            await client.send_message
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 50 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 70 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 80 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    #####
    elif message.content == ",c 30 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 40 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 60 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 120 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 20 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 50 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 70 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",c 80 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    ###
    elif message.content == ",c 30 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "=g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 40 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "=g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 60 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "=g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",c 120 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Cheap Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "=g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "=g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "=g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "=g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "=g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    

    if message.content == ",r 1": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key - Very Short** \n<:redicon:494926303053479936> Secs remaining: **1** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(2)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    
    if message.content == ",r 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key - Short** \n<:redicon:494926303053479936> Secs remaining: **5** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(5)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            

    elif message.content == ",r 40": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 60": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 120": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",t 120": #get a role soon
        if "503992220370862080" in [role.id for role in message.author.roles]:
            spleet = message.content.split()
            name = spleet[1]
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(5)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ",gtickets <" + myline + "> " + name
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",r 20": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",r 50": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 70": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 80": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 30 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' Giveaway starting now! React to enter. Ending in **30** seconds @here **2 Winners**')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1 ```You won the giveaway!  //  Pm the person that started the giveaway for your reward if you win anything from this key```"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)

            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 40 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 60 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 120 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 20 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 50 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 70 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 80 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 30 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 40 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 60 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @her')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour = discord.Colour.blue(), description= "** Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 120 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 20 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            await client.send_message
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 50 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 70 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 80 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    #####
    elif message.content == ",r 30 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 40 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 60 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 120 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 20 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 50 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 70 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",r 80 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    ###
    elif message.content == ",r 30 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "!g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 40 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "!g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 60 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "!g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",r 120 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "!g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "!g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "!g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "!g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "!g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    
            
    elif message.content == ",s 3w 1e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",s 3w 2e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",s 3w 3e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")



    elif message.content == ",s 4w 1e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 4w 2e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **2 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 4w 3e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **3 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",s 5w 1e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",s 5w 2e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **2 Free Platinum Keys** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 2"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            
    elif message.content == ",s 5w 3e": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **3 Free Platinum Keys** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 3"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 20 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 50 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == " 70 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 80 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Recruit Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter! • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">  **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
           
           
    elif message.content == ",s 30": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            

    elif message.content == ",s 40": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 60": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 120": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 20": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 50": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 70": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 80": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 30 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' Giveaway starting now- React to enter. Ending in **30** seconds @here **2 Winners**')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1 ```You won the giveaway-  //  Pm the person that started the giveaway for your reward if you win anything from this key```"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)

            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 40 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 60 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 120 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 20 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 50 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 70 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 80 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 30 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 40 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 60 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 120 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 20 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 50 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 70 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 80 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    #####
    elif message.content == ",s 30 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 40 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 60 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 120 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 20 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 50 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 70 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",s 80 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    ###
    elif message.content == ",s 30 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 40 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 60 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",s 120 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Platinum Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter- • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "-g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "-g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "-g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "-g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "-g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")          
   
    if message.content == ",e 30": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            

    elif message.content == ",e 40": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 60": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 120": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 20": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 50": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 70": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 80": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 30 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' Giveaway starting now> React to enter. Ending in **30** seconds @here **2 Winners**')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1 ```You won the giveaway>  //  Pm the person that started the giveaway for your reward if you win anything from this key```"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)

            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 40 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 60 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 120 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 20 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 50 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 70 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 80 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 30 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 40 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 60 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 120 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 20 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 50 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 70 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 80 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    #####
    elif message.content == ",e 30 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 40 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 60 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 120 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 20 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 50 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 70 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",e 80 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    ###
    elif message.content == ",e 30 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = ">g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 40 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = ">g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 60 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = ">g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",e 120 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = ">g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = ">g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = ">g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = ">g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = ">g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
         

    if message.content == ",d 30": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            

    elif message.content == ",d 40": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 60": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 120": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 20": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 50": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 70": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 80": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 30 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' Giveaway starting now+ React to enter. Ending in **30** seconds @here **2 Winners**')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1 ```You won the giveaway+  //  Pm the person that started the giveaway for your reward if you win anything from this key```"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)

            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 40 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 60 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 120 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 20 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 50 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 70 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 80 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 30 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 40 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 60 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 120 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 20 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 50 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 70 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 80 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    #####
    elif message.content == ",d 30 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 40 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 60 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 120 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 20 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 50 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 70 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",d 80 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    ###
    elif message.content == ",d 30 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "+g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 40 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "+g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 60 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "+g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",d 120 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Diamond Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter+ • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "+g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "+g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "+g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "+g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "+g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    if message.content == ",m 30": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
            

    elif message.content == ",m 40": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 60": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 120": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 20": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 50": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 70": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 80": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **1** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 30 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' Giveaway starting now> React to enter. Ending in **30** seconds @here **2 Winners**')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1 ```You won the giveaway>  //  Pm the person that started the giveaway for your reward if you win anything from this key```"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)

            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 40 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 60 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 120 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 20 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 50 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 70 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 80 2": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **2** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<"+ myline1 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 30 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 40 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 60 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 120 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 20 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 50 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 70 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<"+ myline2 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 80 3": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **3** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    #####
    elif message.content == ",m 30 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 40 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 60 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 120 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 20 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **20** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(20)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 50 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **50** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(50)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 70 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **70** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(70)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
    elif message.content == ",m 80 4": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **80** \n<:redicon:494926303053479936> Winners:  **4** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(80)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<"+ myline3 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    ###
    elif message.content == ",m 30 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **30** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(30)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "\g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + ">**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 40 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **40** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(40)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "\g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 60 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **60** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(60)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "\g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")

    elif message.content == ",m 120 5": #get a role soon
        if "441137252664475649" in [role.id for role in message.author.roles]:
            msg = await client.send_message(message.channel, ' <a:keygif:480118619964047380> **1 Free Sapphire Key** \n<:redicon:494926303053479936> Secs remaining: **120** \n<:redicon:494926303053479936> Winners:  **5** \nReact with :apple: to enter> • @here')
            file = open("giveaway.txt","a")
            await client.add_reaction(msg, "\U0001F34E")
            await asyncio.sleep(120)
            lines = open("giveaway.txt").read().splitlines()
            myline =random.choice(lines)
            msg = "\g <" + myline + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg)
            myline1=random.choice(lines)
            msg1 = "\g <" + myline1 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg1)
            myline2=random.choice(lines)
            msg2 = "\g <" + myline2 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg2)
            myline3=random.choice(lines)
            msg3 = "\g <" + myline3 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg3)
            myline4=random.choice(lines)
            msg4 = "\g <" + myline4 + "> 1"
            await client.send_message(client.get_channel('479315144527052810'), msg4)
            embed = discord.Embed(colour= 0xffffff , description= "**Winners: \n<" + myline + "> \n<" + myline1 + "> \n<" + myline2 + "> \n<" + myline3 + "> \n<"+ myline4 + "> **")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/503141814321283082/ezgif-5-e0e0ce81b7.gif")
            author1 = message.author.id
            profile = message.server.get_member(author1)
            pfp = profile.avatar_url
            embed.set_author(name= message.author.name + "'s Giveaway", icon_url=pfp)
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
            file.close()
            os.remove("giveaway.txt")
        
    elif message.content.startswith("recruit key"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xff0000, title = "Information" , description = "Recruit keys cost 500,000 gp. And payout 445,994 gp on average. This key has a 10.4% House edge. And can pay out anything from 0 gp to 28,907,503 gp.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504101243875098641/recruit_key.png")
            await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("platinum key"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xC0C0C0, title = "Information" , description = "Platinum keys cost 1,300,000 gp. And payout 1,090,831 gp on average. This key has a 16.5% House edge. And can pay out anything from 3,500 gp to 86,500,000 gp.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504101242927054849/plat_key.png")
            #await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("sapphire key"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0x0067ff , title = "Information" , description = "Sapphire keys cost 1,600,000 gp. And payout 1,418,448 gp on average. This key has a 11.38% House edge. And can pay out anything from 57 gp to 73,472,421 gp.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504101245523591194/Sapphire_key.png")
            #await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("diamond key"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0x800080, title = "Information" , description = "Diamond keys cost 2,800,000 gp. And payout 2,512,698 gp on average. This key has a 10.29% House edge. And can pay out anything from 500 gp to 200,000,000 gp.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504101241719226368/diamond_key.png")
            await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("gold key"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xc5f442, title = "Information" , description = "Gold keys are obtained from the Jackbox Chest. This key holds 10 items that each, have a 10% chance of being opened. The Gold keys average reward is 114,600,000 gp. Do 'goldkey items' for keys content list.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504105164358287360/Ment_Icons_key_4.png")
            await client.send_message(message.channel, embed=embed)
        
    elif message.content.startswith("goldkey items"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xc5f442, title = "Information" , description = "Gold keys contain 10 items that hold a value of 10% each. \nYou can win any of these prizes: \n10,000,000 gp %10 chance \n20,000,000 gp %10 chance \n30,000,000 gp %10 chance \n50,000,000 gp %10 chance \n75,000,000 gp %10 chance \n100,000,000 gp %10 chance \nfull 3rd age range(57m) %10 chance \nfull 3rd age mage(84m) %10 chance \nfull 3rd age melee (170m) %10 chance \nElysian spirit shield (550m) %10 chance.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504105164358287360/Ment_Icons_key_4.png")
            await client.send_message(message.channel, embed=embed)
        
    elif message.content.startswith("silverkey items"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xe0ded7, title = "Information" , description = "Silver keys contain 10 items that hold a value of 10% each. \nYou can win any of these prizes: \n2,000,000 gp %10 chance \n4,000,000 gp %10 chance \n6,000,000 gp %10 chance \n8,000,000 gp %10 chance \n10,000,000 gp %10 chance \n3rd age range legs (13m) %10 chance\nBandos chestplate (17m) %10 chance \nfull 3rd age robe bottom (19m) %10 chance\n3rd age kite (26m) %10 chance\n3rd age range top (31m) %10 chance.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504110604978749474/Ment_Icons_key_2.png")
            await client.send_message(message.channel, embed=embed)
        
    elif message.content.startswith("silver key"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xe0ded7 , title = "Information" , description = "Silver keys are obtained from the Decent Chest. This key holds 10 items that each, have a 10% chance of being opened. The Silver keys average reward is 13,600,000 gp. Do 'silverkey items' for keys content list.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504110604978749474/Ment_Icons_key_2.png")
            await client.send_message(message.channel, embed=embed)
               
    elif message.content.startswith("poop box"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xBA6B50, title = "Information" , description = "Poop Chests are used to open different amount of keys. You can win anything from 2 to 5 Recruit keys. House edge 0%.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504112336341172235/a06232afba59c6aaa178f5d00e042bfd.png")
            await client.send_message(message.channel, embed=embed)
    elif message.content.startswith("anymeds box"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0x8BDF81, title = "Information" , description = "AnyMeds Chests are used to open different amount of keys. You can win anything from 1 to 10 Platinum keys. House edge 0%.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504112337943396362/ce932052ae503664cb4475481a1cb465.png")
            #await client.send_message(message.channel, embed=embed)
    elif message.content.startswith("decent box"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xB11000, title = "Information" , description = "Decent Chests contain Silver keys & Sapphire keys. You can win anything from 5 to 20 Sapphire keys. There is also a 20% chance you will receive a Silver key. House edge 1.67%.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504112333770194944/4e938e7551e3c5be1d6e2df91d22724a.png")
            #await client.send_message(message.channel, embed=embed)
    elif message.content.startswith("jackpot box"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = discord.Embed(colour = 0xEDEB08, title = "Information" , description = "Jackpot Chests contain Gold keys & Diamond keys. You can win anything from 5 to 15 Diamond keys. You also have a 10% chance, to receive a gold key. House edge 3.2%.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/452046110622613514/504112334961377293/23770230862dba4e571583e8e507f2f5.gif")
            await client.send_message(message.channel, embed=embed)


    elif message.content.startswith("xp"):
        spleet = message.content.split()
        name = spleet[1]
        embed = (discord.Embed(title="", description="", colour=0xff0000))
        num = random.randint(1,1)
        if num == 1:
            embed.set_image(url="https://cdn.discordapp.com/attachments/475697983418007555/487975766475407370/unknown.png")
        await asyncio.sleep(1)
        await client.send_message(message.channel, embed=embed)
        

    elif message.content.startswith(",srice"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = (discord.Embed(description="**======Keys======\n<:Cheap:507907099825799169> Cheap = 100k \n<:Recruit:484841919067717664> Recruit = 500k  \n<:Platinum:484841999955001346> Shadow = 1.3m\n<:jackpot:507907109409783819> Jackpot = 1.8m \n<:emerald:512374499401007144> Emerald = 2m \n<:Diamond:484841953561935873> Diamond = 2.8m\n<:Rs3:507907081680977920> Rs3 = 26m \n<:3Age:507911540507148298> 3rd age = 33m\n\n=======Boxes=======\n<:poop:471926207286607872> Poop Box = 1.75m \n<:anymeds:471926217742745611> Anymeds Box = 5m\n<:decent:471926224252436481> Decent Box = 28m \n<a:xjackpot:471884993652850718> Jackpot Box = 41m**", colour=	0x000000))
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/461181074253414409.gif?v=1")
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)
    elif message.content.startswith(",srices"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = (discord.Embed(description="**======Keys======\n<:Cheap:507907099825799169> Cheap = 100k \n<:Recruit:484841919067717664> Recruit = 500k  \n<:Platinum:484841999955001346> Shadow = 1.3m\n<:jackpot:507907109409783819> Jackpot = 1.8m \n<:emerald:512374499401007144> Emerald = 2m \n<:Diamond:484841953561935873> Diamond = 2.8m\n<:Rs3:507907081680977920> Rs3 = 26m \n<:3Age:507911540507148298> 3rd age = 33m\n\n=======Boxes=======\n<:poop:471926207286607872> Poop Box = 1.75m \n<:anymeds:471926217742745611> Anymeds Box = 5m\n<:decent:471926224252436481> Decent Box = 28m \n<a:xjackpot:471884993652850718> Jackpot Box = 41m**", colour=	0x000000))
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/461181074253414409.gif?v=1")
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("price"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = (discord.Embed(description="**======Keys======\n<:Cheap:507907099825799169> Cheap = 100k \n<:Recruit:484841919067717664> Recruit = 500k  \n<:Platinum:484841999955001346> Shadow = 1.3m\n<:jackpot:507907109409783819> Jackpot = 1.8m \n<:emerald:512374499401007144> Emerald = 2m \n<:Diamond:484841953561935873> Diamond = 2.8m\n<:Rs3:507907081680977920> Rs3 = 26m \n<:3Age:507911540507148298> 3rd age = 33m\n\n=======Boxes=======\n<:poop:471926207286607872> Poop Box = 1.75m \n<:anymeds:471926217742745611> Anymeds Box = 5m\n<:decent:471926224252436481> Decent Box = 28m \n<a:xjackpot:471884993652850718> Jackpot Box = 41m**", colour=	0x000000))
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/461181074253414409.gif?v=1")
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)


    elif message.content.startswith("prices"):
        if "485760579437592576" in [role.id for role in message.author.roles]:
            embed = (discord.Embed(description="**======Keys======\n<:Cheap:507907099825799169> Cheap = 100k \n<:Recruit:484841919067717664> Recruit = 500k  \n<:Platinum:484841999955001346> Shadow = 1.3m\n<:jackpot:507907109409783819> Jackpot = 1.8m \n<:emerald:512374499401007144> Emerald = 2m \n<:Diamond:484841953561935873> Diamond = 2.8m\n<:Rs3:507907081680977920> Rs3 = 26m \n<:3Age:507911540507148298> 3rd age = 33m\n\n=======Boxes=======\n<:poop:471926207286607872> Poop Box = 1.75m \n<:anymeds:471926217742745611> Anymeds Box = 5m\n<:decent:471926224252436481> Decent Box = 28m \n<a:xjackpot:471884993652850718> Jackpot Box = 41m**", colour=	0x000000))
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/461181074253414409.gif?v=1")
            await asyncio.sleep(1)
            await client.send_message(message.channel, embed=embed)

        
    if message.content.upper().startswith(',SAY'):
        args = message.content.split(" ")
        #args[0] = ,say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(client.get_channel('436347354136969226'), "%s" % (" ".join(args[1:])))
        await client.delete_message(message)
        
        await client.send_message(message.channel, embed=embed)
                        

    elif message.content.startswith(",help"):
        embed = discord.Embed(colour = discord.Colour.red(), description = "This bot is a modified version of another \nbot and is missing 84 commands")
        embed.set_author(name = "MG Tools help manual", icon_url="https://cdn.discordapp.com/avatars/480043110680887336/5bc3a846e352efabfed5f609667614b0.webp?size=1024")
        embed.set_footer(text="Created by Apple#0001")
        await client.send_message(message.channel, embed=embed)


        

        






    
   
    
        
        
    
        
        

            


            
            


bot.run(os.environ['BOT_TOKEN'])
