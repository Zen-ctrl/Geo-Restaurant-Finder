# Documentation: Geo Restaurant Grep

This script uses the Google Maps Places API to find restaurants based on specific search keywords around given geographical coordinates. The results are then written to an Excel file, a CSV file, or displayed as a Pandas DataFrame, based on the user's choice.

## Functionality

The script is divided into several parts:

1. **Initialization**: The script first sets up a client connection to the Google Maps API using a specified API key. It also creates a Pandas DataFrame to store the restaurant data.

2. **Data Collection**: For each coordinate (latitude, longitude) in a given list, and for each keyword, the script performs a search using the `places_nearby()` method from the Google Maps API. This search is performed within a certain radius around the coordinates and is restricted to the specified keyword.

3. **Data Extraction**: The script processes each restaurant returned by the search. It extracts the restaurant's name, the keyword (which represents the cuisine), the restaurant type, its address, the state, and its coordinates. It then checks whether the restaurant is already in the list of unique restaurants (based on its coordinates and name). If not, it adds the restaurant to the DataFrame and the list of unique restaurants.

4. **Output Selection**: After collecting data for all coordinates and keywords, the script asks the user to choose an output format. The user can choose to write the data to a CSV file, an Excel file, or print it as a Pandas DataFrame. The script will keep asking until a valid option is chosen, or the user chooses to exit the program.

5. **Data Visualization**: The user is then asked whether they would like to plot the number of restaurants for each cuisine. If they choose to do so, a bar graph is displayed, showing the count of restaurants for each cuisine.

## Methodology

The script uses  `googlemaps` Python  library to interface with the Google Maps API. The `pandas` library is used for creating and managing the DataFrame, and the `openpyxl` library is used for writing the Excel workbook. Python's built-in `csv` module is used for writing the CSV file. The `matplotlib` library is used for data visualization.

For coordinates and keyword, the `places_nearby()` method is called, which returns a list of places near a specific location, within a given radius, and matching a specific keyword. The method can return up to 20 results per call, but there may be additional results available. The Google Maps API includes a `next_page_token` in the response if more results are available. The script waits for a few seconds (to allow the token to become valid) and then uses this token to request the next page of results.

The script continues this process of retrieving and writing restaurant data until all coordinates and keywords have been processed. The output format is determined by user input. If the user chooses to visualize the data, a bar graph is generated using `matplotlib`, showing the number of restaurants found for each cuisine.
