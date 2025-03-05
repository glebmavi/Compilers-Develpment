import unittest
from main import DFA


class TestDFA(unittest.TestCase):
    def setUp(self):
        self.dfa = DFA()


    def test_trivial_accept(self):
        accepted = ["abb", "cbb", "bbb", "bbc"]
        for string in accepted:
            with self.subTest(input=string):
                self.assertTrue(self.dfa.accepts(string), f"Цепочка '{string}' должна приниматься")

    def test_trivial_reject(self):
        rejected = ["", "a", "c", "bb"]
        for string in rejected:
            with self.subTest(input=string):
                self.assertFalse(self.dfa.accepts(string), f"Цепочка '{string}' не должна приниматься")


    def test_nontrivial_accept(self):
        accepted = ["abbccab", "bcbbbac", "cabbabaaaccba", "babcaccabbc"]
        for string in accepted:
            with self.subTest(input=string):
                self.assertTrue(self.dfa.accepts(string), f"Цепочка '{string}' должна приниматься")

    def test_nontrivial_reject(self):
        rejected = ["abccbabb", "abbb", "babab", "babb", "ccbcccbbaa"]
        for string in rejected:
            with self.subTest(input=string):
                self.assertFalse(self.dfa.accepts(string), f"Цепочка '{string}' не должна приниматься")


if __name__ == '__main__':
    unittest.main()
