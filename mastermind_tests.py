import unittest

from mastermind import check_exact_matches


class MyTestCase(unittest.TestCase):
    def test_check_exact_matches(self):
        # some true
        code = [1, 3, 3, 5]
        guess = [1, 2, 3, 4]
        expected = [2, 4]
        _, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert len(code_to_check) == len(expected) & len(guess_to_check) == len(expected)
        assert expected == guess_to_check

        # all true
        code = [1, 3, 3, 5]
        guess = [1, 3, 3, 5]
        expected = []
        _, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert len(code_to_check) == len(expected) & len(guess_to_check) == len(expected)
        assert expected == guess_to_check

        # all false
        code = [1, 3, 3, 5]
        guess = [2, 2, 2, 2]
        expected = [2, 2, 2, 2]
        _, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert len(code_to_check) == len(expected) & len(guess_to_check) == len(expected)
        assert expected == guess_to_check


if __name__ == '__main__':
    unittest.main()
