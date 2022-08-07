import os
import sys
from argparse import ArgumentParser
from typing import List

from application.ranking_results_calculator import RankingResultsCalculator


class CLI:
    def __create_parser__(self) -> ArgumentParser():
        with open("version", "r", encoding="utf8") as version_file:
            version = version_file.read().strip()

        parser = ArgumentParser(
            description="Calculate the ranking table for a league's results",
            prog="ranking_results_calculator",
            epilog="If no flags were provided, %(prog)s will take manual input.",
        )
        parser.version = version

        parser.add_argument(
            "-p", "--path", metavar="path", type=str, help="The path to the text file containing the match results"
        )
        parser.add_argument(
            "-i",
            "--input",
            action="store_true",
            help="Indicates that the user wants to manually input the match results",
        )
        parser.add_argument("-v", "--version", action="version", help="Shows the version of the application")

        return parser

    def __get_input__(self, manual_input_flag: bool, input_path: str = "") -> List:
        raw_input = []

        if manual_input_flag:
            print("No path was provided. Please manually enter the match results.")
            print("If you are done with entering results, please press enter on an empty line.")
            print("If you which to leave the application without executing it, please type the word 'exit'.")
            print("========================================================================================")
            print("")

            for result in sys.stdin:
                result = result.rstrip("\n")

                if "exit" in result.lower() and result.replace(" ", "").lower() == "exit":
                    sys.exit()
                elif result == "":
                    break
                else:
                    raw_input.append(result)

        elif not input_path.lower().endswith((".txt")):
            print("The path specified is not a text file.")
            sys.exit()
        elif not os.path.exists(input_path):
            print("The path specified does not exist.")
            sys.exit()
        else:
            with open(input_path, "r", encoding="utf8") as file:
                raw_input = [result.rstrip("\n") for result in file]

        if len(raw_input) == 0:
            print("No input provided. Application is quitting...")
            sys.exit()

        print(raw_input)

        return raw_input

    def main(self, argv: List = None) -> None:
        parser = self.__create_parser__()
        args = parser.parse_args(argv)

        raw_input = self.__get_input__(args.input, args.path)

        calculator = RankingResultsCalculator()
        calculator.process_results(raw_input)

        print("Leaderboard ranking completed successfully.")
        print("Please find the text file containing the leaderboard in the results folder.")


if __name__ == "__main__":  # pragma: no cover
    cli = CLI()
    cli.main()
