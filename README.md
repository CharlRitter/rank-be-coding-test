<h1 align="center"> SPAN BE Coding Test </h1> <br>

<p align="center">
  This is my solution to the Back-End coding challenge as part of SPAN's interview process
</p>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Project Structure](#project-structure)
- [How To Run The CLI](#how-to-run-the-cli)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
  - [Update requirements](#update-requirements)
  - [Installs dependencies](#installs-dependencies)
- [Problem Statement](#problem-statement)
- [Miscellaneous](#miscellaneous)
  - [Compiling into executale file](#compiling-into-executale-file)
  - [Running the tests](#running-the-tests)
  - [Running the linting checks](#running-the-linting-checks)


## Project Structure
.
├── Makefile
├── README.md
├── application
│   ├── cli.py
│   └── ranking_results_calculator.py
├── assets
│   ├── problem_statement_1.png
│   └── problem_statement_2.png
├── dev-requirements.in
├── dev-requirements.txt
├── lib
│   └── constants.py
├── pyproject.toml
├── requirements.in
├── requirements.txt
├── results
├── scripts
│   └── test.sh
├── setup.py
├── test_input
│   └── example_input.txt
├── tests
│   ├── test_cli.py
│   └── test_ranking_results_calculator.py
└── version

## How To Run The CLI
1. TODO

## Technologies Used
- For the creation of the CLI, the `argparse` library was used.
- For compiling the application into an executable file the `pyinstaller` library was used.
- For testing the `pytest`, `coverage`, `mockito` & `parameterized` libraries were used.
- For code quality the `pre-commit`, `black`, `flake8`, `isort`, & `pylint` libraries were used.
- For dependency management the `pip-tools` library was used.

## Installation Instructions
Before running the following commands, please ensure you have started a virtual environment.

### Update requirements
`make update`

### Installs dependencies
`make deps`

## Problem Statement
![page1](https://github.com/CharlRitter/span-ranking-coding-test/blob/main/assets/problem_statement_1.png)
![page2](https://github.com/CharlRitter/span-ranking-coding-test/blob/main/assets/problem_statement_2.png)

## Miscellaneous
Before running the following commands, please ensure you have started a virtual environment and run the `make deps` command.

###  Compiling into executale file
`make compile`

### Running the tests
`make test`

### Running the linting checks
`make lint`
