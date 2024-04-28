import pandas as pd
import plotly.express as px

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

# Function to generate interactive pie chart for a given city
def generate_pie_chart(city):
    selected_city = crime_df[crime_df['City'] == city]
    population = selected_city['Population'].values[0]  # Extract population number
    crime_labels = selected_city.columns[2:]
    crime_values_str = selected_city.values[0][2:]

    crime_values = [int(value.replace(',', '')) for value in crime_values_str]

    custom_colors = ['#89CFF0', '#B0E0E6', '#87CEEB', '#F0F8FF', '#CCCCFF', '#e5f2ff', '#81D8D0', '#00CCCC', '#AFEEEE', '#B2F0E4', '#ADD8E6']

    fig = px.pie(values=crime_values, names=crime_labels, title=f'<b>Crime Distribution in {city}<br><span style="font-size: 18px;">Population: {population}</span></b>',
                 hover_name=crime_labels, labels={'label': 'Crime'}, hole=0.3, color_discrete_sequence=custom_colors)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False, title_x=0.5, title_font_size=24)  # Increase title font size

    fig.show()



