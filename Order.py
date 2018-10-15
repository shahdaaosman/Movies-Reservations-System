'''
Name: Shahd Osman
Email: shahdo@bu.edu
Class: MET CS 521 O1 Information Structures with Python
Date: 6/20/2018
Assignment: 6
Problem: 7.3
Description: this code represent an Order class.
'''
class Order:
     
    def __init__(self, orderNumber= 0 , ticketNumTotal = 0 , total= 0.00):
        """Description: this function construct an Account objects
        :input param : orderNumber is intger
        :input param : ticketNumTotal is integer
		:input param : total is float	
        :return: N/A
        """
        self.__orderNumber = orderNumber
        self.__ticketNumTotal = ticketNumTotal
        self.__total = total

    def getOrderNumber(self):
        """This function return the user orderNumber"""
        return self.__orderNumber

    def setOrderNumber(self, orderNumber):
        """This function change the user orderNumber"""
        self.__orderNumber = orderNumber
		
    def getTicketNumTotal(self):
        """This function return the user ticketNumTotal"""
        return self.__ticketNumTotal

    def setticketNumTotal(self, balance):
        """This function change the user ticketNumTotal"""
        self.__ticketNumTotal = ticketNumTotal
		
    def getTotal(self):
        """This function return the total"""
        return self.__total

    def setTotal(self, total):
        """This function change the total"""
        self.__total = total

    def __str__(self):
	    return " "


