import unittest

from mastermind import check_exact_matches, check_for_content_matches


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_check_exact_matches():
        code = [1, 3, 3, 5]

        # some true
        guess = [1, 2, 3, 4]
        expected = [2, 4]
        flags, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert flags == ['X', 'X']
        assert len(code_to_check) == len(expected) & len(guess_to_check) == len(expected)
        assert expected == guess_to_check

        # all true
        guess = [1, 3, 3, 5]
        expected = []
        flags, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert flags == ['X', 'X', 'X', 'X']
        assert len(code_to_check) == len(expected) & len(guess_to_check) == len(expected)
        assert expected == guess_to_check

        # all false
        guess = [2, 2, 2, 2]
        expected = [2, 2, 2, 2]
        flags, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert flags == []
        assert len(code_to_check) == len(expected) & len(guess_to_check) == len(expected)
        assert expected == guess_to_check

    @staticmethod
    def test_check_for_content_matches():
        code = [1, 3, 3, 5]

        # some true
        guess = [3, 2, 5, 3]
        flags = []
        flags = check_for_content_matches(code, flags, guess)
        assert flags == ['0', '0', '0']

        # all true
        guess = [3, 1, 5, 3]
        flags = []
        flags = check_for_content_matches(code, flags, guess)
        assert flags == ['0', '0', '0', '0']

        # all false
        guess = [4, 4, 4, 4]
        flags = []
        flags = check_for_content_matches(code, flags, guess)
        assert flags == []


if __name__ == '__main__':
    unittest.main()
