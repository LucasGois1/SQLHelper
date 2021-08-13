import unittest

from SQLHelper import SQLHelper


class InsertCase(unittest.TestCase):
    def test_should_return_insert_into_with_values(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.insert_one({
            'name': 'Lucas',
            'email': 'lucas@gmail.com'
        }).query()

        self.assertEqual("INSERT INTO register.user(name,email) VALUES('Lucas','lucas@gmail.com')", response)

    def test_should_return_insert_into_with_values_on_set_only_table(self):
        sut = SQLHelper(table='user')

        response = sut.insert_one({
            'name': 'Lucas',
            'email': 'lucas@gmail.com'
        }).query()

        self.assertEqual("INSERT INTO user(name,email) VALUES('Lucas','lucas@gmail.com')", response)

    def test_should_return_insert_with_a_NULL_value(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.insert_one({
            'name': 'Lucas',
            'email': None
        }).query()

        self.assertEqual("INSERT INTO register.user(name,email) VALUES('Lucas',NULL)", response)

    def test_should_return_insert_with_a_int_value(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.insert_one({
            'name': 'Lucas',
            'age': 26
        }).query()

        self.assertEqual("INSERT INTO register.user(name,age) VALUES('Lucas',26)", response)

    def test_should_return_insert_with_a_two_tuples(self):

        sut = SQLHelper(schema='register', table='user')

        values = [{
            'name': 'Lucas',
            'age': 26
        }, {
            'name': 'Camila',
            'age': 30
        }]

        response = sut.insert_many(values).query()
        self.assertEqual("INSERT INTO register.user(name,age) VALUES('Lucas',26),('Camila',30)", response)


if __name__ == '__main__':
    unittest.main()
