def parse_sequence_unique(string):
    dct = dict()
    string = string.split()
    cur_ind = 0
    while cur_ind < len(string):
        if string[cur_ind] in dct.keys():
            raise ValueError
        dct[string[cur_ind]] = int(string[cur_ind + 1])
        cur_ind += 2
    return dct

class DatasetLine:
    def __init__(self, line_list_csv):
        self.CLIENT_ID, self.RETRO_DT, self.tokens, self.DEF, self.urls_hashed = line_list_csv

        self.tokens = parse_sequence_unique(line_list_csv[2])
        self.DEF = int(self.DEF)
        self.urls_hashed = parse_sequence_unique(line_list_csv[4])

        return




def dataset_parser_iterator(name_string, logging = False):
    with open(name_string, 'r') as csv_file:
        line_count = 0
        for row in csv_file:
            row_l = row.split('\t')
            if line_count == 0:
                if logging:
                    print(f'Column names are {", ".join(row_l)}')
                line_count += 1
            else:
                yield row, DatasetLine(row_l)
                line_count += 1
        if logging:
            print(f'Processed {line_count} lines.')