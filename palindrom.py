
st = 'eeffree'

if st == '' or st.isspace() or len(st) == 1:
    print('Its not a palindrome')
else:
    st = (st.lower()).replace(' ', '')
    long = len(st)
    step_1 = long / 2
    st2 = ''
    st3 = st[0:int(step_1)]

    if long % 2 == 0:
        st2 = st[int(step_1):]
        st2 = st2[::-1]
    elif long % 2 != 0:
        st2 = st[int(step_1) + 1:]
        st2 = st2[::-1]

    print(st3)
    print(st2)
    if st3 == st2:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

