import argparse
import os
import sys

from ranking_results_calculator import ResultCalculator

with open("version", "r", encoding="utf8") as version_file:
    version = version_file.read().strip()

parser = argparse.ArgumentParser(
    description="Calculate the ranking table for a league's results",
    prog="ranking_results_calculator",
    epilog="If no flags were provided, %(prog)s will take manual input.",
)
parser.version = version

parser.add_argument(
    "-p", "--path", metavar="path", type=str, help="The path to the text file containing the match results"
)
parser.add_argument("-v", "--version", action="version", help="Shows the version of the application")

args = parser.parse_args()
input_path = args.path
raw_input = []


if not input_path:
    print("No path was provided. Please manually enter the match results.")
    print("If you are done with entering results, please press enter on an empty line.")
    print("If you which to leave the application without executing it, please type the word 'exit'.")
    print("========================================================================================")
    print("")

    for result in sys.stdin:
        if result.lower() == "exit":
            sys.exit()
        elif result == "\n":
            break
        else:
            raw_input.append(result.rstrip("\n"))

elif not os.path.exists(input_path):
    print("The path specified does not exist.")
    sys.exit()
elif not input_path.lower().endswith((".txt")):
    print("The path specified is not a text file.")
    sys.exit()
else:
    with open(input_path, "r", encoding="utf8") as file:
        raw_input = [result.rstrip("\n") for result in file]

calculator = ResultCalculator(raw_input)
calculator.process_results()

print("Leaderboard ranking completed successfully.")
print("Please find the text file containing the leaderboard in the results folder.")
