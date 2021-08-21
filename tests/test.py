from main import calculate_standings, parse_input
import unittest
from contextlib import redirect_stdout
import io


class TestRankings(unittest.TestCase):
    # This test data is the data from good-sample-input.txt
    GOOD_TEST_DATA = [
        (("San Jose Earthquakes", 3), ("Santa Cruz Slugs", 3)),
        (("Capitola Seahorses", 1), ("Aptos FC", 0)),
        (("Felton Lumberjacks", 2), ("Monterey United", 0)),
        (("Felton Lumberjacks", 1), ("Aptos FC", 2)),
        (("Santa Cruz Slugs", 0), ("Capitola Seahorses", 0)),
        (("Monterey United", 4), ("San Jose Earthquakes", 2)),
        (("Santa Cruz Slugs", 2), ("Aptos FC", 3)),
        (("San Jose Earthquakes", 1), ("Felton Lumberjacks", 4)),
        (("Monterey United", 1), ("Capitola Seahorses", 0)),
        (("Aptos FC", 2), ("Monterey United", 0)),
        (("Capitola Seahorses", 5), ("San Jose Earthquakes", 5)),
        (("Santa Cruz Slugs", 1), ("Felton Lumberjacks", 1)),
    ]

    # This test data is sourced from bad-sample-input-score.txt
    BAD_TEST_DATA = [
        (("San Jose Earthquakes", 3), ("Santa Cruz Slugs", 3)),
        (("Capitola Seahorses", 1), ("Aptos FC", 0)),
        (("Felton Lumberjacks", 2), ("Monterey United", 0)),
        (("Santa Cruz Slugs", 0), ("Capitola Seahorses", 0)),
        (("Monterey United", 4), ("San Jose Earthquakes", 2)),
        (("Santa Cruz Slugs", 2), ("Aptos FC", 3)),
        (("San Jose Earthquakes", 1), ("Felton Lumberjacks", 4)),
        (("Monterey United", 1), ("Capitola Seahorses", 0)),
        (("Aptos FC", 2), ("Monterey United", 0)),
        (("Capitola Seahorses", 5), ("San Jose Earthquakes", 5)),
        (("Santa Cruz Slugs", 1), ("Felton Lumberjacks", 1)),
    ]

    def test_good_input(self):
        good_input = parse_input("tests/input/good-sample-input.txt")
        assert self.GOOD_TEST_DATA == good_input

    def test_bad_input(self):
        # One of the matches for the input in this test has a string instead of
        # an int for the score, and thus the game gets skipped when parsing
        # the input
        bad_input = parse_input("tests/input/bad-sample-input-score.txt")
        assert self.BAD_TEST_DATA == bad_input

    def test_calculate_standings(self):
        captured_stdout = io.StringIO()
        with open("tests/output/expected-output.txt", "r") as f:
            output = f.read().strip()
        with redirect_stdout(captured_stdout):
            calculate_standings(self.GOOD_TEST_DATA)

        standings = captured_stdout.getvalue().strip()
        assert standings == output


if __name__ == "__main__":
    unittest.main()