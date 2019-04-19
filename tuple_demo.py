def tuple_test():
    tupleA = (1,2,'a','b')
    print("tupleA =", tupleA)

    # index
    print("tupleA[2] =", tupleA[2])
    print("tupleA[-1] =", tupleA[-1])
    
    # slice
    print("tupleA[1:3:1]", tupleA[1:3:1])
    print("tupleA[0:4:2]", tupleA[0:4:2])
    print("tupleA[:2]", tupleA[:2])
    print("tupleA[::2]", tupleA[::2])

    # for
    print("item in tupleA")
    for item in tupleA:
        print(item)

    # check if item in tuple
    print("'a' in tupleA: ", 'a' in tupleA)

    print("for index, item in enumerate(tupleA)")
    for index, item in enumerate(tupleA):
        print("%i,%s" % (index, item))

    return