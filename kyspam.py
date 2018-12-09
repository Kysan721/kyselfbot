"""
#kyspam.py

    script de spam

"""

import subprocess
import requests
import sys


def main():
    if len(sys.argv) == 2:


    else:
        print("arguments invalide veuillez uttiliser la syntaxe suivante: kyspam <lien d'invite> <id du chan a spam>")
        if len(sys.argv) == 2:
        
        elif 

    invite_link = sys.argv[1].split(
        "https://discord.gg/")[1]  # code d'invitation
    print(invite_code)
    chan = sys.argv[2]

    file = "kysan.token.txt"
    tokenlist = [line.rstrip('\n') for line in open(file)]      # list de token

    subprocess.Popen(["python", "botjoin.py", invite_link, shell=True)      # pour que le bot join le serv

    counter = 0
    for token in tokenlist:
        # on lance le script de spam en passant le token du bot en args
        subprocess.Popen(["python", "spambot.py", dateTime, chan], shell=True)
        
        counter += 1
        print("bot " + str(counter) + " lancé")


main()

# made by Kysan721
