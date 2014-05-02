all: run
run: main.py
	python main.py $(FILENAME) $(MIN_SUP) $(MIN_CONF)

