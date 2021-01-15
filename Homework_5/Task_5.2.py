
def some_data(fileName):
    with open(fileName, encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        print(f'The document contains the following information: {content}')
        print('The number of lines is: {} '.format(len(content)))
        for symbols in content:
            print(f'The number of symbols for string {symbols.strip()} is {len(symbols.strip())}')
some_data('some_data_5.2.txt')

