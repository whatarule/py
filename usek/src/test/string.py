
def inStr(char,str):
    print(char in str)


if __name__=="__main__":

    print()

    inStr("a","abc")
    inStr("d","abc")
    inStr("d","abc"+"d")

    print()

    print(int("10")+20)
    print(str(10)+"20")
    print("a"*3)
    print("abcde"[0:3])

    print()


def enmLs(ls):
    for i in enumerate(ls):
        print("{0}".format(i))
    else:
        print("done")
    print()
    for i,v in enumerate(ls):
        print("{0}={1}".format(i,v))
    print("done")
    print()

def whLs(ls):
    i = 0
    while i < 2:
        print("{0}".format(ls[i]))
        i = i + 1
    else:
        print("done")
    print()


if __name__=="__main__":

    enmLs("abc")
    whLs("abc")

    print()

