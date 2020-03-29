import pymir

dt_class = pymir.pymir_clock.date_time
date = dt_class()
for n in range(0, 10000):
    pass
new_date = dt_class()
print(date)
print(new_date)