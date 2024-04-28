import pandas as pd
crime_index = pd.read_csv('CA City Crimes - Sheet1.csv')

print(crime_index)

city = input("Input city name: ")
def get_crime_rating(city):
    # Extract city rank based on the user's city input
    city_rank = crime_index[crime_index['City / Population'].str.contains(city, case=False)]['Rank'].values
    if len(city_rank) > 0:
        return(f'{city_rank[0]}/{crime_index["Rank"].max()}')
    else:
        return('Rating N/A')
