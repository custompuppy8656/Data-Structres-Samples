def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        value_to_sort = list_a[i]
        while list_a[i-1]>value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1
    return  list_a
print(insertion_sort([7,8,9,8,9,5,4,3,2,6,1,1,2,3,4,5,6,9,8,7]))