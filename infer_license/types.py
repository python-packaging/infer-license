from dataclasses import dataclass

import pkg_resources


@dataclass
class License:
    name: str
    shortname: str
    trove_classifier: str

    @property
    def text(self) -> str:
        return pkg_resources.resource_string(
            __name__, f"licenses/{self.shortname}.txt"
        ).decode()

# See some discussion at https://github.com/pypa/warehouse/issues/2996 about
# using SPDX names, which is what we use for shortname.  The two marked TODO
# here don't have a current Trove classifier.
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
    License("Creative Commons Attribution 4.0 International", "CC-BY-4.0", "TODO"),
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
        "GNU Lesser General Public License v2.1 or later", "LGPL-2.1-or-later", "TODO"
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
]


def license_by_shortname(shortname: str) -> License:
    for el in KNOWN_LICENSES:
        if el.shortname == shortname:
            return el
    raise KeyError(f"Unknown license: {shortname!r}")
