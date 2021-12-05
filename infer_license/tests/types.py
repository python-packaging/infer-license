import unittest
from packaging_classifiers import classifiers
from .. import types


class TypesTest(unittest.TestCase):
    def test_classifiers_are_valid(self) -> None:
        for license in types.KNOWN_LICENSES:
            if license.trove_classifier:
                with self.subTest(msg=license.shortname):
                    self.assertTrue(license.trove_classifier in classifiers)

    def test_all_licenses_classifiers_covered(self) -> None:
        covered_licenses = [
            license.trove_classifier for license in types.KNOWN_LICENSES
        ]

        for classifier in classifiers:
            if classifier.startswith('License ::'):
                with self.subTest(msg=classifier):
                    self.assertTrue(classifier in covered_licenses)
