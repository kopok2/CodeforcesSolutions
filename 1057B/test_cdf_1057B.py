import unittest
from unittest.mock import patch

from cdf_1057B import CodeforcesTask1057BSolution


class TestCDF1057B(unittest.TestCase):
    def test_1057B_acceptance_1(self):
        mock_input = ['5', '100 200 1 1 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1057BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1057B_acceptance_2(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1057BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1057B_acceptance_3(self):
        mock_input = ['2', '101 99']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1057BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()