"""
Tests the CLI.
"""
import sys
from io import StringIO
from unittest import TestCase

from mockito import expect, unstub, verifyNoUnwantedInteractions

from application.cli import CLI
from application.ranking_results_calculator import RankingResultsCalculator


class TestCLI(TestCase):
    def setUp(self) -> None:
        self.cli = CLI()
        self.parser = self.cli.__create_parser__()

    def tearDown(self) -> None:
        verifyNoUnwantedInteractions()
        unstub()

    def test_main(self) -> None:
        """
        Test the cli main method
        """
        raw_input = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0",
        ]

        expect(CLI, times=1).__get_input__(True, None).thenReturn(raw_input)
        expect(RankingResultsCalculator, times=1).process_results(raw_input).thenReturn(None)

        assert self.cli.main(["-i"]) is None

    def test_get_input_success_manual_input(self) -> None:
        """
        Test the cli get_input method with manual input
        """
        raw_input = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
        ]

        sys.stdin = StringIO(
            "Lions 3, Snakes 3\nTarantulas 1, FC Awesome 0\nLions 1, FC Awesome 1\nTarantulas 3, Snakes 1\n\n"
        )

        assert self.cli.__get_input__(True, None) == raw_input

    def test_get_input_success_manual_input_exit(self) -> None:
        """
        Test the cli get_input method with manual input to stop application
        """
        sys.stdin = StringIO("Lions 3, Snakes 3\nTarantulas 1, FC Awesome 0\nLions 1, FC Awesome 1\nexit\n")

        with self.assertRaises(SystemExit):
            self.cli.__get_input__(True, None)

    def test_get_input_fail_no_input(self) -> None:
        """
        Test the cli get_input method with empty input
        """
        sys.stdin = StringIO("\n")

        with self.assertRaises(SystemExit):
            self.cli.__get_input__(True, None)

    def test_get_input_success_file_input(self) -> None:
        """
        Test the cli get_input method with file input
        """
        raw_input = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0",
        ]

        assert self.cli.__get_input__(False, "test_input/example_input.txt") == raw_input

    def test_file_input_fail_on_existence(self) -> None:
        """
        Test the cli with file input that doesn't exist
        """
        with self.assertRaises(SystemExit):
            self.cli.__get_input__(False, "file.txt")

    def test_file_input_fail_on_extension(self) -> None:
        """
        Test the cli with file input with the wrong file extension
        """
        with self.assertRaises(SystemExit):
            self.cli.__get_input__(False, "file.pdf")
