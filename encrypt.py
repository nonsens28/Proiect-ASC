import sys
import os.path


def encrypt(key, text):
    cipher = []
    for i in range(len(text)):
        cipher.append((ord(key[i % len(key)]) ^ ord(text[i])))
    return cipher


def main():
    args = sys.argv
    input_path = args[1]
    key = args[2]
    output_path = args[3]
    if not os.path.exists(input_path):
        exit(-1)
    file = open(input_path, 'r')
    output_file = open(output_path, 'wb')
    text = file.read()
    output_file.write(bytearray(encrypt(key, text)))


if __name__ == '__main__':
    main()
