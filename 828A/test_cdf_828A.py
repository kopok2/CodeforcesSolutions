import unittest
from unittest.mock import patch

from cdf_828A import CodeforcesTask828ASolution


class TestCDF828A(unittest.TestCase):
    def test_828A_acceptance_1(self):
        mock_input = ['4 1 2', '1 2 1 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask828ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_828A_acceptance_2(self):
        mock_input = ['4 1 1', '1 1 2 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask828ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
