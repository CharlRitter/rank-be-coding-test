<h1 align="center"> SPAN BE Coding Test </h1> <br>

<p align="center">
  This is my solution to the Back-End coding challenge as part of SPAN's interview process
</p>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Project Structure](#project-structure)
- [How To Run The CLI](#how-to-run-the-cli)
  - [1. Compiled executale (preferred)](#1-compiled-executale-preferred)
  - [2. Directly executing the CLI using](#2-directly-executing-the-cli-using)
- [Technologies Used](#technologies-used)
- [Future Expansions](#future-expansions)
- [Installation Instructions](#installation-instructions)
  - [Update requirements](#update-requirements)
  - [Installs dependencies](#installs-dependencies)
- [Problem Statement](#problem-statement)
- [Miscellaneous](#miscellaneous)
  - [Compiling into executale file](#compiling-into-executale-file)
  - [Running the tests](#running-the-tests)
  - [Running the linting checks](#running-the-linting-checks)


## Project Structure
```bash
.
├── Makefile
├── README.md
├── application
│   └── ranking_calculator.py
├── assets
│   ├── problem_statement_1.png
│   └── problem_statement_2.png
├── cli.py
├── dev-requirements.in
├── dev-requirements.txt
├── lib
│   └── constants.py
├── pyproject.toml
├── requirements.in
├── requirements.txt
├── results
├── scripts
│   └── test.sh
├── setup.py
├── test_input
│   └── example_input.txt
├── tests
│   ├── test_cli.py
│   └── test_ranking_calculator.py
└── version
```

## How To Run The CLI
The CLI has 2 flags to specify input. `-i, --input` indicates manual input and `-p path, --path path` provides the path to the file to be used as input.
The CLI also has 2 suppourting flags. `-h, --help` for help and `-v, --version ` for the CLI's version.

There are 2 ways one can run this project

### 1. Compiled executale (preferred)
Note: Since this project should run on OSX, I will have included a OSX compatible executable file in the root folder already.
1. Clone the repo
2. Create a virtual environment
3. Run `make deps`
4. Run `make compile`
5. In the root folder a new exe file should appear
6. From the root folder the CLI can be started using the executale. PS. try `ranking_calculator -h`

### 2. Directly executing the CLI using
1. Clone the repo
2. Create a virtual environment
3. Run `make deps`
4. From the root folder the CLI can be started using python. PS. try `python cli.py -h`



## Technologies Used
- For the creation of the CLI, the `argparse` library was used.
- For compiling the application into an executable file the `pyinstaller` library was used. The executale has to be regenerated on different operating systems, as it generates and executable file for that type of operating system.
- For testing the `pytest`, `coverage`, `mockito` & `parameterized` libraries were used.
- For code quality the `pre-commit`, `black`, `flake8`, `isort`, & `pylint` libraries were used.
- For dependency management the `pip-tools` library was used.
- Github actions were used to automate testing & linting

## Future Expansions
- Using the Github actions, it would've been useful to automate the compilation to an executable file as well, but since `pyinstaller` compiles the exectable to be compatible with the OS the user is using, the compiled executable file would only work on the OS of whatever Github runs their actions on (some light-weight Linux probably). Thus in future it would be great to find a library that can compile it into three executable files, one for the 3 most popular OS's, and have it auto compile as part of Github actions.

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
