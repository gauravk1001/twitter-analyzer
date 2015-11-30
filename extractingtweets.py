from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import os

ckey='C9afrqfHZprKGmg3gNdUg'
csecret='SFHb24Uin1b1bGd3Qc7OwLT44c22jpTTWmdlWsBAI'
atoken='2358376346-n2Z2vDLxyD1nyltUMkQ8qM87IaTdcFWmKnDIiFr'
asecret='GLRGzdxmELUbY7VWueXTPzLdnxxtGqPDX4QwaOfyaRSSF'



input = raw_input('Enter the Keyword : ')
class listener(StreamListener):
	
	def on_data(self, data):
		try:	
			saveFile = open('E:\json.txt','a')
			saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet
			saveFile = open('final.csv','a')
			saveFile.write(tweet)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			
			
	def on_error(self, status):
		print status


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream=Stream(auth,listener())
twitterStream.filter(track = [input], languages = ['en'])

os.system('project.py')
 #Open/Create a file to append data
csvFile = open('resultGota.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
print (tweet.created_at, tweet.text);
csvFile.close()
