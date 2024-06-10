import sys

def main():
    print("In main()")

    args = sys.argv[1:]
    print(f"count of args :: {len(args)}")

    for arg in args:
        print(f"passed argument :: {arg}")

if __name__ == "__main__":
    main()