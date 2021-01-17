# Наследование. Расширение класса в Python. Extending python class in Python
# https://www.youtube.com/watch?v=EYfg7OUQNog&list=PLQAt0m1f9OHvyjJNjZK_unnLwMOXPTja8&index=29&ab_channel=egoroff_channel
class Person:

    def stop(self):
        print("Human stop")

    def combo(self):
        self.stop()
        if hasattr(self, "sleep") and hasattr(self, "go"):
            self.sleep()
            self.go()



class Doctor(Person):

    def sleep(self):
        print("Doctor sleep")

    def go(self):
        print("Doctor Go")

s = Person()
p = Doctor()

s.combo()
print("-" * 20)
p.combo()
