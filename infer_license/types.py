from dataclasses import dataclass

import pkg_resources


@dataclass
class License:
    name: str
    shortname: str

    @property
    def text(self) -> str:
        return pkg_resources.resource_string(
            __name__, f"licenses/{self.shortname}.txt"
        ).decode()


KNOWN_LICENSES = [
    License("Apache License 2.0", "Apache-2.0"),
    License('BSD 2-Clause "Simplified" License', "BSD-2-Clause"),
    License('BSD 3-Clause "New" or "Revised" License', "BSD-3-Clause"),
    License("Creative Commons Attribution 4.0 International", "CC-BY-4.0"),
    License("GNU Affero General Public License v3.0 or later", "AGPL-3.0-or-later"),
    License("GNU Lesser General Public License v2 or later", "LGPL-2.0-or-later"),
    License("GNU Lesser General Public License v2.1 or later", "LGPL-2.1-or-later"),
    License("GNU Lesser General Public License v3.0 or later", "LGPL-3.0-or-later"),
    License("GNU General Public License v2.0 or later", "GPL-2.0-or-later"),
    License("GNU General Public License v3.0 or later", "GPL-3.0-or-later"),
    License("MIT License", "MIT"),
    License("MIT No Attribution", "MIT-0"),
]


def license_by_shortname(shortname: str) -> License:
    for el in KNOWN_LICENSES:
        if el.shortname == shortname:
            return el
    raise KeyError(f"Unknown license: {shortname!r}")
