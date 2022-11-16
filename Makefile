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

migrate: prepare_venv
	${PYTHON} -m manage makemigrations
	${PYTHON} -m manage migrate

serve: prepare_venv
	${PYTHON} -m manage runserver

test: prepare_venv
	${PYTHON} -m manage test
	${PYTHON} -m pytest -v

test_planets: prepare_venv
	${PYTHON} -m manage test planets
	${PYTHON} -m pytest -v planets

test_movies: prepare_venv
	${PYTHON} -m manage test movies
	${PYTHON} -m pytest -v movies

test_characters: prepare_venv
	${PYTHON} -m manage test characters
	${PYTHON} -m pytest -v characters
