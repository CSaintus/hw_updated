# both the space and the time complexity are linear due to the fact the length stays the same, it dosen't grow in length 

def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            position = ord(char.upper()) - ord('A') + 1
            result.append(str(position))
    
    return ' '.join(result)



# The time complexity of this function is linear, but the space complexity is constant cause the function uses a sigle variable.

def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result    


# The time complexity of this function is linear, but the space complexity is constant cause the function uses a constant additional space.

def xo(s):
    count_x = s.lower().count('x')
    count_o = s.lower().count('o')
    return count_x == count_o