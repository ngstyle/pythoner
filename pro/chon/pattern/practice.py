import re

def is_valid_email(addr):
    addr_pattern = re.compile(r'[a-zA-Z0-9\.]+@[a-zA-z]+\.com')
    if addr_pattern.match(addr):
        return True
    else:
        return False


print(is_valid_email('bill.gates@microsoft.com'))


def name_of_email(addr):
    addr_pattern = re.compile(r'(\<?([a-zA-Z]+\.?\s?[a-zA-Z]*)\>?\s?[a-zA-Z]*)@([a-zA-z]+)[\.com|\.org]')
    return addr_pattern.match(addr).groups()


print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))