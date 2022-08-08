checkfiles = application tests cli.py setup.py

help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    update        Updates dev/test dependencies"
	@echo  "    deps          Installs dev/test dependencies"
	@echo  "    lint          Reports/Fixes linter violations"
	@echo  "    test          Runs all tests"
	@echo  "    compile       Compiles the application into an executale file"

update:
	pip-compile -U --no-emit-index-url --no-emit-trusted-host requirements.in
	pip-compile -U --no-emit-index-url --no-emit-trusted-host dev-requirements.in

deps:
	@pip install --upgrade pip
	@pip install -q pip-tools
	@pip-sync requirements.txt dev-requirements.txt
	@pip install --no-cache-dir -qe .
	@pre-commit install

lint:
	isort $(checkfiles)
	black $(checkfiles)
	-flake8 $(checkfiles)
	-pylint $(checkfiles) -r n -f colorized

test:
	scripts/test.sh

compile:
	pyinstaller --onefile cli.py --name ranking_calculator
	mv ./dist/ranking_calculator ./
	rm -rf build
	rm -rf dist
