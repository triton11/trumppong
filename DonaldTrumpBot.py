import tweepy
import random
import time

auth = tweepy.OAuthHandler("UsNb2r0khXajXiX9hwmaepDFQ", "XK3HWJ1arIpKC4gFa6rPbQaAZtdiIsYmnqOP0KV9fqlPEIURsc")
auth.set_access_token("4190733136-lUBiPtEKT10jQ0LcVSFsjMddb4GZZHk4cmIZRZA", "rnuR792qthb0WlN5CYrYtPtxyTGUTgr4MHC1Kejn0LH3r")

api = tweepy.API(auth)

count = 0
on = True
while on == True:

    process = random.randrange(0,100)

    #Sometimes
    insults = ["5 wives", "a mexican in his closet", "testicular rabbies", "a terrible relationship with his mother", "an addiction to anal beads", "too much money", "an illegitimate child", "horse AIDs", "a poor taste in music", "no memory of his time spent in Guantanamo Bay", "a private prison", "a well-paid blunt roller", "no idea how to wash his own armpits", "a micropenis", "a private circus of midgets", "a bed-wetting problem", "too many cooks", "a racist grandma", "no control of his bladder", "penis scurvy due to a lack of vitamin C", "anal contusions", "no idea where the country Haiti is located", "a jar of orphan tears under his bed", "a goal to one day attend a real college", "silicon implants to make his breasts look bigger", "a strong dislike for anything pink", "almost an entire percent chance at becoming president!", "no eyelids", "a pet cactus named rob", "a man-gina", "weasels. Like, tons and tons of weasels", "hives and HIVs", "no game", "a first round draft pick in the 2016 WNBA", "windows 95", "a Yung Lean t-shirt", "WPA encrypted Wi-Fi", "a biography titled: My Worst Colonoscopy", "a hidden third eye right below his belly button", "no idea how to ban a twitter bot", "a friend named Willy Wonka", "the appearance of an immigrant bashing carnival barker", "a pimple on his butthole", "a 300$ bounty for his head in Taiwan", "the strength of a thousand men", "a sexual attraction to penguins", "a platinum ELO League of Legends account", "two transgender pet monkeys named Steve and Felicia", "a love-hate relationship with both his wives", "a dildo for special occasions, like Christmas or funerals", "oodles of noodles for breakfast every day", "no idea how to read", "made an appearance on the shows Survivor, Cake Boss, and Teen Virgin Diaries XXX", "tried and failed at becoming a pole dancer before getting into real estate", "a hard time pretending to be human", "a pet fox that lives on top of his head", "a lifetime supply of dick deodorant"]
    if process <= 30:
        for result in api.search(q="Donald Trump"):
            sn = result.user.screen_name
            x = insults[count]
            m = "@%s Fun Fact: Donald Trump has " %(sn) + insults[x]
            print m
            api.update_status(status=m)
            count += 1
            break
    elif process <= 50:
        start = ["Fox News claims ", "Cool fact: ", "This just in: ", "Little known fact about Trump: ", "According to Trump's mom, ", "According to Trump's campaign manager, ", "A little birdy told us ", "Interestingly enough, ", "Fun fact: "]
        x = random.randrange(0, len(insults)-1)
        m = 




    #Every time
    user = api.me()
    print user.followers_count
    for friend in user.followers():
        a = friend.id
        b = friend.screen_name
        api.create_friendship(a,b)
    count += 1
    if count == len(insults)-1
        
    time.sleep(random.randrange(3000, 4000))
    
        
    

