import unittest

from SQLHelper import SQLHelper


class WhereCase(unittest.TestCase):
    def test_should_return_where_with_two_condition(self):
        sut = SQLHelper(schema='register', table='user')

        conditions = {
            'name': 'Lucas',
            'age': 26
        }

        response = sut.select().where(conditions).query()
        self.assertEqual("SELECT * FROM register.user WHERE name = 'Lucas' AND age = 26", response)

    def test_should_return_where_with_one_condition(self):
        sut = SQLHelper(schema='register', table='user')

        conditions = {
            'age': 26
        }

        response = sut.select().where(conditions).query()
        self.assertEqual("SELECT * FROM register.user WHERE age = 26", response)


if __name__ == '__main__':
    unittest.main()
