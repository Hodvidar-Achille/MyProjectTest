def is_no_common_letters(word1, word2):
    for i in word1:
        for j in word2:
            if i == j:
                return True

    return False


def do(h1, h2, v1, v2):
    counter = 0

    # check is for h1 there are letters of v1 and v2 that are fitty
    if is_no_common_letters(h1, v2) \
            or is_no_common_letters(h1, v2) \
            or is_no_common_letters(h2, v1) \
            or is_no_common_letters(h2, v2):
        return counter

    if counter == 1:
        pass

    return counter


horizontal_1 = "OTTO"
horizontal_2 = "OXXO"
vertical_1 = "OCCO"
vertical_2 = "OZZO"

"""
    OTTO    
    C  Z    
    C  Z    
    OXXO    

    --> counter == 4
"""
print(do(horizontal_1, horizontal_2, vertical_1, vertical_2))
