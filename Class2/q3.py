def charCount():
    dict = {}
    f = open("t.txt", "r")
    content = f.read()

    for char in content:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

print(charCount())

