import googlemaps
import pandas as pd
import openpyxl
import csv
import time
import matplotlib.pyplot as plt


gmaps = googlemaps.Client(key='xxxxxxxxxxxxxxxxxxxxxxx')

coordinates = [
    # Your coordinates go here
]

keywords = ['Asian cuisine', 'Italian cuisine', 'Mexican cuisine']  # Add more search keywords here if needed
radius = 50000  # You can adjust the search radius here
unique_restaurants = set()

# Creating a pandas DataFrame to hold the data
data = {
    'Name': [],
    'Cuisine': [],
    'Restaurant Type': [],
    'Address': [],
    'State': [],
    'Latitude': [],
    'Longitude': []
}

for lat, lng in coordinates:
    location = f"{lat},{lng}"
    for keyword in keywords:

        response = gmaps.places_nearby(location=location, radius=radius, keyword=keyword)

        while response:
            results = response['results']

            for result in results:
                name = result['name']
                cuisine = keyword
                restaurant_type = result.get('types', [''])[0]
                address = result['vicinity']
                state = 'Florida'
                latitude = result['geometry']['location']['lat']
                longitude = result['geometry']['location']['lng']
                restaurant_identifier = (latitude, longitude, name)

                if restaurant_identifier in unique_restaurants:
                    continue  # Skip if the restaurant already exists

                data['Name'].append(name)
                data['Cuisine'].append(cuisine)
                data['Restaurant Type'].append(restaurant_type)
                data['Address'].append(address)
                data['State'].append(state)
                data['Latitude'].append(latitude)
                data['Longitude'].append(longitude)
                unique_restaurants.add(restaurant_identifier)

            # Try to get the next page of results
            if 'next_page_token' in response:
                # slight delay before the next request
                time.sleep(2)
                response = gmaps.places_nearby(page_token=response['next_page_token'])
            else:
                response = None

df = pd.DataFrame(data)

while True:
    output_format = input("Please choose an output format (csv/excel/pandas/exit): ")

    if output_format.lower() == "csv":
        df.to_csv('restaurant_results.csv', index=False)
        print("Results saved to restaurant_results.csv")
        break
    elif output_format.lower() == "excel":
        df.to_excel('restaurant_results.xlsx', index=False)
        print("Results saved to restaurant_results.xlsx")
        break
    elif output_format.lower() == "pandas":
        print(df)
        break
    elif output_format.lower() == "exit":
        break
    else:
        print("Invalid option. Please try again.")

plot_option = input("Would you like to plot the number of restaurants for each cuisine (yes/no): ")

if plot_option.lower() == "yes":
    df['Cuisine'].value_counts().plot(kind='bar')
    plt.ylabel('Number of Restaurants')
    plt.xlabel('Cuisine')
    plt.title('Number of Restaurants for Each Cuisine')
    plt.show()
