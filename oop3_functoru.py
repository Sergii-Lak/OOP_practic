

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(self.__counter)
        return self.__counter

c1 = Counter()
c1()
c1()
c1()
c1()
c1()

# ------------------------------------------------

class StripChars:
    def __init__(self, chars):
        self.__chars = chars
        self.__a = None

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Argument not corrected")
        print(args[0])
        #return "".join(c for c in args[0] if c.isalnum())
        self.__a = args[0]
        for char in self.__chars:
            self.__a = self.__a.replace(char, "")
        return self.__a

symb = "-,.:+=)(w!& ?%$#@ÈÇÀ:"
s1 = StripChars(symb)

text = " sd W c R ,w.:+=) w, Olwld 11 # e"
print(s1(text))