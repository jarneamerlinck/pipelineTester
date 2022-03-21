#!/usr/bin/env python3

# Imports
import math
import abc
import matplotlib.pyplot as plt


from tokenize import String
# Start

def makeImage():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
    plt.savefig("images/saveDemo.png")

def formatting(a:String, b:String):
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
