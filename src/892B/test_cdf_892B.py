import unittest
from unittest.mock import patch

from cdf_892B import CodeforcesTask892BSolution


class TestCDF892B(unittest.TestCase):
    def test_892B_acceptance_1(self):
        mock_input = ['4', '0 1 0 10']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask892BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_892B_acceptance_2(self):
        mock_input = ['2', '0 0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask892BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_892B_acceptance_3(self):
        mock_input = ['10', '1 1 3 0 0 0 2 1 0 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask892BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
