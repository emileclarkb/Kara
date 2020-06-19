from datetime import datetime
# timezones
#import pendulum


# list of all months
months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

# list of all weekdays
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")

# ordinal indicators
indicators = ['st', 'nd', 'rd', 'th']


# time in the day
def currentTime(Kara, command):
    # get current local time
    now = datetime.now()

    # remove all but hours and minutes
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    # period of the day (AM or PM)
    period = 'AM'

    # not morning
    if hour >= 12:
        # convert from 24h time
        hour %= 12
        # change period
        period = 'PM'

    # not minute not double digits
    if minute[0] == '0':
        # split for better speech
        # '05' -> '0 5'
        minute = ' '.join(list(minute))

    # format speech
    Kara.speak('The Time is ' + hour + minute + period)


# Today is Thursday the 18th

# date in the year
def currentDate(Kara, command):
    # get date and split into year, month, and day
    date = datetime.date(datetime.now())
    day = date.day # select month and convert to int

    # get relevent ordinal indicator
    indicator = max(0, 3, day % 10 - 1) # clamp to stay within the list
    indicator = indicators[indicator]

    weekday = weekdays[date.weekday()]

    # format speech
    Kara.speak('Today is ' + weekday + ' the ' +  day + indicator)



# month in the year
def currentMonth(Kara, command):
    # get date and split into year, month, and day
    date = datetime.date(datetime.now())
    month = date.month # select month and convert to int

    # format speech
    Kara.speak('We are currently in ' + months[month - 1])

# the current year
def currentYear(Kara, command):
    # get date and split into year, month, and day
    date = datetime.date(datetime.now())
    year = str(date.year) # select year

    # split year for better speech
    # ie. '2020' -> '20 20'
    a = year[:2] # first section
    b = year[2:] # final section

    # format speech
    Kara.speak('The year is ' + a + ' ' + b)
