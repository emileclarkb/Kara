import datetime
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
    now = datetime.datetime.now()

    # remove all but hours and minutes
    hour = int(now.strftime("%H"))
    minute = now.strftime("%M")

    # period of the day (AM or PM)
    period = 'AM'

    # not morning
    if hour >= 12:
        # convert from 24h time
        hour %= 12
        # change period
        period = 'PM'

    # format speech
    print('The time is {}:{} {}'.format(str(hour), minute, period))
    Kara.speak('The time is {}:{} {}'.format(str(hour), minute, period))


# date in the year
def currentDate(Kara, command):
    # get date and split into year, month, and day
    date = datetime.datetime.date(datetime.datetime.now())

    # customizable opening words
    opening = 'Today is '

    # move date to tomorrow
    if 'tomorrow' in command:
        date += datetime.timedelta(days=1)
        # chaning opening for "tomorrow"
        opening = 'Tomorrow it will be '
    # date in an amount of days
    # ie. "what's the date in 4 days?"
    elif 'days' in command:
        # split str to list
        split = command.split()
        # find where days was said
        index = split.index('days')
        days = split[index - 1] # get word before "days"
        date += datetime.timedelta(days=int(days))

        # chaning opening to be relevent
        opening = 'In {} days it will be '.format(days)

    day = date.day # select day
    # get relevent ordinal indicator
    # clamp to stay within the list
    indicator = int(str(day)[-1]) - 1 # get final place and align with list (-1)
    indicator = indicators[indicator]

    weekday = weekdays[date.weekday()] # select weekday

    # format speech
    Kara.speak('{}{} the {}{}'.format(opening, weekday, str(day), indicator))



# month in the year
def currentMonth(Kara, command):
    # get date and split into year, month, and day
    date = datetime.datetime.date(datetime.datetime.now())
    month = date.month # select month and convert to int

    # format speech
    Kara.speak('We are currently in {}'.format(months[month - 1]))

# the current year
def currentYear(Kara, command):
    # get date and split into year, month, and day
    date = datetime.datetime.date(datetime.datetime.now())
    year = str(date.year) # select year

    # split year for better speech
    # ie. '2020' -> '20 20'
    a = year[:2] # first section
    b = year[2:] # final section

    # format speech
    Kara.speak('The year is {} {}'.format(a, b))
