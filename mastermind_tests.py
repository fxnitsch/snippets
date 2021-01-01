import unittest

from mastermind import check_exact_matches, check_for_content_matches, check_for_win


class MyTestCase(unittest.TestCase):
    def test_check_exact_matches(self):
        code = [1, 3, 3, 5]

        # some true
        guess = [1, 2, 3, 4]
        expected = [2, 4]
        flags, code_to_check, guess_to_check = check_exact_matches(code, guess)
        self.assertEqual(flags, ['X', 'X'])
        self.assertEqual(expected, guess_to_check)

        # all true
        guess = [1, 3, 3, 5]
        expected = []
        flags, code_to_check, guess_to_check = check_exact_matches(code, guess)
        self.assertEqual(flags, ['X', 'X', 'X', 'X'])
        self.assertEqual(expected, guess_to_check)

        # all false
        guess = [2, 2, 2, 2]
        expected = [2, 2, 2, 2]
        flags, code_to_check, guess_to_check = check_exact_matches(code, guess)
        assert flags == []
        self.assertEqual(expected, guess_to_check)

    def test_check_for_content_matches(self):
        code = [1, 3, 3, 5]

        # some true
        guess = [3, 2, 5, 3]
        flags = []
        flags = check_for_content_matches(code, flags, guess)
        self.assertEqual(flags, ['0', '0', '0'])

        # all true
        guess = [3, 1, 5, 3]
        flags = []
        flags = check_for_content_matches(code, flags, guess)
        self.assertEqual(flags, ['0', '0', '0', '0'])

        # all false
        guess = [4, 4, 4, 4]
        flags = []
        flags = check_for_content_matches(code, flags, guess)
        self.assertEqual(flags, [])

    def test_check_for_win(self):
        # win
        flags = ['X', 'X', 'X', 'X']
        self.assertTrue(check_for_win(flags))

        # no win
        flags = ['X', 'X', 'X', '0']
        self.assertFalse(check_for_win(flags))


if __name__ == '__main__':
    unittest.main()
