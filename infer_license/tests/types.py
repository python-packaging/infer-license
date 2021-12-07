import unittest

from trove_classifiers import classifiers

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

        # Below licenses are to broad, not a license or not part of SPDX-license list
        not_covered = [
            "License :: DFSG approved",
            "License :: Free For Educational Use",
            "License :: Free For Home Use",
            "License :: Free for non-commercial use",
            "License :: Free To Use But Restricted",
            "License :: Freely Distributable",
            "License :: Freeware",
            "License :: GUST Font License 1.0",
            "License :: GUST Font License 2006-09-30",
            "License :: Nokia Open Source License (NOKOS)",
            "License :: OSI Approved :: Eiffel Forum License",
            "License :: OSI Approved :: Jabber Open Source License",
            "License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)",
            "License :: Other/Proprietary License",
            "License :: Public Domain",
            "License :: Repoze Public License",
        ]

        for classifier in classifiers:
            if classifier.startswith("License ::") and classifier not in not_covered:
                with self.subTest(msg=classifier):
                    self.assertTrue(classifier in covered_licenses)
