import colorama
import datetime
from colorama import Fore, Style
from sys import stdout


def log_company(msg):
    stdout.write(f"{Fore.LIGHTBLUE_EX} [{msg}]")


def log_time():
    stdout.write(f"{Fore.WHITE}{datetime.datetime.now()}")


def log_item(msg):
    stdout.write(f"{Fore.WHITE} {msg} ")


def log_stock(inStock):
    logcolor = Fore.GREEN if inStock else Fore.RED
    logText = "IN STOCK" if inStock else "Out Of Stock"
    stdout.write(f"{logcolor}[{logText}]")


