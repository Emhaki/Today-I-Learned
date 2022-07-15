with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    data2 = data.split('\n')
    # data2.count()
    data3 = {}

    for i in data2:
        if i in data3:
            data3[i] += 1
        else:
            data3[i] = 1
    # print(data3)
    itemlist = str(data3.items())
    key = str(data3.keys())
    value = str(data3.values())

    with open('03.txt', 'w', encoding='utf-8') as f:
        for k, v in data3.items():
            f.write(str(k)+" ")
            f.write(str(v)+"\n")
