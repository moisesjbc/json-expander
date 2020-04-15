import unittest
from json_expander.functions.repeat_function import RepeatFunction


class TestRepeatFunction(unittest.TestCase):
    def test_simple_repeat(self):
        repeat_function = RepeatFunction()

        repeat_result = repeat_function.run([3, {
            "first_name": "John",
            "last_name": "Doe",
            "age": 19
        }])
        expected_repeat_result = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "age": 19
            },
            {
                "first_name": "John",
                "last_name": "Doe",
                "age": 19
            },
            {
                "first_name": "John",
                "last_name": "Doe",
                "age": 19
            }
        ]
        self.assertEqual(repeat_result, expected_repeat_result)


if __name__ == '__main__':
    unittest.main()
