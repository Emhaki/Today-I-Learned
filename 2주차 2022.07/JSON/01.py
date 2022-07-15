with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    data2 = data.split('\n')
    print(len((data2)))

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(len(data2)))
