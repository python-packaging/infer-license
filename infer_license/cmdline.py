import sys
from .api import guess_text
from typing import List

# TODO use click
def main(filenames: List[str]) -> None:
    for filename in filenames:
        with open(filename) as f:
            data = f.read()
        result = guess_text(data)
        if result:
            print(filename, result.shortname)
        else:
            print(filename, "Unknown")

if __name__ == "__main__":
    main(sys.argv[1:])
