def search_substring():
    my_set = set()
    search_in = input('Введите данные: ')
    for i in range(len(search_in)):
        for k in range(len(search_in)):
            if i == k:
                my_set.add(search_in[i])
            elif i < k and search_in != search_in[i:k + 1]:
                my_set.add(search_in[i:k + 1])

    return len(my_set)


print(search_substring())