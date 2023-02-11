# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Если таких чисел, выдать внятное диагностическое сообщение
#     Примеры/Тесты:
#     Input1: 2 4 6 8 10 12 10 8 6 4 2
#     Input2: 3 6 9 12 15 18
#     Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#     Input1: 2 4 6 8 10 10 8 6 4 2
#     Input2: 3 9 12 15 18
#     Output: Повторяющихся чисел нет



lst1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
lst2 = [3, 6, 9, 12, 15, 18]

set_rez = set(lst1).intersection(set(lst2))
if len(set_rez) != 0:
    for el in sorted(list(set_rez)):
        print(el, end=" ")
else:
    print("Повторяющихся чисел нет")