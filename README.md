# Weather Scraping App
A simple Python application that scrapes weather data for various cities around the world. This app retrieves information from **Weather.com**.
[![PyPI - Version](https://img.shields.io/pypi/v/weatherscraper.svg)](https://pypi.org/project/weatherscraper/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/weatherscraper.svg)](https://pypi.org/project/weatherscraper/)
[![PyPI - License](https://img.shields.io/pypi/l/weatherscraper.svg)](https://pypi.org/project/weatherscraper/)
[![GitHub last commit](https://img.shields.io/github/last-commit/Unknownuserfrommars/weatherscraper.svg)](https://github.com/Unknownuserfrommars/weatherscraper)
## Features
Get current weather data for cities worldwide.
Supports both Fahrenheit and Celsius for temperature.
Displays additional weather data: description, humidity, and wind speed. **(EDITOR'S NOTE: UNSTABLE, WORKING ON HOW TO FIX)**
### Cities Supported
Los Angeles, USA
San Francisco, USA
New York, USA
London, UK
Tokyo, Japan
Paris, France
Beijing, PRC
Sydney, Australia
Moscow, Russia
Cairo, Egypt
Mumbai, India
Dubai, UAE
Hong Kong, PRC
Singapore, Singapore
Toronto, Canada
São Paulo, Brazil
Sao Paulo, Brazil (same as São Paulo)
Seoul, ROK (South Korea)
Rome, Italy
Berlin, Germany
Barcelona, Spain
Amsterdam, Netherlands
Istanbul, Turkey
Buenos Aires, Argentina
Madrid, Spain
Johannesburg, South Africa
Bangkok, Thailand
Athens, Greece
Vienna, Austria
Stockholm, Sweden
Dublin, Ireland
Rio de Janeiro, Brazil
Melbourne, Australia
Chicago, USA
Taipei, PRC

## Installation
### Using Git
1. Clone this repository to your local machine:
```commandline
git clone https://github.com/Unknownuserfrommars/weatherscraper.git
```
2. Install the required dependencies:
```commandline
pip install -r requirements.txt
```
### Or: Install the Python Package
1. Using pip
```commandline
python -m pip install weatherscraper
```
## Usage
Import `weatherscraper` and call the get_weather() function with a city's identifier:
```python
from weatherscraper import get_weather, Cities
# Or run: import weatherscraper as wscrape
weather = get_weather(Cities.Tokyo) # Or: weather = wscrape.get_weather(wscrape.Cities.Beijing)
print(weather)
```
If you want the temperature in Celsius, pass the `celsius=True` argument into the `get_weather()` function (default is `False`).

# **Disclaimer**
This project uses **web scraping** to collect weather data from **Weather.com**. Please ensure that you comply with any applicable **robots.txt** rules, and use this tool responsibly. The weather data retrieved by this application is **not guaranteed to be 100% accurate** and should not be used for critical applications.

**This project is for educational purposes only.** The author is not responsible for any damage or loss resulting from the use of this application.

**Weather.com** may change its website structure at any time, which could break the functionality of the scraper.

# License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
- Please Read the [LICENSE](LICENSE.md) file for details.
