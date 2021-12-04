import unittest
from packaging_classifiers import classifiers
from .. import types


class TypesTest(unittest.TestCase):
    def test_classifiers_are_valid(self) -> None:
        for license in types.KNOWN_LICENSES:
            if license.trove_classifier:
                with self.subTest(msg=license.shortname):
                    self.assertTrue(license.trove_classifier in classifiers)
