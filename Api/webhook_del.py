import os
import requests
import colorama
from dhooks import Webhook
import time

os.system("title Lofy Webhook Deleter")

def banner():
    print(f"""{colorama.Fore.MAGENTA}

     
      █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▓█████▄ ▓█████  ██▓    ▓█████▄▄▄█████▓▓█████ 
     ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██▀ ██▌▓█   ▀ ▓██▒    ▓█   ▀▓  ██▒ ▓▒▓█   ▀ 
     ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ░██   █▌▒███   ▒██░    ▒███  ▒ ▓██░ ▒░▒███   
     ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░▓█▄   ▌▒▓█  ▄ ▒██░    ▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄ 
     ░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ░▒████▓ ░▒████▒░██████▒░▒████▒ ▒██▒ ░ ░▒████▒
     ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒    ▒▒▓  ▒ ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░
       ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░    ░ ▒  ▒  ░ ░  ░░ ░ ▒  ░ ░ ░  ░   ░     ░ ░  ░
       ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░     ░ ░  ░    ░     ░ ░      ░    ░         ░   
         ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░         ░       ░  ░    ░  ░   ░  ░           ░  ░
                           ░                                      ░                                           
     

     /Webhook delete

     """)

def nuker():
    start = input("     [>] Link da Webhook:")
    hook = Webhook(start)
    x = requests.delete(start)

def end():
    print("     Webhook Deletada")
    print("     [>]Saindo...")
    time.sleep(10)
    os.system("exit")


banner()
nuker()
end()