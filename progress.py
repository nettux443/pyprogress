#!/usr/bin/python

import sys

class ProgressBar (object):
    def __init__(self, length = 50):
        """
        create object at 0 percent and set the size of the bar on screen
        50 by default
        """
        self.length = length
        self.current = 0

    def get(self):
        """
        return the current percentage
        """
        return self.current

    def set(self, i):
        """
        set the current percentage
        """
        if i > 100:
            i = 100
        if i < 0:
            i = 0
        self.current = i

    def increment(self, i):
        """
        increment the current percentage by i
        """
        if self.current <= 100 - i:
            self.current += i
        else:
            self.current = 100

    def show(self):
        """
        display the bar
        """
        i = self.current / (100/self.length)
        sys.stdout.write(("\r%s %% " % str(self.current).rjust(4)) + "[" + ("=" * i) + ">" + (" " * (self.length - i)) + "\b]")
        sys.stdout.flush()

# example usage
"""
import time
import progress
bar = progress.ProgressBar(10)
for i in range(0, 101):
    bar.increment(1)
    bar.show()
    if i == 100:
        print "\nDone"
    else:
        time.sleep(0.1)
"""
