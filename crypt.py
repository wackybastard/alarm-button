import pyAesCrypt
import io
import os

def decrypt(path, password):

    buffer_size = 1024 * 1024

    bytes_stream = io.BytesIO()

    with open(path, 'rb', buffer_size) as file:
        crypted_stream = io.BytesIO(file.read())
        pyAesCrypt.decryptStream(crypted_stream, bytes_stream, password, buffer_size, len(crypted_stream.getvalue()))

    with open(path, 'wb', buffer_size) as file:
        file.write(bytes_stream.getvalue())

    print('[Decrypted] ' + path)

    del password

def crypt(path, password):

    buffer_size = 1024 * 1024

    bytes_stream = io.BytesIO()

    with open(path, 'rb', buffer_size) as file:
        decrypted_stream = io.BytesIO(file.read())
        pyAesCrypt.encryptStream(decrypted_stream, bytes_stream, password, buffer_size)
        del decrypted_stream

    with open(path, 'wb', buffer_size) as file:
        file.write(bytes_stream.getvalue())

    print('[Crypted] ' + path)

    del password


def walk(directory, password, func):

    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        if os.path.isfile(path):
            func(path, password)
        else:
            walk(path, password, func)


if __name__ == '__main__':
    directory = input('d: ')
    password = input('p: ')

    walk(directory, password, decrypt)
    print('decrypted successfully')
