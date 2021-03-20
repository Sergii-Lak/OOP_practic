
# Caesar cipher.
text = input("Enter your message: ")
step1 = int(input('Your step: '))

cipher = ''

for char in text:
    if not char.isalpha():
        cipher += char
    if char.isalpha():
        if 64 < ord(char) < 91:
            code = ord(char) + step1
            if code > ord('Z'):
                code = ((ord(char) + step1) - ord('Z')) + (ord('A') - 1)
                print('code: ' + str(code) + ' // ' + 'Char: ' + str(ord(char)) + ' // new char: ' + chr(code))
            cipher += chr(code)
        if 96 < ord(char) < 123:
            code = ord(char) + step1
            if code > ord('z'):
                code = ((ord(char) + step1) - ord('z')) + (ord('a') - 1)
                print('code: ' + str(code) + ' // ' + 'Char: ' + str(ord(char)) + ' // new char: ' + chr(code))
            cipher += chr(code)

print(cipher)

