time_sec = int(input('Enter time in seconds: '))

hours = time_sec // 3600
minutes = ((time_sec % 3600) // 60)
seconds = (time_sec % 3600) % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))






