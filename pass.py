import random
from tkinter import *



lower = "abcdefghijklmnopqrstuwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "!@#$%^&*()_+"

jam = lower + upper + num + symbol

leng = int(input("len of your password: "))

password = "".join(random.sample(jam,leng))

print(password)

