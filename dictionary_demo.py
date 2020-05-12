def dictionary_test():
    dict_A = {'name' : 'lexel',
                'age' : 18,
                'number' : '0926'
                }

    print("dict_A", dict_A)

    # check
    print("dict_A['name'] =", dict_A['name'])

    # Add
    dict_A['gender'] = 'M'
    print("dict_A", dict_A)

    # delete
    del dict_A['age']
    print("dict_A", dict_A)

    # clear
    dict_A.clear()
    print("dict_A", dict_A)
