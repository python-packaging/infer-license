import os
import tempfile
import unittest

from .. import api, types


class ApiTest(unittest.TestCase):
    def test_probabilities_no_valid_license(self) -> None:
        p = api.probabilities("foo")
        self.assertEqual(len(types.KNOWN_LICENSES), len(p))
        self.assertEqual(0.0, sum(i[1] for i in p))

    def test_guess_no_valid_license(self) -> None:
        g = api.guess_text("foo")
        self.assertEqual(None, g)

    def test_guess_filename(self) -> None:
        g = api.guess_file("LICENSE")
        assert g is not None
        self.assertEqual("MIT", g.shortname)

    def test_guess_filename_latin1(self) -> None:
        fn = tempfile.mktemp()
        with open("LICENSE", "rb") as f2:
            data = f2.read()
        try:
            with open(fn, "wb") as f:
                f.write(data + b"\xe9")
                f.flush()
            g = api.guess_file(fn)
            assert g is not None
            self.assertEqual("MIT", g.shortname)
        finally:
            try:
                os.unlink(fn)
            except OSError:
                pass  # presume it never got created

    def test_bsd_exact(self) -> None:
        bsd = types.license_by_shortname("BSD-2-Clause")
        g = api.guess_text(bsd.text)
        self.assertEqual(bsd, g)

    def test_bsd_some_words_changed(self) -> None:
        bsd = types.license_by_shortname("BSD-2-Clause")
        text = bsd.text
        text = text.replace("<year>", "1900").replace("<owner>", "Amusing Company Name")
        self.assertIn("Amusing Company Name", text)
        g = api.guess_text(text)
        self.assertEqual(bsd, g)

    def test_license_by_shortname_invalid(self) -> None:
        with self.assertRaises(KeyError, msg="Unknown license: 'Foo'"):
            types.license_by_shortname("Foo")
