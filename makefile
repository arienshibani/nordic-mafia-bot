# Makefile for Beer Recommendation System

PYTHON := python3.12  # Specify the required Python version
VENV := venv
REQ := src/requirements.txt
SRC := src
MAIN := main.py

start: setup run  ## Set up the environment and run the script

setup:  ## Set up the virtual environment and install dependencies
	@echo "Checking if $(PYTHON) is installed..."
	@if ! command -v $(PYTHON) &> /dev/null; then \
		echo "Error: $(PYTHON) is not installed. Please install Python 3.12."; \
		exit 1; \
	fi

	@echo "Creating virtual environment..."
	@if [ ! -d "$(VENV)" ]; then \
		$(PYTHON) -m venv $(VENV); \
		echo "Virtual environment created."; \
	fi
	@echo "Activating virtual environment and installing packages..."
	@. $(VENV)/bin/activate && \
		pip install -r $(REQ)

run:  ## Run the main script
	@echo "Setup the environment and run the bot..."
	@. $(VENV)/bin/activate && \
		cd $(SRC) && $(PYTHON) $(MAIN)

clean:  ## Remove the virtual environment
	@echo "Cleaning up..."
	@rm -rf $(VENV)

help:  ## Show this help
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
