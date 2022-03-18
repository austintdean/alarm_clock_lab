# As a developer, I want to use Python’s proper snake_case for variable names.
# As a developer, I want to create a AlarmClock class.
# As a developer, I want the AlarmClock class to have class instance variables to keep track of the
# AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. (You can use
# arbitrary strings to represent the time, it does not need to accurately tell the current time or change
# over time).
# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and
# print to the console the current time.
# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.
# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to
# the console the current alarm time.
# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new
# AlarmClock object and call methods on it.
# 1. Print the clock’s time to the terminal
# 2. Call the alarm clock’s change current time method to change the current time
# 3. Toggle the alarm clock’s on off switch



from alarmclock import AlarmClock

alarm_one = AlarmClock()

alarm_one.set_time('9 PM')

alarm_one.on_off()

alarm_one.is_on()

alarm_one.on_off()

alarm_one.is_on()

alarm_one.on_off()

                                                                                                      