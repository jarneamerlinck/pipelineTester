#!/usr/bin/env python3

# Imports
import math
import abc
# Start



def formatting(a, b):
    return b.format(a)


class superClass():
    def execute(a, b):
        pass

class adding(superClass):
    def execute(a, b):
        return a+b

class divide(superClass):
    def execute(a, b):
        return a/b
