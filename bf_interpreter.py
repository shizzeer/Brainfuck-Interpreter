#!/usr/bin/python3
#
# Brainfuck interpreter with read from the file
# Copyright 2017 Kamil Szpakowski
#
# You can use it like this: ./bf_interpreter.py [FILENAME]

import sys


def execute(filename):
    f = open(filename, 'r')
    translate(f.read())
    f.close()


def translate(commands):

    cells, cell_pointer, code_pointer = [0], 0, 0
    bf_code = list(commands)
    stack = []

    while code_pointer < len(bf_code):

        if bf_code[code_pointer] == '>':
            cell_pointer += 1
            if cell_pointer == len(cells): cells.append(0)

        if bf_code[code_pointer] == '<':
            if cell_pointer <= 0:
                cell_pointer = 0
            else:
                cell_pointer -= 1

        if bf_code[code_pointer] == '+':
           if cells[cell_pointer] < 255:
                cells[cell_pointer] += 1
           else:
               cells[cell_pointer] = 0

        if bf_code[code_pointer] == '-':
            if cells[cell_pointer] > 0:
                cells[cell_pointer] -= 1
            else:
                cells[cell_pointer] = 255

        if bf_code[code_pointer] == '.': print(chr(cells[cell_pointer]))

        if bf_code[code_pointer] == ',': cells[cell_pointer] = ord(input('Write a sign: '))

        if bf_code[code_pointer] == '[':
            stack.append(code_pointer)

        if bf_code[code_pointer] == ']' and cells[cell_pointer] != 0:
            code_pointer = stack[-1]

        if bf_code[code_pointer] == ']' and cells[cell_pointer] == 0:
            stack.pop()

        code_pointer += 1


def main():
    if len(sys.argv) == 2: execute(sys.argv[1])
    else: print('Try:', sys.argv[0], 'filename.')


main()
