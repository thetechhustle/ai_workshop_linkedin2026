.PHONY: help install setup run test lint format check serve docs-serve docs-build clean tmux docker-build docker-run

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(PY) -m pip
MKDOCS := $(VENV)/bin/mkdocs
PORT ?= 8000

help:
	@echo "LinkedIn AI Workshop 2026"
	@echo ""
	@echo "make install      Create .venv and install docs + starter app dependencies"
	@echo "make run          Run the Opportunity Tracker API on http://127.0.0.1:$(PORT)"
	@echo "make test         Run the starter app tests"
	@echo "make lint         Run ruff checks"
	@echo "make format       Format starter app code with ruff"
	@echo "make check        Run lint, tests, and docs build"
	@echo "make serve        Serve the course site locally"
	@echo "make tmux         Launch the workshop tmux cockpit"
	@echo "make clean        Remove generated files"

$(PY):
	python3 -m venv $(VENV)

install: $(PY)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e "starter_app[dev]"

setup: install

run: install
	$(PY) -m uvicorn opportunity_tracker.app:app --app-dir starter_app/src --reload --host 127.0.0.1 --port $(PORT)

test: install
	$(PY) -m pytest starter_app/tests -q

lint: install
	$(PY) -m ruff check starter_app/src starter_app/tests

format: install
	$(PY) -m ruff format starter_app/src starter_app/tests

check: lint test docs-build

docs-serve: install
	$(MKDOCS) serve --dev-addr 127.0.0.1:8001

serve: docs-serve

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
