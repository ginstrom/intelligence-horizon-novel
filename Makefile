.PHONY: help build wordcount

# Default target
help:
	@echo "Available commands:"
	@echo "  help      - Show this help message"
	@echo "  build     - Generate master document from chapters"
	@echo "  wordcount - Display word count statistics"

build:
	python scripts/create_master.py > build/intelligence-horizon.md
	@echo "Master document generated: build/intelligence-horizon.md"

wordcount:
	python scripts/wordcount.py
