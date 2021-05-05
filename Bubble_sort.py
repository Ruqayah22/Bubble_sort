def swap(bubs):
    l = len(bubs)

    for i in range(l - 1):
        position = 0
        for j in range(l - 1):
            if bubs[j] > bubs[j + 1]:
                tmp = bubs[j]
                bubs[j] = bubs[j + 1]
                bubs[j + 1] = tmp

                position = 1

        if position == 0:
            break
    return bubs


swap_arr = [9, 3, 5, 4, 8, 6, 7, 1, 2]
result = swap(swap_arr)
print(result)


