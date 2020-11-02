# Required executables
ifeq (, $(shell which python3))
 $(error "No python3 on PATH.")
endif
ifeq (, $(shell which pipenv))
 $(error "No pipenv on PATH.")
endif

# Suppress warning if pipenv is started inside .venv
#export PIPENV_VERBOSITY=1
# Use relative .venv folder instead of home-folder based
export PIPENV_VENV_IN_PROJECT=1
# Ignore existing venvs (required for travis)
export PIPENV_IGNORE_VIRTUALENVS=1
# Setup python path
export PYTHONPATH=.
# Make sure we are running with an explicit encoding
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
# Current package parameters
VERSION = $(shell python3 setup.py --version)
NAME = $(shell python3 setup.py --name)
# Help REGEX
#HELP_REGEX = "(\S*:).*(\s###\s)(.*)(?=\s###)"

all: clean venv sync

run: ### Run the script ###
	pipenv run python3 $(NAME)

venv: clean ### Initialize virtualenv, i.e., install required packages etc. ###
	LD_LIBRARY_PATH=$HOME/.mujoco/mujoco200/bin
	pipenv --three install --dev

clean: ### Clean project ###
	rm -rfv .venv .tox .egg build dist src
	find . -type d -name ".ropeproject" -exec rm -rf "{}" +;
	find . -type d -name ".pytest_cache" -exec rm -rf "{}" +;
	find . -type d -name "__pycache__" -exec rm -rf "{}" +;

test: ### Run all tests ###
	pipenv run pytest tests

coverage: ### NOT IMPLEMENTED: Run test coverage checks ###
	@echo NOT IMPLEMENTED: codecov

isort: ### Check for incorrectly sorted imports ###
	pipenv run isort $(NAME) tests

lint: ### Run code formatting checks ###
	pipenv run flake8 $(NAME) tests

reformat: isort ### Reformat code with Black ###
	pipenv run black $(NAME) tests

build: test coverage isort reformat lint ### NOT IMPLEMENTED: BUILD ###
	@echo NOT IMPLEMENTED: Build

sync: ### Sync git submodule for UDRFs ###
	git submodule update --remote --recursive
	git submodule sync --recursive

help: ### Prints this help message ###
	@echo Syntax: make [target]
	@echo Targets:
	@IFS=$$"\n"; \
	grep -ahoP "(\S*:).*(\s###\s)(.*)(?=\s###)" $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?### "}; {printf "\t%-20s %s\n", $$1, $$2}'