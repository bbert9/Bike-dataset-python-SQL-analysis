import time
import datetime
import statistics
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
    print('Hello from the refactoring branch')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = 'none'
    month = 'none'
    day = 'none'

    city = input('Enter a city name: ').lower()

    while city not in CITY_DATA:
       print('wrong input')
       city = input('Enter a city name: ').replace('_',' ').lower()

    months =  ['january','february','march','april','may','june','july','august','september','october','november','december','all']
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter a month: ').lower()

    while month not in months:
       print('wrong input')
       month = input('Enter a month: ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday','thuesday','wednesday','thursday','friday','saturday','sunday','all']
    day = input('Enter a day: ').lower()

    while day not in days:
      print('wrong input')
      day = input('Enter a day: ').lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','spetember','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':

        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month

    try:

        pop_month = df['month'].mode()[0]
        print('most common month: ' ,pop_month)

         # TO DO: display the most common day of week
        df['day'] = df['Start Time'].dt.dayofweek
        pop_day = df['day'].mode()[0]
        print('most common day: ', pop_day)


    # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        pop_hour = df['hour'].mode()[0]
        print('most common hour: ' ,pop_hour)
    except:
        print("An exception occurred")
    finally:






        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:
        # TO DO: display most commonly used start station
        pop_start_station = df['Start Station'].mode()[0]
        print('most commonly used start station: ', pop_start_station)


       # TO DO: display most commonly used end station
        pop_end_station = df['End Station'].mode()[0]
        print('most commonly used end station: ', pop_end_station)
    except:
        print('an exception occured')
    finally:


       # TO DO: display most frequent combination of start station and end station trip
       most_frequent_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(3)
       print('\nmost frequent combination of start station and end station trip\n',most_frequent_station)
       #here i can have a combination of the same station wich is problematic
       #i dont know how to access only unique combinations of different stations!


       print("\nThis took %s seconds." % (time.time() - start_time))
       print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print("total travel time: ",tot_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nmean travel time: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count_user_type = df['User Type'].value_counts()
    print('\ncounts of user types: \n',count_user_type)
    # TO DO: Display counts of gender

    if 'Gender Type' in df.columns:

        count_gender_type = df['Gender'].value_counts()
        print("\ncounts of gender types: \n",count_gender_type)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        earliest = df['Birth Year'].min()
        print("\nEarliest year of birth: ",earliest)

        date = datetime.datetime.now()
        most_recent = df['Birth Year'].sort_values(ascending=False)[0]
        print('\nmost recent year of birth: ',most_recent)

        most_common = df['Birth Year'].mode()[0]
        print("\nmost common year of birth: ", most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    input1 = input('Do you want to see raw data ? y or n').lower()
    i=0 #iterations
    while input1 != 'n':

        if input1 == 'y':

            print('\nRaw datas :\n', df.head(5+i*5))
            i+=1
        input1 = input('Do you want to see raw data ? y or n\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data(df) #you forgot this one

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
