#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: while loops"""


def fibonacci(maxint):
    """The fibonacci sequence in a while loop"""
    new_list = [0, ]
    first, second = 0, 1
    while second <= maxint:
        first, second = second, first + second
        new_list.append(first)
    return new_list
