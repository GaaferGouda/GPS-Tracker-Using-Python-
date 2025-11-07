#  GPS Tracker Using Python

##  Overview
A simple Python-based GPS Tracker that locates your position using your **IP address** and displays it on an interactive map with **Folium**.  
The map automatically opens in your Chrome browser for easy visualization.

---

##  Requirements

Before running the project, install the following Python libraries:

```bash
pip install requests folium selenium
```

> **Note:** `datetime` and `time` are built-in Python modules; no need to install them.

---

##  How It Works

1. The script fetches your **IP address details** using the `ipinfo.io` API.  
2. Extracts **latitude**, **longitude**, **city**, and **region/state**.
3. Generates an **interactive map** using the `folium` library.
4. Saves the map locally as an **HTML file**.
5. Opens the map automatically in **Google Chrome** for a few seconds using Selenium.

---

##  Code Structure

- **`locationCoordinates()`** → Fetches coordinates and city details.  
- **`gps_locator()`** → Generates and saves the map.  
- **`main`** → Runs the program, opens the map in Chrome.

---

##  Example Output

```
--------------- GPS Tracker Using Python ---------------
You are in Cairo, Cairo Governorate
Your coordinates are: Latitude = 30.0444, Longitude = 31.2357
📍 Map saved to: C:/screengfg/Location_2025-07-23.html

Opening map in Chrome browser...
Browser closed. 
```

---

##  Notes

- The accuracy depends on IP-based geolocation (not satellite GPS).
- Replace the path `"C:/screengfg/"` with a valid folder on your computer.
- For **real GPS tracking**, connect to GPS hardware or a smartphone sensor.

---

##  Author
**Gaafer Gouda**  
Digital Egypt Pioneers Initiative (DEPI) | AI & Data Science Track

---

###  “Track smart, visualize faster.”
