#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sort(func):
    def sort_inside(line):
        return sorted(func(line))

    return sort_inside


@sort
def get_list(line):
    return [int(i) for i in line.split()]


if __name__ == '__main__':
    print(get_list(input('Введите числа через пробел: ')))