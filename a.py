from tkinter import *
import random

#=====================================METHODS===================================
def Random():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = 8
    new_password = ""

    for i in range(length):
        next_index = random.randrange(len(alphabet))
        new_password = new_password + alphabet[next_index]


    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(new_password)//2)
        new_password = new_password[0:replace_index] + str(random.randrange(10)) + new_password[replace_index+1:]


    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(new_password)//2,len(new_password))
        new_password = new_password[0:replace_index] + new_password[replace_index].upper() + new_password[replace_index+1:]

    PASSWORD.set(new_password);


#=====================================MAIN======================================
root = Tk()
root.title("Sourcesoft")
width = 400
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
