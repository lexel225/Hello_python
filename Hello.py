from list_demo import list_test as list_test_run
from tuple_demo import tuple_test as tuple_test_run
from dictionary_demo import dictionary_test as dictionary_test_run
from set_demo import set_test as set_test_run

class Hello():
    def __init__(self, name):
        self.name = name
        return

    def sayHello(self, yourname):
        print("Hello, %s. I'm %s" % (yourname, self.name))
        return

def main():
    list_test_run()
    tuple_test_run()
    dictionary_test_run()
    set_test_run()

    A = Hello("Lexel")
    A.sayHello("Kay")

    print("Welcome back {}".format('Lexel'))

    return

# __name__ is a python self-maintain variable, the value is different in bellow condition
#   1) py Hello.py         => __name__ = __main__
#   2) from Hello import X => __name__ = Hello
if __name__ == '__main__':
    main()