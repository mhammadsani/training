from utils import get_annual_report_of_temperature_and_humidity, get_hottest_day_of_the_year


def annual_report_of_temperature_and_humidity() -> None:
    """display the annual report containing
       min, max temperatures and humidities
    """
    
    print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
    print("--------------------------------------------------------------------------")
    for year in range(1996, 2012):
        max_temp, min_temp, max_humidity, min_humidity = get_annual_report_of_temperature_and_humidity(year) 
        print(f'{year} {max_temp:>12} {min_temp:>15} {max_humidity:>15} {min_humidity:>20}')
            
            
def hottest_day_of_each_year() -> None:
    """display hottest day of each yeay from 1996 to 2011
    """
    print("Year        Date          Temp")
    print("------------------------------")
    for year in range(1996, 2012):
        date, temp = get_hottest_day_of_the_year(year)
        print(f'{year} {date:>15} {temp:>8}')