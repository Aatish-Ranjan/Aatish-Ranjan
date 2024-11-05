def dict_to_string(D:dict) -> str:
    '''
    Convert the given dictionary back to the string format produced by `Dict_fromString`. Again, do not use loops or conditionals, use comprehensions.

    '''

    result='\n'.join([f'''{k},{v}''' for k, v in D.items()])
    return result

D={'aatish': 26, 'bantu': 25, 'simant': 26, 'malli': 32}
print(dict_to_string(D))