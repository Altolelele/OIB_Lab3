import json
import os
from encryption import encryption
from generation import generation, encryption_sym_key
from decryption import decryption

if __name__ == '__main__':
    settings = {
        'initial_file': 'initial_file.txt',
        'encrypted_file': 'encrypted_file.pickle',
        'decrypted_file': 'decrypted_file.txt',
        'symmetric_key': 'symmetric_key.txt',
        'public_key': 'public_key.pem',
        'private_key': 'private_key.pem',
    }
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)
    with open('settings.json') as json_file:
        json_data = json.load(json_file)

    while True:
        print("1. 64 бит")
        print("2. 128 бит")
        print("3. 192 бит")
        print("0. Выйти из программы")
        cmd = input("Выберите длину ключа: ")
        if cmd == "1":
            print("Генерируем ключи шифрования...")
            generation(settings, 8)
            encryption_sym_key(settings)
            iv = os.urandom(8)
            print("Шифруем...")
            encryption(settings, iv)
            print("Дешифруем...")
            decryption(settings, iv)
            print("Готово!")
            break
        elif cmd == "2":
            print("Генерируем ключи шифрования...")
            generation(settings, 16)
            encryption_sym_key(settings)
            iv = os.urandom(8)
            print("Шифруем...")
            encryption(settings, iv)
            print("Дешифруем...")
            decryption(settings, iv)
            print("Готово!")
            break
        elif cmd == "3":
            print("Генерируем ключи шифрования...")
            generation(settings, 24)
            encryption_sym_key(settings)
            iv = os.urandom(8)
            print("Шифруем...")
            encryption(settings, iv)
            print("Дешифруем...")
            decryption(settings, iv)
            print("Готово!")
            break
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")

