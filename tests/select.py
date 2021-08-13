import unittest

from SQLHelper import SQLHelper


class SelectCase(unittest.TestCase):
    def test_should_return_asteristic_if_no_arguments_are_provided(self):
        sut = SQLHelper(schema='any_schema', table='any_table')

        response = sut.select().query()

        self.assertEqual('SELECT * FROM any_schema.any_table ', response)

    def test_should_return_select_with_column_if_column_are_provided(self):
        sut = SQLHelper(schema='any_schema', table='any_table')

        response = sut.select('name').query()

        self.assertEqual('SELECT name FROM any_schema.any_table ', response)

    def test_should_return_select_with_all_columns_if_columns_are_provided(self):
        sut = SQLHelper(schema='any_schema', table='any_table')

        response = sut.select('name', 'email', 'age').query()

        self.assertEqual('SELECT name, email, age FROM any_schema.any_table ', response)

    def test_should_calls_thow_selects(self):
        sut = SQLHelper(schema='any_schema', table='any_table')

        response = sut.select('name', 'email', 'age').select('name', 'email', 'age').query()

        self.assertEqual('SELECT name, email, age FROM any_schema.any_table SELECT name, email, age FROM any_schema.any_table ', response)

    def test_should_return_select_count_asteristic_if_no_arguments_are_provided(self):
        sut = SQLHelper(schema='any_schema', table='any_table')

        response = sut.count().query()

        self.assertEqual('SELECT COUNT(*) FROM any_schema.any_table ', response)

    def test_should_return_select_count_columns_if_columns_are_provided(self):
        sut = SQLHelper(schema='any_schema', table='any_table')

        response = sut.count('name', 'email').query()

        self.assertEqual('SELECT COUNT(name,email) FROM any_schema.any_table ', response)


if __name__ == '__main__':
    unittest.main(verbosity=2)
