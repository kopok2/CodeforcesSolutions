import unittest
from unittest.mock import patch

from cdf_946A import CodeforcesTask946ASolution


class TestCDF946A(unittest.TestCase):
    def test_946A_acceptance_1(self):
        mock_input = ['3', '1 -2 0']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask946ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_946A_acceptance_2(self):
        mock_input = ['6', '16 23 16 15 42 8']
        expected = '120'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask946ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
