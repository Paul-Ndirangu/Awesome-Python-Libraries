import pendulum

time_delta = pendulum.duration(years=2, months=7, 
                               weeks=3, days=2, hours=1, 
                               minutes=1, seconds=20)
print(f"Duration: {time_delta}")
