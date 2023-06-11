import logging
import os

print("Revving up those fryers, please wait!") #message to pass time wit dis junk below
logging.getLogger('discord').setLevel(logging.WARNING)
logging.getLogger('discord.http').setLevel(logging.WARNING)
logging.getLogger('discord.client').setLevel(logging.WARNING)
logging.getLogger('discord.gateway').setLevel(logging.WARNING)

import threading
import discord
import time
from colorama import init, Fore
from os import system

def UpTtl(title):
    while True:
        system("title " + title)
        time.sleep(0.2)
        title = title[1:] + title[0]
title = "T's React Bot V2 "
ttlUp = threading.Thread(target=UpTtl, args=(title,)) #makes a cool looking title bar, makes IDLE horrid though.
ttlUp.start()

init()

BotToken = 'InsertBotTokenHere' #well... put the token here...
Channelid = [Channel 1, Channel 2(Optional)] #You dont need a second channel. If you want just one set the 2nd ID to 0. Supports multiple Channel IDs.
Wut2ReactWit = '🦫' #set it to an emoji you would like, its a beaver by default. This does not work with custom emojis

intents = discord.Intents.default()
intents.reactions = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    ChannelNames = []
    for ChandelID2 in Channelid:
        channel = bot.get_channel(ChandelID2)
        if channel:
            ChannelNames.append(channel.name)
    
    system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.MAGENTA}[{Fore.WHITE}-{Fore.MAGENTA}]{Fore.RESET} Bot is ready and logged in as: {Fore.YELLOW}{bot.user.name}{Fore.RESET} | Scanning channel{"s" if len(ChannelNames) > 1 else ""}: {Fore.GREEN}{", ".join(ChannelNames)}{Fore.RESET}\n')

@bot.event
async def on_message(message):
    if message.channel.id in Channelid:
        channel = bot.get_channel(message.channel.id)
        StartingTime = time.time()
        await message.add_reaction(Wut2ReactWit)
        EndTime = time.time()
        ReactTime = EndTime - StartingTime

        MessageLog = f"{Fore.GREEN}[+]{Fore.RESET} Reacted to {Fore.YELLOW}{message.author}{Fore.RESET} | Time: {Fore.GREEN}{ReactTime:.2f}s{Fore.RESET} | Channel: {Fore.GREEN}{channel.name}{Fore.RESET}"
        print(MessageLog)

bot.run(BotToken)
