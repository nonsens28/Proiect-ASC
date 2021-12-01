import sys
import os.path


def decrypt(key, text):
    text = "".join(map(chr, text))
    plaintext = []
    for i in range(len(text)):
        plaintext.append((ord(key[i % len(key)]) ^ ord(text[i])))
    return plaintext


def main():
    args = sys.argv
    input_path = args[1]
    key = args[2]
    output_path = args[3]
    if not os.path.exists(input_path):
        exit(-1)
    file = open(input_path, 'rb')
    output_file = open(output_path, 'w')
    text = file.read()
    output_file.write("".join(map(chr, decrypt(key, text))))


if __name__ == '__main__':
    main()
