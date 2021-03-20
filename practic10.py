def mysplit(strng):
    b = []
    if strng.isspace() or strng == '':
        return b
    else:
        a = []
        m = ''
        for i in strng:
            if i != ' ':
                m += i
            else:
                if m != '':
                    a.append(m)
                m = ''
        return a



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

n = [
    ["###", "  #", "###", "###", "# #", "###", "###", "###", "###", "###"],
    ["# #", "  #", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #"],
    ["# #", "  #", "###", "###", "###", "###", "###", "  #", "###", "###"],
    ["# #", "  #", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #"],
    ["###", "  #", "###", "###", "  #", "###", "###", "  #", "###", "###"]
]

m = input('Your number: ')

for i in n:
    for j in str(m):
        print(i[int(j)], end=' ')
    print('')