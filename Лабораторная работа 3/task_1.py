src = not False and True or False and not True

# TODO расписать упрощение выражения
# src = True and True or False and False # избавляемся от отрицаний
# src = True or True # избавляемся от логического "И"
# src = True # избавляемся от логического "ИЛИ"

result = True

print(src == result)
