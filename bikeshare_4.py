import datetime
import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv', 'Newyork': 'new_york_city.csv',
             'Washington': 'washington.csv'}


"""This defined function is to catch error associated
                            with space and lettercase"""


def error_catch(name_input):
    name_input = name_input.capitalize().replace(" ", "")
    return name_input


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" \
        to apply no month filter
        (str) day - name of the day of week to filter by, or "all"\
         to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = error_catch(str(input('\nWhich City will you like to explore: \
                            Chicago, New York, or Washington ? \n')))
            if city in ['Chicago', 'Newyork', 'Washington']:
                break
            else:
                print('Sorry! please check the options again?')
                continue

            break
        except:
            print('There must be a mistake with the city name. Please check \
                    and try again')


# get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = error_catch(str(input('\nWhich month will you like to explore: \
                January, February, March, April, May, June, or all? \n')))
            if month in ['January', 'February', 'March', 'April', 'May',
                                    'June', 'All']:
                break
            else:
                print('Sorry! please check the options again?')
                continue
            break
        except:
            print('There must be a mistake with the month name. Please check \
                and try again')
# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = error_catch(str(input('\nWhich day will you like to explore: \
                        Monday, Tuesday, Wednesday, Thursday, Friday, \
                                Saturday, Sunday, or All? \n')))
            if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                       'Saturday', 'Sunday', 'All']:
                break
            else:
                print('Sorry! please check the options again?')
                continue
            break
        except:
            print('you must have typed in something wrong. Please check \
                and try again')

    print('-'*40)
    return city, month, day


# test code
# print(get_filters())
""" Here I imported the bikeshare data and converted the time column dtype to
 date. I also created some new columns for the ease of working with the data"""

chicago_csv = pd.read_csv('C:\\Users\\Obi\\Desktop\\RMIT\\my_codes\\my_project2\\chicago.csv')

# print(chicago_csv)
# pd.set_option('display.max_columns', None)

chicago_csv['Start Time'] = pd.to_datetime(chicago_csv['Start Time'])
chicago_csv['End Time'] = pd.to_datetime(chicago_csv['End Time'])

"""Adding new columns to the chicago_csv data"""

chicago_csv['day'] = chicago_csv['Start Time'].dt.day_name()
chicago_csv['month'] = chicago_csv['Start Time'].dt.month_name()
chicago_csv['year'] = chicago_csv['Start Time'].dt.year

""" To delete redundant tables"""

chicago_csv.drop(['Unnamed: 0'], axis=1, inplace=True)

"""Here for the new_york_city dataset"""

new_york_city_csv = pd.read_csv(
    'C:\\Users\\Obi\\Desktop\\RMIT\\my_codes\\my_project2\\new_york_city.csv')

# pd.set_option('display.max_columns', None)

new_york_city_csv['Start Time'] = pd.to_datetime(new_york_city_csv['Start Time'])
new_york_city_csv['End Time'] = pd.to_datetime(new_york_city_csv['End Time'])

"""Adding new columns to the new_york_city_csv data"""

new_york_city_csv['day'] = new_york_city_csv['Start Time'].dt.day_name()
new_york_city_csv['month'] = new_york_city_csv['Start Time'].dt.month_name()
new_york_city_csv['year'] = new_york_city_csv['Start Time'].dt.year

""" To delete redundant tables"""

new_york_city_csv.drop(['Unnamed: 0'], axis=1, inplace=True)

""" Here for the washington dataset"""

washington_csv = pd.read_csv('C:\\Users\\Obi\\Desktop\\RMIT\\my_codes\\my_project2\\washington.csv')

washington_csv['Start Time'] = pd.to_datetime(washington_csv['Start Time'])
washington_csv['End Time'] = pd.to_datetime(washington_csv['End Time'])

"""Adding new columns to the washington_csv data"""

washington_csv['day'] = washington_csv['Start Time'].dt.day_name()
washington_csv['month'] = washington_csv['Start Time'].dt.month_name()
washington_csv['year'] = washington_csv['Start Time'].dt.year

""" To delete redundant tables"""

washington_csv.drop(['Unnamed: 0'], axis=1, inplace=True)


""" Here I defined a city and csv data dictionary for the purpose of load data"""

city_data = {'Chicago': chicago_csv,
             'Newyork': new_york_city_csv, 'Washington': washington_csv}


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
    df = city_data[city]
    if month != 'All':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['month'].value_counts().idxmax()
    print('The most common month is: {}'.format(common_month))

    # display the most common day of week

    common_day = df['day'].value_counts().idxmax()
    print('The most common day is:{}'.format(common_day))

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_start_time = df['hour'].value_counts().idxmax()
    print('the most common start hour is: {}'.format(common_start_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: {} '.format(common_start_station))

    # display most commonly used end station

    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: {} '.format(common_end_station))

    # display most frequent combination of start station and end station trip

    combined_station = df['Start Station'] + ' ' + df['End Station']
    freq_combined_station = combined_station.value_counts().idxmax()
    print('The most frequent combined station is: {}'.format(freq_combined_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    Total_time_travelled = df['Trip Duration'].sum()
    print('The total time travelled is : {}'.format(
        time.strftime('%H:%M:%S', time.gmtime(Total_time_travelled))))

    # display mean travel time

    mean_travelled_time = df['Trip Duration'].mean()
    print('The mean travelled time is: {}'.format(
        time.strftime('%H:%M:%S', time.gmtime(mean_travelled_time))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    User_type = df['User Type'].value_counts()
    print('The counts of user type is: {}'.format(User_type))

    # Display counts of gender

    """ Here I used a try statement to handle another KeyError"""

    gender = 1
    while gender == 1:
        try:
            df['Gender'] = df['Gender'].dropna()
            Gender = df['Gender'].value_counts()
            print('The counts of gender are as follows: {}'.format(Gender))
            break
        except KeyError:
            print('There are no data for Gender in Washington')
        finally:
            print('I will continue providing you other results')
            gender -= 1
            print('-'*40)

    # Display earliest, most recent, and most common year of birth

    """ Here I used a try statement to handle another KeyError"""

    birth_year = 1
    while birth_year == 1:
        try:
            earliest_birth_year = df['Birth Year'].dropna().max()
            recent_birth_year = df['Birth Year'].dropna().min()
            common_birth_year = df['Birth Year'].dropna().mode()[0]
            print('Earliest Birth Year: {}'.format(earliest_birth_year))
            print('Recent Birth Year: {}'.format(recent_birth_year))
            print('Common Birth Year: {}'.format(common_birth_year))
        except KeyError:
            print('There are no data for Birth Year record in Washington')
        finally:
            print('I will continue providing you other results')
            birth_year -= 1
            print('-'*40)

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

        Answer = 'yes'
        while Answer == 'yes':
            show_five_lines = input(
                '\nDo you want to see first 5 lines of raw data? Enter yes or no \n').lower()
            if show_five_lines == Answer:
                read_five = pd.read_csv(CITY_DATA[city], chunksize=5)

                print(read_five)
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
