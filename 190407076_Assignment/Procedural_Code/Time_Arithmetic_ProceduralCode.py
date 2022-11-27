time = []
def Time(day, hour, minute, second):
    time.append([day, hour, minute, second])
    return time
def dayConversion(time, type):
        """Converts days to hours, minutes, seconds"""
        time = time[0]
        if type == 'h':
            return time*24
        elif type == 'm':
            return time*24*60
        elif type == 's':
            return time*24*60*60
def hourConversion(time, type):
    """Converts hours to days, minutes, seconds"""
    time = time[1]
    if type == 'd':
        return time/24
    elif type == 'm':
        return time*60
    elif type == 's':
        return time*60*60
def minuteConversion(time, type):
    """Converts minutes to days, hours, seconds"""
    time = time[2]
    if type == 'd':
        return time/(24*60)
    elif type == 'h':
        return time/60
    elif type == 's':
        return time*60
def secondsConversion(time, type):
    """Converts seconds to days, hours, minutes"""
    time = time[3]
    if type == 'd':
        return time/(24*60*60)
    elif type == 'h':
        return time/(60*60)
    elif type == 'm':
        return time*60

def toSeconds(time):
    """Returns time in seconds"""
    return f"Total seconds: {(time[0]*24*60*60) + (time[1]*60*60) + (time[2]*60) + time[3]} seconds"
def toMinutes(time):
    """Returns time in minutes"""
    return f"Total minutes: {(time[0]*24*60) + (time[1]*60) + time[2] + (round((time[3]/60), ndigits=2))} minutes"
def toHours(time):
    """Returns time in hours"""
    return f"Total hours: {(time[0]*24) + time[1] + round((time[2]/60), ndigits=2) + round((time[3]/(60*60)), ndigits=2)} hours"
def toDays(time):
    """Returns time in days"""
    return f"Total days: {time[0] + round((time[1]/24), ndigits=2) + round((time[2]/(24*60)), ndigits=2) + round((time[3]/(24*60*60)), ndigits=2)} days"
def timeSubtraction(time, form1, form2, returntype):
        days_in_seconds = (time[0])*(24*60**2)
        hours_in_seconds = time[1]*(60**2)
        minutes_in_seconds = time[2]*(60)
        seconds = time[3]
        time = [days_in_seconds, hours_in_seconds, minutes_in_seconds, seconds]
        time_form = ['d', 'h', 'm', 's']
        for tim in time_form:
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

time1 = Time(90, 48, 239, 889)
time2 = Time(30, 40, 289, 500)
time3 = Time(365, 599, 89, 9680)

print(f"Time specified: {time1[0][0]} days, {time1[0][1]} hours, {time1[0][2]} minutes, {time1[0][3]} seconds\n")
print("Day Conversion")
print(f"{dayConversion(time1[0], 'h')} hours")
print(f"{dayConversion(time1[0], 'm')} minutes")
print(f"{dayConversion(time1[0], 's')} seconds")
print("\nHour Conversion")
print(f"{hourConversion(time1[0], 'd')} days")
print(f"{hourConversion(time1[0], 'm')} minutes")
print(f"{hourConversion(time1[0], 's')} seconds")
print("\nMinute Conversion")
print(f"{minuteConversion(time1[0], 'd')} days")
print(f"{minuteConversion(time1[0], 'h')} hours")
print(f"{minuteConversion(time1[0], 's')} seconds")
print("\nSecond Conversion")
print(f"{secondsConversion(time1[0], 'd')} days")
print(f"{secondsConversion(time1[0], 'h')} hours")
print(f"{secondsConversion(time1[0], 'm')} minutes")
print("\nTotal Conversion")
print(toDays(time1[0]))
print(toHours(time1[0]))
print(toMinutes(time1[0]))
print(toSeconds(time1[0]))
print("")
print(f"Time 1 days - Time 1 hours = {timeSubtraction(time1[0], 'd', 'h', 'd')} days")
print(f"Time 1 days - Time 1 Seconds = {timeSubtraction(time1[0], 'd', 's', 'm')} minutes")
print(f"Time 1 days - Time 1 minutes = {timeSubtraction(time1[0], 'd', 'm', 'h')} hours")
print(f"Time 1 hours - Time 1 minutes = {timeSubtraction(time1[0], 'h', 'm', 's')} seconds")
print("")
print(f"Time specified: {time1[1][0]} days, {time1[1][1]} hours, {time1[1][2]} minutes, {time1[1][3]} seconds\n")
print("Day Conversion")
print(f"{dayConversion(time2[0], 'h')} hours")
print(f"{dayConversion(time2[0], 'm')} minutes")
print(f"{dayConversion(time2[0], 's')} seconds")
print("\nHour Conversion")
print(f"{hourConversion(time2[0], 'd')} days")
print(f"{hourConversion(time2[0], 'm')} minutes")
print(f"{hourConversion(time2[0], 's')} seconds")
print("\nMinute Conversion")
print(f"{minuteConversion(time2[0], 'd')} days")
print(f"{minuteConversion(time2[0], 'h')} hours")
print(f"{minuteConversion(time2[0], 's')} seconds")
print("\nSecond Conversion")
print(f"{secondsConversion(time2[0], 'd')} days")
print(f"{secondsConversion(time2[0], 'h')} hours")
print(f"{secondsConversion(time2[0], 'm')} minutes")
print("\nTotal Conversion")
print(toDays(time2[0]))
print(toHours(time2[0]))
print(toMinutes(time2[0]))
print(toSeconds(time2[0]))
print("")
print(f"Time 2 days - Time 2 hours = {timeSubtraction(time2[1], 'd', 'h', 'd')} days")
print(f"Time 2 days - Time 2 Seconds = {timeSubtraction(time2[1], 'd', 's', 'm')} minutes")
print(f"Time 2 days - Time 2 minutes = {timeSubtraction(time2[1], 'd', 'm', 'h')} hours")
print(f"Time 2 hours - Time 2 minutes = {timeSubtraction(time2[1], 'h', 'm', 's')} seconds")
print("")
print(f"Time specified: {time1[2][0]} days, {time1[2][1]} hours, {time1[2][2]} minutes, {time1[2][3]} seconds\n")
print("Day Conversion")
print(f"{dayConversion(time3[0], 'h')} hours")
print(f"{dayConversion(time3[0], 'm')} minutes")
print(f"{dayConversion(time3[0], 's')} seconds")
print("\nHour Conversion")
print(f"{hourConversion(time3[0], 'd')} days")
print(f"{hourConversion(time3[0], 'm')} minutes")
print(f"{hourConversion(time3[0], 's')} seconds")
print("\nMinute Conversion")
print(f"{minuteConversion(time3[0], 'd')} days")
print(f"{minuteConversion(time3[0], 'h')} hours")
print(f"{minuteConversion(time3[0], 's')} seconds")
print("\nSecond Conversion")
print(f"{secondsConversion(time3[0], 'd')} days")
print(f"{secondsConversion(time3[0], 'h')} hours")
print(f"{secondsConversion(time3[0], 'm')} minutes")
print("\nTotal Conversion")
print(toDays(time3[0]))
print(toHours(time3[0]))
print(toMinutes(time3[0]))
print(toSeconds(time3[0]))
print("")
print(f"Time 3 days - Time 3 hours = {timeSubtraction(time3[2], 'd', 'h', 'd')} days")
print(f"Time 3 days - Time 3 Seconds = {timeSubtraction(time3[2], 'd', 's', 'm')} minutes")
print(f"Time 3 days - Time 3 minutes = {timeSubtraction(time3[2], 'd', 'm', 'h')} hours")
print(f"Time 3 hours - Time 3 minutes = {timeSubtraction(time3[2], 'h', 'm', 's')} seconds")
print("")