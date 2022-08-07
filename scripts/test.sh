#!/usr/bin/env bash
# Run all tests with coverage report
coverage erase
coverage run --source=application -m pytest -v tests/
passed=$?
coverage report -m
coverage xml

if [ $passed -eq 0 ]
then
    echo "All tests passed"
    exit 0
else
    echo "Some tests failed"
    exit 1
fi
