import base64
import argparse
from Crypto.Cipher import AES


def decrypt(encrypted):
    key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
    aes = AES.new(key, AES.MODE_CBC, b'\00' * 16)
    return aes.decrypt(base64.b64decode(encrypted)).strip().decode()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypted', help='encrypted password.')
    args = parser.parse_args()
    print(f'> password : {decrypt(args.encrypted)}')
