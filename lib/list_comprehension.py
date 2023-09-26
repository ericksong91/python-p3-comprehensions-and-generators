#!/usr/bin/env python3
# new_list = [optional_operation(item) for item in old_list if optional_condition == True]
# condition = if % 2 is 0
#


def return_evens(num_list):
    new_list = [n for n in num_list if n % 2 == 0]
    return new_list


def make_exclamation(sentence_list):
    new_list = [f"{sent}!" for sent in sentence_list]
    return new_list


print(return_evens([1, 2, 4, 7, 9, 10, 12]))
print("Expect => [2, 4, 10, 12]")

print(make_exclamation(["Help", "Me", "Please"]))
print('Expect => ["Help!", "Me!", "Please!"]')
