import itertools

# for i in itertools.count(10):
#     print(i)
#     if i == 35:
#         break

for i, a in enumerate(itertools.cycle(['AA', 'aa'])):
    print(a)
    if i == 40:
        break



