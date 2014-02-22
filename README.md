fizzbuzz
========

[![Build Status](https://travis-ci.org/lhp81/fizzbuzz.png?branch=master)](https://travis-ci.org/lhp81/fizzbuzz)
My solution for fizzbuzz

This file contains two functions:

fizzbuzz(num)
fizzbuzz_extendible(num, userdict)

In the first, if num is divisible by 3 and 5, the function returns FizzBuzz; if divisible by 3, Fizz; if divisible by 5, Buzz. If num is not divisible by 3 or 5, then num is returned as a string.

In the second, a user-created dictionary can be used to give numbers others than multiples of 3 & 5 special sounds. 3 & 5 are analyzed on their own in order to make sure FizzBuzz will appear together (if appropriate).

e.g.

userdict = {1:'ting', 2:'pop', 967:'whiz!'}
fizzbuzz_extendible(967, userdict)
>>> whiz!
