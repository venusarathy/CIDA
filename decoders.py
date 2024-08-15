import base64
import binascii
import codecs

# Hex to Text (ASCII)
def hex_to_text(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

# Decimal to Text (ASCII)
def decimal_to_text(decimal_str):
    chars = [chr(int(d)) for d in decimal_str.split()]
    return ''.join(chars)

# Octal to Text (ASCII)
def octal_to_text(octal_str):
    chars = [chr(int(o, 8)) for o in octal_str.split()]
    return ''.join(chars)

# Base64 to Text (ASCII)
def base64_to_text(base64_str):
    return base64.b64decode(base64_str).decode('utf-8')

# ROT13 to Text
def rot13_to_text(rot13_str):
    return codecs.decode(rot13_str, 'rot_13')

# Caesar Cipher (Shift by 3 for now) #Yet implement to bruteforce caesar 
def caesar_to_text(caesar_str):
    shifted_chars = [(ord(char) - 3) if 'D' <= char <= 'Z' or 'd' <= char <= 'z' else ord(char) + 23 for char in caesar_str]
    return ''.join([chr(char) for char in shifted_chars])

