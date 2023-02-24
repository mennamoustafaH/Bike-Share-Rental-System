import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    city = input("what is the city name? chose from (chicago,new york city,washington )  : ").lower()
    cities = ['chicago', 'new york city', 'washington']
   
    while city  not in cities:
        print(" WRONG CHOISE ")
        city = input("what is the city name? chose from (chicago,new york city,washington )  : ").lower()
    

    month = input("what is the chosen month , select form january  to june or select all  :").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while month not in  months:
        print(" WRONG CHOISE ")
        month = input("what is the chosen month , select form january  to june or select all  :").lower()
        
    day = input("what is the chosen day or choose All : ").lower()
    days= ["satrday", "sunday", "monday", "tuesday", " wednesday", "thursday", "all"]

    while day not in days :
        print(" WRONG CHOISE ")
        day = input("what is the chosen day  : ").lower() 

        # ----------------------------------------------------------

    print('-' * 40)

  

    return city, month, day

   

 
    """
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)

def load_data(city, month, day):
   
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
  
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    return df    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    # TO DO: display the most common month
    print(" the most common month :\n " ,df["month"].mode()[0]," / 2017")

    # TO DO: display the most common day of week

    print("the most common day of week :\n" ,df["day_of_week"].mode()[0])
    
    # TO DO: display the most common start hour
    
    print("the most common start hour :\n" ,df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("the most commonly used start station : \n", df['Start Station'].mode()[0])
    print("the most commonly used End station : \n", df['End Station'].mode()[0])
    print("most frequent combination: \n",df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1))
      
          #agg(pd.Series.mode).to_frame())

    print("\nThis took %s seconds." % (time.time() - start_time))

    # TO DO: display the most commonly used End station
    ##########
    
    print('-' * 40)

    # TO DO: display most frequent combination of start station and end station trip
    
    
          
def trip_duration_stats(df):
          print('\nCalculating Trip Duration...\n')
          start_time = time.time()

    # TO DO: display total travel time
          print(" total travel time by second is : " ,df['Trip Duration'].sum())


    # TO DO: display mean travel time
          print(" the mean travel time by second is : " ,df['Trip Duration'].mean())


          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)


def user_stats(df,city):
    
    print('\nCalculating User Stats...\n') 
    start_time = time.time()
   
    # TO DO: Display counts of user types
    print(" the total user types count :\n", df['User Type'].value_counts())
    if city != "washington":
       
        print(" the counts  of Gender are \n", df['Gender'].value_counts())
        print("\n the most common birthday : \n", int(df['Birth Year'].mode()[0]))
        print("the earliest birthday :\n", int(df['Birth Year'].min()))
        print(" the most recent :\n ", int(df['Birth Year'].max()))
    else:
        pass
    
        
    # TO DO: Display earliest, most recent, and most common year of birth

    # TO DO: Display counts of gender


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def main():
    
    
    while True:
        
        city ,month ,day = get_filters()
         
        df = load_data(city, month, day)

        time_stats (df)
        station_stats(df)
        trip_duration_stats (df)
        user_stats(df,city)
        i = 0
        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            if view_data.lower() == 'yes':
                
    
                print(df.iloc[i:i+5])
            
                i += 5
            if view_data.lower() != 'yes':
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
    #view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    
if __name__ == "__main__":
	main()


    