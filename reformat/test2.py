def remove_bracketed_vo_notes(text, brackets = "[]()"):
    count = [0] * (len(brackets) // 2)
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b:
                kind = i // 2
                is_close = i % 2
                count[kind] += (-1)**is_close
                print(kind)
                print(is_close)
                if count[kind] < 0: #unbalanced bracket
                    count[kind] = 0
                else:   # found bracket to remove
                    break
        else: # character is not a [balanced] brackets
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)


print(repr(remove_bracketed_vo_notes("This is a sentence. (once a day) [twice a day] hey there")))
