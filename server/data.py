import pandas as pd
import matplotlib.pyplot as plt


crime_df = pd.read_csv('/Users/julzhusainzada/Desktop/california.csv')

# Dropping first three rows bc no data in them
crime_df = crime_df.drop([0, 1, 2, 3])

# Reset the index after dropping rows
crime_df.reset_index(drop=True, inplace=True)

# Reassigning column names because originally unnamed
crime_df.columns = ['City', 'Population', 'Violent crime', 'Murder and nonnegligent manslaughter',
                'Rape', 'Robbery', 'Aggravated assault', 'Property Crime', 'Burglary',
                'Larcenytheft', 'Motor vehicle theft', 'Arson']

city = str(input("Enter a city: "))
city_row_index = crime_df[crime_df['City'] == city].index.item()


