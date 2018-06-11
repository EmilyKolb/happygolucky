def remove_bracketed_vo_notes(test_str):
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



def maketitle(test_str):
    start = 0
    end = 0
    counter = -1
    starttitle = False
    endtitle = False
    title = ''

    while not endtitle:
        for character in test_str:
            counter += 1

            if character.isalpha() and not starttitle:
                start = counter
                starttitle = True

            elif start != 0 and character is "\n":
                end = counter
                endtitle = True

    title = test_str[start:end]
    return(title)


text = "12\ntitular\n//vo note 12:00:12:05 happy dog happy cat/dog [go to bed] "
#aprint(remove_bracketed_vo_notes(text))
print(maketitle(text))
