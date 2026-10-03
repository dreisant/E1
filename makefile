CC ?= gcc
CFLAGS ?= -Wall -Wextra
FLEX ?= flex
TARGET = e1

PYTHON ?= python3
ifeq ($(OS),Windows_NT)
    PYTHON := python
    BIN := $(TARGET).exe
else
    BIN := ./$(TARGET)
endif

.PHONY: all compile test run clean

all: compile

compile: scanner.l main.c token.h
	$(FLEX) -o scanner.c scanner.l
	$(CC) $(CFLAGS) -o $(TARGET) main.c scanner.c

test:
	$(PYTHON) executar_testes.py

run:
	$(BIN)

clean:
ifeq ($(OS),Windows_NT)
	-cmd /C "del /Q scanner.c $(TARGET).exe $(TARGET) *.o 2>nul"
	-cmd /C "if exist __pycache__ rmdir /S /Q __pycache__"
else
	rm -f scanner.c $(TARGET) $(TARGET).exe *.o
	rm -rf __pycache__
endif
