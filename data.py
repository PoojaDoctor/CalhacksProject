import tweepy
import json

auth = tweepy.OAuthHandler('pFduB9dBKq5zvEWrAkhfTSnyv',
'cBcMj9z9jIO3HhmeaykDdfaCsByDqQujF4mZ6VO8mTyjDn5SGG')
auth.set_access_token('1058601288223514624-piQQ1twMDAwuAg7jTwJzvjHIRGVGNA' , 'nOcTYajRX8RRQDQ5cb4Rpl12GVGM2atSUqpRRg2aCDP8n')

api = tweepy.API(auth)

trends1 = api.trends_available()

with open('data.json', 'w') as outfile:
    json.dump(trends1, outfile)

with open('data.json', 'r+') as f:
    data = json.load(f)
    data['id'] = 134 # <--- add `id` value.
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()
