#Real time analyis of Twitter feed based on Twitter Streaming API (Python (nltk, tweepy, webbrowser, MySQLdb))

Steps to setup and run the Real-time Tweets Analyzer (built in 2014)

1)Download and install Python 2.7. Add the path of the installation directory to the Path variable in Environment Variables under Control Panel > System > Advanced System Settings

2)Install setup tools Python Package Index from python.org

3)Have a Twitter account ready. Make an application on dev.twitter.com and obtain the 4 keys, viz. Consumer Key, Consumer Secret, API Key, API Secret required for authorization.

4)Install Tweepy API for Twitter Streaming API from dev.twitter.com

5)Put the files project.py and extractingtweets.py into the Python directory.

6)Open two separate command line windows and go to the Python directory.

7)Run the extractingtweets.py as 
>python extractingtweets.py

8)Run the project.py as 
>python project.py

9)The window running extractingtweets.py will show the live stram of tweets which will also be stored in a csv file and the one running project.py will show the analysis of the tweets as positive or negative cumulatively after 10 tweets as they come.

Thank you for using our application.
