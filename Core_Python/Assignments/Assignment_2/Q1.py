# Convert the time entered in hh,min and sec into seconds.

hh = int(input('Enter Hours '))
min = int(input('Enter Minutes '))
sec = int(input('Enter Seconds '))

total_seconds = (hh * 3600) + (min * 60) + sec
print(f'Total Seconds = {total_seconds}')