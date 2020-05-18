
from utils import list_demo

class Hello:
    def __init__(self, name):
        self.name = name

    def say_hello(self, yourname):
        print("Hello, %s. I'm %s" % (yourname, self.name))
    
    def get_true(self):
        return True

def main():

    list_demo.list_test()

    A = Hello("Lexel")
    A.say_hello("Kay")

    print("Welcome back {}".format('Lexel'))

    return True

# __name__ is a python self-maintain variable, the value is different in bellow condition
#   1) py Hello.py         => __name__ = __main__
#   2) from Hello import X => __name__ = Hello
if __name__ == '__main__':
    main()