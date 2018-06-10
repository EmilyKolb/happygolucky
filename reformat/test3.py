def a(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    numofslashes = 0
    for character in test_str:
        if character == '[':
            skip1c += 1
        elif character == ']' and skip1c > 0:
            skip1c -= 1
        elif character == '/' and numofslashes == 0:
            numofslashes += 1
            ret += character
        elif character == '/' and numofslashes == 1:
            skip2c += 1
            ret = ret[:-1]
            numofslashes -= 1
        elif character.isdigit() and skip2c > 0:
            skip2c -= 1
            ret += character
        elif skip1c == 0 and skip2c == 0:
            ret += character


    return ret

x = "this is something [with a vo note] now here is something else //vo note 12:00:12:05 happy dog happy cat/dog "
x = a(x)

print (x)
print (repr(x))
