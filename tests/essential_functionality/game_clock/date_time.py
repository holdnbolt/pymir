import pymir
import time

dt_class = pymir.pymir_clock.date_time
initial_time = dt_class(
    1, 2, 3,
    test = 'huh',
)
print(initial_time)
#time.sleep(1)
