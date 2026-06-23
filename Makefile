.PHONY: help install setup run serve docs-serve docs-build startapp app example-app test lint format check clean tmux docker-build docker-run

VENV := .venv
PORT ?= 8000
DOCS_PORT ?= 8001

ifeq ($(OS),Windows_NT)
PYTHON ?= py -3
PY := $(VENV)/Scripts/python.exe
MKDOCS := $(VENV)/Scripts/mkdocs.exe
else
PYTHON ?= python3
PY := $(VENV)/bin/python
MKDOCS := $(VENV)/bin/mkdocs
endif

PIP := $(PY) -m pip

help:
	@echo "LinkedIn AI Workshop 2026"
	@echo ""
	@echo "make install      Create .venv and install docs + starter app dependencies"
	@echo "make run          Serve the workshop book at http://127.0.0.1:$(DOCS_PORT)"
	@echo "make serve        Same as make run"
	@echo "make startapp     Run the Opportunity Tracker API at http://127.0.0.1:$(PORT)"
	@echo "make example-app  Same as make startapp"
	@echo "make test         Run the starter app tests"
	@echo "make lint         Run ruff checks"
	@echo "make format       Format starter app code with ruff"
	@echo "make check        Run lint, tests, and docs build"
	@echo "make tmux         Launch the workshop tmux cockpit"
	@echo "make clean        Remove generated files"

$(PY):
	$(PYTHON) -m venv $(VENV)

install: $(PY)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e "starter_app[dev]"

setup: install

run: docs-serve

serve: docs-serve

docs-serve: install
	$(MKDOCS) serve --dev-addr 127.0.0.1:$(DOCS_PORT)

startapp: install
	$(PY) -m uvicorn opportunity_tracker.app:app --app-dir starter_app/src --reload --host 127.0.0.1 --port $(PORT)

app: startapp

example-app: startapp

test: install
	$(PY) -m pytest starter_app/tests -q

lint: install
	$(PY) -m ruff check starter_app/src starter_app/tests

format: install
	$(PY) -m ruff format starter_app/src starter_app/tests

check: lint test docs-build

docs-build: install
	$(MKDOCS) build --strict

tmux:
	bash scripts/start_tmux_lab.sh

docker-build:
	docker build -t linkedin-ai-workshop-starter ./starter_app

docker-run:
	docker run --rm -p $(PORT):8000 linkedin-ai-workshop-starter

clean:
	rm -rf $(VENV) site .pytest_cache .ruff_cache starter_app/.pytest_cache starter_app/src/*.egg-info
