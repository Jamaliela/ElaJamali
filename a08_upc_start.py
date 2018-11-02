######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
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


def is_valid_input(barcode):
    if int(len(barcode)) == 12:
        return True
    else:
        return False


def is_valid_modulo(barcode):
    odd_numbers = list(barcode)
    odd_numbers.remove = barcode[1]
    odd_numbers.re = barcode[2]
    odd_numbers.append = barcode[4]
    odd_numbers.append = barcode[6]
    odd_numbers.append = barcode[8]
    odd_numbers.append = barcode[10]

    return odd_numbers


def translate(barcode_num, side):

    return ""


def main():
    input_code = input("Enter a 12 digit code [0-9]: ")
    # while not is_valid_input(input_code):
    #     input_code = input("Invalid number. Enter a 12 digit code [0-9]: ")
    is_valid_modulo(input_code)

    # if is_valid_modulo(input_code):
    #     print(input_code)
    # #     # TODO turtle draw code
    # #     pass
    # # else:
    # #     # TODO turtle draw error message
    # #     pass


if __name__ == "__main__":
    main()
