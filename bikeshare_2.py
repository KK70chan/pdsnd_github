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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please specify the city you want : ").lower()
    if city not in CITY_DATA:
        #print('if 진입')
        while city not in CITY_DATA:
            city = input("Only data for chicago, new york city, washington are available.\n Please specify the city you want : ").lower()
    print('city confirmed')
        
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please specify the month you want (use number 1~6 or 'all') : ")
            if month == 'all':
                break
            else:
                month = int(month)
                if month <= 6:
                    break
                else:
                    print('Oops! you entered more than 6. Please try again')
        except:
            print('Oops! you entered incorrect information, Please use number only')
            
    if month != 'all':
        if month == 1:
            month = "january"
        if month == 2:
            month = "february"
        if month == 3:
            month = "march"
        if month == 4:
            month = "april"
        if month == 5:
            month = "may"
        if month == 6:
            month = "june"
    
    #print(month)            
    print('month confirmed')
    
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_check = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    while True:
        try:
            day = input("Please specify the day you want (use monday~sunday or 'all') : ").title()
            if day == 'All':
                day = day.lower()
                break
            else:
                if day in day_check:
                    break
                else:
                    print('Oops! you entered wrong inforamtion. Please try again')
        except:
            print('Oops! you entered incorrect information, Please use number only')

    print('day confirmed')
    


    print('-'*40)
    print("you entered {}, {}, {}".format(city,month,day))
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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    
    print("Display - most frequent Month : {}, most frequent Day : {}, most frequent Hour : {}".format(popular_month, popular_day, popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df['Trip Route'] = df['Start Station'] + " ~ " + df['End Station']
       
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Trip Route'].mode()[0]
    
    print("Display - most frequent most commonly used start station : {}, most commonly used end station : {}, most frequent trip route : {}".format(popular_start_station, popular_end_station, popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Travel Time'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    total_travel_time = df['Travel Time'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    
    print("Display - total travel time : {}, mean travel time : {}".format(total_travel_time, mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #print(df.groupby(['User Type']).size())
    ##print(df.groupby(['User Type']).count())
    ##print(df.groupby(['User Type']).describe())
    count_user_type = df.groupby(['User Type']).size()

    # TO DO: Display counts of gender
    count_gender = df.groupby(['Gender']).size()

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth_year = df['Birth Year'].mode()[0]

    print("Display - counts of user types :\n {}, counts of gender :\n {}".format(count_user_type, count_gender))
    print("Display - earliest birth : {}, most recent birth : {}, most common birth year : {}".format(earliest_birth, most_recent_birth, most_common_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

                
        showing_5 = input('\nWould you like to see first 5 rows from raw data? Enter yes or no.\n')
        if showing_5.lower() == 'yes':
            print(df.head(5))
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
