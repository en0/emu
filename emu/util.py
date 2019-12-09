def itoh(value, width=4):
    return '0x' + hex(value)[2:].zfill(width)

def itob(value, width=16):
    return '0b' + bin(value)[2:].zfill(width)

def check_flag(flag: int, value: int):
    return (value & flag) == flag

def mask_off(mask: int, value: int):
    return mask & value
