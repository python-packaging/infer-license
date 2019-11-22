import os  # noqa: F401
from typing import List, Optional, Tuple, Union

from .types import KNOWN_LICENSES, License, trigrams


def guess_text(license_text: str) -> Optional[License]:
    """
    Returns the most matching license iif it is 85% similar to a known one.

    This logic mirrors that of https://github.com/sol/infer-license/ (haskell)
    """
    p = probabilities(license_text)
    # print("\n".join(repr(x) for x in p))
    if p and p[0][1] > 0.80:
        return p[0][0]

    return None


def guess_file(filename: Union[str, "os.PathLike[str]"]) -> Optional[License]:
    try:
        with open(filename, encoding="utf-8") as f:
            data = f.read()
    except UnicodeDecodeError:
        with open(filename, encoding="latin-1") as f:
            data = f.read()

    return guess_text(data)


def probabilities(license_text: str) -> List[Tuple[License, float]]:
    """
    Returns potential licenses and their probabilities, in decreasing order.
    """
    probabilities: List[Tuple[License, float]] = []
    tg = trigrams(license_text)
    for license in KNOWN_LICENSES:
        count = sum(1 for t in license.trigrams if t in tg)
        f = count / max(len(license.trigrams), len(tg))
        probabilities.append((license, f))

    probabilities.sort(key=lambda i: i[1], reverse=True)
    return probabilities
