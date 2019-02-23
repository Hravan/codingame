#Binary with 0 and 1 is good, but binary with only 0, or almost, is even better! Originally, this is a concept designed by Chuck Norris to send so called unary messages.
#
#Write a program that takes an incoming message as input and displays as output the message encoded using Chuck Norris’ method.

#Here is the encoding principle:
#
#    The input message consists of ASCII characters (7-bit)
#    The encoded output message consists of blocks of 0
#    A block is separated from another block by a space
#    Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
#    - First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
#    - Second block: the number of 0 in this block is the number of bits in the series

from itertools import takewhile

def encode_to_unary(message):
    '''
       str -> str
       Consume a message and return its unary representation.
    '''
    binary_message = asci_to_binary(message)

    unary_list = []
    while binary_message:
        # take n first elements that are equal to the first element
        to_process = list(takewhile(lambda x: x == binary_message[0], binary_message))

        n_chars = len(to_process)

        if to_process[0] == '1':
            unary_list.append('0 ' + '0' * n_chars)
        else:
            unary_list.append('00 ' + '0' * n_chars)

        binary_message = binary_message[n_chars:]

    unary_message = ' '.join(unary_list)

    return unary_message

def asci_to_binary(text):
    '''
       str -> str
       Consume an ASCII string and return binary representation of its characters
       as a string.
    '''
    #encoded_text = ''.join(map(lambda x: x[2:], map(bin, bytearray(text, encoding='ascii'))))
    encoded_text = ''.join([bin(ord(x))[2:].zfill(7) for x in text])

    return encoded_text
