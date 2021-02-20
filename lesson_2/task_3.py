import yaml

data = {
    1: [1, 2, 3],
    2: 54,
    3: {'a': '8$', 'b': '6€'}
}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=True, allow_unicode=True)

with open('data_write.yaml') as f_n:
    print(f_n.read())
