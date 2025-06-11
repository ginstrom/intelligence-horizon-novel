.PHONY: help build wordcount bootstrap

# Default target
help:
	@echo "Available commands:"
	@echo "  help      - Show this help message"
	@echo "  build     - Generate master document from chapters"
	@echo "  wordcount - Display word count statistics"
	@echo "  bootstrap - Set up Python virtual environment and install dependencies"

build:
	python scripts/create_master.py --smart-quotes > build/intelligence-horizon.md
	@echo "Master document generated: build/intelligence-horizon.md"

wordcount:
	python scripts/wordcount.py

bootstrap:
	python -m venv venv
	./venv/bin/pip install -r scripts/requirements.txt
	@echo "Virtual environment created and dependencies installed."
	@echo "To activate: source venv/bin/activate"
