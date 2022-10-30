from random import randint


def get_unique_list_numbers() -> list[int]:
    left_border = -10
    right_border = 10
    amount = 15
    list_ = []
    while len(list_) != 15:
        i = randint(left_border, right_border)
        if i not in list_:
            list_.append(i)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
