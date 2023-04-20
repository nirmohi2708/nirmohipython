# WAP to check if a given key already exists in a dictionary.

v = {7:27, 1: 8, 7: 3, 9: 10, 34: 43}


def is_key_present(x):

    if x in v:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
is_key_present(2)


