.PHONY: installs requirements and run server

PYTHON=${VENV_NAME}/bin/python

install: prepare_venv

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	python3 -m venv venv
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt
	sudo touch $(VENV_NAME)/bin/activate

serve: prepare_venv
	${PYTHON} -m manage runserver

test: prepare_venv
	${PYTHON} -m manage test
	${PYTHON} -m pytest -s

test_planets: prepare_venv
	${PYTHON} -m manage test planets
	${PYTHON} -m pytest -s planets

test_movies: prepare_venv
	${PYTHON} -m manage test movies
	${PYTHON} -m pytest -s movies

test_characters: prepare_venv
	${PYTHON} -m manage test characters
	${PYTHON} -m pytest -s characters
