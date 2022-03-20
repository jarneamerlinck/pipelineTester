#!/usr/bin/env python3

# Imports
import math
import abc
# Start



def formatting(a, b):
    return b.format(a)


class superClass():
    def execute(self, a, b):
        pass

class adding(superClass):
    def execute(self, a, b):
        return a+b

class divide(superClass):
    def execute(self, a, b):
        return a/b
