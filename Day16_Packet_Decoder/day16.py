# 3 bits "version"
# 3 bits "type id"

# if type id == 4, it is a "literal value". Literal value packets encode a single binary number.
# To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits,
# and then it is broken into groups of four bits. (ACTUALLY FIVE)
# Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit.

# literal packets don't contain other packets

# every other type id than 4 is an "operator"
# operator package contains one or more packages


def prepare_BITS(hex_input):
    """Converts hexadecimal input to binary number where length is a multiple of four bits.
    Adds leading zeroes until length is a multiple of four bits.
    """
    binary_string = str(bin(int(hex_input, 16))[2:])
    length = len(binary_string)
    modulo = length % 4
    if modulo != 0:
        binary_string = "0" * modulo + binary_string
    return binary_string


def bin_to_int(bin_input: str) -> int:
    return int(bin_input, 2)


def parse_version(packet: str) -> int:
    return bin_to_int(packet[:3])


def parse_type(packet: str) -> int:
    return bin_to_int(packet[3:6])


def return_literal(packet:str) -> (int, int):
    # returns version and length as tuple
    assert parse_type(packet) == 4
    len_pointer = 6
    add = 5
    while True:
        next_slice = packet[len_pointer:len_pointer+add]
        len_pointer += add
        if next_slice[0] == '0':
            break
    return parse_version(packet), len_pointer

def is_operator(packet: str) -> bool:
    if parse_type(packet) != 4:
        return True
    return False

def return_operator_packets(packet: str):
    assert is_operator(packet)
    length_type_id = packet[6]
    assert length_type_id in ["0", "1"]
    if length_type_id == "0":
        temp = packet[7:22]
        assert len(temp) == 15
        sub_packets_len = bin_to_int(temp)
        print(sub_packets_len)
    else:
        temp = packet[7:18]
        assert len(temp) == 11
        sub_packets_number = bin_to_int(temp)
        print(sub_packets_number)

def test():
    assert prepare_BITS("38006F45291200") == "00111000000000000110111101000101001010010001001000000000"
    assert prepare_BITS("D2FE28") == "110100101111111000101000"

    assert bin_to_int("100") == 4

    assert parse_version("110100101111111000101000") == 6
    assert parse_version("00111000000000000110111101000101001010010001001000000000") == 1

    assert parse_type("110100101111111000101000") == 4
    assert parse_type("11101110000000001101010000001100100000100011000001100000") == 3

    assert return_literal("110100101111111000101000") == (6, 21)
    assert return_literal("11010001010") == (6, 11)
    assert return_literal("01010010001001000000000") == (2, 16)

    assert not is_operator("01010010001001000000000")
    assert is_operator("00111000000000000110111101000101001010010001001000000000")

    #return_operator_packets("00111000000000000110111101000101001010010001001000000000")
    return_operator_packets("00111000000000000110111101000101001010010001001000000000")

if __name__ == '__main__':
    # with open("day16.dat", 'r') as f:
    #     input_data = f.readline()
    # print(to_bin(input_data))
    test()
