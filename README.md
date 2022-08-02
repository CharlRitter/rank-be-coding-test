<h1 align="center"> Rank BE Coding Test </h1> <br>

<p align="center">
  This is my solution to the Back-End coding challenge as part of Rank's interview process
</p>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Project Structure](#project-structure)
- [Installation Instructions](#installation-instructions)
  - [Update requirements.txt](#update-requirementstxt)
  - [Update dependencies in virtual environment](#update-dependencies-in-virtual-environment)
- [Execution Instructions](#execution-instructions)
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
│   └── main.py
├── assets
│   ├── problem_statement_1.png
│   └── problem_statement_2.png
├── dev-requirements.in
├── dev-requirements.txt
├── match_results
│   └── example_results.txt
├── pre-commit-config.yaml
├── pyproject.toml
├── requirements.in
├── requirements.txt
├── tests
│   └── test_main.py
└── version
```

## Installation Instructions
### Update requirements.txt
```bash
make update
```

### Update dependencies in virtual environment
```bash
make deps
```

## Execution Instructions
```bash
make run
```

## Problem Statement
![page1](https://github.com/CharlRitter/rank-be-coding-test/blob/main/assets/problem_statement_1.png)
![page2](https://github.com/CharlRitter/rank-be-coding-test/blob/main/assets/problem_statement_2.png)

## Miscellaneous
### Running the tests
```bash
make test
```

### Running the linting checks
```bash
make lint
```
