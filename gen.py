import random
import string
import time

d = "abcdefghijklmnopqrstuvwxyz1234567890"


def main ():

    letters = string.ascii_lowercase 
    gen =( f''.join(random.choice(d) for i in range(4)))

    filename = "userlist.txt"
    myfile = open(filename, 'a')
    myfile.write(gen + "\n")
    myfile.close()

    time.sleep(0)
    main()

main()