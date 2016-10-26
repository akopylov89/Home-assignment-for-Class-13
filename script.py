
def to_weird(text):
    text_list = text.split(' ')
    final_text = ''
    for word in text_list:
        count = 0
        for i in word:
            if count % 2 == 0:
                final_text += i.upper()
            else:
                final_text += i.lower()
            count += 1
        final_text += ' '
    return final_text

def sum(*args):
    sum_of_int = 0
    for i in args:
        if type(i) == int:
            sum_of_int += i
    return sum_of_int

def spam(number):
    return 'egg'*number

def int_to_words(number):
    dict_of_numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                       7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
                       12: 'twelve', 13: 'thirteen', 14:'fourteen', 15: 'fifteen',
                       16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    dict_of_tens = {2: 'twenty', 3: 'thirty', 4: 'forty',
                    5: 'fifty', 6: 'sixty', 7: 'seventy',
                    8: 'eighty', 9: 'ninety'}
    dict_of_ranks = {100: 'hundred', 1000: 'thousand'}
    in_words = ''
    if number//100000 >= 1:
        in_words = in_words + dict_of_numbers[number//100000] + ' ' + dict_of_ranks[100] + ' '
        number = number % 100000
        if number > 0:
            in_words += 'and '
    if number//10000 >= 1:
        if number//1000 >= 20:
            if (number % 10000) < 1:
                in_words += dict_of_tens[number//10000] + ' ' + dict_of_ranks[1000] + ' '
            else:
                in_words += dict_of_tens[number//10000] + ' ' +\
                            dict_of_numbers[number//1000 - (number//10000)*10] + ' ' + dict_of_ranks[1000] + ' '
        else:
            in_words += dict_of_numbers[number//1000] + ' ' + dict_of_ranks[1000] + ' '
        number = number % 10000
        number = number % 1000
    if number//1000 >= 1:
        in_words += dict_of_numbers[number//1000] + ' ' + dict_of_ranks[1000] + ' '
        number = number % 1000
    if number//100 >= 1:
        in_words += dict_of_numbers[number//100] + ' ' + dict_of_ranks[100] + ' '
        number = number % 100
    if number//10 >= 1:
        if number//10 >= 2:
            if (number % 10) < 1:
                in_words += dict_of_numbers[number//10]
            else:
                in_words += dict_of_tens[number//10] + ' ' + dict_of_numbers[number - (number//10)*10]
        else:
            in_words += dict_of_numbers[number]
    if number//10 < 1 and number//10 != 0:
        in_words += dict_of_numbers[number]
    if number//10 == 0:
        in_words = in_words
    return in_words


print(to_weird('abcdf sansdn asndnsa'))

print(int_to_words(34010))