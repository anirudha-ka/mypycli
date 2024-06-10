import sys
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    print("In main()")

    args = sys.argv[1:]
    print(f"count of args :: {len(args)}")

    for arg in args:
        print(f"passed argument :: {arg}")

    my_function("Function import works")

    obj = MyClass("Anirudha")
    obj.say_thanks()

if __name__ == "__main__":
    main()