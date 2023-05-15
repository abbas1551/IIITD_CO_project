import reader

def dec_to_bin(dec_str):
    dec_str = int(dec_str[1:])
    binary = bin(dec_str)[2:]
    binary = binary.zfill(7)
    return binary

def gen_address(count):
    address = bin(count)[2:]
    address = address.zfill(7)
    return address


