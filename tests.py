import utils
import sys

def unit_test(expected, actual):
    if expected != actual:
        print("Failed")
        sys.exit()
    else:
        print("Passed")
        
unit_test(True, utils.is_ipv4_address("111.111.111.111"))
unit_test(True, utils.is_ipv4_address("1.1.1.1"))
unit_test(True, utils.is_ipv4_address("11.1.111.11"))
unit_test(True, utils.is_ipv4_address("198.243.13.0"))
unit_test(True, utils.is_ipv4_address("31.0.13.45"))

unit_test(False, utils.is_ipv4_address("111.111"))
unit_test(False, utils.is_ipv4_address("1.1.1.-1"))
unit_test(False, utils.is_ipv4_address("test"))
unit_test(False, utils.is_ipv4_address(""))
unit_test(False, utils.is_ipv4_address("31.0.13.."))

