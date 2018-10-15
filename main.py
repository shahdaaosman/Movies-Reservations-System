'''
Name: Shahd Osman
Email: shahdo@bu.edu
Class: MET CS 521 O1 Information Structures with Python
Date: 6/23/2018
Assignment: Final Project
Description: Movies Tickets System
'''
import sys

from Ticket import Ticket
from Movie import Movie
from Order  import Order 

"""Movies Data """
movie1 = Movie(1,"Incredibles 2","Science fiction film/Action",\
              "Everyone’s favorite family of superheroes is back\
			  in Incredibles but this time Helen is in the\
			  spotlight, leaving Bob (voice of Craig T. Nelson)\
			  at home with Violet (voice of Sarah Vowell) and Dash\
			  to navigate the day-to-day heroics of normal life.\
			  Ita's a tough transistion for everyone, made tougher\
			  by the fact that the family is still unaware of baby\
			  Jack-Jack's emerging superpowers. When a new villain\
			  hatches a brilliant and dangerous plot, the family \
			  and Frozone (voice of Samuel L. Jackson) must find\
			  a way to work together againa' which is easier said\
			  than done, even when they're all Incredible.",\
		   ["Mon,June 25, 5:30pm","Tue,June 26 7:15pm"]) 
movie2 = Movie(2,"TAG","Comedy","One month every year,\
                five highly competitive friends hit the \
				ground running for a no-holds-barred game\
				of tag -- risking their necks, their jobs\
				and their relationships to take one another \
				down. This time, the game coincides with the\
				wedding of the only undefeated player. What\
				should be an easy target soon becomes an all-out\
				war as he knows they're coming to get him."\
				,["Wed,June 27, 5:30pm","Fri,June 29 8:15pm"]) 
movie3 = Movie(3,"Ocean's 8","Crime","Five years, eight months,\
                12 days and counting -- that's how long Debbie\
				Ocean has been devising the biggest heist of her \
				life. She knows what it's going to take -- a team \
				of the best people in the field, starting with her\
				partner-in-crime Lou Miller. Together, they recruit\
				a crew of specialists, including jeweler Amita, \
				street con Constance, suburban mom Tammy, hacker \
				Nine Ball, and fashion designer Rose. Their target\
				-- a necklace that's worth more than $150 million.",\
		  ["Sat,June 30, 5:30pm","Sun,July 1 3:15pm"]) 
movie4 = Movie(4,"Hereditary","Drama/Mystery",\
             "When Ellen passes away, her daughter's family begins\
			 to unravel cryptic and increasingly terrifying secrets\
			 about their ancestry. The more they discover, the more \
			 they find themselves trying to outrun the sinister fate\
			 they seem to have inherited"\
		   ,["Mon,June 25, 5:30pm","Tue,June 26 7:15pm"]) 
movie5 = Movie(5,"SuperFly 2","Action/Adventure",\
               "Cocaine kingpin Youngblood Priest realizes that \
			   it's time to get out of the game after surviving\
			   a violent attack from a crazed rival. Hoping for\
			   one last score, Priest and his partner travel to\
			   Mexico to arrange a deal. The career criminal now \
			   finds himself trying to outmaneuver the cartel,\
			   two corrupt police officers and all the\
			   double-crossers that threaten his path to freedom."\
			,["Mon,June 25, 5:30pm","Tue,June 26 7:15pm"]) 


movies= {1:movie1, 2:movie2 ,3:movie3,4:movie4,5:movie5}



def displyMoveis():
    """Description: this function Display Movie Menu
    """
    print("\n n  | Movies title")
    print("-"*50)
    for key in movies:
        print ("\n",key," : ",movies[key].getName(), "("\
		,movies[key].getGenre(),")")
    print("-"*50)
    print("\n Which movie would you like to watch?")


	
def choseMovie() :
    """Description: this function ask the user ti chose a movie
    :return: movie number : int
    """
	
    while True:
        try:
           # Prompt the user to enter an account Id :
            movie_number = int(input("\nEnter a movie number:"))
	
        except:
            assert False, 'Please try again and enter an Integer number.'

        # Check if the movie number is valid
        if movie_number not in movies:
            print("\n Please Try again and select a movie number\
		   from the menu")
            continue
        break
    return movie_number

def movieMenue(movie_number):
    """Description: this function disply a choises to a user
    :input param : movie number  integer
    """
    #movieMenu
    while True:
        print ("\n *****{:}*****".format(movies[movie_number].getName()))
        print("\nPlease Select from the from the following menu!")
        print(""" 
           \n 1: Movie storyline
           \n 2: Movie showtimes
           \n 3: Ticket Booking
           \n 4: Return to main menu""")
        try:
            # Prompt the user to chose from menu list :
            movieChoice = int(input("\nEnter a number:"))
	
        except:
            assert False, 'Please try again and enter an Integer number.'

	    # check the user choice
        if movieChoice == 1 :
            print("\n Movie Story :", movies[movie_number].getStoryline())
            continue
        elif movieChoice == 2 :
            n=choseShowtime()
            continue
        elif movieChoice == 3 :
            total=bookTikets()
            out=checkOut()
            if out == 0 :
                break
            else :
                #get the order detail
                print ("Your order detail : ")
                print ("-"*50)
                getorder()
                print("Thanks for your parches ")
                print ("-"*50)
                continue
			
        elif movieChoice == 4 :
            break
			
        else :
            print("\n Please Try again and select a number from the menu")
            continue
        break

def choseShowtime():
    """Description: this function display movie times
    :return: time_number int
    """    
    while True:
		
        # Movies time menu	
        for i in range(len(movies[movie_number].getShowtimes())):
            print ("\n",i+1," : ",movies[movie_number].getShowtimes()[i])		

        try:
            # Prompt the user to enter a movi time 
            time_number = int(input("\n Chose a movie time :"))
			
        except:
            assert False, 'Please try again and enter an Integer number.'

		# Check if the time number is valid
        if time_number not in range(1,3):
            print("\n Please Try again and select a movie Time "
	          "number from the menu")
            continue
        break
    return time_number

def bookTikets():
    """Description: this function let the user to chose 
    tickets count then print the total price
    :return total price
    """    
    while True:
		
        # Ticket type menu		

        try:
            # Prompt the user to enter Adult Ticket number :
            adultTicket = int(input("\nHow many Adult ticket do you want:"))
			
        except :
            assert False, 'Please try again and enter an Integer number.'

		# Check if the ticket number is valid
        if adultTicket > 10 :
            print("\n The maximum Tikcket you can buy is 10")
            continue		

			
        try:
            # Prompt the user to enter Child Ticket number :
            childTicket = int(input("\nHow many child ticket do you want:"))
			
        except :
            assert False, 'Please try again and enter an Integer number.'

		# Check if the ticket number is valid
        if childTicket > 10 :
            print("\n The maximum Tikcket you can buy is 10")
            continue
			
        try:
            # Prompt the user to enter Senior Ticket number :
            seniorTicket = int(input("\nHow many Senior ticket do you want:"))
			
        except :
            assert False, 'Please try again and enter an Integer number.'

		# Check if the ticket number is valid
        if seniorTicket > 10 :
            print("\n The maximum Tikcket you can buy is 10")
            continue	

        # call the Ticket class		
        ticket = Ticket(adultTicket,childTicket,seniorTicket)	
        total= ticket.getTotalCost()
 
        print ("-"*50)
        print("\n Total Ticket price is {:,.2f}".format(total))
			
        break
    return total 

def checkOut():
    """Description: this function ask the user to checkout
    :return: checkout value 0 or 1
    """    
    while True :
        try:
            # Prompt the user to enter a movi time 
            checkout = int(input("\n Do you want to check out "
	                         "enter '1 for Yes' or '0 for No' :"))
			
        except:
            assert False, 'Please try again and enter an Integer number.'

        # Check if the time number is valid
        if checkout not in range (2):
            print("\n Please Try again and enter 0 or 1")
            continue
        break
    return checkout
	
def getorder():
    """
    this function get the user id and return his 
    booking detail
    """
    pass

if __name__ == '__main__':
    
	# Print welcome massege
    print("-"*50)
    print("| Welcome to the Cinema Ticket Purchasing System |")
    print("-"*50)
			
    while True:

        #Menu
        print("\nPlease Select from the from the following menu!")
        print(""" 
           \n 1: Available Movies
           \n 2: Tickets Prices
           \n 3: Check Reservation
           \n 4: Exit""")
		   
        try:
            # Prompt the user to chose from menu list :
            choice = int(input("\nEnter a number:"))
	
        except:
            assert False, 'Please try again and enter an Integer number.'

		# check the user choice
        if choice == 1 :
		    # Display moveis menue
            displyMoveis()
            movie_number=choseMovie()
            movieMenue(movie_number)
            continue
			
        elif choice == 2 :
		
            # call Ticket class
            ticketPrice = Ticket()
			# Display tickets
            print ("\n ",ticketPrice.__str__())
            continue
		
        elif choice == 3 :
		    # Show booking details
            getorder()
            continue
			
        elif choice == 4 :
		    #Exit
            print("\nThank you")
            sys.exit()	
        else :
            print("\n Please Try again and select a number from the menu")
            continue
		
        break
			