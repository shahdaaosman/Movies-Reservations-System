'''
Name: Shahd Osman
Email: shahdo@bu.edu
Class: MET CS 521 O1 Information Structures with Python
Date: 6/20/2018
Assignment: 6
Problem: 7.3
Description: this code represent a Ticket class.
'''
class Ticket:
     
    def __init__(self, adultTicketCount=0, childTicketCount=0, seniorTicketCount=0):
        """Description: this function construct an Account objects
        :input param : adultTicketCount , childTicketCount and seniorTicketCount are integers		
        :return: N/A
        """
		
        self.__adultTicketCount = adultTicketCount
        self.__childTicketCount = childTicketCount
        self.__seniorTicketCount = seniorTicketCount

    def getAdultTicketCount(self):
        """This function return the ticket count"""
        return self.__adultTicketCount

    def setAdultTicketCount(self, adultTicketCount):
        """This function change the ticket count"""
        self.__adultTicketCount = adultTicketCount

    def getChildTicketCount(self):
        """This function return the ticket count"""
        return self.__childTicketCount

    def setChildTicketCount(self, childTicketCount):
        """This function change the ticket count"""
        self.__childTicketCount = childTicketCount

    def getSeniorTicketCount(self):
        """This function return the ticket count"""
        return self.__seniorTicketCount

    def setSeniorTicketCount(self, seniorTicketCount):
        """This function change the ticket count"""
        self.__seniorTicketCount = seniorTicketCount
		

    def getAdultTicketPrice(self):
        """This function return the ticket price"""
        return self.__adultTicketCount * 10

    def getChildTiketsPrice(self ):
        """This function returns the Ticket  Price"""
        return self.__childTicketCount  * 5	

    def getSeniorTiketsPrice(self ):
        """This function returns the Ticket  Price"""
        return self.__seniorTicketCount  * 7	
			
    def getTotalCost(self):	
	    return self.__adultTicketCount * 10 + self.__childTicketCount  * 5\
		+ self.__seniorTicketCount  * 7
	
    def __repr__(self):
	    return "\n Tickets Prices "+ "\n Adult : $10.00 "+"\n Child : $5.00 "\
		+"\n Senior : $7.00 "
	
