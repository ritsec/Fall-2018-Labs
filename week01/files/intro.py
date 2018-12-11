#!/usr/bin/env python3
#
# Intro to linux script!
# This is awful code, I know.  If you want, make a better one and send it to
# me, because that would be cool :)!
#
# Author: Scott Brink
#

import sys
import os
from subprocess import check_output

def ls():
    print("\nTo exit at any point, type ctrl+c\n")
    print("First, let me introduce you to the shell!\nThis is the command line in linux that let's you run commands, it's a very powerful tool.\n\nThe first command to learn is \"ls\", which will list the current files within your directory.")
    while True:
        try: 
            cmd = input("Enter the command \'ls\' to continiue: ")
            if cmd != "ls":
                print("\nType \'ls\'.")
            else:
                print("")
                print(check_output("ls").decode())
                return
        except KeyboardInterrupt:
            exit()

def lsla():
    print("You can also add arguments to your commands!\nTry typing \"ls -la\"")
    while True:
        try:
            cmd = input("Enter the command \'ls -la\' to continue: ")
            if cmd != "ls -la" and cmd != "ls -al":
                print("\nType \'ls -la\'.")
            else:
                print("")
                print(check_output(["ls", "-la"]).decode())
                print("This is using two flags, -a and -l.\n-a shows hidden files, while -l shows more information about a file in a long listing format.")
                return
        except KeyboardInterrupt:
            exit()

def pwd_cd():
    print("Now, time to figure out where we are!")
    while True:
        try:
            cmd = input("Enter the command \"pwd\": ")
            if cmd != "pwd":
                print("\nType \"pwd\"")
            else:
                print("")
                print(check_output(["pwd"]).decode())
                print("This command means print working directory, which prints the directory you are currently working in.")
                break
        except KeyboardInterrupt:
            exit()
    
    print("We are in your home directory now, denoted by \'/home/ritsec\'")
    while True:
        try:
            cmd = input("Enter the command \"cd /\": ")
            if cmd != "cd /":
                print("\nType \"cd /\"")
            else:
                print("")

                # I know this isn't actually running the command, but it works.
                os.chdir("/")
                break

        except KeyboardInterrupt:
            exit()

    print("We have now gone to the base directory of our virtual machine!  Type pwd to see that we are actually there!")
    while True:
        try:
            cmd = input("Enter the command \"pwd\": ")
            if cmd != "pwd":
                print("\nType \"pwd\"")
            else:
                print("")
                print(check_output(["pwd"]).decode())
                break
        except KeyboardInterrupt:
            exit()
    print("And now we want to jump back to our home directory, so we can now type\"cd\" with no arguments to get to the home directory of the user we are currently logged in as.")
            
    while True:
        try:
            cmd = input("Enter the command \"cd\": ")
            if cmd != "cd":
                print("\nType \"cd\"")
            else:

                # don't @ me
                os.chdir("/home/ritsec/")

                print("\nCool!  We are now back in our home directory, the directory that contained file.txt!")
                break

        except KeyboardInterrupt:
            exit()
    return

def cat():
   print("Final thing!  Let's read this file by using \"cat file.txt\"\n")
   while True:
        try:
            cmd = input("Enter the command \"cat file.txt\": ")
            if cmd != "cat file.txt":
                print("\nType \"cat file.txt\"")
            else:
                print(check_output(["cat","file.txt"]).decode())
                break
        except KeyboardInterrupt:
            exit()
   return
 
def exit():
    print("\nGood luck out there!  Feel free to ask for help from anyone!\n")
    sys.exit()

def main():
    ls()
    lsla()
    pwd_cd()
    cat()

if __name__ == '__main__':
    main()
