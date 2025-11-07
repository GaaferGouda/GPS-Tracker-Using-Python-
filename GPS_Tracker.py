#  GPS Tracker Using Python
# ---------------------------------------------------------
# Author: Gaafer Gouda
# Date: November 8, 2025
# Description: Tracks your approximate location using your
#              IP address and displays it on an interactive map.
# ---------------------------------------------------------

import os
import requests
from selenium import webdriver
import folium
import datetime
import time


# -----------------------------------------------------
# Function: locationCoordinates()
# Description: Fetch user's approximate coordinates
#              (latitude & longitude) using IP address.
# -----------------------------------------------------
def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        loc = data['loc'].split(',')
        lat, lon = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, lon, city, state

    except Exception as e:
        print(" Internet Not Available or API Error:", e)
        exit()
        return False


# -----------------------------------------------------
# Function: gps_locator()
# Description: Generates a map HTML file showing the
#              user's current location.
# -----------------------------------------------------
def gps_locator():
    # Create a map object (global view initially)
    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, lon, city, state = locationCoordinates()
        print(f"You are in {city}, {state}")
        print(f"Your Latitude = {lat} and Longitude = {lon}")

        # Add marker for current location
        folium.Marker([lat, lon], popup=f"Current Location: {city}, {state}").add_to(obj)

        # Set folder path to Desktop
        folder = os.path.join(os.path.expanduser("~"), "Desktop", "GPS_Maps")
        os.makedirs(folder, exist_ok=True)  # Automatically create folder if missing

        # Save the map HTML file
        fileName = os.path.join(folder, f"Location_{datetime.date.today()}.html")
        obj.save(fileName)

        print(f"Map saved successfully to: {fileName}")
        return fileName

    except Exception as e:
        print(" Error generating map:", e)
        return False


# -----------------------------------------------------
# Main Execution
# -----------------------------------------------------
if __name__ == "__main__":
    print("--------------- GPS Tracker Using Python ---------------\n")

    # Call the GPS locator function
    page = gps_locator()

    if page:
        print("\nOpening file in Chrome browser...")
        driver = webdriver.Chrome()  # Make sure ChromeDriver is set up
        driver.get(page)
        time.sleep(6)
        driver.quit()
        print("\nBrowser Closed Successfully ")
    else:
        print(" Could not open map file.")
