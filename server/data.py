import pandas as pd

data = pd.read_csv('/Users/julzhusainzada/Desktop/california.csv')

# Dropping first three rows bc no data in them
data = data.drop([0, 1, 2, 3])

# Reset the index after dropping rows
data.reset_index(drop=True, inplace=True)

# Reassigning column names because originally unnamed
data.columns = ['City', 'Population', 'Violent crime', 'Murder and nonnegligent manslaughter',
                'Rape', 'Robbery', 'Aggravated assault', 'Property Crime', 'Burglary',
                'Larcenytheft', 'Motor vehicle theft', 'Arson']

city = str(input("Enter a city: "))
city_row_index = data[data['City'] == city].index.item()