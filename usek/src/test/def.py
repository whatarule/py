
# def leapYear(year):
def leapYear(year=2400):
    if ( year % 100 != 0 and year % 4 == 0 ) or year % 400 == 0 :
        leap = True
    else:
        leap = False
    print("{0} = {1}".format(
            year,leap
        ))
    return leap

leapYear(2017)
leapYear(2016)
leapYear(2000)
leapYear()


def spam(*args):
    print("{0}".format(args))

def spamd(**args):
    print("{0}".format(args))

spam(1,2,3)
spamd(a=1,b=2,c=3)

