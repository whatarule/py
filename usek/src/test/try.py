
print()

try:
    a = 10/0
    print("{0}".format(a))
except ValueError as e:
    print("{0}".format(e))
# except ZeroDivisionError:
except ZeroDivisionError as e:
#   print("ZeroDivisionError")
    print("type: {0}".format(type(e)))
    print("args: {0}".format(e.args))
#   print("message: {0}".format(e.message))
    print("{0}".format(e))

print()

try:
    f = open(file_name,'w')
    data = dict_input['data']
    f.write(data)
    f.close()
except KeyError as e:
    print("{0}".format(e))
except (FileNotFoundError, TypeError) as e:
    print("{0}".format(e))
except:
    print("{0}".format("Unexpected error"))

print()

try:
#   a = 10/0
    a = 10/1
    print("{0}".format(a))
except ZeroDivisionError as e:
    print("{0}".format(e))
else:
    print("else statement")
finally:
    print("finally statement")

print()

try:
    raise NameError("Hi")
except NameError as e:
    print("{0}".format(e))
    raise

print()

