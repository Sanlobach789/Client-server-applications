import yaml

data = {
    1: [1, 2, 3],
    2: 54,
    3: {'a': '8$', 'b': '6€'}
}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data, f_n)

with open('data_write.yaml') as f_n:
    print(f_n.read())
