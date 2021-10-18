import argparse
import random
from generate import generate

# created by Daniel Jung and Brian Da Silva


def main():
    parser = argparse.ArgumentParser(
        description="Generate a secure, memorable password using the XKCD method", prog="xkcdpwgen")
    parser.add_argument("-w", "--words", dest="WORDS", default="4",
                        help="include WORDS words in the password (default-4)")
    parser.add_argument("-c", "--caps", dest="CAPS", default="0",
                        help="capitalize the first letter of CAPS random words(default=0)")
    parser.add_argument("-n", "--numbers", dest="NUMBERS", default="0",
                        help="insert NUMBERS random numbers in the password(default=0)")
    parser.add_argument("-s", "--symbols", dest="SYMBOLS", default="0",
                        help="insert SYMBOLS random symbols in the password(default=0)")
    args = parser.parse_args()

    password = generate(int(args.WORDS), int(args.CAPS),
                        int(args.NUMBERS), int(args.SYMBOLS))
    print(password)


if __name__ == "__main__":
    main()
