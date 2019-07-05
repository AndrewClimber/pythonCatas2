'''
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''


import re
# aka
def reverse_words(text):
    return " ".join(map(lambda text: text[::-1], text.split(' ')))



# codewars
def reverse_words1(text):
    return re.sub(r'([^ ]+)', lambda x: x.group()[::-1], text)

###################################################
def reverse_words2(str):
    return ' '.join(x[::-1] for x in str.split(" "))



print(reverse_words("asd                    sasdf 2343"))
