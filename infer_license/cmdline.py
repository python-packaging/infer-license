import sys
from typing import List, Optional

from .api import guess_file


# TODO use click
def main(filenames: Optional[List[str]] = None) -> None:
    if filenames is None:
        filenames = sys.argv[1:]

    for filename in filenames:
        try:
            result = guess_file(filename)
        except IOError:
            result = None
        print(f"{filename}: {result.shortname if result else 'Unknown'}")


if __name__ == "__main__":  # pragma: no cover
    main()
