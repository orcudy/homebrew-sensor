import re

def int_to_bool(num):
    if (num == 0):
        return False
    return True

def is_ipv4_address(string):
    decimals = string.split('.')
    if len(decimals) != 4:
        return False
    for number in decimals:
        if number > 255 or 0 >= number:
            return False
    return True

def is_domain_name(string):
    if re.match("^[0-9a-zA-Z][0-9a-zA-Z_]*[0-9a-zA-Z].[a-zA-Z]{2,}", string):
        return True
    return False

def is_valid_port(port):
    max_valid_port = 2 ** 16 - 1
    min_valid_port = 2 ** 10
    if port > max_valid_port or min_valid_port >= port:
        return False
    return True
