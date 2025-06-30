import time
import os
import random


def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')


def show_bars(arr):
    for number in arr:
        bar_line = "█" * (number // 2)  
        print(f"{number:3} | {bar_line}")
    print() 


# to continue