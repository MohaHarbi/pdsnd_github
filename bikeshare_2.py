import time
import pandas as pd

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
    city = input("Enter The name of the city  || Chicago, New York city, Washington || ").lower()
    while city not in CITY_DATA :
        city = input("\n Invalid city ,Please Try again!  Should be Chicago , New York city , Washington ")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june']
    month = input("Please Entet a month:[ January February March April May June: ]  ").lower()
    while month not in months:
        month = input("Invalid input: please type from january to june : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    day = input("Which day? Monday, Tuesday, Wednesday ... : ").lower()
    while day not in days:
        day = input("Sorry but that is not a day , please try again! ").lower()
        
        
        
        
    print("you Entered {} as city , {} as month  {} as day".format(city,month,day))

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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    
    if month!= 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df =df[df['Month']==month]
        
        
    if day!='all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['Day_of_Week']== day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

#     TO DO: display the most common month
    comonth = df['Month'].mode()[0]
    print("The most common month is: {} ".format(comonth))

#    TO DO: display the most common day of week
    codays = df['Day_of_Week'].mode()[0]
    print("The most common day is: {}".format(codays))


    # TO DO: display the most common start hour
    cohour = df['Hour'].mode()[0]
    print("The most common hour is: {}".format(cohour))
#           format(common_hour.title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start = df['Start Station'].mode()

    # TO DO: display most commonly used end station
    end = df['End Station'].mode()
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination'].mode()[0])
    
    print("For the selected filters, the most common start-end combination "
          "of stations is: " + most_common_start_end_combination)
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
     
    print("\nthe Total travel time is {}s \nthe mean travel time is {}".format(total_travel,mean_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type : \n{} ".format(user_types))

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('\n Gender type: \n{}  '.format(counts_of_gender))
    except:
        print('\nSorry no data available this month ')
    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df):
        early = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print("\nEarly is : {}\nMost Recent is : {}\nMost Common is : {}".format(early,recent,common))
    else: 
        print('There is no birth year information: ')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data =='no':
            break
        elif view_data =='yes':
            continue
        else:
            view_data = input("Sorry i didn't catch that! , Try again: ")
   
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
