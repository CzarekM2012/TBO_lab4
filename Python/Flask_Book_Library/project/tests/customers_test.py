import unittest
from itertools import product
from project.customers.models import Customer

# PESEL                   | Ciąg znaków składający się z 11 cyfr
# Ulica                   | Ciąg [2-30] znaków składający się z liter i znaków {' ', '.', '-'}, może być pusty
# Numer_mieszkania        | Ciąg znaków składający się z [1-3] cyfr, po cyfrach może znajdować się pojedyncza litera, może być pusty

EXAMPLE_GOOD_ARGUMENTS = {
    "name": "a" * 10,
    "city": "a" * 10,
    "age": 20,
    "pesel": "0" * 11,
    "street": "",
    "appNo": "",
}


def swap_value_in_copy(base: dict, swapped_key: str, new_value):
    new = base.copy()
    new[swapped_key] = new_value
    return new


class TestCustomerCreation(unittest.TestCase):
    def test_name_length(self):
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "a" * 2))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "a" * 3))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "a" * 40))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "a" * 41))

    def test_name_allowed_characters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "amnz ZNMA"))

    def test_name_forbidden_characters(self):
        # fmt: off
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '-', '_', '=', '+', ',', '.', '/', '<', '>', '?',
                          ';', '\'', '\\', ':', '\"', '|', '[', ']', '{', '}',
                          '`', '~']:
        # fmt:on
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", character * 10))

    def test_city_length(self):
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "a" * 2))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "a" * 3))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "a" * 30))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "a" * 31))

    def test_city_allowed_characters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "amnz ZNMA"))

    def test_city_forbidden_characters(self):
        # fmt: off
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '_', '=', '+', '/', '<', '>', '?', ';', '\'', '\\',
                          ':', '\"', '|', '[', ']', '{', '}', '`', '~']:
        # fmt: on
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", character * 10))

    def test_age_not_string(self):
        with self.assertRaises(TypeError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "age", "20"))

    def test_age_edge_values(self):
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "age", -1))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "age", 0))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "age", 122))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "age", 123))

    def test_pesel_length(self):
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", "0" * 10))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", "0" * 11))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", "0" * 12))

    def test_pesel_allowed_characters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", "12345678901"))

    def test_pesel_forbidden_characters(self):
        # fmt: off
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for character in alphabet + [letter.upper() for letter in alphabet] + [
                         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                         '_', '=', '+', '/', '<', '>', '?', ';', '\'', '\\',
                         ':', '\"', '|', '[', ']', '{', '}', '`', '~']:
        # fmt: on
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", character * 11))

    def test_street_length(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", ""))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "a"))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "a" * 2))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "a" * 30))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "a" * 31))

    def test_street_allowed_characters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "am.nz ZN-MA"))

    def test_street_forbidden_characters(self):
        # fmt: off
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '_', '=', '+', ',',  '/', '<', '>', '?', ';', '\'',
                          '\\', ':', '\"', '|', '[', ']', '{', '}', '`', '~']:
        # fmt:on
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", character * 10))

    def test_appNo_length_no_letters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", ""))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "1"))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "111"))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "1111"))

    def test_appNo_length_with_letters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "1a"))
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "111a"))
        with self.assertRaises(ValueError):
            Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "1111a"))

    def test_appNo_allowed_characters(self):
        Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "159C"))

    def test_appNo_forbidden_characters(self):
        # fmt: off
        for character in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '-', '_', '=', '+', ',', '.', '/', '<', '>', '?',
                          ';', '\'', '\\', ':', '\"', '|', '[', ']', '{', '}',
                          '`', '~']:
        # fmt:on
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", character * 2))

    def test_appNo_letter_positioning(self):
        for string in ["a", "a1", "1a1", "a1a", "1aa"]:
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", string))


class TestCustomerCreationExtremeData(unittest.TestCase):
    def test_name(self):
        for power in range(3, 11):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "a" * 10**power))

    def test_city(self):
        for power in range(3, 11):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "a" * 10**power))

    def test_age(self):
        for power in range(3, 11):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "age", 10**power))

    def test_pesel(self):
        for power in range(3, 11):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", "0" * 10**power))

    def test_street(self):
        for power in range(3, 11):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "a" * 10**power))

    def test_appNo(self):
        for power in range(2, 11):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "a" * 10**power))


class TestCustomerCreationJavascriptInjections(unittest.TestCase):
    def test_name(self):
        with self.assertRaises(ValueError):
            Customer(
                **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", "<script>alert(1)</script>")
            )

    def test_city(self):
        with self.assertRaises(ValueError):
            Customer(
                **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", "<script>alert(1)</script>")
            )

    def test_pesel(self):
        with self.assertRaises(ValueError):
            Customer(
                **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", "<script>alert(1)</script>")
            )

    def test_street(self):
        with self.assertRaises(ValueError):
            Customer(
                **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", "<script>alert(1)</script>")
            )

    def test_appNo(self):
        with self.assertRaises(ValueError):
            Customer(
                **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", "<script>alert(1)</script>")
            )


class TestCustomerCreationSQLInjections(unittest.TestCase):
    SQL_TAUTOLOGIES = ["1=1", "TRUE", "1", "NONE IS NONE"]
    COMMENT_OPENERS = ["#", "--", "/*"]

    def test_name(self):
        for tau in self.SQL_TAUTOLOGIES:
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", f"' OR {tau}"))
        for tau, com in product(self.SQL_TAUTOLOGIES, self.COMMENT_OPENERS):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", f"' OR {tau} {com} "))
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "name", f"' OR {tau}) {com} ")
                )

    def test_city(self):
        for tau in self.SQL_TAUTOLOGIES:
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", f"' OR {tau}"))
        for tau, com in product(self.SQL_TAUTOLOGIES, self.COMMENT_OPENERS):
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", f"' OR {tau} {com} "))
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "city", f"' OR {tau}) {com} ")
                )

    def test_pesel(self):
        for tau in self.SQL_TAUTOLOGIES:
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", f"' OR {tau}"))
        for tau, com in product(self.SQL_TAUTOLOGIES, self.COMMENT_OPENERS):
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", f"' OR {tau} {com} ")
                )
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "pesel", f"' OR {tau}) {com} ")
                )

    def test_street(self):
        for tau in self.SQL_TAUTOLOGIES:
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", f"' OR {tau}"))
        for tau, com in product(self.SQL_TAUTOLOGIES, self.COMMENT_OPENERS):
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", f"' OR {tau} {com} ")
                )
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "street", f"' OR {tau}) {com} ")
                )

    def test_appNo(self):
        for tau in self.SQL_TAUTOLOGIES:
            with self.assertRaises(ValueError):
                Customer(**swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", f"' OR {tau}"))
        for tau, com in product(self.SQL_TAUTOLOGIES, self.COMMENT_OPENERS):
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", f"' OR {tau} {com} ")
                )
            with self.assertRaises(ValueError):
                Customer(
                    **swap_value_in_copy(EXAMPLE_GOOD_ARGUMENTS, "appNo", f"' OR {tau}) {com} ")
                )
