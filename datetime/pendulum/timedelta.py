import pendulum

dur = pendulum.duration(days=15)

# More properties
dur.weeks
dur.hours

# Handy methods
dur.in_hours()
360
dur.in_words(locale="en_us")
# '2 weeks 1 day'
