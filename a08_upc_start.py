######################################################################
# Author: Dr. Scott Heggen       Emely Alfaro, Elaheh Jamali
# Username: heggens              alfarozavalae, jamalie
#
# Assignment: A08: UPC Barcodes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle                       # importing the turtle library

def is_valid_input(barcode):
    """
    This function verifies if the barcode is 12 digits and if they are all positive numbers.
    :param barcode:  parameter that takes the user's input to check if it is a valid 12 digit or not
    :return: Fruitful. a True or False Boolean value.
    """
    if int(len(barcode)) == 12:     # checks the user's input to see if it is a valid 12 digit barcode
        return True                 # true when the barcode is 12 digits
    else:
        return False                # returns false when it is not 12 digits input


def is_valid_modulo(barcode):
    """

    :param barcode: takes the user's input and does several operations to the odd and even positions with the module check character method.
    :return: checkdigit (the variable that should match the last digit of the barcode
    """
    oddnumbers = []                             # creating new list
    for i in range(0,len(barcode),2):           # creating for loop to go through the elements in the barcode starting from the first one (odd) and skipping every other one
        oddnumbers.append(barcode[i])           # appending into the oddnumbers list each of the elements retrieved in the for loop
    print(oddnumbers)
    oddnumber_sum = sum(map(int,oddnumbers))    # adding all the elements in the list created and using map to make them integers
    oddbythree = int(oddnumber_sum) * 3         # multiplying the oddnumber_sum by three as one of the steps in module check character

    evennumbers = []                            # creates new empty list for even numbers
    for i in range(1,len(barcode),2):           # for loop to start in the first even element of the barcode and skipping every other one
        evennumbers.append(barcode[i])          # appending the retrieved even numbers into the empty list
    evennumbers = evennumbers[:-1]              # taking out the last even number (module check character)
    print(evennumbers)
    evennumber_sum = sum(map(int,evennumbers))  # adding all the even numbers after changing them into integers.
    final = oddbythree + evennumber_sum         # adding the result from odd numbers and even numbers to get to the final step
    final = final % 10                          # checking if the final number is divisible by 10 with modulus
    if final is not 0:                          # if function to check if the final digit is not zero
        checkdigit = 10 - final                 # subtracting 10 from the final one when the final is not zero
    else:
        checkdigit = final                      # if there's no remainder in modulus of final % 10 the final value stays the same
    return checkdigit                           # returning the checkdigit value


def translate(barcode):
    """
    This function will translate the barcode into binary numbers so that we can draw the turtle by using the turtle module
    :param barcode: taking the barcode from the user's input
    :return: Fruitful. returns leftl and rights values of the lists lefside and rightside
    """
    leftside = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']  # creating a list with all the elemnets from the left side table.
    rightside = ['1110010','1100110','1101100','1000010','1011100','1001110','1010000','1000100','1001000','1110100']          # # creating a list with all the elemnets from the right side table.
    centerside = ['']
    barcode = list(barcode)                     # making the barcode a list
    leftl = []                                  # creating an empty list to go through the first 6 elements of barcode
    for i in barcode[0:6]:                      # for loop to run in the first 6 elements
        lf = leftside[int(i)]                   # getting the first six elements of the list
        leftl.append(lf)                        # appending the first 6 elements into the leftl variable

    rights = []                                 # creating an empty list to go through the remainder 6 elements of barcode
    for i in barcode[6:12]:                     # for loop to run in the remainder 6 elements
        rs = rightside[int(i)]                  # getting the first six elements of the list
        rights.append(rs)                       # appending the first 6 elements into the leftl variable
    return leftl, rights                        # returning both leftl and rights to use them in main for drawing


def drawing_blackline(t):
    """

    :param t: turtle object that will draw the black lines in the barcode
    :return: None. Void
    """
    t.color("black")                            # setting the color of the turtle to be black
    t.begin_fill()                              # beginning to fill with the turtle
    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(200)                          # turtle t goes forward 200 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace


def drawing_blackline_long(t):
    """

    :param t: turtle object that will draw the black lines in the barcode for guard and center
    :return: None. Void
    """
    t.color("black")                            # setting the color of the turtle to be black
    # t.right(250)
    # t.forward(248)
    # t.left(90)
    # beginning to fill with the turtle
    t.begin_fill()
    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(240)                          # turtle t goes forward 200 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace



def drawing_white_line(t):
    """

    :param t: turtle object t to draw the while lines.
    :return: none. Void function .
    """
    t.color("white")                            # setting the color of the turtle to be black
    t.begin_fill()                              # beginning to fill with the turtle
    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(200)                          # turtle t goes forward 200 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace


def drawing_white_line_long(t):
    """

    :param t: turtle object t to draw the while lines for guard and center
    :return: none. Void function .
    """
    t.color("white")                            # setting the color of the turtle to be black
                                  # beginning to fill with the turtle
    t.begin_fill()
    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(240)                          # turtle t goes forward 200 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace

def main():
    """

    :return: main function where the user is asked for a barcode and list is created to run the other functions that check characters in barcode
    """
    input_code = input("Enter a 12 digit code [0-9]: ")                         # asking user for input of barcode
    while not is_valid_input(input_code):                                       # while loop to check if it is valid
         input_code = input("Invalid number. Enter a 12 digit code [0-9]: ")    # asking user to input a valid barcode again
    list(input_code)                                                            # making the barcode a list
    if is_valid_modulo(input_code):            # if function run the module check character in the barcode
        print(input_code)
        # TODO turtle draw code
    t = turtle.Turtle()                         # creating the turtle
    t.hideturtle()                              # hiding turtle to move its position
    wn = turtle.Screen()                        # setting up the turtle screen
    t.penup()                                   # putting the pen up to start moving
    t.setpos(-250, -100)                        # setting the left side position
    t.speed(0)                                  # setting up speed to go faster
    left, right = translate(input_code)         # calling the two return variables from the translate function

    # t.penup()                                   # putting the pen up to start moving
    # t.setpos(-270, -100)                        # setting the left side position
    # t.color("black")
    # t.pensize(20)
    # t.write(input_code[0], move=False, align="center", font=("Arial", 15, "normal"))

    guard_left = ["1", "0", "1"]
    for i in guard_left:
        if i == "0":
            drawing_white_line_long(t)
        else:
            drawing_blackline_long(t)

    t.penup()                                   # putting the pen up to start moving
    t.setpos(-240, -60)                        # setting the left side position

    for i in range(len(left)):                  # for loop to run in the len of the first 6 elements retrieved for the left side
        for j in left[i]:                       # nested for loop to run in the first 6-digit binary element inside the left side list
            if j == "0":                        # if the element is zero then
                drawing_white_line(t)           # a white line is drawn
            else:
                drawing_blackline(t)            # if it is anything else a black line is drawn


    t.penup()                                   # putting the pen up to start moving
    t.setpos(-150, -100)                        # setting the left side position

    guard_center = ["0", "1", "0", "1","0"]
    for i in guard_center:
        if i == "0":
            drawing_white_line_long(t)
        else:
            drawing_blackline_long(t)

    t.penup()                                   # putting the pen up to start moving
    t.setpos(-140, -60)                        # setting the left side position

    for i in range(len(right)):                 # for loop # for loop to run in the len of the first 6 elements retrieved for the center side
        for j in right[i]:                      # nested for loop to run in the first 6-digit binary element inside the center side list
            print(j)                            # if the element is zero then
            if j == "0":                        # if the element is zero then
                drawing_white_line(t)           # a white line is drawn
            else:
                drawing_blackline(t)            # if it is anything else a black line is drawn

    t.penup()                                   # putting the pen up to start moving
    t.setpos(-60, -100)                        # setting the left side position

    guard_center = ["1", "0", "1"]
    for i in guard_center:
        if i == "0":
            drawing_white_line_long(t)
        else:
            drawing_blackline_long(t)


    # writing bar code
    # t.penup()                                   # putting the pen up to start moving
    # t.setpos(-270, -100)                        # setting the left side position
    # t.color("black")
    # t.pensize(20)
    # t.write(input_code, move=False, align="center", font=("Arial", 15, "normal"))

    #     pass
    # else:
    #     # TODO turtle draw error message
    #     pass
    #

    wn.exitonclick()

if __name__ == "__main__":
    main()
