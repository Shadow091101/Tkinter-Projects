# AQI Search Application

This is a simple desktop application built using Python's Tkinter library that allows users to search for the Air Quality Index (AQI) of a specific region based on its zipcode. The application retrieves the geographical coordinates using the OpenCage Geocoding API and fetches the AQI data from the World Air Quality Index (WAQI) API.

## Features

- **Zipcode Search**: Enter a zipcode to find the corresponding AQI data.
- **Geocoding**: Converts the entered zipcode into geographical coordinates using the OpenCage Geocoding API.
- **AQI Data Retrieval**: Fetches real-time AQI data from the WAQI API.
- **User-Friendly Interface**: Displays AQI information, including the AQI value, air quality level, source of data, and city name, in a visually appealing format.
- **Color-Coded Results**: The background color of the result window changes based on the AQI level, providing a quick visual indicator of air quality.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/aqi-search.git
    ```
2. Navigate to the project directory:
    ```sh
    cd aqi-search
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Obtain API keys:
    - **OpenCage Geocoding API**: Sign up at [OpenCage Geocoding API](https://opencagedata.com/) to get your API key.
    - **WAQI API**: Sign up at [WAQI API](https://aqicn.org/data-platform/token/) to get your API key.

2. Update the `search` function in the script with your API keys:
    ```python
    geocoding_api_key = "your_opencage_api_key"
    waqi_api_key = "your_waqi_api_key"
    ```

3. Run the application:
    ```sh
    python main.py
    ```

4. Enter a zipcode in the input field and click the "Search AQI" button to get the AQI information.

## Screenshots

![AQI Search](screenshots/aqi_search.png)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
