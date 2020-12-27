def something_like_this():
    sum_1 = []
    while True:
        data_request = input('Enter numbers separated by a space: ').split(' ')

        if '***' in data_request:
            data_request = data_request[:data_request.index('***')]

            data_request_num = list(map(int, data_request))
            sum_1.extend(data_request_num)
            sum_number = sum(sum_1)
            print(sum_number)
            break
        else:
            data_request_num = list(map(int, data_request))
            sum_1.extend(data_request_num)
            sum_number = sum(sum_1)
            print(sum_number)
            
something_like_this()


