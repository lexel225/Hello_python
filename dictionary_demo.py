def dictionary_test():
    dictA = {'name' : 'lexel',
                'age' : 18,
                'number' : '0926'
                }

    print("dictA", dictA)

    # check
    print("dictA['name'] =", dictA['name'])

    # Add
    dictA['gender'] = 'M'
    print("dictA", dictA)

    # delete
    del dictA['age']
    print("dictA", dictA)

    # clear
    dictA.clear()
    print("dictA", dictA)

    return