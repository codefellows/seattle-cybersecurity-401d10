#!/usr/bin/env python3

# Script:         Ops 401 Class 2 Demo
# Purpose:        Work with DatTime
# Why:            Prep for Ops Challenge

# DONE: Practice Creating a Function, calling the function, and passing a variable to the function.

def my_function(my_list = [6, 7, 8, 9, 10]):
    for number in my_list:
        print(number)

# DONE: Set an Optional Argument List for the function

    # DONE: Loop through the Argument List

# DONE: Using the library datetime, print out the current date and time

import datetime

now  = datetime.datetime.now()
print(now)

# DONE: Using the library datetime, override the existing date

new_date = datetime.date(1996, 12, 11)
print(new_date)

# DONE: Using the time module, print out the current time

import time

time_now = time.time()
print(time_now)

# DONE: Using the time module, pause the script for 5 seconds

time.sleep(5)
print('Did I spee for 5 seconds')

# DONE: Using the OS module, ping the localhost 2 times

import os

result = os.system('ping localhost -c 2')


# if __name__ == "__main__":
#     my_variable = [1, 2, 3, 4, 5]
#     my_function(my_variable)
#     my_function()
