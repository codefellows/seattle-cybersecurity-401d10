#!/usr/bin/python3
# Author: Marco Vazquez

# Import libraries

from sys import platform
import os, time, datetime, hashlib
from time import sleep
import math

# Variables

my_os = platform


# Functions

# Handles linux search
def linuxSearch():
    filename = input("Please enter the filename you want to search for:")
    filepath = input("Please enter the directory you want to search in:")
    print("Please wait while we search...")
    sleep(1)

    # Count and print the number of files searched
    os.system("ls " + str(filepath) + " | echo \"$(wc -l) files searched.\"")

    # Count and print the number of files discovered
    os.system("find " + str(filepath) + ' -name ' + str(filename) + " -print | echo \"Found $(grep -c /) files that matched:\"")
    os.system("find " + str(filepath) + ' -name ' + str(filename))

# Handles windows search
def windowsSearch():
    filename = input("Please enter the filename you want to search for:")
    filepath = input("Please enter the directory you want to search in:")
    print("Please wait while we search...")
    sleep(1)

    # count the number of files searched and store number in a variable
    searchCount = os.popen("dir /a:-d /s /b " + str(filepath) + " | find /c \":\\\"").read()
    print("Files searched: " + searchCount)

    # count the number of files found and store number in variable
    foundCount = os.popen("dir /b/s " + str(filepath) + " | find /c \":\\\"").read()
    print("Files found: "+ foundCount)
    os.popen("dir /b/s " + str(filepath) + "\\" + str(filename))

# Handle the OS check
def os_check():
    print("Let's check your system's OS")
    sleep(1)

    print("Your system is running " + my_os)
    sleep(1)
    print("Now that we know which OS you're running, let's scan your system")
    sleep(1)

    # Call the correct function depending on the OS
    if my_os == "linux":
        linuxSearch()
    elif my_os == "win32" or "win64":
        windowsSearch()

# Timestamp function
def currenttime():
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H-%M-%S')

# Hashing function - This function returns the hash of the file passed into it
def hash_file(filename):

    # Make a hash object
    h = hashlib.md5()

    # open up a file for reading in binary
    with open(filename, 'rb') as file:

        # loop until the end of the file
        chunk = 0
        while chunk != b'':
            #read in 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()

# Hash getter - os.walk to crawl through directories and display hash of all files
def hash_getter():

    print("Taking a look at the hashes of all the files in a given directory")
    sleep(1)

    # Initiate some variables
    dir_count = 0
    file_count = 0
    start_path = input("Please enter the absolute path to the directory you want to get the file hashes in:")
    for (path,dirs,files) in os.walk(start_path):
        print('DIRECTORY: {:s}'.format(path))
        print("")
        dir_count += 1

        # Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path,file))

            # Convert the file sizes to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            file_count += 1
            filename = os.path.join(path,file)
            md5 = hash_file(filename)
            timestamp = currenttime()
            print(timestamp)
            print(f"FILENAME: {file}\tSIZE: {str(fsize) + unit}\tPATH: {filename}")
            print("Virus scan using VirusTotal:")
            malwareCheck(md5)
            print("HASH: " + md5 + "\n")

# Print total files and directory count
    print('Summary: hashed {} files in {} directories'.format(file_count,dir_count))
    dir_count = 0
    file_count = 0

# Malware check function
def malwareCheck(the_hash):
    apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set the ENV variable

    query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + the_hash

    os.system(query)

# Main Menu

print("Malware Analysis and Removal Tool")
sleep(1)
print("What do you want the tool to do?")
if __name__ == "__main__": # when I run this file.. do this stuff
    while True:
        mode = input("""
        Options:
        1 - Check OS, Search for file
        2 - Get File Hashes for all files in a folder
        3 - Exit
        Please enter a number:
                      """)
        if (mode == "1"):
            os_check()
            #print("Option 1")
        elif (mode == "2"):
            hash_getter()
            #print("Option 2")
        elif (mode == "3"):
            break
        else:
            print("Invalid Selection...")
