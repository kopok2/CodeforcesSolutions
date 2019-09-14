import unittest
from unittest.mock import patch

from cdf_670A import CodeforcesTask670ASolution


class TestCDF670A(unittest.TestCase):
    def test_670A_acceptance_1(self):
        mock_input = ['14']
        expected = '4 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask670ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_670A_acceptance_2(self):
        mock_input = ['2']
        expected = '0 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask670ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
