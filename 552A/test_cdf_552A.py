import unittest
from unittest.mock import patch

from cdf_552A import CodeforcesTask552ASolution


class TestCDF552A(unittest.TestCase):
    def test_552A_acceptance_1(self):
        mock_input = ['2', '1 1 2 3', '2 2 3 3']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask552ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_552A_acceptance_2(self):
        mock_input = ['2', '1 1 3 3', '1 1 3 3']
        expected = '18'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask552ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
