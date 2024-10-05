def bubble_sort(lst):
    """
    Функция сортирует список методом пузырьковой сортировки и возвращает отсортированную копию списка.

    :param lst: Список чисел
    :return: Отсортированный список
    """
    sorted_lst = lst.copy()
    for i in range(len(sorted_lst)):
        for j in range(0, len(sorted_lst) - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    return sorted_lst
