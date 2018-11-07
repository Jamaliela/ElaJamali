from a08_upc_start import *
import sys

def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def a08_test_suite():

    # The following tests test the is_valid_input() function
    print("Testing is_valid_input()")

    testit(is_valid_input("123456789123") == True)
    testit(is_valid_input("123") == False)


    # The following tests test the is_valid_module() function
    print("\nTesting is_valid_modulo()")

    testit(is_valid_modulo("311917045597") == 7)
    testit(is_valid_modulo("044000036935") == 5)
    testit(is_valid_modulo("722868906224") == 4)


    # The following tests test the translate() function
    print("\nTesting translate()")

    testit(translate("311917045597") == (['0111101','0011001','0011001','0001011','0011001','0111011'],['1110010','1011100','1001110','1001110','1110100','1000100']))
    testit(translate("044000036935") == (['0001101','0100011','0100011','0001101','0001101','0001101'],['1110010','1000010','1010000','1110100','1000010','1001110']))
    testit(translate("722868906224") == (['0111011','0010011','0010011','0110111','0101111','0110111'],['1110100','1110010','1010000','1101100','1101100','1011100']))


a08_test_suite()
