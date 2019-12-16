PYTHON?=python
SOURCES=infer_license setup.py

.PHONY: venv
venv:
	$(PYTHON) -m venv .venv
	source .venv/bin/activate && make setup
	@echo 'run `source .venv/bin/activate` to use virtualenv'

# The rest of these are intended to be run within the venv, where python points
# to whatever was used to set up the venv.

.PHONY: setup
setup:
	$(PYTHON) -m pip install -Ur requirements-dev.txt

.PHONY: test
test:
	$(PYTHON) -m coverage run -m infer_license.tests $(TESTOPTS)
	$(PYTHON) -m coverage report

.PHONY: format
format:
	$(PYTHON) -m isort --recursive -y $(SOURCES)
	$(PYTHON) -m black $(SOURCES)

.PHONY: lint
lint:
	$(PYTHON) -m isort --recursive --diff $(SOURCES)
	$(PYTHON) -m black --check $(SOURCES)
	$(PYTHON) -m flake8 $(SOURCES)
	$(PYTHON) -m mypy --strict infer_license

.PHONY: release
release:
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
