import calendar
from typing import Tuple
import weather


get_month_name = lambda month: calendar.month_name[month][:3]


def get_annual_report_of_temperature_and_humidity(year: int) -> Tuple:
    """Returns the annual report (temperature and humidity)

    Args:
        year (int):year of which you want annual report

    Returns:
        Tuple: containing every month maximum temperature,
               minimum temperature, maximum humidity and 
               minimum humidity 
    """
    
    yearly_data = weather.weatherman[year]
    every_month_max_temp = []
    every_month_min_temp = []
    every_month_max_humidity = []
    every_month_min_humidity = []
    
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            day_important_information = {}
            
            day_important_information["everyday_max_temps"] = []
            day_important_information["everyday_min_temps"] = []
            day_important_information["everyday_max_humidities"] = []
            day_important_information["everyday_min_humidities"] = []
            max_temp_index = 0
            min_temp_index = 2
            max_humidity_index = 6
            min_humidity_index = 8
            positive_infinity = float('+inf')
            negative_infinity = float('-inf')
            for day in range(len(monthly_data)):
                max_temp = monthly_data[day][max_temp_index]
                min_temp = monthly_data[day][min_temp_index]
                max_humidity = monthly_data[day][max_humidity_index] 
                min_humidity = monthly_data[day][min_humidity_index]
                
                day_important_information['everyday_max_temps'].\
                    append(negative_infinity 
                           if max_temp == "" 
                           else int(max_temp))
                day_important_information['everyday_min_temps'].\
                    append(positive_infinity 
                           if min_temp == "" 
                           else int(min_temp))    
                day_important_information['everyday_max_humidities'].\
                    append(negative_infinity 
                           if max_humidity == "" 
                           else int(max_humidity))
                day_important_information['everyday_min_humidities'].\
                    append(positive_infinity 
                           if min_humidity == "" 
                           else int(min_humidity))
                
            every_month_max_temp.append(
                max(day_important_information['everyday_max_temps'])
                )
            every_month_min_temp.append(
                min(day_important_information['everyday_min_temps'])
                )
            every_month_max_humidity.append(
                max(day_important_information['everyday_max_humidities'])
                )
            every_month_min_humidity.append(
                min(day_important_information['everyday_min_humidities'])
                )           
        except (KeyError):
            continue
        
    return (max(every_month_max_temp), min(every_month_min_temp), \
            max(every_month_max_humidity), min(every_month_min_humidity))


def get_day_and_max_temperature(daily_max_temp: list) -> Tuple:
    """Returns the maximum temperature and date of that day.

    Args:
        daily_max_temp (list): a list consisting of maximum temperatures
                               of every day for a month

    Returns:
        Tuple: containing maximum temperature of month and date
    """
    daily_max = daily_max_temp[0]
    day = 1
    for day_idx in range(len(daily_max_temp)):
        if daily_max_temp[day_idx] > daily_max:
            day = day_idx + 1
            daily_max = daily_max_temp[day_idx]
    return (day, daily_max)


def get_hottest_day_of_the_year(year: int) -> Tuple:
    """Find the hottest day of the year

    Args:
        year (int): year of which hottest day needs to be find out

    Returns:
        Tuple: containing the hottest day exact date and temperature on that day
    """
    yearly_data = weather.weatherman[year]
    every_month_max_temps = []
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            every_day_max_temps = []   
            negative_infinity = float('-inf')
            for day in range(len(monthly_data)):
                temperature = monthly_data[day][0]
                every_day_max_temps.append(
                    int(temperature) if temperature != "" else negative_infinity
                    )
            day_and_max_temp = get_day_and_max_temperature(every_day_max_temps)
            date = (year, month, day_and_max_temp[0], day_and_max_temp[1])
            every_month_max_temps.append(date)
        except KeyError:
            continue
    maximum_temperatue = 3
    hottest_days = sorted(every_month_max_temps,
                          key=lambda x: x[maximum_temperatue],
                          reverse=True)
    hottest_day = 0
    hottest_day_details = hottest_days[hottest_day]
    hottest_day_date_idx = 2
    hottest_day_month_idx = 1
    hottest_day_temperature_idx = 3
    hottest_day_date = hottest_day_details[hottest_day_date_idx]
    hottest_day_month = hottest_day_details[hottest_day_month_idx]
    hottest_day_temperature = hottest_day_details[hottest_day_temperature_idx]
    return (
        f'{hottest_day_date}/{hottest_day_month}/{year}', hottest_day_temperature
        )
