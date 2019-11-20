from dataclasses import dataclass
import pkg_resources

@dataclass
class License:
    name: str
    shortname: str

    @property
    def text(self):
        return pkg_resources.resource_string(__name__,
            f"licenses/{self.shortname}.txt").decode()

KNOWN_LICENSES = [
    License("Apache License 2.0", "Apache-2.0"),
    License('BSD 2-Clause "Simplified" License', "BSD-2-Clause"),
    License('BSD 3-Clause "New" or "Revised" License', 'BSD-3-Clause'),
    License("Creative Commons Attribution 4.0 International", "CC-BY-4.0"),
    License("MIT License", "MIT"),
    License("MIT No Attribution", "MIT-0"),
]
