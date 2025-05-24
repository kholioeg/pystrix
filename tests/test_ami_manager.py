import unittest
from pystrix.ami import Manager
from pystrix.ami.core import Login

class TestManager(unittest.TestCase):
    def test_manager_instantiation(self):
        manager = Manager()
        self.assertIsNotNone(manager)

    def test_login_action_creation(self):
        login_action = Login("testuser", "testsecret")
        self.assertEqual(login_action['Action'], "Login")
        self.assertEqual(login_action['Username'], "testuser")
        self.assertEqual(login_action['Secret'], "testsecret")

if __name__ == '__main__':
    unittest.main()
