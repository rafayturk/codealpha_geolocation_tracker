import requests  # Import the requests library to make HTTP requests
import folium  # Import the folium library to create maps

def get_ip_geolocation(ip):
    """
    Fetches the geolocation (latitude and longitude) of the given IP address.
    
    Parameters:
    ip (str): The IP address to look up.
    
    Returns:
    tuple: A tuple containing latitude and longitude.
    """
    url = f"http://ip-api.com/json/{ip}"  # Construct the URL for the IP-API service
    response = requests.get(url)  # Make a GET request to the API
    data = response.json()  # Parse the JSON response
    return (data['lat'], data['lon'])  # Return the latitude and longitude as a tuple

def main():
    """
    Main function to get user input, fetch geolocation, and display it on a map.
    """
    ip_address = input("Enter IP Address: ")  # Prompt the user to enter an IP address
    location = get_ip_geolocation(ip_address)  # Fetch the geolocation for the given IP address
    map = folium.Map(location=location, zoom_start=12)  # Create a Folium map centered at the geolocation
    # Add a marker at the geolocation with a popup and tooltip
    folium.Marker(location=location, popup="IP Location", tooltip="Click for more info").add_to(map)
    map.save('map.html')  # Save the map as an HTML file
    print(f"Map saved as map.html. Open the file in a web browser to view the location.")  # Inform the user

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
