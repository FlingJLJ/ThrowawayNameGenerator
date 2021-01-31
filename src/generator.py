import wordlists as wl
from random import randint

adjlist = wl.adjectives.split('\n')
nounlist = wl.nouns.split('\n')

def generate():
    return adjlist[randint(0, len(adjlist))] + nounlist[randint(0, len(nounlist))] + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
