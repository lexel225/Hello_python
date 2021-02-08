
from utils import list_demo

class Hello:
    def __init__(self, name):
        self.name = name

    def say_hello(self, yourname):
        print("Hello, %s. I'm %s" % (yourname, self.name))
    
    def get_true(self):
        return True

    def print_args(self, a, *args):

        print(f'a: {a}')
        for idx,i in enumerate(args):
            print(f'args_{idx}: {i}')

    def print_kwargs(self, **kwargs):

        for key,value in kwargs.items():
            print(f'{key}: {value}')

def main():

    print("Welcome back {}".format('Lexel'))

    list_demo.list_test()

    A = Hello("Lexel")
    A.say_hello("Kay")


    A.print_args('Head', 'First', 'Second')

    kwargs = {'KEY_1': 1, 'KEY_2': 2}

    A.print_kwargs(**kwargs)

    A.print_kwargs(KEY_3=3, KEY_4=4)

    return True

# __name__ is a python self-maintain variable, the value is different in bellow condition
#   1) py Hello.py         => __name__ = __main__
#   2) from Hello import X => __name__ = Hello
if __name__ == '__main__':
    main()