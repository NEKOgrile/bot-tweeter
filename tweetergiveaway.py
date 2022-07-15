from gettext import find
from telnetlib import STATUS
from xmlrpc.client import Fault
from numpy import append
import tweepy
import time
import json
import random
import os
import re

# authentication


api_key = "vb2Z6mE1ufyYn7hfqotdbFeeS"

api_key_secret = "utPqHUre5NomOUT7ETqugWzh0GF7ptff095VXDkigOaBHjdenz"

access_token = "1509075007481204738-u9e7dVSCnlDmstmfGo96OLA3RvixjN"

access_token_secret = "gqzT22L2NNH7t4Bvg79mZko0xrmeo9PPd3hF8GkEo9sa6"


auth = tweepy.OAuthHandler(api_key, api_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print("connection réussi")


def followplus(data):
    # je cherche si dans rulle . follow c est egal a true dans le dernier puis
    print("c est le n° "+str(len(data)-2)+" tweets")
    idafollow = data[str(len(data)-2)]["rule"]["follow"]
    print("follow = "+str(idafollow))
    if idafollow == True:
        # si c est vrais alors je prend tout le text
        textfile = data[str(len(data)-2)]["text"]
        # et je recupaire tout la chaine de caractére apres le @
        tableaudenom = re.findall("@(\S+)", textfile)
    return tableaudenom


def valeurrandom(min, max):
    # fonction permettent de donner une valeur aléatoire a partir d un min et max donné
    valeur = random.randint(min, max)
    return valeur


def match_string_in_array(list, items):
    # je regarde si le dans la list forni il y a une valeur qui existe ( item )
    for obj in list:
        if obj in items:
            return True
    return False


def find_id(tweet_id):
    # je regarde si l id du twit que j ai trouver et deja ping sinon il passe
    try:
        # j ouvre le J.son mais si il existe pas je passe
        # avec une fonction qui permet de le trouver au niveau du code present
        with open(f'{os.path.abspath( os.path.dirname( __file__ ))}\\valeur_bot.json', 'r') as f:
            f_str = f.read()
        # print(f_str.find(tweet_id))
        return f_str.find(tweet_id) != -1

    except:
        return False


def get_tweets(query, count):
    print("hey")
    fetched_tweets = api.search_tweets(
        query, count=count, tweet_mode='extended')

    for tweet in fetched_tweets:
        status = api.get_status(tweet.id_str, tweet_mode="extended")

        if "retweeted_status" not in status._json and not find_id(tweet.id_str):

            fdata = {}
            tablename = []
            try:
                with open(f'{os.path.abspath( os.path.dirname( __file__ ))}\\valeur_bot.json', 'r') as f:
                    fdata = json.load(f)
                    f.close()
            except:
                pass

            for i in range(max(0, len(fdata)-3), len(fdata)):

                tablename.append("@"+fdata[str(i)].get('name'))

            # tableau

            likelist = ["like", "\u2764", "\u2665", "Like",
                        "♥️", "\u2764\ufe0f", "\u2764\ufe0f\n"]

            discodlist = ["JOIN DISCORD", "rejoi le discord",
                          "rejoin discord", "rejoin notre discord", "discord"]

            RTlist = ["RT", "Retweet", "\n2-RT", "-RT", '2-RT', "RT ", " RT"]
            walletlistjson = ["Wallet"]

            followlist = ["Follow", " Follow", "follow"]

            aleatoire = " ".join(tablename)

            reponcelist = ["\U0001f688", "\U0001f680", "\U0001f681", "\U0001f682", "\U0001f683", "\U0001f684", "\U0001f685", "\U0001f686", "\U0001f687", "\U0001f688", "\U0001f689", "\U0001f68a", "\U0001f68b", "\U0001f68c", "\U0001f68d", "\U0001f68e", "\U0001f68f", "\U0001f690", "\U0001f691", "\U0001f692", "\U0001f693", "\U0001f694", "\U0001f695", "\U0001f696", "\U0001f697", "\U0001f697", "\U0001f698", "\U0001f699", "\U0001f69a", "\U0001f69b", "\U0001f69c", "\U0001f69d", "\U0001f69e", "\U0001f69f", "\U0001f6a0", "\U0001f6a1", "\U0001f6a2", "\U0001f6a3",
                           "\U0001f6a4", "\U0001f6a5", "\U0001f6a6", "\U0001f6a7", "\U0001f6a8", "\U0001f6a9", "\U0001f6aa", "\U0001f6ab", "\U0001f6ac", "\U0001f6ad", "\U0001f6ae", "\U0001f6af", "\U0001f6b0", "\U0001f6b1", "\U0001f6b2", "\U0001f6b3", "\U0001f6b4", "\U0001f6b5", "\U0001f6b6", "\U0001f6b7", "\U0001f6b8", "\U0001f6b9", "\U0001f6c0", "\U0001f6c1", "\U0001f6c2", "\U0001f6c3", "\U0001f6c4", "\U0001f6c5", "\U0001f6c6", "\U0001f6c7", "\U0001f6c8", "\U0001f6c9", "\U0001f6ca", "\U0001f6cb", "\U0001f6cd", "\U0001f6cc", "\U0001f6ce", "\U0001f6cf"
                           ]

            walletlist = [" opensea : 0xec5c2b51b350c3A441899221Ef61aC20426b27Fe",
                          " polygone : 0xf97eb1B541eb2030479dc32329033774E249C9f3"]

            # mise en page du fichier json
            newdata = {
                "text": status.full_text,
                "date": str(tweet.created_at),
                "ID": tweet.id_str,
                "name": status.user.screen_name,
                "rule": {

                    "like": match_string_in_array(likelist, status.full_text.lower()),

                    "RT": match_string_in_array(RTlist, status.full_text.lower()),
                    "Discord": match_string_in_array(discodlist, status.full_text.lower()),
                    "wallet": match_string_in_array(walletlistjson, status.full_text.lower()),
                    "follow": match_string_in_array(followlist, status.full_text.lower()),

                }
            }
            valeur = valeurrandom(min=300, max=800)
            print(
                "--------------------------------------------------------------------------------------------")
            print("avent de prendre le tweet il fait attendre : "+str(valeur)+" sec")
            time.sleep(valeur)

            fdata[len(fdata)] = newdata

            # follow la personne qui a cree le post

            api.create_friendship(user_id=status.user.id, follow=False)

            api.create_favorite(id=status.id_str)

            api.retweet(id=status.id_str)
            print("le twwet a etais cree le "+str(tweet.created_at),
                  " avec un id de : "+str(status.id))

            randomwallet = random.choice(walletlist)

            randomemodji = random.choice(reponcelist)

            randomemodji2 = random.choice(reponcelist)

            print("les personnes ping seron : " + str(aleatoire))

            api.update_status(
                status=f"@{status.user.screen_name} {randomemodji}{randomemodji}{randomemodji}{randomemodji}{randomemodji}{randomemodji}\nfriends: {aleatoire} \ni Ping for {query} \nMy wallet NFT {randomwallet}\n{randomemodji2}{randomemodji2}{randomemodji2}{randomemodji2}{randomemodji2}{randomemodji2}", in_reply_to_status_id=status.id)

            # creation / ouverture du fichier json

            with open(f'{os.path.abspath( os.path.dirname( __file__ ))}\\valeur_bot.json', 'w') as f:
                json.dump(fdata, f, indent=4)
                f.close()

            tableauafollow = followplus(fdata)

            # faire une boucle qui se repte auten qu il y a de valeur dans le tableau a follow

            if tableauafollow:
                for nom in tableauafollow:
                    print("nom a follow est : "+str(nom))
                    api.create_friendship(screen_name=nom, follow=False)
                    print("il a bien follow")
                    print("-------------------------")


while True:
    try:
        get_tweets(query="#NFTGiveaways", count=50)
        valeur = valeurrandom(min=300, max=800)
        print("la prochaine foi que je lance la fonction c est dans : " +
              str(valeur)+" sec")
        time.sleep(valeur)
    except:
        pass
    # except Exception as e:
        # print(f"Unable to update PokeAlarm data: {e}")
        # print("Stack trace: \n {}".format(traceback.format_exc()))
