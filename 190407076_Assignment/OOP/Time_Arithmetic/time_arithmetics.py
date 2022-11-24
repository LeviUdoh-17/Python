#Create time class
class Time():
    def __init__(self, days, hours, minutes, seconds):
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    def days(self):
        return self._days
    def hours(self):
        return self._hours
    def minutes(self):
        return self._minutes
    def seconds(self):
        return self._seconds
#Create time conversion class
class Time_Conversion(Time):
    def __init__(self, days, hours, minutes, seconds):
        super().__init__(days, hours, minutes, seconds)
    def dayConversion(self, type):
        """Converts days to hours, minutes, seconds"""
        if type == 'h':
            return self._days*24
        elif type == 'm':
            return self._days*24*60
        elif type == 's':
            return self._days*24*60*60
    def hourConversion(self, type):
        """Converts hours to days, minutes, seconds"""
        if type == 'd':
            return self._hours/24
        elif type == 'm':
            return self._hours*60
        elif type == 's':
            return self._hours*60*60
    def minuteConversion(self, type):
        """Converts minutes to days, hours, seconds"""
        if type == 'd':
            return self._minutes/(24*60)
        elif type == 'h':
            return self._minutes/60
        elif type == 's':
            return self._minutes*60
    def secondsConversion(self, type):
        """Converts seconds to days, hours, minutes"""
        if type == 'd':
            return self._seconds/(24*60*60)
        elif type == 'h':
            return self._seconds/(60*60)
        elif type == 'm':
            return self._seconds*60
    
    def toSeconds(self):
        """Returns time in seconds"""
        return f"Total seconds: {(self._days*24*60*60) + (self._hours*60*60) + (self._minutes*60) + self._seconds} seconds"
    def toMinutes(self):
        """Returns time in minutes"""
        return f"Total minutes: {(self._days*24*60) + (self._minutes*60) + self._minutes + (round((self._seconds/60), ndigits=2))} minutes"
    def toHours(self):
        """Returns time in hours"""
        return f"Total hours: {(self._days*24) + self._hours + round((self._minutes/60), ndigits=2) + round((self._seconds/(60*60)), ndigits=2)} hours"
    def toDays(self):
        """Returns time in days"""
        return f"Total days: {self._days + round((self._hours/24), ndigits=2) + round((self._minutes/(24*60)), ndigits=2) + round((self._seconds/(24*60*60)), ndigits=2)} days"
class Time_Arithmetics(Time_Conversion):
    '''Subtracts different forms of time'''
    def __init__(self, days, hours, minutes, seconds):
        super().__init__(days, hours, minutes, seconds)
    def timeSum(self):
        days_in_seconds = self.days*24*60**2
        hours_in_seconds = self._hours*(60**2)
        minutes_in_seconds = self._minutes*(60)
        seconds = self._seconds
        sumTotal = days_in_seconds + hours_in_seconds + minutes_in_seconds + seconds
        return sumTotal
    def timeSubtraction(self, form1, form2, returntype):
        days_in_seconds = (self.days())*(24*60**2)
        hours_in_seconds = self._hours*(60**2)
        minutes_in_seconds = self._minutes*(60)
        seconds = self._seconds
        time = [days_in_seconds, hours_in_seconds, minutes_in_seconds, seconds]
        time_form = ['d', 'h', 'm', 's']
        for times in time_form:
            if form1 in time_form:
                index1 = time_form.index(form1)
            if form2 in time_form:
                index2 = time_form.index(form2)
        result = time[index1] - time[index2]
        if returntype == 'd':
            result = result/(24*60**2)
        elif returntype == 'h':
            result = result/(60**2)
        elif returntype == 'm':
            result = result/(60)
        elif returntype == 's':
            result = result
        else:
            ("Wrong input")
        return result
        
time1 = Time_Arithmetics(90, 48, 239, 889)
time2 = Time_Arithmetics(30, 40, 289, 500)
time3 = Time_Arithmetics(365, 599, 89, 9680)

print(f"Time One specified: {time1.days()} days, {time1.hours()} hours, {time1.minutes()} minutes, {time1.seconds()} seconds\n")
print(time1.toDays())
print(time1.toHours())
print(time1.toMinutes())
print(time1.toSeconds())
print("")
print(f"Time Two specified: {time2.days()} days, {time2.hours()} hours, {time2.minutes()} minutes, {time2.seconds()} seconds\n")
print(time2.toDays())
print(time2.toHours())
print(time2.toMinutes())
print(time2.toSeconds())
print("")
print(f"Time Three specified: {time3.days()} days, {time3.hours()} hours, {time3.minutes()} minutes, {time3.seconds()} seconds\n")
print(time3.toDays())
print(time3.toHours())
print(time3.toMinutes())
print(time3.toSeconds())
print("")
print(f"Time 1 days - Time 1 hours = {time1.timeSubtraction('d', 'h', 'd')} days")
print(f"Time 1 days - Time 1 Seconds = {time1.timeSubtraction('d', 's', 'm')} minutes")
print(f"Time 1 days - Time 1 minutes = {time1.timeSubtraction('d', 'm', 'h')} hours")
print(f"Time 1 hours - Time 1 minutes = {time1.timeSubtraction('h', 'm', 's')} seconds")
print("")
print(f"Time 2 days - Time 2 hours = {time2.timeSubtraction('d', 'h', 'd')} days")
print(f"Time 2 days - Time 2 Seconds = {time2.timeSubtraction('d', 's', 'm')} minutes")
print(f"Time 2 days - Time 2 minutes = {time2.timeSubtraction('d', 'm', 'h')} hours")
print(f"Time 2 hours - Time 2 minutes = {time2.timeSubtraction('h', 'm', 's')} seconds")
print("")
print(f"Time 3 days - Time 3 hours = {time3.timeSubtraction('d', 'h', 'd')} days")
print(f"Time 3 days - Time 3 Seconds = {time3.timeSubtraction('d', 's', 'm')} minutes")
print(f"Time 3 days - Time 3 minutes = {time3.timeSubtraction('d', 'm', 'h')} hours")
print(f"Time 3 hours - Time 3 minutes = {time3.timeSubtraction('h', 'm', 's')} seconds")