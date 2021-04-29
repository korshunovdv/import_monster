PACKAGE_NAME="import_monster"
REQUIREMENTS_DEV="requirements-dev.txt"
REQUIREMENTS="requirements.txt"

test:
	@py.test tests

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -rf `find . -type d -name '.pytest_cache' `
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@python setup.py clean
	@rm -rf .tox
	@rm -f .develop
	@rm -f .flake

uninstall:
	@pip uninstall ${PACKAGE_NAME} -y

install-dev: uninstall
	@python -m pip install --upgrade pip
	@pip install -r ${REQUIREMENTS_DEV}
	@pip install -e .

install: uninstall
	@python -m pip install --upgrade pip
	@pip install -r ${REQUIREMENTS}
	@pip install -e .
	@echo "Done"

install-pre-commit: install-dev
	@pre-commit install

run-pre-commit: install-pre-commit
	@pre-commit run --all-files

.PHONY: all install-dev uninstall clean test
