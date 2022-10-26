def get_count_char(str_):
    list_of_words = list(str_.lower())
    dict_ = {}
    for symbol in list_of_words:
        if symbol.isalpha():
            if symbol in dict_:
                n = dict_.get(symbol)
                n += 1
                dict_[symbol] = n
            else:
                dict_.setdefault(symbol, 1)

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

dict1 = get_count_char(main_str)

def get_char_percent(dict_):
    sum_ = sum(dict_.values())
    new_dict = {}
    for symbol in dict_:
        value = dict_.get(symbol)
        new_value = round(value / sum_ * 100, 2)
        new_dict.setdefault(symbol, new_value)
    return new_dict

print(get_char_percent(dict1))

