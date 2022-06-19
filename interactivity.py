from cmd import Cmd
logo = """
 ____        _     ___ _____
|  _ \ _   _| |   / _ \_   _|
| |_) | | | | |  | | | || |
|  __/| |_| | |__| |_| || |
|_|    \__, |_____\___/ |_|
       |___/
"""
from argparse import ArgumentParser

def get_add_parser():
    add_parser: ArgumentParser = ArgumentParser()
    add_parser.prog = "add_numbers"
    add_parser.add_argument('-a', '--num1', dest="num1", required=True, help="num 1")
    add_parser.add_argument('-b', '--num2', dest="num2", required=True, help="num 2") 
    return add_parser



class MyPrompt(Cmd):
    
    prompt = 'pylot> '
    intro : str = f"Welcome to \n{logo}"
    add_parser = get_add_parser()

    def do_exit(self, inp):
        print("Bye")
        return True
 
    def do_add(self, inp):
        args = self.add_parser.parse_args(inp.split())
        print(f"Adding {args.num1} + {args.num2} = {args.num1 + args.num2}")
 
    def get_records(self, inp):
        print("What I am getting records?")

    def help_add(self):
        self.add_parser.print_help()
        

    def help_exit(self):
        print("Press q or ^C to exit")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 
MyPrompt().cmdloop()
print("after")
