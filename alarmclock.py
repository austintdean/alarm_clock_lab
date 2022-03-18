class AlarmClock:
    # instance variables - characteristics
    def __init__(self):
        self.current_time = '12 PM'
        self.on = True
        self.set_alarm_to = ''
        
    # Methods - actions of the class( can do )
    def set_time(self, newtime):
        newtime = input(f'You want {newtime} to be your alarm? ')
        print(f"You have changed your alarm to {newtime}")
        self.set_alarm_to = newtime

    def is_on(self):
        if self.on == True:
            alarm_on = (f"The alarm is on. It is set to {self.set_alarm_to}")
            print(alarm_on)
        else:
            alarm_off = ("The alarm is off.")
            print(alarm_off)
        
    def on_off(self):
        if self.on == True:
            self.on = False
            print("You have turned the alarm off.")
        else:
            self.on = True
            print("You have turned the alarm on.")
    
