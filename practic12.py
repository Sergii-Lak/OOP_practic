
def read_int(prompt, min, max):
    x = input(prompt)
    y = True
    while y:
        try:
            x = int(x)
            assert min <x < max
            y = False
        except ValueError:
            print('Error: wrong input')
            x = input(prompt)
        except AssertionError:
            print('Error: the value is not within permitted range (-10..10)')
            x = input(prompt)
    return x

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
