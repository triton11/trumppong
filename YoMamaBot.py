#YoMAMA Bot

import tweepy
import random
import time
import urllib
import re
this = True
while this == True:
    
    f = open("mamacount.txt", "r+")
    text = f.readline()
    text = int(text)
    numba = text
    text += 1
    if text > 1190:
        text = 1
    f.seek(0)
    text = str(text)
    f.write(text)
    f.truncate()
    f.close()


    url = 'http://www.jokes4us.com/yomamajokes/random/yomama%d.html' % (numba)


    resp = urllib.urlopen(url)
    respData = resp.read()

    match = re.search(r'<p align=center><font size=5>\n(.*?<)', respData)
    # If-statement after search() tests if it succeeded
    if match:
        x = match.group(1)
        print 'found', match.group(1)
    else:
        x = "eat a dick"
        print "eat a dick"


    auth = tweepy.OAuthHandler("IooPsvqHkC3lmQ4Tx2CDdCjn9", "btdSxMCf2X1arBOQHVnTrJj6CBHhgQng5uy9VCbxJwqsxehbLg")
    auth.set_access_token("4277218995-Dy1tGjNlzzFBDvc89va7hUtyS2V6tUa5EneXtPm", "BpeBH3OVEnHr7Gakm1f5e3oldAbaFdUwSbyZtZVI3PAJU")

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in api.search(q="@TruYoMamaFacts"):
        print tweet.text
        user = tweet.user.screen_name
        m = "@%s " %(user) + str(x)
        api.update_status(status=m)
    
        break
    
    time.sleep(random.randrange(1500, 2000))
    
