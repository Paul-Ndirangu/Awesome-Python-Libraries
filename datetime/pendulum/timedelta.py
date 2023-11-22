import pendulum
time_delta = pendulum.duration(days = 2,
                               hours = 10, 
                               years = 2)
print(time_delta)
 
# Date when i am writing this code is 2023-11-22.
print('future date =', 
      pendulum.now() + time_delta)
