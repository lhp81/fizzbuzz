def fizzbuzz(num):
    onomatopeia = ''
    if num % 3 == 0:
        onomatopeia += 'Fizz'
    if num % 5 == 0:
        onomatopeia += 'Buzz'
    if onomatopeia is not '':
        return onomatopeia
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
    opnomatopeia = ''
    if num % 3 == 0:
        opnomatopeia += 'Fizz'
    if num % 5 == 0:
        opnomatopeia += 'Buzz'
    for key in user_dict:
        if num % key == 0:
            opnomatopeia += user_dict[key]
    if len(opnomatopeia) == 0:
        return str(num)
    else:
        return opnomatopeia

extra_sounds = {2:'ping', 9:'pfffft', 11:'tzzzzzzap', 87:'doink', 77:'plink'}
print fizzbuzz_extendible(8, extra_sounds)
print fizzbuzz_extendible(15, extra_sounds)
print fizzbuzz_extendible(87, extra_sounds)
