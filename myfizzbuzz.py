def fizzbuzz(num):
    if num % 15 == 0:
            return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizzbuzz_extendible(num, user_dict):
    """ this function will accept a number and a dictionary.
    the dict's keys are suarched for num. if num is found, the
    appropriate output will be displayed; if it isn't found, num will
    be given the regular fizzbull evaluation."""
    if num in user_dict:
        return user_dict[num] + 'FizzBuzz'
    else:
        return fizzbuzz(num)