
a = "weg"
b = "gew"

if len(a) != len(b):
    print("Not anagrams")
else:
    rep = 'Anagram'
    a_list = list(a)
    b_list = list(b)
    for i in a_list:
        if i in b_list:
            a_list.remove(i)
            b_list.remove(i)
            continue
        elif i not in b_list:
            rep = "Not anagrams"
            break
    print(rep)