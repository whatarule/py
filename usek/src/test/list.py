
# result = []
# for i in range(1,5):
#     result.append(i**2)
# result = [x**2 for x in [1,2,3,4,5]]
# result = [x**2 for x in range(1,5)]

# result = []
# for x in range(1,5):
#     if x > 2 and x < 5:
#         result.append(x**2)
result = [
    x**2 for x in range(1,5)
    if x > 2 and x < 5
    ]

print("{0}".format(result))

print("{0}".format({
        x**2 for x in range(1,5)
        if x > 2 and x < 5
    }))

print("{0}".format({
        str(x):x**2 for x in range(1,5)
    }))

