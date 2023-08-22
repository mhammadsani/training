from utils import get_annual_report_of_temperature_and_humidity, get_hottest_day_of_the_year
from constants import (
    TWELWE_LEFT_SPACES, FIFTEEN_LEFT_SPACES, EIGHT_LEFT_SPACES, TWENTY_LEFT_SPACES
    )

def annual_report_of_temperature_and_humidity() -> None:
    """display the annual report containing
       min, max temperatures and humidities
    """
    
    print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
    print("--------------------------------------------------------------------------")
    for year in range(1996, 2012):
        max_temp, min_temp, max_humidity, min_humidity = get_annual_report_of_temperature_and_humidity(year) 
        print(
            f'{year} {max_temp:>{TWELWE_LEFT_SPACES}} {min_temp:>{FIFTEEN_LEFT_SPACES}} {max_humidity:>{FIFTEEN_LEFT_SPACES}} {min_humidity:>{TWENTY_LEFT_SPACES}}'
            )

            
            
def hottest_day_of_each_year() -> None:
    """display hottest day of each yeay from 1996 to 2011
    """
    print("Year        Date          Temp")
    print("------------------------------")
    for year in range(1996, 2012):
        date, temp = get_hottest_day_of_the_year(year)
        print(f'{year} {date:>{FIFTEEN_LEFT_SPACES}} {temp:>{EIGHT_LEFT_SPACES}}')

