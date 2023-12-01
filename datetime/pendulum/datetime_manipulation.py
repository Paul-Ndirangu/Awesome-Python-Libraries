# importing the library
import pendulum

# creating datetime instance
dt = pendulum.datetime(2023, 12, 1)
print(f"Initial Datetime Created: {dt}")

# Manipulating datetime object using add()
dt = dt.add(years=5)
print(f"Datetime after 5 years: {dt}")

# Manipulating datetime object using subtract()
dt = dt.subtract(years=4)
print(f"Datetime 4 years before: {dt}")

# Similarly you can add or subtract
# months,weeks,days,hours,minutes 
# individually or all at a time.
dt = dt.add(years=3, months=2, days=6,
            hours=7, minutes=8, seconds=45)
print(f"Manipulate Date and Time: {dt}")
