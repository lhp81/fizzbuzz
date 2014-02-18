"""
The below is Cris's code. It's here b/c it is what the lettuce demo
runs from.
What we did in class is below that.
"""

def fizzbuzz(n):
    """return a fizzbuzz-formatted representation of n"""
    if n == 0:
        return str(0)
    out = ''
    if not n % 3:
        out += 'Fizz'
    if not n % 5:
        out += 'Buzz'
    if not out:
        out = str(n)
    return out

# def fizzbuzz(num):
#     result = "" # placeholder for the sounds
#     for div, sub in subs:
#         if num % dive == 0:
#             result += sub
#         else:
#             return str(num)
#     return result

# def fizzbuzz(num):
#     if num % 15 == 0:
#         return 'FizzBuzz'
#     if num % 3 == 0:
#         return 'Fizz'
#     if num % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(num) # we do this to make sure that the return value of the
#                         # function is always the same type, no matter what it
#                         # is that's returned.

# """

# To make more Pythonic:

# (1) More extensible
# (2) Don't want separate tests.
#     * So, we're running three identical statements in series with each other.
#       Since they look like a template, let's break it down to see what the
#       variations are.
#     * We could use a dict or a tuple for input, since there is more than one
#       piece of information being inserted.
# """

# subs[(3, 'Fizz'), (5, 'Buzz'), (15, 'FizzBuzz')]

# """
# now, iterate across the tuple in the function.
# python will iterate across the tuple automatically."""

# for div, sub in subs:
#     if num % dive == 0:
#         return sub
#     else:
#         return str(num)

# """
# however, this makes us dependent upon the order of the stuff in the tuple.
# so, we need to think: do we really want/need to design this so 15 is even an
# issue?

# so, we can use an accumulator pattern."""


# result = "" # placeholder for the sounds
# for div, sub in subs:
#     if num % dive == 0:
#         result += sub
#     else:
#         return str(num)
#     return result

# """
# So that's cool. But it still makes us dependent upon the order of the tuple.
# If you're using dictionaries, then you want to sort() it so everything comes up in order.


# We don't need to say
# """

# if num % 15 == 0:

# """instead, can say:"""
# if not (num % div):

# """the else at the end isn't necessary. you can just..."""
# if not result:          # so an empty string is False.
#     result = str(num)

# """Also, there's a problem with all the ifs. """

# """
# The way that I wrote this, as I noticed, will print that stuff every time
# it's run. We need to add something like this at the bottom.
# Add the simple tests to the bottom of the file.
# That way, if we execute this file in Python, it'll raise an assertion error
# if it isn't returning the results we would expect.
# """

# if __name__ == '__main__':  # put assumption based testing in if __name_ '__main__'
#     expected = [(5, 'Buzz'), (15, 'FizzBuzz')]
#     for extected_result in expected:
#         actual_result = fizzbuzz(expected[0])
#         assert expected[1] == actual_result

# """
# To access this code, you have to run the file from the command line.
# """

# # think about iteration and iterating over the problem.
# # take a step back and think about the problem on another level.