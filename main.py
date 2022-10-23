import random
# tri par sélection

# l = [5, 8, 1, 4]

#  V
# [1, 5, 8, 10, 2]
# sorted / unsorted

#     V
# [1, 5, 8, 10, 2]

#            V
# [1, 5, 8, 10, 2]

# 0(N^2)


def genarate_random_list(n, min, max):
    l = []
    for i in range(n):
        l.append(random.randint(min, max))
    return l


def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[min_index] = l[unsorted_index]  # [5, 8, 10, 2, 5]

        print(l)
        l[unsorted_index] = min  # [1, 8, 10, 2, 1]


l = genarate_random_list(100, 1, 100)

print("UNSORTED:", l)

selection_sort(l)

print("SORTED:", l)
