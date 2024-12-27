
def common_elements():
    list1 = list(range(0, 101, 3))
    list2 = list(range(0, 101, 5))
    set_list1 = set(list1)
    set_list2 = set(list2)
    set_list3 = set_list1 .intersection(set_list2)
    return set_list3


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
