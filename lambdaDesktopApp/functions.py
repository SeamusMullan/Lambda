from instagrapi import *
import beeprint as bp
import instaloader

## Instagram Client Functions

def clientLoginIG(uname, pw):
    client = Client()
    client.login(uname, pw)
    return client


def getUserIG(client, username):
    id = client.user_id_from_username(username)
    info = client.user_info(id).dict()
    return info


def iloaderDownloadUserPublic(target):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, target)
    for post in profile.get_posts():
        loader.download_post(post, target=profile.username)


def iloaderDownloadUserPrivate(target, loginUname, loginPW):
    loader = instaloader.Instaloader()
    loader.login(loginUname, loginPW)
    profile = instaloader.Profile.from_username(loader.context, target)
    loader.download_stories(profile)



