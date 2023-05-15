import reader
def dec_to_bin(dec_str):
    dec_str = int(dec_str[1:])
    binary = bin(dec_str)[2:]
    binary = binary.zfill(7)
    return binary
