# -*- coding: utf-8 -*-
import nltk
import time
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import webbrowser
import csv
import MySQLdb

mydbs = MySQLdb.connect(host='localhost',user='root',passwd='',db='mydb')
cursor = mydbs.cursor()

#new = 2
#url = "file:///C:/Users/Varun/Desktop/trying.html"
#webbrowser.open(url,new=new)

pos_tweets = [('I love   car', 'positive'),
              ('  view is amazing', 'positive'),
              ('I feel great   morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('Success is nothing without someone love to share it with', 'positive'),
              ('And there the grass grows soft and white And there the sun burns crimson bright', 'positive'),
              ('Staying positive is all in head', 'positive'),
              ('Everyday is a new opportunity to make someone smile', 'positive'),
              ('A dream is the bearer of a new possibility the enlarged horizon the great hope', 'positive'),
              ('Friendship is the rainbow between two hearts sharing seven colors feelings love sadness happiness truth faith secret & respect', 'positive'),
              ('The best way to destroy an enemy is to make him a friend', 'positive'),
              ('Find something love to do and you’ll never have to work a day in life', 'positive'),
              ('Whatever be a good one', 'positive'),
              ('The future depends on what we do in the present', 'positive'),
              ('Never regret If it’s good it’s wonderful If it’s bad it’s experience', 'positive'),
              ('Everyday is a gift that’s why they call it the present', 'positive'),
              ('Happy those who dream dreams and ready to pay the price to make them come true', 'positive'),
              ('God never shuts a door without opening a window', 'positive'),
              ('If breathing have hope', 'positive'),
              ('There always flowers for those who want to see them', 'positive'),
              ('I have found that if love life life will love back', 'positive'),
              ('Once replace negative thoughts with positive ones you\'ll start having positive results', 'positive'),
              ('Every person is the creation of himself the image of own thinking and believing As individuals think and believe so they are', 'positive'),
              ('A sense of individual identity is one of the greatest gifts that parents can give a child', 'positive'),
              ('Our greatest glory is not in never falling, but in rising every time we fall', 'positive'),
              ('The secret to success is to start from scratch and keep on scratching', 'positive'),
              ('Blessed those who can give without remembering and take without forgetting', 'positive'),
              ('To a brave man good and bad luck like left and right hand He uses both', 'positive'),
              ('Even if you’re on the right track you’ll get run over if just sit there', 'positive'),
              ('The door to happiness opens outward', 'positive'),
              ('Optimists nostalgic about the future', 'positive'),
              ('Hope is faith holding out its hand in the dark', 'positive'),
              ('Once choose hope anything\'s possible', 'positive'),
              ('You must start with a positive attitude or will surely end without one', 'positive'),
              ('Some days there won\'t be a song in heart Sing anyway', 'positive'),
              ('I\'m doing very good today How you', 'positive'),
              ('Toughness is in the soul and spirit not in muscles', 'positive'),
              ('I have never met a man so ignorant that I couldn\'t learn something from him', 'positive'),
              ('I like rising sun', 'positive'),
              ('Positive anything is better than negative thinking', 'positive'),
              ('What a beautiful ride it was', 'positive'),
              ('To create success with more ease & flow must begin to create new patterns & habits', 'positive'),
              ('The dinner delicious', 'positive'),
              ('Happy is he who dares courageously to defend what he loves', 'positive'),
              ('Take time to laugh it is the music of the soul', 'positive'),
              ('Politeness is to human nature what warmth is to wax', 'positive'),
              ('Make optimism come true', 'positive'),
              ('Happiness is an attitude we eit make ourselves miserable or happy and strong', 'positive'),
              ('You such a genius glamorous and genuine at the same time', 'positive'),
              ('A positive attitude may not solve all problems', 'positive'),
              ('Hard work toil and patience key to success', 'positive'),
              ('Everything is going to be alright', 'positive'),
              ('Today is gonna be a good day', 'positive'),
              ('Tomorrow will be better', 'positive'),
              ('It\'s nice to watch the friendship developing between both of you', 'positive'),
              ('I love when someone holds the door for me', 'positive'),
              ('Smile it keeps people wondering', 'positive'),
              ('Congratulations Great job', 'positive'),
              ('live happy live free', 'positive'),
			  ('dazzling delight delightful divine', 'positive'),
			  ('laugh legendary light learned lively lovely lucid lucky luminous', 'positive'),
			  ('marvelous masterful meaningful merit meritorious miraculous motivating moving', 'positive'),
			  ('natural nice novel nurturing nutritious', 'positive'),
			  ('absolutely adorable accepted acclaimed accomplish', 'positive'),
			  ('accomplishment achievement action active admire adventure affirmative affluent agree', 'positive'),
			  ('agreeable amazing angelic appealing approve aptitude attractive awesome', 'positive'),
			  ('beaming beautiful believe beneficial bliss bountiful bounty brave bravo brilliant bubbly', 'positive'),
			  ('calm celebrated certain champ champion charming cheery choice classic classical', 'positive'),
			  ('clean commend composed congratulation constant cool courageous creative cute', 'positive'),
			  ('earnest easy ecstatic effective effervescent efficient effortless electrifying elegant enchanting', 'positive'),
			  ('encouraging endorsed energetic energized engaging enthusiastic', 'positive'),
			  ('essential esteemed ethical excellent exciting exquisite', 'positive'),
			  ('fabulous fair familiar famous fantastic favorable fetching', 'positive'),
			  ('fine fitting flourishing fortunate free fresh friendly funny', 'positive'),
			  ('generous genius genuine giving glamorous glowing good gorgeous graceful great green grin growing', 'positive'),
			  ('handsome happy harmonious healing healthy hearty heavenly honest honorable honored', 'positive'),
			  ('idea ideal imaginative imagine impressive independent innovate innovative instant instantaneous instinctive', 'positive'),
			  ('intuitive intellectual intelligent inventive jovial joy jubilant keen kind knowing knowledgeable', 'positive'),
			  ('okay optimistic paradise perfect phenomenal pleasurable plentiful pleasant poised polished popular', 'positive'),
			  ('positive powerful prepared pretty principled productive progress prominent protected proud', 'positive'),
			  ('quality quick quiet ready reassuring refined refreshing rejoice reliable remarkable resounding respected', 'positive'),
			  ('restored reward rewarding right robust safe satisfactory secure seemly simple skilled', 'positive'),
			  ('skillful smile soulful sparkling special spirited spiritual stirring stupendous', 'positive'),
			  ('stunning success successful sunny super superb supporting surprising', 'positive'),
			  ('terrific thorough thrilling thriving tops tranquil transforming transformative trusting truthful', 'positive'),
			  ('valued vibrant victorious victory vigorous virtuous vital vivacious', 'positive'),
			  ('wealthy welcome well whole wholesome willing wonderful wondrous worthy', 'positive'),
			  ('yummy zeal zealous', 'positive'),
              ('All of us born with a good amount of courage', 'positive'),
              ('When I becomes We even illness becomes wellness', 'positive'),
              ('love yourself', 'positive'),
              ('listen to Inspirational and motivational stories', 'positive'),
              ('Live out of imagination not history', 'positive'),
              ('I admire courage and loyalty', 'positive'),
              ('you have reached the summit', 'positive'),
              ('my best wishes always with you', 'positive'),
			  ('secure freedom relaxation vacation', 'positive'),
			  ('famous economical determined sagacious', 'positive'),
			  ('credible didactic trust fame proud', 'positive'),
			  ('elegant beautiful attractive graceful handsome robust', 'positive'),
			  ('strong virile pretty ', 'positive'),
			  ('Learned Astute Observant', 'positive'),
			  ('ability helpful altruist popular people donate donation', 'positive'),
			  ('acced major beauty ', 'positive'),
			  ('You the champion', 'positive'),
			  ('summit appreciare honour proud happy', 'positive'),
			  ('laugh smile support winner prime humorous active', 'positive')]
			  
neg_tweets = [('I do not like   car', 'negative'),
              ('  view is horrible', 'negative'),
              ('I feel tired   morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('  band is awful', 'negative'),
              ('  is terrible', 'negative'),
              ('They make me feel bad', 'negative'),
              ('  band not that great', 'negative'),
              ('  is absolutely atrocious', 'negative'),
              ('I dislike them', 'negative'),
              ('  band the worst', 'negative'),
              ('What the hell is   crap', 'negative'),
              ('  band should die', 'negative'),
              ('I hate   band', 'negative'),
              ('  band make me want to die', 'negative'),
              ('My ears dying', 'negative'),
              ('They suck they terrible', 'negative'),
              ('In a closed mouth flies do not enter', 'negative'),
              ('it shits me', 'negative'),
              ('my poor little angel', 'negative'),
              ('teddy in the case BITCHES', 'negative'),
			  ('abysmal adverse alarming angry annoy anxious apathy appalling atrocious awful', 'negative'),
  			  ('bad banal barbed belligerent bemoan beneath boring broken', 'negative'),
			  ('callous clumsy coarse cold collapse confused contradictory contrary corrosive corrupt crazy creepy criminal cruel cry cutting', 'negative'),
			  ('dead decaying damage damaging dastardly deplorable depressed deprived deformed deny despicable detrimental dirty', 'negative'),
			  ('disease disgusting disheveled dishonest dishonorable dismal distress dreadful dreary', 'negative'),
			  ('enraged eroding evil fail faulty fear feeble fight filthy foul frighten frightful', 'negative'),
			  ('gawky ghastly grave greed grim grimace gross grotesque gruesome guilty', 'negative'),
			  ('haggard hard hard-hearted harmful hate hideous homely horrendous horrible hostile hurt hurtful', 'negative'),
			  ('icky ignore ignorant ill immature imperfect impossible inane inelegant  infernal injure', 'negative'),
			  ('injurious insane insidious insipid jealous junky lose lousy lumpy', 'negative'),
			  ('malicious mean menacing messy misshapen missing misunderstood moan moldy monstrous', 'negative'),
			  ('naive nasty naughty negate negative never nobody nondescript nonsense  noxious', 'negative'),
			  ('objectionable odious offensive oppressive', 'negative'),
			  ('pain perturb pessimistic petty plain poisonous poor prejudice', 'negative'),
			  ('questionable quirky quit reject renege repellant reptilian', 'negative'),
			  ('repulsive repugnant revenge revolting rocky rotten rude ruthless', 'negative'),
			  ('sad savage scare scary scream severe shoddy shocking sick sickening sinister slimy smelly', 'negative'),
			  ('sobbing sorry spiteful sticky stinky stormy stressful stuck stupid substandard suspect suspicious', 'negative'),
			  ('tense terrible terrifying threatening', 'negative'),
			  ('ugly undermine unfair unfavorable unhappy unhealthy unjust unlucky unpleasant upset unsatisfactory', 'negative'),
			  ('unsightly untoward unwanted unwelcome unwholesome unwieldy unwise upset', 'negative'),
			  ('vice vicious vile villainous vindictive', 'negative'),
			  ('wary weary wicked woeful worthless wound yell yucky zero', 'negative'),
              ('Even if hopeless at resisting temptations, not doomed to fail at self-control', 'negative'),
              ('In a world full of choice, we live in a world full of regret', 'negative'),
              ('Even if you\'re hopeless at resisting temptations, you\'re not doomed to fail at self-control', 'negative'),
              ('I bet get bullied a lot', 'negative'),
              ('I don\'t even like we can stop pretending to be friends now', 'negative'),
              ('Acting like a slut does not make cute', 'negative'),
              ('If guys do not want me to be mean to you', 'negative'),
              ('DO NOT REALIZE WE ALL WANT TO MURDER RIGHT NOW', 'negative'),
              ('I mean   in the best way possible, but I legitimately can not stand you', 'negative'),
              ('You probably get left when go out with friends because they all hate you', 'negative'),
              ('You not as bad as people say.  much worse', 'negative'),
              ('Please keep talking  Yawning means we interested abhor abdicate abandon', 'negative'),
              ('I don\'t get bitter just better', 'negative'),
              ('I have looked every where but I just can\'t find anyone who cares', 'negative'),
              ('Is that meant to hurt my feelings better try harder next time', 'negative'),
              ('I may look calm but in my head I have killed three times', 'negative'),
              ('You only young once but will be immature forever', 'negative'),
              ('If going to be two faced at least make one of them pretty', 'negative'),
              ('Im glad to see not letting education get in the way of ignorance', 'negative'),
              ('I see looking my direction, going to envy my perfection', 'negative'),
              ('I don\'t know what is making so dumb, but it is working', 'negative'),
              ('People like make people like me look even better', 'negative'),
              ('Maybe should eat some make up so can be pretty on the inside because it is just NOT working out on the outside', 'negative'),
              ('Such a shame when a skinny body is wasted on an ugly face', 'negative'),
              ('we all actually hate you', 'negative'),
              ('You have butt cheeks out in OHill', 'negative'),
              ('Who in their right mind would go near those teeth', 'negative'),
              ('I really can not think straight I am worse off than a goldfish I need to get tested   is bad', 'negative'),
              ('REALLY bad headache   morning', 'negative'),
              ('Join our dog days of summer sale', 'negative'),
              ('we finally no longer at the top of the list of social media screw-ups', 'negative'),
              ('I\'ve heard of getting screwed by an airline but   is ridiculous', 'negative'),
              ('Just be thankful it wasn\'t a model', 'negative'),
              ('we\'re sorry to hear that did not have a good trip, Mr. Armstrong', 'negative'),
              ('we take these tweets very seriously. IP address and details will be forwarded to security and the FBI', 'negative'),
              ('We apologize for an inappropriate image shared in one of our responses. We’ve removed the tweet', 'negative'),
              ('hell with the social media intern yelled I\'ll show how to dominate the news cycle', 'negative'),
              ('I always get stuck sitting near a crying baby', 'negative'),
              ('I\'m so sorry I\'m scared now', 'negative'),
              ('I\'m just a fangirl pls I don\'t have evil thoughts and plus I\'m a white girl', 'negative'),
              ('stocks falling', 'negative'),
              ('He is my enemy', 'negative'),
			  ('Bigoted Stupid mushy dirt arrogant','negative')]

tweets = []

for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))
	
#!/usr/bin/python   
print('Content-type: text/html\r\n\r')
	
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
	all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    #wordss = nltk.tokenize.word_tokenize(wordlist)
    #wordlist = nltk.FreqDist(wordss)
    word_features = wordlist.keys()
    return word_features


word_features  = get_word_features(get_words_in_tweets(tweets))
print (word_features )



def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
	features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

x=1
old=0
count_tweet = 0
positive=0
negative = 0
irrelevant = 0

while x==1:
	fo=open('final.csv', 'rb') 
		
	fo.seek(old)
		
	for line in fo:
		#print line
		count_tweet = count_tweet + 1
		tweet = line+""
		if classifier.classify(extract_features(tweet.split()))+"" == "positive" :
			print ("positive")
			positive = positive + 1
		elif classifier.classify(extract_features(tweet.split()))+"" == "negative" :
			print("negative")
			negative = negative + 1
		else:
			print("irrelevant")
			irrelevant = irrelevant + 1
		if count_tweet == 10 :
			time.sleep(3)
			count_tweet = 0
			mydbs = MySQLdb.connect(host='localhost',user='root',passwd='',db='mydb')
			cursor = mydbs.cursor()
			cursor.execute('''INSERT into mydb_table (pos, neg, irr) values (%s, %s, %s)''',(positive, negative, irrelevant))
			#close the connection to the database.
			mydbs.commit()
			cursor.close()
			#import os
			print ("Positive : "+str(positive)+" Negative : "+str(negative))
			
		old=fo.tell()
			
	time.sleep(0.5)
		
	fo.close()
mydbs.close()
