"""
#kyspam.py

    script de spam

"""

import subprocess
import requests
import sys


def main():
    invite_code = sys.argv[1].split(
        "https://discord.gg/")[1]  # code d'invitation
    print(invite_code)
    chan = sys.argv[2]
    nb_msg = sys.argv[3]

    file = "kysan.token.txt"
    tokenlist = [line.rstrip('\n') for line in open(file)]      # list de token

    subprocess.Popen(["python", "botjoin.py", invite_code, nb_msg], shell=True)      # pour que le bot join le serv

    counter = 0
    for token in tokenlist:
        # on lance le script de spam en passant le token du bot en args
        subprocess.Popen(["python", "spambot.py", token, chan, nb_msg], shell=True)
        
        counter += 1
        print("bot " + str(counter) + " lancé")


main()

# made by Kysan721
