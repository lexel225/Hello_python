def set_test():
    listA = [1,1,2,2]
    tupleB = ('a','b','b','c')

    print("listA =", listA)
    print("tupleB =", tupleB)

    # define set
    setA = set(listA)
    setB = set(tupleB)
    setC = set() # empty set

    print("setA =", setA)
    print("setB =", setB)
    print("setC =", setC)

    # add
    setB.add(1)
    print("setB.add(1) =", setB)

    # discard
    setB.discard('b')
    print("setB.discard('b') =", setB)

    # remove
    setB.remove('c')
    print("setB.remove('c') =", setB) # if 'c' not found, exception will raise

    # pop
    print("setB.pop() =", setB.pop()) # randomly pop an element
    print("setB =", setB)

    # set operation
    setD = set([2,3])
    print("setA =", setA)
    print("setD =", setD)
    print("setA & setD =", setA & setD)
    print("setA | setD =", setA | setD)
    print("setA - setD =", setA - setD)
    print("setD - setA =", setD - setA)
    print("setA ^ setD =", setA ^ setD)

    return