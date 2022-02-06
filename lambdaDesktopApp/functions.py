from inspect import getclosurevars
from instagrapi import *
import beeprint as bp


## Client Functions

def getClientObjectLogin(uname, pw):
    client = Client()
    client.login(uname, pw)
    return client


def getClientObject():
    client = Client()
    return client


## Get User * Functions

def getUser(client, user_id):
    user = client.user_info(user_id)
    return user


def getUserId(client, username):
    user_id = client.user_id_from_username(username)
    return user_id


def getUserFollowers(client, user_id):
    followers = client.user_followers(user_id)
    return followers



# x = getClientObjectLogin("calmingnatureposts", "xN353@uxr")

# with open("test.txt", "w") as f:
#     f.write(str(getUser(x, getUserId(x, "seamo.m")).dict()))

