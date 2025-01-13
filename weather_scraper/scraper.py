import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Cities:
    LosAngeles = "9720462459b9974380a654a8d3df130c9af4b30c3d7626196fcdb9eb99764aa9" # Los Angeles, USA
    SanFrancisco = "7817d246c582f93ab50f97205835f017acc6792a1cd4950fbc80c99b4d53ea86" # San Francisco, USA
    NewYork = "a496cfcba367ffae60ccfdc94e31bcf3d0a12ac6515336dbd274f381a932abbc" # New York, USA
    London = "aac619af0e4a1f0ffbab44e0cd35501d61e2c5d4337767432f5cbac90957d7a1" # London, UK
    Tokyo = "506b6438ed491e9cbe5fa3a054316fdfc7ecd696e5529caee9356099a5df4534" # Tokyo, Japan
    Paris = "d2a540efb4e9604b3c1d01b7851a1d9d2ab4c7b3ba428e5799936ac54404c035" # Paris, France
    Beijing = "b2dc7b2de8f7cf0ab5593e383d375faba071dbb9d8131a6b4910b3f4ee6c51b7" # Beijing, PRC
    Sydney = "068e7946e751c604b7053c3fd420df0f90355418f36c7ef9331b81e2d2032aaf" # Sydney, Australia
    Moscow = "aeea22202ca7af67cd001c86700f5486514081107a161ba8f78177867024ae43" # Moscow, Russia
    Cairo = "f9dd8ba79fe6ded9b8751369e4a1f303e818e62ae114af7a8d5a4bab83c28c55" # Cairo, Egypt
    Mumbai = "cb022e27867bb250b801b119170ab9889e1bc3b65e50c76798362b7f95d29248" # Mumbai, India
    Dubai = "11687d0fb9d792f665b4d62ef7ab768b22abe762fc5f9033c476f152e481eda1" # Dubai, UAE
    HongKong = "a16033779bee84d744ad8c017c2db67cfce767078b737139ec37e3bdab778110" # Hong Kong, PRC
    Singapore = "71875be7823a5b64d1deef4e03ac5824eac586413a1ae0c15296de172dd2cb07" # Singapore, Singapore
    Toronto = "774e43da3c5f218cdf671f93ca3cb901c5ff0731691a2577929bb2ecc3d4e5c1" # Toronto, Canada
    SãoPaulo = "ebe93c0e09d0cfe19844d4281461901cd8f083c310e64255954758c8dcab784b" # São Paulo, Brazil
    SaoPaulo = "ebe93c0e09d0cfe19844d4281461901cd8f083c310e64255954758c8dcab784b" # Same as top, avoided possible Non-ASCII character errors (have not checked for the existence this error)
    Seoul = "18e81cdf57491c51a6fba3c57732b7b61bdf511fc2b613570316978b9f20687a" # Seoul, ROK (South Korea)
    Rome = "d3a11723c54fa85aa92f5f62cd4354c2df3255f09787f5f871305492f63801d3" # Rome, Italy
    Berlin = "153e65f344ab389e17703aae99cf18a182265e8095831d55ddfcfc6c5aa9a91c" # Berlin, Germany
    Barcelona = "6feceaef242fce5c7e95003da90687ae40db63b07f931a0304b8761fe1f8c6e7" # Barcelona, Spain
    Amsterdam = "968d2f1a5509a2f71fca25929b7d83139ac5134f61611a9c6637c90354cd6da8" # Amsterdam, Netherlands
    Istanbul = "7912d03017522301f5c89f4f1d661d18ad10926c15063cf520ee5ec7ce7c787c" # Istanbul, Turkey
    BuenosAires = "254888a010f8d98f74e3de0b643bd87dde60a11ac213eb544348b555d425f2e4" # Buenos Aires, Argentina
    Madrid = "f058e9bea1986012d45e85df8e849c4fba8bd30be90ba0a13b4930bb7c019380" # Madrid, Spain
    Johannesburg = "cf6d7e1f6385beb940f9c3519b074a755690f44e9a3d005d0bff6156ea31a28c" # Johannesburg, South Africa
    Bangkok = "959cf4a42b28680a5c17bd32fd270d7cc25ce0a1058cebc035fb9e16d0b30fe0" # Bangkok, Thailand
    Athens = "959cf4a42b28680a5c17bd32fd270d7cc25ce0a1058cebc035fb9e16d0b30fe0" # Athens, Greece
    Vienna = "bfd25ee1f80dc6eebc4c862da0e02ea678c684f0e3533e102af24f3a8adbd914" # Vienna, Austria
    Stockholm = "e14da340155ce4b2ced8ba15becff883e737da0ba2db2af546e85804c56606f4" # Stockholm, Sweden
    Dublin = "036b720ce96da7a75a1cf4389e0d84511d9b72eda398a8dd0417396de814cab6" # Dublin, Ireland
    RioDeJaneiro = "1ff5f708415c0675e9ddf27ec2c0fb81d235f4b1730d12b3c90879c0c16f7148" # Rio de Janeiro, Brazil
    Melbourne = "ae4d584276953664e2ec532ce5b74b765e170bd1f8569915d5be1d56688bd2d6" # Melbourne, Australia
    Chicago = "c657780d487f955cbdab2fa228cbce3b5a314e7694057bf286e43a46eed060a8" # Chicago, USA
    Taipei = "d357f08735408ecba1ca2cb0961fb423059f506d67b053ae6107c5e508362efa" # Taipei, PRC


def get_weather(city, Celsius=False):
    url = f'https://weather.com/weather/today/l/{city}'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            logger.error(f"Failed to retrieve weather data. Status code: {response.status_code}")
            return f"Error: Could not retrieve data for {city}"

        soup = BeautifulSoup(response.text, 'html.parser')

        weather_data = {}

        # Current Temperature
        temp_element = soup.find('div', class_=lambda c: c and 'CurrentConditions--primary' in c)
        if temp_element:
            temperature = temp_element.find('span', class_=lambda c: c and 'tempValue' in c)
            if temperature:
                temp_str = temperature.text.replace('°', '')
                temp_in_f = float(temp_str)
                if Celsius:
                    weather_data['temperature'] = round((temp_in_f - 32) * 5 / 9, 1)
                else:
                    weather_data['temperature'] = temp_in_f
            else:
                weather_data['temperature'] = "N/A"
                logger.warning("Temperature value not found.")
        else:
            weather_data['temperature'] = "N/A"
            logger.warning("Temperature element not found.")

        # Weather Description
        description = soup.find('div', class_=lambda c: c and 'phraseValue' in c)
        weather_data['description'] = description.text.strip() if description else "N/A"
        if weather_data['description'] == "N/A":
            logger.warning("Weather description not found.")

        # Today's Details
        details_container = soup.find('div', class_='TodayDetailsCard--detailsContainer--jPhjU')
        if details_container:
            # High/Low Temperature
            high_low = details_container.find('div', string='High / Low').find_next('div',
                                                                                    class_='WeatherDetailsListItem--wxData--lW-7H')
            if high_low:
                high, low = high_low.text.split('/')
                weather_data['high'] = high.strip().replace('°', '')
                weather_data['low'] = low.strip().replace('°', '')
            else:
                weather_data['high'] = "N/A"
                weather_data['low'] = "N/A"
                logger.warning("High/Low temperature data not found.")

            # Wind
            wind = details_container.find('div', string='Wind').find_next('div',
                                                                          class_='WeatherDetailsListItem--wxData--lW-7H')
            if wind:
                wind_value = wind.find('span', class_='Wind--windWrapper--NsCjc')
                weather_data['wind'] = wind_value.text.strip() if wind_value else "N/A"
            else:
                weather_data['wind'] = "N/A"
                logger.warning("Wind data not found.")

            # Humidity
            humidity = details_container.find('div', string='Humidity').find_next('div',
                                                                                  class_='WeatherDetailsListItem--wxData--lW-7H')
            if humidity:
                weather_data['humidity'] = humidity.text.strip().replace('%', '')
            else:
                weather_data['humidity'] = "N/A"
                logger.warning("Humidity data not found.")

            # Dew Point
            dew_point = details_container.find('div', string='Dew Point').find_next('div',
                                                                                    class_='WeatherDetailsListItem--wxData--lW-7H')
            if dew_point:
                weather_data['dew_point'] = dew_point.text.strip().replace('°', '')
            else:
                weather_data['dew_point'] = "N/A"
                logger.warning("Dew point data not found.")

            # Pressure
            pressure = details_container.find('div', string='Pressure').find_next('div',
                                                                                  class_='WeatherDetailsListItem--wxData--lW-7H')
            if pressure:
                weather_data['pressure'] = pressure.find('span').text.strip()
            else:
                weather_data['pressure'] = "N/A"
                logger.warning("Pressure data not found.")

            # UV Index
            uv_index = details_container.find('div', string='UV Index').find_next('div',
                                                                                  class_='WeatherDetailsListItem--wxData--lW-7H')
            if uv_index:
                weather_data['uv_index'] = uv_index.text.strip().split('of')[0].strip()
            else:
                weather_data['uv_index'] = "N/A"
                logger.warning("UV index data not found.")

            # Visibility
            visibility = details_container.find('div', string='Visibility').find_next('div',
                                                                                      class_='WeatherDetailsListItem--wxData--lW-7H')
            if visibility:
                weather_data['visibility'] = visibility.text.strip().split()[0]
            else:
                weather_data['visibility'] = "N/A"
                logger.warning("Visibility data not found.")

            # Moon Phase
            moon_phase = details_container.find('div', string='Moon Phase').find_next('div',
                                                                                      class_='WeatherDetailsListItem--wxData--lW-7H')
            if moon_phase:
                weather_data['moon_phase'] = moon_phase.text.strip()
            else:
                weather_data['moon_phase'] = "N/A"
                logger.warning("Moon phase data not found.")
        else:
            logger.warning("Details container not found.")

        if all(value == "N/A" for value in weather_data.values()):
            logger.error("No weather data could be scraped.")
            return "Error: Could not find weather data."

        return weather_data

    except requests.RequestException as e:
        logger.error(f"Network error occurred: {e}")
        return f"Error: Network issue when retrieving data for {city}"
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return f"Error: An unexpected issue occurred while processing data for {city}"

# For Debugging Output
if __name__ == "__main__":
    print(get_weather(Cities.Tokyo))