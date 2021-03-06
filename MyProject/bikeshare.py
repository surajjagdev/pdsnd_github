  #  #importing pandas
  #  #hello test
import pandas as pd
import numpy as np

from datetime import datetime
from datetime import timedelta
import time

  #  # Filenames
  #chicago = 'chicago.csv'
  #new_york_city = 'new_york_city.csv'
  #washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nHello There! Let\'s explore some USA bikeshare data!\n'
                     'Please type the city you want to view information about: Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago' :
            return 'chicago.csv'
        elif city.lower() == 'new york' or city.lower()=="newyork":
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('I do not understand your inputPlease input either '
                  'Chicago, New York, or Washington.')

def getTimeperiod():
    '''this will ask the user for a time period and returns the specified filter.

    '''
    timePeriod = ''
    while timePeriod.lower() not in ['month', 'day', 'none']:
        timePeriod = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
        if timePeriod.lower() not in ['month', 'day', 'none']:
            print('Sorry,I do not understand your input  ')
    return timePeriod

def getMonth():
    '''Asks the user for a month and returns the specified month.
        '''
    monthInput = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while monthInput.lower() not in months_dict.keys():
        monthInput = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if monthInput.lower() not in months_dict.keys():
            print('I do not understand your inputPlease type in a '
                  'month between January and June')
    month = months_dict[monthInput.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    '''
    this_Month = getMonth()[0]
    month = int(this_Month[5:])
    valid_date = False
    while valid_date == False:
        isFalse = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while isFalse == False:
            try:
                day = int(day)
                isFalse = True
            except ValueError:
                print('I do not understand your input Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type your response as an integer.\n')
        try:
            startDate = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    endDate = startDate + timedelta(days=1)
    return (str(startDate), str(endDate))

def popular_month(df):
    '''Finds and prints the most popular month for start time.
        '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df[' startTime'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))

def popular_day(df):
    '''Finds and prints the most popular day of week (Monday, Tuesday, etc.) for start time.
        '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df[' startTime'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

def popular_hour(df):
    '''Finds and prints the most popular hour of day for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_hour = int(df[' startTime'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_pm))

def trip_duration(df):
    '''Finds and prints the total trip duration and average trip duration in
       hours, minutes, and seconds.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))

def popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    pop_start = df['start_station'].mode().to_string(index = False)
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))

def popular_trip(df):
    '''Finds and prints the most popular trip.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_trip = df['journey'].mode().to_string(index = False)
      # The 'journey' column is created in the statistics() function.
    print('The most popular trip is {}.'.format(most_pop_trip))

def users(df):
    '''Finds and prints the counts of each user type.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

def Gender(df):
    '''Finds and prints the counts of Gender.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    maleCount = df.query('Gender == "Male"').Gender.count()
    femaleCount = df.query('Gender == "Male"').Gender.count()
    print('There are {} male users and {} female users.'.format(maleCount, femaleCount))

def birth_years(df):
    ''' Finds and prints the earliest (i.e. oldest user), most recent (i.e.
        youngest user), and most popular birth years.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("I do not understand your inputPlease type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
          # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("I do not understand your inputPlease type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def statistics():
    '''caclulates statistics based on users input
    '''
      # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])

      # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

      # increases the column width so that the long strings in the 'journey'
      # column can be displayed fully
    pd.set_option('max_colwidth', 100)

      # creates a 'journey' column that concatenates 'start_station' with
      # 'end_station' for the use popular_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

      # Filter by time period (month, day, none)
    timePeriod = getTimeperiod()
    if timePeriod == 'none':
        df_filtered = df
    elif timePeriod == 'month' or timePeriod == 'day':
        if timePeriod == 'month':
            filterLower, filter_upper = getMonth()
        elif timePeriod == 'day':
            filterLower, filter_upper = get_day()
        print('Filtering data...')
        df_filtered = df[(df[' startTime'] >= filterLower) & (df[' startTime'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if timePeriod == 'none':
        startTime = time.time()

          # What is the most popular month for start time?
        popular_month(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))
        print("\nCalculating the next statistic...")

    if timePeriod == 'none' or timePeriod == 'month':
        startTime = time.time()

          # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        popular_day(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))
        print("\nCalculating the next statistic...")
        startTime = time.time()

      # What is the most popular hour of day for start time?
    popular_hour(df_filtered)
    startTime = time.time()
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")


      # What is the total trip duration and average trip duration?
    trip_duration(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")
    startTime = time.time()

      # What is the most popular start station and most popular end station?
    popular_stations(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")
    startTime = time.time()

      # What is the most popular trip?
    popular_trip(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")
    startTime = time.time()

      # What are the counts of each user type?
    users(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nCalculating the next statistic...")
        startTime = time.time()

          # What are the counts of Gender?
        Gender(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))
        print("\nCalculating the next statistic...")
        startTime = time.time()

          # What are the earliest (i.e. oldest user), most recent (i.e. youngest
          # user), and most popular birth years?
        birth_years(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))

      # Display five lines of data at a time if user specifies that they would like to
    display_data(df_filtered)

      # Restart?
    Restart = input('\nWould you like to Restart? Type \'yes\' or \'no\'.\n')
    while Restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        Restart = input('\nWould you like to Restart? Type \'yes\' or \'no\'.\n')
    if Restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()


  #  #importing pandas
  #  #hello test
import pandas as pd
import numpy as np

from datetime import datetime
from datetime import timedelta
import time

  #  # Filenames
  #chicago = 'chicago.csv'
  #new_york_city = 'new_york_city.csv'
  #washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nHello There! Let\'s explore some USA bikeshare data!\n'
                     'Please type the city you want to view information about: Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago' :
            return 'chicago.csv'
        elif city.lower() == 'new york' or city.lower()=="newyork":
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('I do not understand your inputPlease input either '
                  'Chicago, New York, or Washington.')

def getTimeperiod():
    '''this will ask the user for a time period and returns the specified filter.

    '''
    timePeriod = ''
    while timePeriod.lower() not in ['month', 'day', 'none']:
        timePeriod = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
        if timePeriod.lower() not in ['month', 'day', 'none']:
            print('Sorry,I do not understand your input  ')
    return timePeriod

def getMonth():
    '''Asks the user for a month and returns the specified month.
        '''
    monthInput = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while monthInput.lower() not in months_dict.keys():
        monthInput = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if monthInput.lower() not in months_dict.keys():
            print('I do not understand your inputPlease type in a '
                  'month between January and June')
    month = months_dict[monthInput.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    '''
    this_Month = getMonth()[0]
    month = int(this_Month[5:])
    valid_date = False
    while valid_date == False:
        isFalse = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while isFalse == False:
            try:
                day = int(day)
                isFalse = True
            except ValueError:
                print('I do not understand your inputPlease type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type your response as an integer.\n')
        try:
            startDate = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    endDate = startDate + timedelta(days=1)
    return (str(startDate), str(endDate))

def popular_month(df):


    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df[' startTime'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))

def popular_day(df):

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df[' startTime'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

def popular_hour(df):
    '''Finds and prints the most popular hour of day for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_hour = int(df[' startTime'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_pm))

def trip_duration(df):
    '''Finds and prints the total trip duration and average trip duration in
       hours, minutes, and seconds.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))

def popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    pop_start = df['start_station'].mode().to_string(index = False)
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))

def popular_trip(df):
    '''Finds and prints the most popular trip.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_trip = df['journey'].mode().to_string(index = False)
      # The 'journey' column is created in the statistics() function.
    print('The most popular trip is {}.'.format(most_pop_trip))

def users(df):
    '''Finds and prints the counts of each user type.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

def Gender(df):
    '''Finds and prints the counts of Gender.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    maleCount = df.query('Gender == "Male"').Gender.count()
    femaleCount = df.query('Gender == "Male"').Gender.count()
    print('There are {} male users and {} female users.'.format(maleCount, femaleCount))

def birth_years(df):
    ''' Finds and prints the earliest (i.e. oldest user), most recent (i.e.
        youngest user), and most popular birth years.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines.
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("I do not understand your input Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
          # prints every column except the 'journey' column in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("I do not understand your inputPlease type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def statistics():
    '''caclulates statistics based on users input
    '''
      # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])

      # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

      # increases the column width so that the long strings in the 'journey'
      # column can be displayed fully
    pd.set_option('max_colwidth', 100)

      # creates a 'journey' column that concatenates 'start_station' with
      # 'end_station' for the use popular_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

      # Filter by time period (month, day, none)
    timePeriod = getTimeperiod()
    if timePeriod == 'none':
        df_filtered = df
    elif timePeriod == 'month' or timePeriod == 'day':
        if timePeriod == 'month':
            filterLower, filter_upper = getMonth()
        elif timePeriod == 'day':
            filterLower, filter_upper = get_day()
        print('Filtering data...')
        df_filtered = df[(df[' startTime'] >= filterLower) & (df[' startTime'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if timePeriod == 'none':
        startTime = time.time()

          # What is the most popular month for start time?
        popular_month(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))
        print("\nCalculating the next statistic...")

    if timePeriod == 'none' or timePeriod == 'month':
        startTime = time.time()

          # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        popular_day(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))
        print("\nCalculating the next statistic...")
        startTime = time.time()

      # What is the most popular hour of day for start time?
    popular_hour(df_filtered)
    startTime = time.time()
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")


    trip_duration(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")
    startTime = time.time()

      # What is the most popular start station and most popular end station?
    popular_stations(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")
    startTime = time.time()

      # What is the most popular trip?
    popular_trip(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))
    print("\nCalculating the next statistic...")
    startTime = time.time()

      # What are the counts of each user type?
    users(df_filtered)
    print("That took %s seconds." % (time.time() -  startTime))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nCalculating the next statistic...")
        startTime = time.time()

          # What are the counts of Gender?
        Gender(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))
        print("\nCalculating the next statistic...")
        startTime = time.time()

          # What are the earliest (i.e. oldest user), most recent (i.e. youngest
          # user), and most popular birth years?
        birth_years(df_filtered)
        print("That took %s seconds." % (time.time() -  startTime))

      # Display five lines of data at a time if user specifies that they would like to
    display_data(df_filtered)

      # Restart?
    Restart = input('\nWould you like to Restart? Type \'yes\' or \'no\'.\n')
    while Restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        Restart = input('\nWould you like to Restart? Type \'yes\' or \'no\'.\n')
    if Restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
