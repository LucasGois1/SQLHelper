import unittest

from SQLHelper import SQLHelper


class MyTestCase(unittest.TestCase):
    def test_should_return_update_query(self):
        sut = SQLHelper(schema='register', table='user')

        updated_user = {
            'name': 'Will',
            'age': 30
        }

        response = sut.update(updated_user).query()
        self.assertEqual("UPDATE register.user SET name = 'Will', age = 30 ", response)


if __name__ == '__main__':
    unittest.main()
