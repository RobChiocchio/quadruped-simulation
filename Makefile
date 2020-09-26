# Required executables
ifeq (, $(shell which python3))
 $(error "No python3 on PATH.")
endif
ifeq (, $(shell which pipenv))
 $(error "No pipenv on PATH.")
endif

# Suppress warning if pipenv is started inside .venv
export PIPENV_VERBOSITY=1
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


all: clean venv run

run:
	@echo Run the script
	pipenv run python3 $(NAME)

venv: clean
	@echo Initialize virtualenv, i.e., install required packages etc.
	LD_LIBRARY_PATH=$HOME/.mujoco/mujoco200/bin
	pipenv --three install --dev

clean:
	@echo Clean project
	rm -rfv .venv .tox .egg build dist src
	find . -type d -name ".ropeproject" -exec rm -rf "{}" +;
	find . -type d -name ".pytest_cache" -exec rm -rf "{}" +;
	find . -type d -name "__pycache__" -exec rm -rf "{}" +;

test:
	@echo Run all tests
	pipenv run pytest tests

coverage:
	@echo NOT IMPLEMENTED: Run test coverage checks

isort:
	@echo Check for incorrectly sorted imports
	pipenv run isort $(NAME) tests

lint:
	@echo Run code formatting checks
	pipenv run flake8 $(NAME) tests

reformat: isort
	@echo Reformat code with Black
	pipenv run black $(NAME) tests

build: test coverage isort reformat lint
	@echo NOT IMPLEMENTED: Build