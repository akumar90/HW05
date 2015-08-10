#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

from sys import exit

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """

    usrInput = raw_input("Enter the number to be determined even or odd")

    try :

        if(not(int(usrInput) == float(usrInput))):
            raise ValueError

        elif (int(usrInput) % 2 == 0):
            print ("Even number entered")

        else :
            print ("Odd number entered")


    except ValueError as ve:
        print ("Incorrect value entered. Exiting the program")
        sys.exit()


    return None

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    
    for i in range(0,10):
        for j in range (0,11):
            print str(i*10 + j) + "\t",

        print 


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    
    """
    sum = 0
    count = 0
    while True:

        usrInput = raw_input("Enter a number : ")

        if(usrInput.lower() == "done"):

            if(count !=0):
                return float(sum)/count

            else :
                return "No numbers entered"

        sum += int(usrInput)
        count += 1



##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    ten_by_ten()
    print repr(find_average())

if __name__ == '__main__':
    main()
