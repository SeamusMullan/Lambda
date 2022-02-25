import instagrapi
import networkx as nx
import pyvis
import matplotlib.pyplot as plt

cl = instagrapi.Client()
# cl.login('calmingnatureposts', 'xN353@uxr')

class Target():
    def __init__(self, username, graph):
        self.username = username
        self.userID = cl.user_id_from_username(self.username)
        self.graph = graph

    def followers(self):
        followers = cl.user_followers(self.userID).items()
        return followers

    def following(self):
        following = cl.user_following(self.userID).items()
        return following

    def userInfo(self):
        info = cl.user_info_by_username(self.username).dict()
        return info

    def addFollowersToGraph(self, graph):
        graph.add_node(self.username)
        for i in self.followers():
            xx = cl.username_from_user_id(i[0])
            graph.add_node(xx)
            graph.add_edge(self.username, xx)

users = ["seamo.m", "notasnakepython", "seamo_skii"]


nxg = nx.DiGraph()

bruh = Target(users[0], nxg)
bruh.addFollowersToGraph(nxg)

pog = Target(users[1], nxg)
pog.addFollowersToGraph(nxg)

cum = Target(users[2], nxg)
cum.addFollowersToGraph(nxg)

g = pyvis.network.Network.from_nx(nxg)
g.show("test.html")


