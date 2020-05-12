
class Hello:
    def __init__(self, name):
        self.name = name
        return

    def sayHello(self, yourname):
        print("Hello, %s. I'm %s" % (yourname, self.name))
        return
    
    def get_true(self):
        return True

def main():
    #list_test_run()
    #tuple_test_run()
    #dictionary_test_run()
    #set_test_run()

    A = Hello("Lexel")
    A.sayHello("Kay")

    print("Welcome back {}".format('Lexel'))

    return True

# __name__ is a python self-maintain variable, the value is different in bellow condition
#   1) py Hello.py         => __name__ = __main__
#   2) from Hello import X => __name__ = Hello
if __name__ == '__main__':
    main()