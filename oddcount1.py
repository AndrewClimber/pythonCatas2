# -*- coding: utf-8 -*-
'''
8 kyu Count Odd Numbers below n
Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
'''
# aka
def odd_count(n):
    return n//2
# codewars
def oddCount(n):
    return n >> 1
####
def odd_count(n):
    return len(range(1, n, 2))

## what is this ??
odd_count=2 .__rdiv__

## what is this ??
odd_count = (2).__rfloordiv__
