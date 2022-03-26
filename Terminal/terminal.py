# import libraries
import subprocess
import platform
import os
import socket
import time
from cryptography.fernet import Fernet
# Frist Assigments
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
# Prints

# Functions

# Main Section of Terminal
while True:
    code = input(">>> ")
    if code == 'ping':
        host = input("Enter The Host Name / IP / Website: ")
        number = input("Enter How Many Times To Ping?")
        def ping(host):
            param = "-n" if platform.system().lower() == 'windows' else '-C'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'local':
        print("Your Local IP Is {} .".format(host_ip))
        print("Your Desktop Name Is {} .".format(host_name))
    if code == 'encrypt -str':
        mes = input("Enter Your Text: ").encode()
        # mes2 = bytes(mes)
        def write_key():
            key = Fernet.generate_key()
            with open("key.txt", "wb") as key_file:
                key_file.write(key)
        def load_key():
            """
            Loads the key from the current directory named `key.txt`
            """
            return open("key.txt", "rb").read()
        key = write_key()
        key = load_key()
        f = Fernet(key)
        encrypted = f.encrypt(mes)
        print("Your Encrypted Text is: {}".format(encrypted))
        print("Your Key Was Saved in your selected Folder Don't Share IT !!")
        # decrypted_encrypted = f.decrypt(encrypted)
        # print("Your Decrypted Text is: {}".format(decrypted_encrypted))
    if code == 'decrypt -str':
        mes2 = input("Enter Your Key: ").encode()
        decrypted = f.decrypt(mes2)
        print(decrypted)