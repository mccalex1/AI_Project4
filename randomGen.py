import random
import sys

def main():
    file = open("newTextFile.txt", 'w')
    i = 0
    min = -1000
    max = 1000
    while i < 1000:

        file.write(str(random.randint(min, max)) + " " + str(random.randint(min, max)) + "\n")
        i += 1

    file.close()
main()
