import datetime
import time

from bs4 import BeautifulSoup

#Class to define a RSS post in Python...
class Post:

	#Post class constructor
	def __init__(self, title, description, link, author, date, category, content):
		self.__title = title										#Initialisation of '__title' attribute
		self.__description = description								#Initialisation of '__description' attribute
		self.__link = link										#Initialisation of '__link' attribute
		self.__author = author										#Initialisation of '__author' attribute
		self.__content = content									#Initialisation of '__content' attribute

		provisional_time = datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")			#Conversion of the received date as string to datetime...
		self.__date = provisional_time.timestamp()							#Initialisation of '__date' attribute (as timestamp)

		self.__category = category									#Initialisation of '__category' attribute

	#'__title' attribute getter
	def getTitle(self):
		return self.__title

	#'__description' attribute getter
	def getDescription(self):
		return self.__description

	#'__author' attribute getter
	def getAuthor(self):
		return self.__author

	#'__date' attribute getter
	def getDate(self):
		return self.__date

	#'__category' attribute getter
	def getCategory(self):
		return self.__category

	#'__content' attribute getter
	def getContent(self):
		return self.__content

	#'__link' attribute getter
	def getLink(self):
		return self.__link

	#Post's image getter from '__content' attribute
	def getImage(self):
		post_image = ""
		soup = BeautifulSoup(self.__content, 'html.parser')

		for imgtag in soup.find_all('img'):
			post_image = imgtag['src']

		return post_image
