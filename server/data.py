import pandas as pd
import plotly.express as px

# crime_df = pd.read_csv('/Users/julzhusainzada/Desktop/california.csv')
crime_df = pd.read_csv('California Crimes.csv')

# Dropping first three rows bc no data in them
crime_df = crime_df.drop([0, 1, 2, 3])

# Reset the index after dropping rows
crime_df.reset_index(drop=True, inplace=True)

# Reassigning column names because originally unnamed
crime_df.columns = ['City', 'Population', 'Violent crime', 'Murder and nonnegligent manslaughter',
                    'Rape', 'Robbery', 'Aggravated assault', 'Property Crime', 'Burglary',
                    'Larcenytheft', 'Motor vehicle theft', 'Arson']

# Function to get top 3 crimes for a given city


def get_top_crimes(city_name):
    try:
        # Find the row index of the city
        city_row_index = crime_df[crime_df['City'] == city_name].index.item()

        # Select the row corresponding to the city
        city_crimes = crime_df.loc[city_row_index]

        # Drop non-crime columns and convert to int
        city_crimes = city_crimes.drop(
            ['City', 'Population', 'Property Crime', 'Violent crime'])
        city_crimes = city_crimes.str.replace(',', '').astype(int)

        # Sort the crimes in descending order and get the top 3
        top_crimes = city_crimes.sort_values(ascending=False).head(3)

        return top_crimes
    except ValueError:
        return "City not found in the dataset."


# Get the top crimes for the entered city
def top_crimes():
    city_input = input("Enter a city: ") #delete
    top_crimes = get_top_crimes(city_input)
    print(f"The top crimes in {city_input} are:")
    for crime_name in top_crimes.index:
        print(crime_name)

# Function to generate interactive pie chart for a given city


def generate_pie_chart(city):
    selected_city = crime_df[crime_df['City'] == city]
    # Extract population number
    population = selected_city['Population'].values[0]
    crime_labels = selected_city.columns[2:]
    crime_values_str = selected_city.values[0][2:]

    crime_values = [int(value.replace(',', '')) for value in crime_values_str]

    custom_colors = ['#89CFF0', '#B0E0E6', '#87CEEB', '#F0F8FF', '#CCCCFF',
                     '#e5f2ff', '#81D8D0', '#00CCCC', '#AFEEEE', '#B2F0E4', '#ADD8E6']

    fig = px.pie(values=crime_values, names=crime_labels, title=f'<b>Crime Distribution in {city}<br><span style="font-size: 18px;">Population: {population}</span></b>',
                 hover_name=crime_labels, labels={'label': 'Crime'}, hole=0.3, color_discrete_sequence=custom_colors)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False, title_x=0.5,
                      title_font_size=24, plot_bgcolor='#AEC9AD', paper_bgcolor='#AEC9AD')  # Set background color

    # fig.show()
    fig.write_image('chart.png')
