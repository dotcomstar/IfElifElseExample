#!/usr/bin/env python
import os
import sys

def main():
    print("Starting main()\n")
    take_personality_test(109)
    take_personality_test(0)
    take_personality_test(-9230)
    print("\nFinishing main()")

# This function will take in your favorite number, then print out which Jonas brother you.
def take_personality_test(number):
    if number < 0:
        message = "You are Nick Jonas."
    elif number > 0:
        message = "You are Joe Jonas."
    else:  # Number equals 0
        message = "You are Kevin Jonas."
    print(message)

# ~~~~ Don't worry about this for now ~~~~
if __name__ == "__main__":
    main()
