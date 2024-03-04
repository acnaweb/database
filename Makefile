# Local development
install:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \	
	pip install -e .[interactive]; \
	
# Continuous Integration
typing: formatter
	mypy src

lint:
	flake8  src

build:
	python setup.py install

test:
	pytest
