import feedparser
import sys
import urllib
import threading
from post import Post

#Class to define a RSS Feed in Python...
class Feed:

	#Feed class constructor
	def __init__(self, feedUrl, feedName):

		self.__feedURL = feedUrl					#Initialisation of '__feedURL' attribute
		self.__feedName = feedName					#Initialisation of '__feedName' attribute
		self.__postsArray = []						#Initialisation of '__postArray' attribute (an array which will contain all posts from this specific feed)

		#Try this code block...
		try:

			#Instruction to parse feed received from the URL and to extract all of its datas
			rss_datas = feedparser.parse(self.__feedURL)

			#For loop to browse the array containing all RSS posts
			for entity in rss_datas['entries']:

				#Adding the newly post to the '__postsArray' attribute
				self.__postsArray.append(Post(entity["title"], entity["description"], entity["link"], entity['author'], entity['published'], entity['category'], entity["content"][0].value))

		#If an HTTP error occurs then...
		except urllib.error.HTTPError as err:

			#Error display
			print("Error occured: " + str(err))

		#If a URL error occurs then...
		except urllib.error.URLError as err:

			#Error display
			print("Error occured: " + str(err))

	#Feed class destructor
	def __del__(self):

		print("Object's destruction")

	#'__feedURL' attribute getter
	def getFeedUrl(self):

		return self.__feedURL

	#'__feedName' attribute getter
	def getFeedName(self):

		return self.__feedName

	#'__postsArray' attribute getter
	def getPostsArray(self):

		return self.__postsArray

	#
	def updateCountDown(self):

		threading.Timer(15, self.updateCountDown).start()

		self.__postsArray = []

		rss_datas = feedparser.parse(self.__feedUrl)

		for entity in rss_datas['entries']:

			self.__postsArray.append(Post(entity["title"], entity["description"], entity['author'], entity['published'], entity['category']))

			# ecriture du fichier JSON

		#
		print("Renouvellement....")
