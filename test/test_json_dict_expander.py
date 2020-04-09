import unittest
from json_expander.json_dict_expander import JsonDictExpander
from json_expander.context import Context


class TestJsonExpander(unittest.TestCase):
    def setUp(self):
        self.json_dict_expander = JsonDictExpander()

    def test_expand_empty_json(self):
        self.assertEqual(self.json_dict_expander.expand({}), {})

    def test_expand_simple_json(self):
        src_json_dict = {
            "first_name": "John",
            "last_name": "Doe",
            "age": 19
        }
        expected_dst_json_dict = {
            "first_name": "John",
            "last_name": "Doe",
            "age": 19
        }
        self.assertEqual(self.json_dict_expander.expand(src_json_dict), expected_dst_json_dict)

    def test_expand_simple_json_with_undefined_var(self):
        context = Context()
        context.set_var("name", "John var")

        src_json_dict = {
            "first_name": "$name2",
            "last_name": "Doe"
        }
        expected_dst_json_dict = {
            "first_name": "$name2",
            "last_name": "Doe"
        }
        self.assertEqual(self.json_dict_expander.expand(src_json_dict, context), expected_dst_json_dict)

    def test_expand_simple_json_with_defined_var(self):
        context = Context()
        context.set_var("name", "John var")
        context.set_var("key", "last_name")
        context.set_var("age", 18)

        src_json_dict = {
            "first_name": "$name",
            "$key": "Doe",
            "age": "$age"
        }
        expected_dst_json_dict = {
            "first_name": "John var",
            "last_name": "Doe",
            "age": 18
        }
        self.assertEqual(self.json_dict_expander.expand(src_json_dict, context), expected_dst_json_dict)

    def test_expand_nested_json_with_vars(self):
        context = Context()
        context.set_var("name", "John var")
        context.set_var("key", "last_name")
        context.set_var("last_name", "Doe")

        src_json_dict = {
            "first_name": "$name",
            "$key": "Doe",
            "children": [
                {
                    "first_name": "Jonas",
                    "last_name": "$last_name"
                },
                {
                    "first_name": "Elizabeth",
                    "last_name": "$last_name"
                }
            ]
        }
        expected_dst_json_dict = {
            "first_name": "John var",
            "last_name": "Doe",
            "children": [
                {
                    "first_name": "Jonas",
                    "last_name": "Doe"
                },
                {
                    "first_name": "Elizabeth",
                    "last_name": "Doe"
                }
            ]
        }
        self.assertEqual(self.json_dict_expander.expand(src_json_dict, context), expected_dst_json_dict)


if __name__ == '__main__':
    unittest.main()
