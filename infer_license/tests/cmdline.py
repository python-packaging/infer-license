import unittest
from unittest import mock

from .. import cmdline


class CmdlineTest(unittest.TestCase):
    def test_cmdline(self) -> None:
        with mock.patch("infer_license.cmdline.print") as print_mock:
            cmdline.main(["LICENSE"])
            print_mock.assert_called_with("LICENSE: MIT")

    def test_cmdline_error_handling(self) -> None:
        with mock.patch("infer_license.cmdline.print") as print_mock:
            cmdline.main(["does_not_exist"])
            print_mock.assert_called_with("does_not_exist: Unknown")

    def test_cmdline_no_args(self) -> None:
        with mock.patch("infer_license.cmdline.print") as print_mock, mock.patch(
            "infer_license.cmdline.sys.argv", ["cmd", "LICENSE"]
        ):
            cmdline.main()
            print_mock.assert_called_with("LICENSE: MIT")
