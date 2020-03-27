import unittest
from json_expander.context import Context


class TestContext(unittest.TestCase):
    def setUp(self):
        self.context = Context()

    def test_set_context_var(self):
        self.assertEqual(self.context.get_var('var'), None)

        self.context.set_var('var', 'val')
        self.assertEqual(self.context.get_var('var'), 'val')


if __name__ == '__main__':
    unittest.main()
