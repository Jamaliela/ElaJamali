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
import turtle

def is_valid_input(barcode):
    if int(len(barcode)) == 12:
        return True
    else:
        return False


def is_valid_modulo(barcode):
    oddnumbers = []
    for i in range(0,len(barcode),2):
        oddnumbers.append(barcode[i])
    print(oddnumbers)
    oddnumber_sum = sum(map(int,oddnumbers))
    oddbythree = int(oddnumber_sum) * 3

    evennumbers = []
    for i in range(1,len(barcode),2):
        evennumbers.append(barcode[i])
    evennumbers = evennumbers[:-1]
    print(evennumbers)
    evennumber_sum = sum(map(int,evennumbers))
    final = oddbythree + evennumber_sum
    final = final % 10
    if final is not 0:
        checkdigit = 10 - final
    else:
        checkdigit = final
    print(checkdigit)

def translate(barcode):

    leftside = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    rightside = ['1110010','1100110','1101100','1000010','1011100','1001110','1010000','1000100','1001000','1110100']
    barcode = list(barcode)
    leftl = []
    for i in barcode[0:6]:
        lf = leftside[int(i)]
        leftl.append(lf)
    print(leftl)

    rights = []
    for i in barcode[6:12]:
        rs = rightside[int(i)]
        rights.append(rs)
    print(rights)

def drawing_blackline(t):
    t.pencolor("black")
    t.left(90)
    t.forward(500)
    t.penup()
    t.backward(500)
    t.forward(20)


def main():
    input_code = input("Enter a 12 digit code [0-9]: ")
    while not is_valid_input(input_code):
         input_code = input("Invalid number. Enter a 12 digit code [0-9]: ")

    list(input_code)
    if is_valid_modulo(input_code):
        print(input_code)
        # TODO turtle draw code
    t = turtle.Turtle
    wn = turtle.Screen()
    translate(input_code)
    drawing_blackline(t)

    #
    #     pass
    # else:
    #     # TODO turtle draw error message
    #     pass
    #

    wn.exitonclick()

if __name__ == "__main__":
    main()
