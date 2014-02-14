fizzbuzz
========

My solution for fizzbuzz

This file contains two functions:

fizzbuzz(num)
fizzbuzz_extendible(num, userdict)

In the first, if num is divisible by 3 and 5, the function returns FizzBuzz; if divisible by 3, Fizz; if divisible by 5, Buzz. If num is not divisible by 3 or 5, then num is returned as a string.

In the second, a user-created dictionary can be used to give numbers others than multiples of 3 & 5 special sounds prepended to 'FizzBuzz'.

e.g.

userdict = {1:'ting', 2:'pop', 967:'whiz!'}
fizzbuzz_extendible(967, userdict)
>>> whiz!FizzBuzz
