import unittest
from unittest.mock import patch

from cdf_215A import CodeforcesTask215ASolution


class TestCDF215A(unittest.TestCase):
    def test_215A_acceptance_1(self):
        mock_input = ['2', '4 5', '3', '12 13 15']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask215ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_215A_acceptance_2(self):
        mock_input = ['4', '1 2 3 4', '5', '10 11 12 13 14']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask215ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
