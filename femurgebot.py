#!/usr/bin/env python3
# femurgebot version 1
#2022-02-03

import tweepy
import time
import sys
from pathlib import Path
import random

Verbraw = './Verb.txt'
Nounraw = './Noun.txt'

VerbFile = open(Verbraw, 'r')
Verb = VerbFile.readlines()
VerbFile.close()

NounFile = open(Nounraw, 'r')
Noun = NounFile.readlines()
NounFile.close()

CONSUMER_KEY = 'unmodified'
CONSUMER_SECRET = 'unmodified'
ACCESS_KEY = 'unmodified'
ACCESS_SECRET = 'unmodified'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

## Set frequency of tweets posted, in SECONDS
## Don't set this too low, or you may get rate-limited, or even put in Twitter Jail!
## 3600 seconds, an hour, is a safe value
tweetFrequency = 3600

## Sanity check.
if ACCESS_SECRET == 'unmodified':
    print("\nYou must first edit the script and configure a few well-labeled variables before you can use it.\n")
    exit()

while True:
	Verbidx = random.randrange(len(Verb))
	Nounidx = random.randrange(len(Noun))

	tvit = "The feminine urge to " + str.lower(Verb[Verbidx].rstrip("\r\n")) + " a " + str.lower(Noun[Nounidx].rstrip("\r\n")) + "."
	print("Next twot phrase will be: " + tvit)

	api.update_status(tvit)

	for i in range(tweetFrequency, 0, -1):
		time.sleep(1)
##if you find the countdown in stdout annoying, remove the following two lines
		sys.stdout.write(str((i - 1))+' ')
		sys.stdout.flush()
