# This program will generate a random password
# from curses.ascii import isdigit
from random import randrange


# generates random characters
def rolldice(length, count):
    for i in range(count):
        for j in range(length):
            print(chr(randrange(ord("!"), ord("~"))), end="")

        print("")


def getquestion(text):
    ans = ""
    while not ans.isdigit():
        ans = input(text)

    ans = eval(ans)
    if ans == 0:
        quit()
    return ans


# ask user to gen new password
def quest():
    getlength = getquestion("what is length?: ")
    getcount = getquestion("what is count?: ")
    print("")
    return getlength, getcount


def main():
    length, count = quest()
    rolldice(length, count)


main()
