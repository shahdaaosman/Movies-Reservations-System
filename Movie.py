'''
Name: Shahd Osman
Email: shahdo@bu.edu
Class: MET CS 521 O1 Information Structures with Python
Date: 6/20/2018
Assignment: 6
Problem: 7.3
Description: this code represent a Movie class.
'''
class Movie:
     
    def __init__(self, id= 0 , name =None , genre =None , storyline=None, showtimes= None):
        """Description: this function construct an Account objects
        :input param : id is  intger
        :input param : name , genre and storyline are string
		:input param : showtimes is a list of strings
        :return: N/A
        """
        self.__id = id
        self.name = name
        self.__genre = genre
        self.__storyline = storyline
        self.__showtimes = showtimes

    def getId(self):
        """This function return the user id"""
        return self.__id

    def setId(self, id):
        """This function change the movie Id"""
        self.__id = id
		
    def getName(self):
        """This function return the movie Name"""
        return self.name

    def setName(self, name):
        """This function change the movie Name"""
        self.name = name

    def getGenre(self):
        """This function return the movie Genre"""
        return self.__genre 
		
    def setGenre(self, genre):
        """This  function change the movie Genre"""
        self.__genre = genre

    def getStoryline(self):
        """This function return the movie Storyline"""
        return self.__storyline 
		
    def setStoryline(self, storyline):
        """This  function change the movie Storyline"""
        self.__storyline = storyline
		
    def getShowtimes(self):
        """This function return the movie Showtime"""
        return self.__showtimes

    def setShowtimes(self,showtimes):
        """This function change the movie Showtime"""
        self.__showtimes = showtimes

    def __str__():
        """This function return string represent the class"""
        return "\nMovie : " + self.name + " ( " +self.__genre +" )"\
		+"\nIt storyline is :"+ self.__storyline +"\n Showstime : " + self.__showtimes


