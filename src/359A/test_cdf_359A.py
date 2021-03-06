import unittest
from unittest.mock import patch

from cdf_359A import CodeforcesTask359ASolution


class TestCDF359A(unittest.TestCase):
    def test_359A_acceptance_1(self):
        mock_input = ['3 3', '0 0 0', '0 1 0', '0 0 0']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask359ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_359A_acceptance_2(self):
        mock_input = ['4 3', '0 0 0', '0 0 1', '1 0 0', '0 0 0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask359ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
