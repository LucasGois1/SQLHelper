import unittest

from SQLHelper import SQLHelper


class SelectCase(unittest.TestCase):
    def test_should_return_asteristic_if_no_arguments_are_provided(self):
        sut = SQLHelper('any_schema', 'any_table')

        response = sut.select().query()

        self.assertEqual('SELECT *', response)

    def test_should_return_select_with_column_if_column_are_provided(self):
        sut = SQLHelper('any_schema', 'any_table')

        response = sut.select('name').query()

        self.assertEqual('SELECT name', response)

    def test_should_return_select_with_all_columns_if_columns_are_provided(self):
        sut = SQLHelper('any_schema', 'any_table')

        response = sut.select('name', 'email', 'age').query()

        self.assertEqual('SELECT name, email, age', response)

    def test_should_calls_thow_selects(self):
        sut = SQLHelper('any_schema', 'any_table')

        response = sut.select('name', 'email', 'age').select('name', 'email', 'age').query()

        self.assertEqual('SELECT name, email, ageSELECT name, email, age', response)

    def test_should_return_select_count_asteristic_if_no_arguments_are_provided(self):
        sut = SQLHelper('any_schema', 'any_table')

        response = sut.select().count().query()

        self.assertEqual('SELECT COUNT(*)', response)

    def test_should_return_select_count_columns_if_columns_are_provided(self):
        sut = SQLHelper('any_schema', 'any_table')

        response = sut.select().count('name', 'email').query()

        self.assertEqual('SELECT COUNT(name,email)', response)

    def test_should_return_insert_into_with_values(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.insert({
            'name': 'Lucas',
            'email': 'lucas@gmail.com'
        }).query()

        self.assertEqual("INSERT INTO register.user(name,email) VALUES('Lucas','lucas@gmail.com')", response)

    def test_should_return_insert_into_with_values_on_set_only_table(self):
        sut = SQLHelper(table='user')

        response = sut.insert({
            'name': 'Lucas',
            'email': 'lucas@gmail.com'
        }).query()

        self.assertEqual("INSERT INTO user(name,email) VALUES('Lucas','lucas@gmail.com')", response)

    def test_should_return_insert_with_a_NULL_value(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.insert({
            'name': 'Lucas',
            'email': None
        }).query()

        self.assertEqual("INSERT INTO register.user(name,email) VALUES('Lucas',NULL)", response)

    def test_should_return_insert_with_a_int_value(self):
        sut = SQLHelper(schema='register', table='user')

        response = sut.insert({
            'name': 'Lucas',
            'age': 26
        }).query()

        self.assertEqual("INSERT INTO register.user(name,age) VALUES('Lucas',26)", response)


if __name__ == '__main__':
    unittest.main(verbosity=2)
