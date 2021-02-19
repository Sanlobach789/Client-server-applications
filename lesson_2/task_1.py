import csv
import re

INFO_1 = './task_files/info_1'
INFO_2 = './task_files/info_2'
INFO_3 = './task_files/info_3'
FILE_EXTENSION = '.txt'
file_arr = [INFO_1, INFO_2, INFO_3]


def space_rm(s):
    s = s.strip()
    s = " ".join([el for el in s.strip().split(' ') if el.strip()])
    return (s)


def get_data(file_path):
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    result_info_list = []

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [headers, result_info_list]

    with open(file_path + FILE_EXTENSION) as f_n:
        f_n_reader = csv.reader(f_n)
        result_dict = {}
        for row in f_n_reader:
            result_data = str.split(str(row[0]), ':')
            if len(result_data) > 1:
                key = space_rm(result_data[0])
                value = space_rm(result_data[1])
                result_dict[key] = value

        os_prod_list.append(result_dict.get(headers[0]))
        os_name_list.append(result_dict.get(headers[1]))
        os_code_list.append(result_dict.get(headers[2]))
        os_type_list.append(result_dict.get(headers[3]))

    result_info_list += os_prod_list + os_name_list + os_code_list + os_type_list

    return main_data


def write_to_csv(file_path):
    data = get_data(file_path)
    with open(file_path + '.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(data)


for file in file_arr:
    write_to_csv(file)
