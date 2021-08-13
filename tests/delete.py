import unittest

from SQLHelper import SQLHelper


class DeleteCase(unittest.TestCase):
    def test_should_return_delete_query(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.delete().query()
        self.assertEqual("DELETE FROM register.user", response)


if __name__ == '__main__':
    unittest.main()
