import unittest

from tests.helpers.action.fake_action_with_no_handler import FakeActionWithNoHandler
from tests.lib.application_test_case import ApplicationTestCase


class FakeActionWithNoHandlerTest(unittest.TestCase, ApplicationTestCase):
    def test_we_get_exception(self):
        command = FakeActionWithNoHandler()
        with self.assertRaises(ModuleNotFoundError):
            self.dispatch_command(command)
