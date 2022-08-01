with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    data2 = data.split('\n')
    data3 = []
    for fruits in data2:
        if 'berry' in fruits:
            data3.append(fruits)
    # for sort_fruits in data3:
    data3.remove('berryfake')
    my_set = set(data3)
    data3 = list(my_set)
    count_data = str(len(data3))
    print(count_data)

    with open('02.txt', 'w', encoding='utf-8') as f:
        f.write(count_data)
        f.write('\n')
        for sort_fruits in data3:
            f.write(f'{sort_fruits}\n')
