#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Noah"

import sys


def is_nested(line):
    line = list(line)
    i = 0
    while i < len(line) - 1:
        if(line[i] == "(" and line[i + 1] == "*"):
            line[i] = "(*"
            line.pop(i + 1)
        elif(line[i] == "*" and line[i + 1] == ")"):
            line[i] = "*)"
            line.pop(i + 1)
        i += 1
    i = 0
    stack = []

    for index, i  in enumerate(line):
        if(i in ["(","[","{","(*","<"]):
            stack.append(i)
        elif(i in [")","]","}","*)",">"]):
            if(stack[-1] + i in ["()", "[]", "{}", "(**)", "<>"]):
                stack.pop()
            else:
                return ("No " +  str(index + 1))
    if len(stack) == 0:
        return "Yes"
    else:
        return "No " + str(len(line))

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    open('output.txt', 'w').close()
    lineArray = []
    with open("input.txt") as fp:
        lineArray = fp.readlines()
    for i in lineArray:
        f = open("output.txt", "a")
        text = is_nested(i)
        f.write(text + "\n")
        f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
