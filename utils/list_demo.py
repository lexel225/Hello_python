
def list_test():
    # index
    listA = [1,2,'a','b']
    print('listA =', listA)
    print("listA[2] = ", listA[2])
    print("listA[-1] = ", listA[-1])
    print("listA.index(2) = ", listA.index(2))
    print("listA.index('b') = ", listA.index('b'))

    # extend
    listA = [1,2,'a','b']
    print('listA =', listA)

    listB = [3,4]
    print('listB =', listB)

    listA.extend(listB)
    print('listA.extend(listB) =', listA)

    # append
    listA = [1,2,'a','b']
    print('listA =', listA)

    listB = [3,4]
    print('listB =', listB)

    listA.append(listB)
    print('listA.extend(listB) =', listA)

    # for x in Y
    print("for item in listA")
    for item in listA:
        print(item)

    # length
    print("len(listA) =", len(listA))

    # pop
    print('listA =', listA)
    print("listA.pop() =", listA.pop())
    print('listA =', listA)
    return