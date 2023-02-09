# Referencia [1]
# Referencia [2] - adaptada
def merge_sort(array):
    if not array:
        return []

    if len(array) == 1:
        return [array[0]]

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] > right[0]:
        return [right[0]] + merge(left, right[1:])
    else:
        return [left[0]] + merge(left[1:], right)


def is_anagram(first_string, second_string):
    # Comparar duas strings:
    #  Ordenar e verificar se uma é anagrama da outra

    array1 = merge_sort(first_string.lower())
    array2 = merge_sort(second_string.lower())

    join_first = ''.join(array1)
    join_second = ''.join(array2)

    if first_string == '' or second_string == '':
        return (join_first, join_second, False)

    for index, _ in enumerate(array1):
        if array1[index] != array2[index]:
            return (join_first, join_second, False)

    return (join_first, join_second, True)

# Referencia
# /https://panda.ime.usp.br/panda/static/
# pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html
# teste = is_anagram("muro", "RuMo")
# print(teste)

# Referencias:
# [1]: Course dia 3- exercicios (merge)
# [2]: https://www.freecodecamp.org/portuguese
# /news/algoritmos-de-ordenacao-explicados-com-exemplos-em-python-java-e-c/
