from dataclasses import dataclass, field
from typing import Optional, Set

import pkg_resources


@dataclass
class License:
    name: str  # SPDX Full name
    shortname: str  # SPDX Identifier
    trove_classifier: Optional[str]

    # For lazy loading
    _text: Optional[str] = field(default=None, repr=False)
    _trigrams: Optional[Set[str]] = field(default=None, repr=False)

    @property
    def text(self) -> str:
        if not self._text:
            self._text = pkg_resources.resource_string(
                __name__, f"licenses/{self.shortname}.txt"
            ).decode()
        return self._text

    @property
    def trigrams(self) -> Set[str]:
        if not self._trigrams:
            self._trigrams = trigrams(self.text)
        assert self._trigrams is not None
        return self._trigrams


def trigrams(text: str) -> Set[str]:
    words = [w for w in text.split() if w not in ("/*", "*", "*/", "#")]
    return {f"{words[i]}-{words[i+1]}-{words[i+2]}" for i in range(len(words) - 3)}


# See some discussion at https://github.com/pypa/warehouse/issues/2996 about
# using SPDX names, which is what we use for shortname.  Several do not have
# Trove classifiers available.
KNOWN_LICENSES = [
    License(
        "Apache License 2.0",
        "Apache-2.0",
        "License :: OSI Approved :: Apache Software License",
    ),
    License(
        'BSD 2-Clause "Simplified" License',
        "BSD-2-Clause",
        "License :: OSI Approved :: BSD License",
    ),
    License(
        'BSD 3-Clause "New" or "Revised" License',
        "BSD-3-Clause",
        "License :: OSI Approved :: BSD License",
    ),
    License("Creative Commons Attribution 4.0 International", "CC-BY-4.0", None),
    License(
        "GNU Affero General Public License v3.0 or later",
        "AGPL-3.0-or-later",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ),
    License(
        "GNU Lesser General Public License v2 or later",
        "LGPL-2.0-or-later",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ),
    License(
        "GNU Lesser General Public License v2.1 or later", "LGPL-2.1-or-later", None,
    ),
    License(
        "GNU Lesser General Public License v3.0 or later",
        "LGPL-3.0-or-later",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ),
    License(
        "GNU General Public License v2.0 or later",
        "GPL-2.0-or-later",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    ),
    License(
        "GNU General Public License v3.0 or later",
        "GPL-3.0-or-later",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ),
    License("MIT License", "MIT", "License :: OSI Approved :: MIT License"),
    License("MIT No Attribution", "MIT-0", "License :: OSI Approved :: MIT License"),
    License("X11 License", "X11", None),
    # This one is a bit unusual; the license text I include is verbatim from the
    # Python distribution, not from https://spdx.org/licenses/Python-2.0.html
    License(
        "Python License 2.0",
        "Python-2.0",
        "License :: OSI Approved :: Python Software Foundation License",
    ),
]


def license_by_shortname(shortname: str) -> License:
    for el in KNOWN_LICENSES:
        if el.shortname == shortname:
            return el
    raise KeyError(f"Unknown license: {shortname!r}")
