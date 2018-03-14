######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: A7: UPC Bar Codes
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



def is_valid_input(barcode):

    return True


def is_valid_modulo(barcode):

    return True


def translate(barcode_num, side):

    return ""


def main():
    input_code = input("Enter a 12 digit code [0-9]: ")
    while not is_valid_input(input_code):
        input_code = input("Invalid number. Enter a 12 digit code [0-9]: ")

    if is_valid_modulo(input_code):
        # TODO turtle draw code
        pass
    else:
        # TODO turtle draw error message
        pass


if __name__ == "__main__":
    main()
