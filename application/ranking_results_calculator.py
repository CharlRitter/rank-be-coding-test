import sys

from lib.constants import SCORE_POINTS


class ResultCalculator:
    def __init__(self, raw_results):
        self.raw_results = raw_results
        self.leaderboard = {}

    def process_results(self):
        try:
            for match_outcome in self.raw_results:
                team_and_scores = match_outcome.split(", ")

                team_and_score_1 = team_and_scores[0].split(" ")
                score_1 = team_and_score_1.pop()
                team_1 = " ".join(team_and_score_1)

                team_and_score_2 = team_and_scores[1].split(" ")
                score_2 = team_and_score_2.pop()
                team_2 = " ".join(team_and_score_2)

                points_1, points_2 = self.__calculate_points__(score_1, score_2)

                if team_1 in self.leaderboard:
                    self.leaderboard[team_1] += points_1
                else:
                    self.leaderboard[team_1] = points_1

                if team_2 in self.leaderboard:
                    self.leaderboard[team_2] += points_2
                else:
                    self.leaderboard[team_2] = points_2

            self.leaderboard = dict(
                sorted(
                    dict(sorted(self.leaderboard.items(), key=lambda item: (item[0].lower()))).items(),
                    key=lambda item: (item[1]),
                    reverse=True,
                )
            )

            # print(self.leaderboard)
            # TO DO Return final dict or invoke generate file method directly

        except Exception:  # pylint: disable=broad-except
            print("Input does not match the expected format. Application is quitting...")
            sys.exit()

    def __calculate_points__(self, score_1, score_2):
        if score_1 > score_2:
            return SCORE_POINTS["WIN"], SCORE_POINTS["LOSS"]

        if score_1 < score_2:
            return SCORE_POINTS["LOSS"], SCORE_POINTS["WIN"]

        return SCORE_POINTS["DRAW"], SCORE_POINTS["DRAW"]

    def __generate_file__(self):
        print("TODO")
