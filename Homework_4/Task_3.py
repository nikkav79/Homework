def seeking_number(num_start, num_end, num_stop_1, num_stop_2):
    print([i for i in range(num_start, num_end) if i % num_stop_1 == 0 or i % num_stop_2 == 0])
seeking_number(20, 240, 20, 21)







