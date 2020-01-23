#!/bin/bash
# Too lazy to write a proper makefile for such a simple demo

python3 ../../src/main.py charcount.cat;
python3 ../../src/main.py charcount.h;
python3 ../../src/main.py main.cat;
gcc -c charcount.pp.c -o charcount.o;
gcc main.pp.c charcount.o -o demo_program;