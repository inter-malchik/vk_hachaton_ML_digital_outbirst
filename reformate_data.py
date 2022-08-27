def waste_digits(dict):

    name_list_split = []

    for name in dict:
        name_list_split.append([name] * dict[name])

    name_list_join = []
    for name_list in name_list_split:
        for name in name_list:
            name_list_join.append(name)

    return name_list_join



