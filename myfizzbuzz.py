def fizzbuzz(num):
    if num % 15 == 0:
            return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

print fizzbuzz(48)
print fizzbuzz(-99)
print fizzbuzz(15**3)

def fizzbuzz_extendible(num, user_dict):
    """ this function will accept a number and a dictionary.
    the dict's keys are suarched for num. if num is found, and num % key == 0,
    appropriate output will be displayed; if it isn't found, num will
    be given the regular fizzbull evaluation."""
    for key in user_dict:
        if num % key == 0:
            return user_dict[key] + 'FizzBuzz'
    else:
        return fizzbuzz(num)

extra_sounds = {2:'ping', 87:'doink', 77:'plink'}
fizzbuzz_extendible(8, extra_sounds)
fizzbuzz_extendible(15, extra_sounds)
fizzbuzz_extendible(87, extra_sounds)