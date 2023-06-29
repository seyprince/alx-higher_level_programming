#!/usr/bin/python3
""" creating class square """


class Square:
    """ square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("must be an integer")
        elif size < 0:
            raise ValueError("must be >= 0")
        else:
            self.__size = size
