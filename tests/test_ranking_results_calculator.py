"""
Tests the RankingResultsCalculator class.
"""
from typing import Dict, Tuple
from unittest import TestCase

from mockito import expect, unstub, verifyNoUnwantedInteractions
from parameterized import parameterized

from application.ranking_results_calculator import RankingResultsCalculator
from lib.constants import SCORE_POINTS


class TestRankingResultsCalculator(TestCase):
    def setUp(self) -> None:
        self.ranking_results_calculator = RankingResultsCalculator()

    def tearDown(self) -> None:
        verifyNoUnwantedInteractions()
        unstub()

    @parameterized.expand(
        [
            # score_1 > score_2
            (
                {"score_1": 3, "score_2": 1},
                (SCORE_POINTS["WIN"], SCORE_POINTS["LOSS"]),
            ),
            # score_1 < score_2
            (
                {"score_1": 1, "score_2": 3},
                (SCORE_POINTS["LOSS"], SCORE_POINTS["WIN"]),
            ),
            # score_1 == score_2
            (
                {"score_1": 3, "score_2": 3},
                (SCORE_POINTS["DRAW"], SCORE_POINTS["DRAW"]),
            ),
        ],
    )
    def test_calculate_points(self, test_input: Dict, test_output: Tuple[int, int]) -> None:
        """
        Test the calculation of ranking points
        """
        assert self.ranking_results_calculator.__calculate_points__(**test_input) == test_output

    @parameterized.expand(
        [
            # Test just on scores
            (
                {"A Team": 2, "B Team": 3, "C Team": 7, "D Team": 1, "E Team": 10},
                {"E Team": 10, "C Team": 7, "B Team": 3, "A Team": 2, "D Team": 1},
            ),
            # Test just on names
            (
                {"G Team": 2, "K Team": 2, "C Team": 2, "Y Team": 2, "E Team": 2},
                {"C Team": 2, "E Team": 2, "G Team": 2, "K Team": 2, "Y Team": 2},
            ),
            # Test just on both scores & names
            (
                {
                    "A Team": 2,
                    "FC Team": 5,
                    "I Team": 3,
                    "C Team": 7,
                    "H Team": 5,
                    "D Team": 1,
                    "B Team": 3,
                    "E Team": 10,
                    "F Team": 5,
                },
                {
                    "E Team": 10,
                    "C Team": 7,
                    "F Team": 5,
                    "FC Team": 5,
                    "H Team": 5,
                    "B Team": 3,
                    "I Team": 3,
                    "A Team": 2,
                    "D Team": 1,
                },
            ),
        ],
    )
    def test_sort_leaderboard(self, test_input: Dict, test_output: Dict) -> None:
        """
        Test the sorting of the leaderboard
        """
        assert self.ranking_results_calculator.__sort_leaderboard__(test_input) == test_output

    def test_generate_results_file_success(self) -> None:
        """
        Test the generate results file function with correct input
        """
        leaderboard = {"FC Awesome": 3, "Snakes": 3, "Lions": 0, "Tarantulas": 0}

        assert self.ranking_results_calculator.__generate_results_file__(leaderboard) is None

    def test_generate_results_file_fail(self) -> None:
        """
        Test the generate results file function with incorrect input
        """
        leaderboard = ["This is not the right format"]

        with self.assertRaises(SystemExit):
            self.ranking_results_calculator.__generate_results_file__(leaderboard)

    def test_process_results_success(self) -> None:
        """
        Test the process results function with correct input
        """
        score_1 = 5
        score_2 = 7
        points = (0, 3)
        unsorted_leaderboard = {"Lions": 0, "Snakes": 3, "Tarantulas": 0, "FC Awesome": 3}
        sorted_leaderboard = {"FC Awesome": 3, "Snakes": 3, "Lions": 0, "Tarantulas": 0}
        raw_input = ["Lions 5, Snakes 7", "Tarantulas 5, FC Awesome 7"]

        expect(RankingResultsCalculator, times=2).__calculate_points__(score_1, score_2).thenReturn(points)
        expect(RankingResultsCalculator, times=1).__sort_leaderboard__(unsorted_leaderboard).thenReturn(
            sorted_leaderboard
        )
        expect(RankingResultsCalculator, times=1).__generate_results_file__(sorted_leaderboard).thenReturn(None)

        assert self.ranking_results_calculator.process_results(raw_input) is None

    def test_process_results_fail(self) -> None:
        """
        Test the process results function with incorrect input
        """
        raw_input = ["This is not the right format"]

        with self.assertRaises(SystemExit):
            self.ranking_results_calculator.process_results(raw_input)
