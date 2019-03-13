import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        city_input = (input('Please enter which of our three cities, chicago, new york city, or washington, you would like to analyze: ')).lower()
        if city_input in ('chicago', 'the windy city'):
            city = 'chicago'
        elif city_input in ('new york city', 'nyc', 'the big apple'):
            city = 'new york city'
        elif city_input in ('washington', "nation's capital"):
            city = 'washington'
        else:
            print('Please enter one of the three cities with an active bikeshare program.')


    # get user input for month (all, january, february, ... , june)
    month = 0
    while month == 0:
        month_input = (input('Please enter the name of the month to filter by, or "all" to apply no month filter: ')).lower()
        if month_input in ('all', 'all months'):
            month = 'all'
        elif month_input in ('january', 'jan', 'the first month of the year', '1'):
            month = 'january'
        elif month_input in ('february', 'feb', 'the month with valentines day', '2'):
            month = 'february'
        elif month_input in ('march', 'mar', "saint patrick's day", '3'):
            month = 'march'
        elif month_input in ('april', 'apr', 'the month with easter', '4'):
            month = 'april'
        elif month_input in ('may', 'still not spring in canada', '5'):
            month = 'may'
        elif month_input in ('june', 'jun', 'the best month', '6'):
            month = 'june'
        else:
            print('Please enter one of the first six months of the year or all.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = 0
    while day == 0:
        day_input = (input('Please enter the name of the day of week to filter by, or "all" to apply no day filter: ')).lower()
        if day_input in ('all', 'all days'):
            day = 'all'
        if day_input in ('sunday', 'sun', '1'):
            day = 'sunday'
        elif day_input in ('monday', 'mon', '2'):
            day = 'monday'
        elif day_input in ('tuesday', 'tue', '3'):
            day = 'tuesday'
        elif day_input in ('wednesday', 'wed', '4'):
            day = 'wednesday'
        elif day_input in ('thursday', 'thur', '5'):
            day = 'thursday'
        elif day_input in ('friday', 'fri', '6'):
            day = 'friday'
        elif day_input in ('saturday', 'sat', '7'):
            day = 'saturday'
        else:
            print('Please enter a valid day or all.')

    print("Great! Let's look at data from " + city)

    if month == 'all':
        print('in all months')
    else:
        print("in the month of " + month)

    if day == 'all':
        print('on all days')
    else:
        print("on " + day + "s.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # extract hour from the Start Time column to create a start hour column
    df['start_hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month_num = df['month'].mode()[0]
    if popular_month_num == 1:
        popular_month = 'January'
    elif popular_month_num == 2:
        popular_month = 'February'
    elif popular_month_num == 3:
        popular_month = 'March'
    elif popular_month_num == 4:
        popular_month = 'April'
    elif popular_month_num == 5:
        popular_month = 'May'
    elif popular_month_num == 6:
        popular_month = 'June'
    print('Most Common Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Common Day of the Week:', popular_day)

    # display the most common start hour
    popular_hour = df['start_hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print ('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print ('Most Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['station_combo'] = df['Start Station'] + ' to ' + df['End Station']

    popular_station_combo = df['station_combo'].mode()[0]

    print('Most Popular Combination of Start and End Stations:', popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_s = df['Trip Duration'].sum()
    s_per_h = 3600
    total_travel_hours = total_travel_time_s // s_per_h
    total_travel_minutes = (total_travel_time_s % s_per_h)//60
    total_travel_seconds = (total_travel_time_s % s_per_h) % 60

    print('The Total Travel Time was:', total_travel_hours, 'hours,', total_travel_minutes, 'minutes, and', total_travel_seconds, 'seconds')

    # display mean travel time
    mean_travel_time_s = df['Trip Duration'].mean()
    mean_travel_hours = mean_travel_time_s // s_per_h
    mean_travel_minutes = (mean_travel_time_s % s_per_h)//60
    mean_travel_seconds = (mean_travel_time_s % s_per_h) % 60

    print('The Mean Travel Time was:', mean_travel_hours, 'hours,', mean_travel_minutes, 'minutes, and', mean_travel_seconds, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of Subscribers:', len(df[df['User Type'] == 'Subscriber']))
    print('Count of Customers:', len(df[df['User Type'] == 'Customer']))


    if city == 'washington':
        print('Gender and Birth Year Data have not been collected for the Washington Bikeshare Program')
    else:
        # Display counts of gender
        print('Count of Male Users:', len(df[df['Gender'] == 'Male']))
        print('Count of Female Users:', len(df[df['Gender'] == 'Female']))
        print('Count of Users with Unspecified Gender:', len(df[df['Gender'] == '']))

        # Display earliest, most recent, and most common year of birth
        df.dropna(subset=['Birth Year'], inplace=True)
        print('Earliest Birth Year:', int(df['Birth Year'].min()))
        print('Most Recent Birth Year:', int(df['Birth Year'].max()))
        print('Most Common Birth Year:', int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_raw_data(city):
    """Displays raw data for the given city 5 lines at a time."""

    #Prompt user if they would like to see raw data
    see_raw = input('Would you like to see 5 lines of raw data? (type yes or no): ')
    if see_raw == 'yes':
        # load data file into a dataframe
        raw_df = pd.read_csv(CITY_DATA[city])
        n = 0

    #Prompt user if they would like to see more raw data
    while see_raw == 'yes':
        print(raw_df[n:n + 5])
        see_raw = input('Would you like to see 5 more lines of raw data? (type yes or no): ')
        n += 5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        see_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
