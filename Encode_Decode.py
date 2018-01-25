"""
Script Name : Encode_Decode.py
Version     : 1.0.0
Description : Encoding/decoding functionality
Compatible  : 2.7x
"""

__author__ = 'Amahapa'

# Global Variables
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3


def encode_(message):
    """
    Function Name : encode_
    Parameters    : str
    Return Value  : str
    Purpose       : To encode a given string
    Description   : every Character in the string is read and is checked against
                    alphabet variable. When found, the character is changed to a character
                    <key> places forward. If the character goes out of bound, it is restarted
                    at the first character
    """
    encoded_msg = ''
    for character in message:
        position = alphabet.find(character)
        new_pos = (position + key) % 26
        new_char = alphabet[new_pos]
        encoded_msg += new_char
    return encoded_msg


def decode_(message):
    """
    Function Name : decode_
    Parameters    : str
    Return Value  : str
    Purpose       : To decode a given encoded string
    Description   : Every Character in the string is read and is checked against
                    alphabet variable. When found, the character is changed to a character
                    <key> places backward. If the character goes out of bound, it is restarted
                    at the last character
    """
    decoded_msg = ''
    for character in message:
        position = alphabet.find(character)
        new_pos = (position - key) % 26
        new_char = alphabet[new_pos]
        decoded_msg += new_char
    return decoded_msg
