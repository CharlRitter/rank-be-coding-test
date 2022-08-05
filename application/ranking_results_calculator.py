import sys
from collections import defaultdict

from lib.constants import SCORE_POINTS


class ResultCalculator:
    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.leaderboard = defaultdict(int)

    def __calculate_points__(self, score_1, score_2):
        if score_1 > score_2:
            return SCORE_POINTS["WIN"], SCORE_POINTS["LOSS"]

        if score_1 < score_2:
            return SCORE_POINTS["LOSS"], SCORE_POINTS["WIN"]

        return SCORE_POINTS["DRAW"], SCORE_POINTS["DRAW"]

    def __sort_leaderboard__(self):
        self.leaderboard = dict(
            sorted(
                dict(sorted(self.leaderboard.items(), key=lambda item: (item[0].lower()))).items(),
                key=lambda item: (item[1]),
                reverse=True,
            )
        )

    def __generate_results_file__(self):
        rank = 1
        count = 1
        old_score = None
        newline = ""

        try:
            with open("results/leaderboard_ranking.txt", "w+", encoding="utf8") as results_file:
                for team, score in self.leaderboard.items():
                    if old_score == score:
                        rank -= 1
                    else:
                        rank = count

                    results_file.write(f"{newline}{rank}. {team}, {score} {'pt' if score == 1 else 'pts'}")
                    newline = "\n"

                    rank += 1
                    count += 1
                    old_score = score
        except Exception:  # pylint: disable=broad-except
            print("An error occurred while generating the leaderboard ranking file. Application is quitting...")
            sys.exit()

    def process_results(self):
        try:
            for match_outcome in self.raw_input:
                team_and_scores = match_outcome.split(", ")

                team_and_score_1 = team_and_scores[0].split(" ")
                score_1 = team_and_score_1.pop()
                team_1 = " ".join(team_and_score_1)

                team_and_score_2 = team_and_scores[1].split(" ")
                score_2 = team_and_score_2.pop()
                team_2 = " ".join(team_and_score_2)

                points_1, points_2 = self.__calculate_points__(score_1, score_2)

                self.leaderboard[team_2] += points_2
                self.leaderboard[team_1] += points_1

        except Exception:  # pylint: disable=broad-except
            print("Input does not match the expected format. Application is quitting...")
            sys.exit()

        self.__sort_leaderboard__()
        self.__generate_results_file__()
