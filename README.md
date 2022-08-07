<h1 align="center"> SPAN BE Coding Test </h1> <br>

<p align="center">
  This is my solution to the Back-End coding challenge as part of SPAN's interview process
</p>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Project Structure](#project-structure)
- [Installation Instructions](#installation-instructions)
  - [Update requirements](#update-requirements)
  - [Installs dependencies](#installs-dependencies)
- [How to run this project](#how-to-run-this-project)
- [Problem Statement](#problem-statement)
- [Miscellaneous](#miscellaneous)
  - [Running the tests](#running-the-tests)
  - [Running the linting checks](#running-the-linting-checks)


## Project Structure
```bash
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
```

## Installation Instructions
### Update requirements
```bash
make update
```

### Installs dependencies
```bash
make deps
```

## How to run this project
1. TODO

## Problem Statement
![page1](https://github.com/CharlRitter/span-ranking-coding-test/blob/main/assets/problem_statement_1.png)
![page2](https://github.com/CharlRitter/span-ranking-coding-test/blob/main/assets/problem_statement_2.png)

## Miscellaneous
### Running the tests
```bash
make test
```

### Running the linting checks
```bash
make lint
```
