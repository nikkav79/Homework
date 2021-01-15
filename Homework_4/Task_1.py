import sys

print(sys.argv)
time, rate, bonus = sys.argv[1:]

time = float(time)
rate = float(rate)
bonus = float(bonus)

def wage():
    print((time * rate) + bonus)
wage()


