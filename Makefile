PYTHON := python3
ifeq ($(OS),Windows_NT)
	PYTHON := python
endif

run:
	$(PYTHON) main.py